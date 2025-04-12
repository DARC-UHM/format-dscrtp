"""
This script is used to retrieve all annotations for a specified list of dives from HURLSTOR and reformat them into
Deep Sea Corals Research and Technology Program's submission format.

The basic program structure:

1) For each dive in the specified list, get the dive information from Dives.csv.
2) For each dive in the specified list, get every annotation for the dive from HURLSTOR.
3) For each annotation in the dive, load the annotation data and update the taxon info from WoRMS (optional).
4) For each annotation, merge the annotation data, the dive information, and the WoRMS information.
5) Perform merging and checks (e.g. remove duplicate records and populate 'associated taxa' fields).
6) Output a formatted .tsv file.
"""

import json
import csv
import os
import errno

from util.functions import *
from annotation.annotation_row import AnnotationRow
from concept.concept_handler import *
from util.terminal_output import Color, Messages

OUTPUT_FILE_NAME = ''
OUTPUT_FILE_PATH = ''
SEQUENCE_NAMES_PATH = ''
SAVE_HIGHLIGHT_IMAGES = False
REPORTER = 'Bingo, Sarah'
REPORTER_EMAIL = 'sarahr6@hawaii.edu'

"""#####################################################################################################################
If you need to run this script multiple times (e.g. for testing or troubleshooting), you can hardcode names and file
paths here so you don't have to enter them in the CLI every time. If these are left blank, the script will prompt you
to enter this information at runtime. If you don't want to use the hardcoded values, simply comment out this block of
code. """

# the name of the output file without the .tsv extension, e.g. 'NA134'
# OUTPUT_FILE_NAME = 'test'
# path where you want the output file to be saved, e.g. '/Volumes/maxarray2/varsadditional/AnnotationExtracts'
# OUTPUT_FILE_PATH = '/Users/darc/Desktop'
# path to a csv of the sequence names, e.g. '/Users/darc/Documents/GitHub/Format-Output/reference/test_sequences.csv'
# SEQUENCE_NAMES_PATH = '/Users/darc/Documents/Github/Format-Output/reference/test_sequences.csv'

"""##################################################################################################################"""

# Initialization: Get the cache directory (note: does not consider Linux file structure)
current_folder = os.getcwd()

if os.name == 'nt':
    # Windows
    save_folder = os.getenv('LOCALAPPDATA')
else:
    # Mac
    save_folder = os.getenv('HOME') + '/Library/Application Support'

os.chdir(save_folder)

try:
    os.mkdir('CTDProcess')
except OSError as err:
    if err.errno != errno.EEXIST:
        # if the OS error is something other than 'directory already exists', raise the error
        raise
    # otherwise, ignore the error
    pass

save_folder = os.path.join(save_folder, 'CTDProcess')
print(f'\n{Color.BOLD}Saved cache files located in:{Color.END} {Color.UNDERLINE}{save_folder}{Color.END}')

os.chdir(current_folder)

dive_info = []  # the script's copy of Dives.csv

# Load info from Dives.csv: Dives.csv must be in the same directory that the script was called. This file must be
# up to date with all video sequences listed in the input file
with open('reference/Dives.csv', 'r', encoding='utf-8') as dive_csv:
    reader = csv.reader(dive_csv)
    dive_info_headers = next(reader)
    for row in reader:
        dive_info.append(row)

output_file_name = OUTPUT_FILE_NAME or input('Name of output file (without the .tsv file extension: ')
output_file_path = OUTPUT_FILE_PATH or input('Path to folder of output files: ')
sequence_names_path = SEQUENCE_NAMES_PATH or input('Path to a list of sequence names: ')
save_highlight_images = SAVE_HIGHLIGHT_IMAGES or input('Download highlight images? (y/n): ').lower() in ['y', 'yes']

# Decide whether to output only localizations or only regular annotations
output_type = input('Output regular annotations or localizations? (enter "r" for regular or "l" for localizations): ').lower()

# Decide whether to load or overwrite concepts
load_concepts = input(Messages.LOAD_CONCEPTS_PROMPT).lower() in ['y', 'yes']

concepts = {}

