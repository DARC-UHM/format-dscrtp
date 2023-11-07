import json
import csv
import os
import errno

from util.functions import *
from annotation.annotation_row import AnnotationRow
from concept.concept_handler import *
from util.terminal_output import Color, Messages


class FormatOutput:
    """
    Used to retrieve all annotations for a specified list of dives from HURLSTOR and reformat them into Deep Sea Coral
    Research and Technology Program's submission format.

    The basic program structure:

    1) For each dive in the specified list, get the dive information from Dives.csv
    2) For each dive in the specified list, get every annotation for the dive from HURLSTOR
    3) For each annotation in the dive:
        a) Load the annotation data and update the taxon info from WoRMS
        b) Merge the annotation data, the dive information, and the WoRMS information
    4) Perform merging and checks (e.g. remove duplicate records and populate 'associated taxa' fields).
    5) Output a formatted .tsv file.
    """

    def __init__(self, sequence_names: list):
        self.sequence_names = sequence_names
        self.load_concepts_from_file = True
        self.concepts = {}
        self.app_data_path = ''
        self.save_path = ''
        self.dive_info = []
        self.dive_info_headers = ''

    def find_paths(self):
        """ Gets the cache directory and the path to Downloads """
        if os.name == 'nt':
            # Windows
            self.app_data_path = os.getenv('LOCALAPPDATA')
            self.save_path = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
        else:
            # Mac
            self.app_data_path = os.getenv('HOME') + '/Library/Application Support'
            self.save_path = os.path.join(os.getenv('HOME'), 'Downloads')

        os.chdir(self.app_data_path)

        try:
            os.mkdir('CTDProcess')
        except OSError as err:
            if err.errno != errno.EEXIST:
                # if the OS error is something other than 'directory already exists', raise the error
                raise
            # otherwise, ignore the error
            pass

    def load_concepts(self, from_file: bool):
        self.load_concepts_from_file = from_file
        save_folder = os.path.join(self.app_data_path, 'CTDProcess')

        print(f'\n{Color.BOLD}Saved concept data located in:{Color.END} {Color.UNDERLINE}{save_folder}{Color.END}')

        if self.load_concepts_from_file:
            try:
                os.chdir(save_folder)
                with open('concepts.json') as file:
                    self.concepts = json.load(file)
            except FileNotFoundError:
                print('No concepts file found, using WoRMS instead.')

    def load_dives_csv(self, dives_csv_path: str):
        try:
            with open(dives_csv_path, 'r', encoding='utf-8') as dive_csv:
                reader = csv.reader(dive_csv)
                self.dive_info_headers = next(reader)
                for row in reader:
                    self.dive_info.append(row)
            return True
        except FileNotFoundError:
            return False

    def process_records(self, file_name):
        # GeoForm: declaring here so val is saved across multiple annotations AND multiple dives
        # (this is only updated once per major change in VARS)
        current_cmecs_geo_form = NULL_VAL_STRING

        full_report_records = []  # list of every concept formatted for final output
        warning_messages = []  # list of items to review (QA/QC)

        if self.load_concepts_from_file:
            print(Messages.DIVE_HEADER)

        ###################################################################
        # Outer loop: iterates over each dive listed in the input CSV file
        ###################################################################
        for dive_name in self.sequence_names:
            first_round = True  # to print header in terminal
            report_records = []  # array of concepts records for the dive
            concepts_from_worms = 0  # count of how many concepts were loaded from worms

            if self.load_concepts_from_file:
                print(f'{Color.BOLD}%-35s{Color.END}' % dive_name, end='')
                sys.stdout.flush()
            else:
                print(f'\nFetching annotations for {Color.CYAN}{dive_name}{Color.END}')

            url = f'http://hurlstor.soest.hawaii.edu:8086/query/dive/{dive_name.replace(" ", "%20")}'

            with requests.get(url) as r:
                report_json = r.json()

            # Tries to get the current dive from Dives.csv, links information from Dives.csv to the current dive
            dive_row = next((row for row in self.dive_info if row[0] in dive_name or dive_name in row[0]), None)
            if not dive_row:
                print(Messages.dive_not_found(dive_name=dive_name))
                return False

            # Set all blank values to the null val string
            for i in range(len(dive_row)):
                if dive_row[i] == '':
                    dive_row[i] = NULL_VAL_STRING
            dive_dict = dict(zip(self.dive_info_headers, dive_row))

            if self.load_concepts_from_file:
                print('%-30s' % len(report_json['annotations']), end='')
                sys.stdout.flush()
            else:
                print(f'{len(report_json["annotations"])} annotations found')

            # sort objects by uuid - this is so the final output can match the expected output for easier testing
            report_json['annotations'].sort(key=extract_uuid)
            # Sort json objects by time
            report_json['annotations'].sort(key=extract_recorded_datetime)

            if dive_dict['LocationAccuracy'] == NULL_VAL_STRING:
                warning_messages.append([
                    dive_name, 'NA', 'NA',
                    f'{Color.YELLOW}No location accuracy found{Color.END} - Add to {Color.UNDERLINE}Dives.csv{Color.END}'
                ])

            if dive_dict['WebSite'] == NULL_VAL_STRING:
                warning_messages.append([
                    dive_name, 'NA', 'NA',
                    f'{Color.YELLOW}No website found{Color.END} - Add to {Color.UNDERLINE}Dives.csv{Color.END}'
                ])

            # get start and end time of each video (to use later to check whether annotation falls inside a video time)
            dive_video_timestamps = []
            for i in range(len(report_json['media'])):
                media = report_json['media'][i]
                # the second check here can be removed if we need to consider clips longer than 10 minutes
                #                                     ↓           remove me               ↓
                if 'image' not in media['video_name'] and media['duration_millis'] > 600000:  # 600000 millis = 10 min
                    start_time = parse_datetime(report_json['media'][i]['start_timestamp'])
                    dive_video_timestamps.append([start_time, start_time + timedelta(milliseconds=media['duration_millis'])])

            ############################################################################################################
            # Main inner loop: iterates through all annotations for the dive and fills out the fields required by DSCRTP
            ############################################################################################################
            for annotation in report_json['annotations']:
                concept_name = annotation['concept']

                annotation_row = AnnotationRow(annotation)  # object to store all annotation information

                # populate simple data from annotation & Dives.csv
                annotation_row.set_sample_id(dive_name=dive_name)
                annotation_row.set_simple_static_data()
                annotation_row.set_ancillary_data(warning_messages=warning_messages)
                annotation_row.set_dive_info(dive_info=dive_dict)

                # get concept info: check WoRMS if specified by user OR if concept info missing from save file
                if concept_name != 'none':
                    if concept_name not in self.concepts:  # if concept name not in saved concepts file, search WoRMS
                        if first_round:  # for printing worms header
                            first_round = False
                            print(Messages.WORMS_HEADER)
                        concept = Concept(concept_name=concept_name)
                        cons_handler = ConceptHandler(concept=concept)
                        cons_handler.fetch_worms()
                        cons_handler.fetch_vars_synonyms(warning_messages=warning_messages)
                        self.concepts[concept_name] = {
                            'scientific_name': concept.scientific_name,
                            'aphia_id': concept.aphia_id,
                            'authorship': concept.authorship,
                            'synonyms': concept.synonyms,
                            'taxon_rank': concept.taxon_rank,
                            'taxon_ranks': concept.taxon_ranks,
                            'descriptors': concept.descriptors,
                            'vernacular_name': concept.vernacular_names
                        }

                    # populate annotation row object with concept info
                    annotation_row.set_concept_info(concepts=self.concepts, warning_messages=warning_messages)

                # loop through timestamps and check if recorded_timestamps is in retrieved timestamp ranges
                media_type = 'still image'
                for i in range(len(dive_video_timestamps)):
                    if dive_video_timestamps[i][0] <= annotation_row.recorded_time.timestamp <= dive_video_timestamps[i][1]:
                        media_type = 'video observation'
                        break

                # update megahabitat
                if get_association(annotation, 'megahabitat'):
                    current_cmecs_geo_form = get_association(annotation, "megahabitat")["to_concept"]
                # update habitat
                if get_association(annotation, 'habitat'):
                    current_cmecs_geo_form = f'{current_cmecs_geo_form.split(",")[0]}, ' \
                                              f'{get_association(annotation, "habitat")["to_concept"]}'

                # populate the rest of the annotation data
                annotation_row.set_media_type(media_type=media_type)
                annotation_row.set_id_comments()
                annotation_row.set_indv_count_and_cat_abundance()
                annotation_row.set_size(warning_messages=warning_messages)
                annotation_row.set_condition_comment(warning_messages=warning_messages)
                annotation_row.set_comments_and_sample()
                annotation_row.set_cmecs_geo(cmecs_geo=current_cmecs_geo_form)
                annotation_row.set_habitat(warning_messages=warning_messages)
                annotation_row.set_upon()
                annotation_row.set_id_ref()
                annotation_row.set_image_paths()

                record = [annotation_row.columns[x] for x in HEADERS]  # convert to list
                report_records.append(record)  # append annotation to a list of all annotations from this dive

            # remove duplicates (ie records with matching id reference numbers)
            dupes_removed = collapse_id_records(report_records=report_records)

            if self.load_concepts_from_file:
                print('%-30s' % str(dupes_removed), end='')
                sys.stdout.flush()
            else:
                print(f'\n{str(dupes_removed)} duplicate records removed')

            # find associates and hosts
            find_associated_taxa(report_records=report_records, concepts=self.concepts, warning_messages=warning_messages)

            # translate substrate (upon) names - this must be done after finding the associated taxa (relies on concept name)
            for i in range(len(report_records)):
                record = report_records[i]
                if record[SUBSTRATE] == 'organism (dead)':
                    record[SUBSTRATE] = 'dead organism'
                elif record[SUBSTRATE] in self.concepts:
                    saved = self.concepts[record[SUBSTRATE]]
                    record[SUBSTRATE] = saved["scientific_name"]
                    if saved["descriptors"]:
                        record[SUBSTRATE] += f' ({" ".join(saved["descriptors"])})'

            # Add this formatted dive to the full list of report associate_records
            full_report_records += report_records
            print(f'{Color.GREEN}Complete{Color.END}')

        # Save concept taxonomy info to cache file
        print('\nSaving output file...')
        os.chdir(self.app_data_path)
        with open('concepts.json', 'w') as file:
            json.dump(self.concepts, file)

        # Save all records to tsv
        os.chdir(self.save_path)
        with open(f'{file_name}.tsv', 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file, delimiter='\t')
            csv_writer.writerow(HEADERS[:88])
            for record in full_report_records:
                csv_writer.writerow(record[:88])

        print(f'\n{Color.BOLD}Output file saved to:{Color.END} {Color.UNDERLINE}{self.save_path}/{file_name}.tsv{Color.END}')
        print(f'\n{Color.YELLOW}There are {len(warning_messages)} warning messages.{Color.END}\n')

        # Print warning messages
        if len(warning_messages) > 0:
            with open('warnings.tsv', 'w') as file:
                csv_writer = csv.writer(file, delimiter='\t')
                csv_writer.writerow(['Sample ID', 'Concept Name', 'UUID', 'Message'])
                for message in warning_messages:
                    raw_message = []
                    for col in message:
                        raw_message.append(col.replace(Color.BOLD, '')
                                           .replace(Color.END, '').replace(Color.YELLOW, '')
                                           .replace(Color.RED, '').replace(Color.UNDERLINE, ''))
                    csv_writer.writerow(raw_message)

            print(f'{Color.BOLD}Warnings saved to: {Color.END}{Color.UNDERLINE}{self.save_path}/warnings.tsv{Color.END}')

        return True