if load_concepts:
    try:
        os.chdir(save_folder)
        with open('concepts.json') as file:
            concepts = json.load(file)
    except FileNotFoundError:
        print('No concepts file found, using WoRMS instead.')

sequence_names = []  # list of video sequences numbers to query VARS API

with open(sequence_names_path, 'r') as seq_names_file:
    seq_reader = csv.reader(seq_names_file)
    h = next(seq_reader)
    for row in seq_reader:
        sequence_names.append(row[1])

# GeoForm: declaring here so val is saved across multiple annotations AND multiple dives
# (this is only updated once per major change in VARS)
current_cmecs_geo_form = NULL_VAL_STRING

full_report_records = []  # list of every concept formatted for final output
warning_messages = []  # list of items to review (QA/QC)

if load_concepts:
    print(Messages.DIVE_HEADER)

###################################################################
# Outer loop: iterates over each dive listed in the input CSV file
###################################################################
for dive_name in sequence_names:
    first_round = True  # to print header in terminal
    report_records = []  # array of concepts records for the dive
    concepts_from_worms = 0  # count of how many concepts were loaded from worms

    if load_concepts:
        print(f'{Color.BOLD}%-35s{Color.END}' % dive_name, end='')
        sys.stdout.flush()
    else:
        print(f'\nFetching annotations for {Color.CYAN}{dive_name}{Color.END}')

    if save_highlight_images:  # create folder for highlight images
        os.chdir(output_file_path)
        try:
            os.mkdir('highlight-images')
        except OSError as err:
            if err.errno != errno.EEXIST:
                raise  # if the OS error is something other than 'directory already exists', raise the error
            pass  # otherwise, ignore the error

    with requests.get(f'http://hurlstor.soest.hawaii.edu:8086/query/dive/{dive_name.replace(" ", "%20")}') as r:
        report_json = r.json()

    # Tries to get the current dive from Dives.csv, links information from Dives.csv to the current dive
    dive_row = next((row for row in dive_info if row[0] in dive_name or dive_name in row[0]), None)
    if not dive_row:
        print(Messages.dive_not_found(dive_name=dive_name))
        break

    # Set all blank values to the null val string
    for i in range(len(dive_row)):
        if dive_row[i] == '':
            dive_row[i] = NULL_VAL_STRING
    dive_dict = dict(zip(dive_info_headers, dive_row))

    if load_concepts:
        print('%-30s' % len(report_json['annotations']), end='')
        sys.stdout.flush()
    else:
        print(f'{len(report_json["annotations"])} annotations found')

    # sort objects by uuid - this is so the final output can match the expected output for easier testing
    report_json['annotations'].sort(key=extract_uuid)
    # Sort json objects by time
    report_json['annotations'].sort(key=extract_time)

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

    # get start time and end time of each video (to use later to check whether annotation falls inside a video time)
    dive_video_timestamps = []
    for i in range(len(report_json['media'])):
        media = report_json['media'][i]
        # the second check here can be removed if we need to consider clips longer than 10 minutes
        #                                     ↓           remove me               ↓
        if 'image' not in media['video_name'] and media['duration_millis'] > 600000:  # 600000 millis = 10 mins
            start_time = parse_datetime(report_json['media'][i]['start_timestamp'])
            dive_video_timestamps.append([start_time, start_time + timedelta(milliseconds=media['duration_millis'])])

    #############################################################################################################
    # Main inner loop: iterates through all annotations for the dive and fills out the fields required by DSCRTP
    #############################################################################################################
    for annotation in report_json['annotations']:
        if output_type == 'r':  # only output regular annotations
            if annotation.get('group') == 'localization':
                continue  # skip annotations in the 'localization' group
        else:  # only output localizations
            if annotation.get('group') != 'localization':
                continue  # skip annotations not in the 'localization' group
        concept_name = annotation['concept']

        annotation_row = AnnotationRow(
            annotation=annotation,
            reporter=REPORTER,
            reporter_email=REPORTER_EMAIL
        )  # object to store all annotation information

        # populate simple data from annotation & Dives.csv
        annotation_row.set_sample_id(dive_name=dive_name)
        annotation_row.set_simple_static_data()
        annotation_row.set_ancillary_data(warning_messages=warning_messages)
        annotation_row.set_dive_info(dive_info=dive_dict)

        # get concept info: check WoRMS if specified by user OR if concept info missing from save file
        if concept_name != 'none':
            if concept_name not in concepts:  # if concept name not in saved concepts file, search WoRMS
                if first_round:  # for printing worms header
                    first_round = False
                    print(Messages.WORMS_HEADER)
                concept = Concept(concept_name=concept_name)
                cons_handler = ConceptHandler(concept=concept)
                cons_handler.fetch_worms()
                cons_handler.fetch_vars_synonyms(warning_messages=warning_messages)
                concepts[concept_name] = {
                    'scientific_name': concept.scientific_name,
                    'aphia_id': concept.aphia_id,
                    'authorship': concept.authorship,
                    'synonyms': concept.synonyms,
                    'taxon_rank': concept.taxon_rank,
                    'taxon_ranks': concept.taxon_ranks,
                    'descriptors': concept.descriptors,
                    'vernacular_name': concept.vernacular_names
                }

            annotation_row.set_concept_info(concepts=concepts, warning_messages=warning_messages)  # populate annotation row object with concept info

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
        annotation_row.set_id_ref(warning_messages=warning_messages)
        annotation_row.set_image_paths(
            download_highlight_images=save_highlight_images,
            output_file_path=os.path.join(output_file_path, 'highlight-images'),
            warning_messages=warning_messages,
        )
        annotation_row.set_bounding_box_uuid()

        record = [annotation_row.columns[x] for x in HEADERS]  # convert to list
        report_records.append(record)  # append annotation to a list of all annotations from this dive

    # find associates and hosts
    find_associated_taxa(report_records=report_records, concepts=concepts, warning_messages=warning_messages)

    # remove duplicates (ie records with matching id reference numbers)
    dupes_removed = collapse_id_records(report_records=report_records)

    if load_concepts:
        print('%-30s' % str(dupes_removed), end='')
        sys.stdout.flush()
    else:
        print(f'\n{str(dupes_removed)} duplicate records removed')

    # translate substrate (upon) names - this must be done after finding the associated taxa (relies on concept name)
    for i in range(len(report_records)):
        record = report_records[i]
        if record[SUBSTRATE] == 'organism (dead)':
            record[SUBSTRATE] = 'dead organism'
        elif record[SUBSTRATE] in concepts:
            saved = concepts[record[SUBSTRATE]]
            record[SUBSTRATE] = saved["scientific_name"]
            if saved["descriptors"]:
                record[SUBSTRATE] += f' ({" ".join(saved["descriptors"])})'

    # Add this formatted dive to the full list of report associate_records
    full_report_records += report_records
    print(f'{Color.GREEN}Complete{Color.END}')

# Save everything to output file
print('\nSaving output file...')
os.chdir(save_folder)

with open('concepts.json', 'w') as file:
    json.dump(concepts, file)
os.chdir(output_file_path)

with open(output_file_name + '.tsv', 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file, delimiter='\t')
    csv_writer.writerow(HEADERS[:len(HEADERS) - 3])  # all headers except the last 3
    for record in full_report_records:
        csv_writer.writerow(record[:len(HEADERS) - 3])

print(f'\n{Color.BOLD}Output file saved to:{Color.END} {Color.UNDERLINE}{output_file_path}/{output_file_name}.tsv{Color.END}')
if save_highlight_images:
    print(f'{Color.BOLD}Highlight images saved to:{Color.END} {Color.UNDERLINE}{output_file_path}/highlight-images/{Color.END}')
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

    print(f'{Color.BOLD}Warnings saved to: {Color.END}{Color.UNDERLINE}{OUTPUT_FILE_PATH}/warnings.tsv{Color.END}')

    print(f'\nView messages in console?')
    view_messages = input('\nEnter "y" to view, or press enter to skip >> ').lower() in ['y', 'yes']

    if view_messages:
        print(Messages.WARNINGS_HEADER)
        for message in warning_messages:
            if len(message[1]) > 22:
                message[1] = f'{message[1][:22]}...'
            message[2] = message[2][:37]
            print("%-37s%-25s%-40s%-s" % (message[0], message[1], message[2], message[3]))
