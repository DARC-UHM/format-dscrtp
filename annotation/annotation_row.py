import os
import requests

from datetime import datetime, timezone
from typing import Dict

from annotation.timestamp_processor import TimestampProcessor
from util.constants import NULL_VAL_STRING, HEADERS, NULL_VAL_INT
from util.functions import get_association, convert_username_to_name, get_associations_list, add_meters, \
    translate_substrate_code, grain_size
from util.terminal_output import Color


class AnnotationRow:
    """
    Stores information for a specific annotation. See util.constants.HEADERS for a list of all the columns.
    """

    def __init__(self, annotation: Dict, reporter: str, reporter_email: str):
        """
        :param dict annotation: A VARS annotation object retrieved from the HURL server.
        """
        self.columns = dict(zip(HEADERS, [NULL_VAL_STRING] * len(HEADERS)))  # inits dict of header keys with NA vals
        self.annotation = annotation
        self.reporter = reporter
        self.reporter_email = reporter_email
        self.recorded_time = TimestampProcessor(self.annotation['recorded_timestamp'])
        self.observation_time = TimestampProcessor(self.annotation['observation_timestamp'])

    def set_simple_static_data(self):
        """
        Sets columns values to simple annotation data directly from the annotation JSON object.
        """
        self.columns['VARSConceptName'] = self.annotation['concept']
        self.columns['TrackingID'] = self.annotation['observation_uuid']
        self.columns['AphiaID'] = NULL_VAL_INT
        self.columns['IdentifiedBy'] = convert_username_to_name(self.annotation['observer'])
        self.columns['IdentificationDate'] = self.observation_time.timestamp.strftime('%Y-%m-%d')
        self.columns['IdentificationVerificationStatus'] = 1
        self.columns['DepthMethod'] = 'reported'
        self.columns['ObservationDate'] = self.recorded_time.timestamp.strftime('%Y-%m-%d')
        self.columns['ObservationTime'] = self.recorded_time.timestamp.strftime('%H:%M:%S')
        self.columns['OtherData'] = 'CTD'
        self.columns['Modified'] = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        self.columns['Reporter'] = self.reporter
        self.columns['ReporterEmail'] = self.reporter_email

        self.columns['EntryDate'] = ''  # this column is left blank, to be filled by DSCRTP admin

        # these seven values are hardcoded for now, keeping columns in case of future update
        self.columns['SampleAreaInSquareMeters'] = NULL_VAL_INT
        self.columns['Density'] = NULL_VAL_INT
        self.columns['Cover'] = NULL_VAL_INT
        self.columns['WeightInKg'] = NULL_VAL_INT
        self.columns['SampleAreaInSquareMeters'] = NULL_VAL_INT
        self.columns['Density'] = NULL_VAL_INT
        self.columns['WeightInKg'] = NULL_VAL_INT

    def set_ancillary_data(self, warning_messages: list):
        """
        Sets ancillary data from annotation object. Adds a warning message if ancillary data or lat/long data is
        missing.

        :param list warning_messages: The list of warning messages to display at the end of the script.
        """
        if 'ancillary_data' not in self.annotation:
            warning_messages.append([
                self.columns['SampleID'],
                self.annotation['concept'],
                self.annotation['observation_uuid'],
                f'{Color.RED}No ancillary data found for this record{Color.END}'
            ])
            self.columns['Latitude'] = NULL_VAL_INT
            self.columns['Longitude'] = NULL_VAL_INT
            self.columns['VerbatimLatitude'] = NULL_VAL_INT
            self.columns['VerbatimLongitude'] = NULL_VAL_INT
            self.columns['DepthInMeters'] = NULL_VAL_INT
            self.columns['MinimumDepthInMeters'] = NULL_VAL_INT
            self.columns['MaximumDepthInMeters'] = NULL_VAL_INT
            self.columns['Temperature'] = NULL_VAL_INT
            self.columns['Salinity'] = NULL_VAL_INT
            self.columns['Oxygen'] = NULL_VAL_INT
            return
        if 'latitude' in self.annotation['ancillary_data'] and 'longitude' in self.annotation['ancillary_data']:
            self.columns['Latitude'] = round(self.annotation['ancillary_data']['latitude'], 8)
            self.columns['Longitude'] = round(self.annotation['ancillary_data']['longitude'], 8)
            self.columns['VerbatimLatitude'] = self.annotation['ancillary_data']['latitude']
            self.columns['VerbatimLongitude'] = self.annotation['ancillary_data']['longitude']
        else:
            self.columns['Latitude'] = NULL_VAL_INT
            self.columns['Longitude'] = NULL_VAL_INT
            self.columns['VerbatimLatitude'] = NULL_VAL_INT
            self.columns['VerbatimLongitude'] = NULL_VAL_INT
            # flag warning
            warning_messages.append([
                self.columns['SampleID'],
                self.annotation['concept'],
                self.annotation['observation_uuid'],
                f'{Color.RED}No location data found for this record{Color.END}'
            ])
        self.set_depth(warning_messages=warning_messages)
        self.set_temperature(warning_messages=warning_messages)
        self.set_salinity(warning_messages=warning_messages)
        self.set_oxygen(warning_messages=warning_messages)

    def set_sample_id(self, dive_name: str):
        """
        Sets the SampleID column with the properly formatted SampleID: [DIVE_NAME]_[TIMESTAMP]

        :param str dive_name: The name of the dive, e.g. 'Deep Discoverer 14040201'.
        """
        self.columns['SampleID'] = dive_name.replace(' ',
                                                     '_') + '_' + self.recorded_time.get_formatted_timestamp()

    def set_dive_info(self, dive_info: dict):
        """
        Sets dive-related annotation data from passed dive_info dict.

        :param dict dive_info: A dictionary of information about the dive (imported from Dives.csv).
        """
        self.columns['Citation'] = dive_info['Citation'] if dive_info['Citation'] != NULL_VAL_STRING else ''
        self.columns['Repository'] = dive_info['DataProvider'].split(';')[0] + \
            ' | University of Hawaii Deep-sea Animal Research Center'
        self.columns['Locality'] = dive_info['Locality'].replace(',', ' |')
        self.columns['Ocean'] = dive_info['Ocean']
        self.columns['LargeMarineEcosystem'] = dive_info['LargeMarineEcosystem']
        self.columns['Country'] = dive_info['Country']
        self.columns['FishCouncilRegion'] = dive_info['FishCouncilRegion']
        self.columns['SurveyID'] = dive_info['SurveyID']
        self.columns['Vessel'] = dive_info['Vessel']
        self.columns['PI'] = dive_info['PI']
        self.columns['PIAffiliation'] = dive_info['PIAffiliation']
        self.columns['Purpose'] = dive_info['Purpose']
        self.columns['Station'] = dive_info['Station']
        self.columns['EventID'] = dive_info['EventID']
        self.columns['SamplingEquipment'] = dive_info['SamplingEquipment']
        self.columns['VehicleName'] = dive_info['VehicleName']
        self.columns['LocationAccuracy'] = \
            add_meters(dive_info['LocationAccuracy']) if dive_info['LocationAccuracy'] != 'NA' else ''
        self.columns['NavType'] = \
            'USBL' if dive_info['Vessel'] == 'Okeanos Explorer' or dive_info['Vessel'] == 'Nautilus' else 'NA'
        self.columns['WebSite'] = dive_info['WebSite']
        self.columns['DataProvider'] = dive_info['DataProvider']
        self.columns['DataContact'] = dive_info['DataContact']

    def set_concept_info(self, concepts: dict, warning_messages: list):
        """
        Sets annotation's concept info from saved concept dict.

        :param dict concepts: Dictionary of all locally saved concepts.
        :param list warning_messages: The list of warning messages to display at the end of the script.
        """
        concept_name = self.annotation['concept']
        scientific_name = concepts[concept_name]['scientific_name']
        aphia_id = concepts[concept_name]['aphia_id']
        taxon_ranks = concepts[concept_name]['taxon_ranks']

        self.columns['ScientificName'] = scientific_name
        self.columns['VernacularName'] = concepts[concept_name]['vernacular_name']
        self.columns['TaxonRank'] = concepts[concept_name]['taxon_rank']
        self.columns['AphiaID'] = aphia_id

        if scientific_name == NULL_VAL_STRING:
            warning_messages.append([
                self.columns['SampleID'],
                self.annotation['concept'],
                self.annotation['observation_uuid'],
                f'{Color.RED}Concept name {concept_name} is {NULL_VAL_STRING} (no WoRMS match found){Color.END}'
            ])

        if self.columns['AphiaID'] != NULL_VAL_INT:
            self.columns['LifeScienceIdentifier'] = f'urn:lsid:marinespecies.org:taxname:{aphia_id}'

        # Fill out the taxonomy from the taxon ranks
        if taxon_ranks != {}:
            for key in ['Kingdom', 'Phylum', 'Class', 'Subclass', 'Order', 'Suborder', 'Family',
                        'Subfamily', 'Genus', 'Subgenus', 'Species', 'Subspecies']:
                if key in taxon_ranks:
                    self.columns[key] = taxon_ranks[key]

        self.columns['ScientificNameAuthorship'] = concepts[concept_name]['authorship']
        self.columns['CombinedNameID'] = scientific_name

        if concepts[concept_name]['descriptors']:
            self.columns['Morphospecies'] = ' '.join(concepts[concept_name]['descriptors'])
            if self.columns['CombinedNameID'] != NULL_VAL_STRING:
                self.columns['CombinedNameID'] += f' {self.columns["Morphospecies"]}'
            else:
                self.columns['CombinedNameID'] = self.columns['Morphospecies']

        self.columns['Synonyms'] = ' | '.join(concepts[concept_name]['synonyms']) \
            if concepts[concept_name]['synonyms'] else NULL_VAL_STRING

        if '/' in concept_name:
            self.columns['IdentificationComments'] = concept_name.replace('/', ' or ')

    def set_media_type(self, media_type: str):
        """
        Populates the 'RecordType' column with the passed media type if it is an annotation of an organism.

        :param str media_type: The type of media for the annotation record ('still image' or 'video observation').
        """
        self.columns['RecordType'] = media_type
        if self.columns['ScientificName'] != NULL_VAL_STRING:
            self.columns['IdentificationQualifier'] = \
                'ID by expert from video' if media_type == 'video observation' else 'ID by expert from image'

    def set_id_comments(self):
        """
        Populates 'IdentificationQualifier' column with ID comments from annotation object.
        """
        id_comments = get_association(self.annotation, 'identity-certainty')
        if id_comments:
            id_comments = id_comments['link_value']
            id_comments = id_comments.split('; ')
            if 'maybe' in id_comments:
                self.columns['IdentificationQualifier'] = self.columns['IdentificationQualifier'] + ' | ID Uncertain'
                id_comments.remove('maybe')
            id_comments = ' | '.join(id_comments)
            self.columns['IdentificationComments'] = id_comments if id_comments != '' else NULL_VAL_STRING

    def set_indv_count_and_cat_abundance(self):
        """
        Populates the 'IndividualCount' and 'CategoricalAbundance' columns from annotation object.
        """
        pop_quantity = get_association(self.annotation, 'population-quantity')
        if pop_quantity:
            self.columns['IndividualCount'] = pop_quantity['link_value']
        elif self.columns['ScientificName'] != NULL_VAL_STRING:
            self.columns['IndividualCount'] = '1'
        else:
            self.columns['IndividualCount'] = NULL_VAL_INT
        cat_abundance = get_association(self.annotation, 'categorical-abundance')
        if cat_abundance:  # if there are a lot of cats
            self.columns['CategoricalAbundance'] = cat_abundance['link_value']
            self.columns['IndividualCount'] = NULL_VAL_INT

    def set_size(self, warning_messages: list):
        """
        Populates columns related to size ('VerbatimSize', 'MinimumSize', and 'MaximumSize') with the size from the
        annotation object. Saves a warning message if the size in the annotation object does not match one of the
        expected size categories.

        :param list warning_messages: The list of warning messages to display at the end of the script.
        """
        min_size = NULL_VAL_INT
        max_size = NULL_VAL_INT
        size_str = NULL_VAL_STRING
        size_category = get_association(self.annotation, 'size')
        old_size_category = get_association(self.annotation, 'length-centimeters')  # old VARS data
        if size_category:
            if size_category['to_concept'] != 'nil':
                size_str = size_category['to_concept']
            else:
                # another old VARS used 'link_value' instead of 'to_concept' :)
                size_str = size_category['link_value']

            if size_str == 'greater than 100 cm':
                min_size = '101'
            elif '-' in size_str and 'cm' in size_str:
                # turn a 'size category' into a maximum and minimum size
                sizes = size_str.replace(' ', '-').split('-')
                min_size = sizes[0]
                max_size = sizes[1]
            else:
                warning_messages.append([
                    self.columns['SampleID'],
                    self.annotation['concept'],
                    self.annotation['observation_uuid'],
                    f'Unable to parse size string: {Color.BOLD}"{size_str}"{Color.END}'
                ])
        elif old_size_category:
            size_str = old_size_category['link_value']
            if '-' in size_str and len(size_str.split('-')) == 2:
                sizes = size_str.split('-')
                min_size = sizes[0]
                max_size = sizes[1]
            else:
                warning_messages.append([
                    self.columns['SampleID'],
                    self.annotation['concept'],
                    self.annotation['observation_uuid'],
                    f'Unable to parse size string: {Color.BOLD}"{size_str}"{Color.END}'
                ])
        self.columns['VerbatimSize'] = size_str
        self.columns['MinimumSize'] = min_size
        self.columns['MaximumSize'] = max_size

    def set_condition_comment(self, warning_messages: list):
        """
        Populates the 'Condition' column with information from the annotation object. Assumes all organisms are 'Live'
        unless otherwise noted. Saves a warning message if a dead animal is reported.

        :param list warning_messages: The list of warning messages to display at the end of the script.
        """
        condition_comment = get_association(self.annotation, 'condition-comment')
        if condition_comment:
            if condition_comment['link_value'] in ['dead', 'Dead']:
                # flag warning
                warning_messages.append([
                    self.columns['SampleID'],
                    self.annotation['concept'],
                    self.annotation['observation_uuid'],
                    'Dead animal reported',
                ])
                self.columns['Condition'] = 'Dead'
            else:
                self.columns['Condition'] = 'Damaged'
        else:
            self.columns['Condition'] = 'Live' if self.columns['ScientificName'] != NULL_VAL_STRING else NULL_VAL_STRING

    def set_comments_and_sample(self):
        """
        Populates 'OccurrenceComments' column with information from the annotation object. If there is a sample, appends
        the sample ID to the 'TrackingID' column and appends a note to 'OccurrenceComments'.
        """
        # build occurrence remark string
        occurrence_remark = get_associations_list(self.annotation, 'occurrence-remark')
        remark_string = NULL_VAL_STRING
        if occurrence_remark:
            remark_list = []
            for remark in occurrence_remark:
                remark_list.append(remark['link_value'])
            remark_string = ' | '.join(remark_list)
        if self.columns['VerbatimSize'] != NULL_VAL_STRING:
            if remark_string != NULL_VAL_STRING:
                remark_string += ' | size is estimated greatest length of individual in cm.' \
                                 ' Size estimations placed into size category bins'
            else:
                remark_string = 'size is estimated greatest length of individual in cm.' \
                                ' Size estimations placed into size category bins'

        # old VARS data
        observation_notes = get_association(self.annotation, 'observation notes')
        if observation_notes:
            if remark_string != NULL_VAL_STRING:
                remark_string += f' | notes: {observation_notes["link_value"]}'
            else:
                remark_string = f'notes: {observation_notes["link_value"]}'

        # old VARS data
        habitat_comment = get_association(self.annotation, 'habitat-comment')
        if habitat_comment:
            if remark_string != NULL_VAL_STRING:
                remark_string += f' | comment: {habitat_comment["link_value"]}'
            else:
                remark_string = f'comment: {habitat_comment["link_value"]}'

        sampled_by = get_association(self.annotation, 'sampled-by')
        if sampled_by and 'to_concept' in sampled_by.keys():
            if remark_string != NULL_VAL_STRING:
                remark_string += f' | sampled by {sampled_by["to_concept"]}'
            else:
                remark_string = f'sampled by {sampled_by["to_concept"]}'
        sample_ref = get_association(self.annotation, 'sample-reference')
        if sample_ref:
            self.columns['TrackingID'] += f' | {sample_ref["link_value"]}'

        self.columns['OccurrenceComments'] = remark_string

    def set_cmecs_geo(self, cmecs_geo: str):
        """
        Sets the 'CMECSGeoForm' column to the value passed in the function call.

        :param str cmecs_geo: The current habitat.
        """
        self.columns['CMECSGeoForm'] = cmecs_geo

    def set_habitat(self, warning_messages):
        """
        Populates the 'Habitat' with information from the annotation object. Adds a warning message if one of the
        habitats is missing or cannot be parsed.

        :param list warning_messages: The list of warning messages to display at the end of the script.
        """
        secondary = []
        s1 = get_association(self.annotation, 's1')
        if s1:
            primary = translate_substrate_code(s1['to_concept'])
            if not primary:
                primary = translate_substrate_code(s1['link_value'])  # this is how the data is stored in old VARS
            if not primary:
                # flag warning
                warning_messages.append([
                    self.columns['SampleID'],
                    self.annotation['concept'],
                    self.annotation['observation_uuid'],
                    f'{Color.RED}Missing s1 or could not parse substrate code:{Color.END} '
                    f'{Color.BOLD}to_concept: {s1["to_concept"]}, link_value: {s1["link_value"]}{Color.END}'
                ])
            else:
                self.columns['Habitat'] = f'primarily: {primary}'
        elif self.columns['ScientificName'] != NULL_VAL_STRING:
            # flag warning
            warning_messages.append([
                self.columns['SampleID'],
                self.annotation['concept'],
                self.annotation['observation_uuid'],
                f'{Color.RED}Missing s1{Color.END}'
            ])

        s2_records = get_associations_list(self.annotation, 's2')
        if len(s2_records) != 0:
            s2s_list = []
            failures = []
            for s2 in s2_records:  # remove duplicates
                if s2['to_concept'] == 'nil' or s2['to_concept'] == 'self':
                    # this is old VARS data, formatted as one record separated by semicolons
                    s2s_list = s2['link_value'].replace(',', ';').replace('; ', ';').replace(';;', ';')\
                        .replace(' ', ';').replace(':', ';').replace("'", ';').split(';')
                elif s2['to_concept'] not in s2s_list:
                    s2s_list.append(s2['to_concept'])
            s2s_list.sort(key=grain_size)
            for s2 in s2s_list:
                s2_temp = translate_substrate_code(s2)
                if s2_temp:
                    secondary.append(s2_temp)
                else:
                    failures.append(s2)
            if len(secondary) != len(s2s_list):
                warning_messages.append([
                    self.columns['SampleID'],
                    self.annotation['concept'],
                    self.annotation['observation_uuid'],
                    f'Could not parse s2 substrate codes {Color.BOLD}{failures}{Color.END}'
                ])
            self.columns['Habitat'] = self.columns['Habitat'] + f' / secondary: {"; ".join(secondary)}'
        habitat_comment = get_association(self.annotation, 'habitat-comment')
        if habitat_comment:
            self.columns['Habitat'] = self.columns['Habitat'] + f' / comments: {habitat_comment["link_value"]}'

    def set_upon(self):
        """
        Sets the 'Substrate' column if there is an 'upon' record in the annotation object.
        """
        upon = get_association(self.annotation, 'upon')
        self.columns['UponIsCreature'] = False
        if upon:
            subs = translate_substrate_code(upon['to_concept'])
            if subs:
                self.columns['Substrate'] = subs
            else:
                # the item in 'upon' is not in the substrate list, so it must be upon another creature
                self.columns['UponIsCreature'] = True

                if upon['to_concept'] == 'orgsp':
                    self.columns['Substrate'] = 'Porifera'
                    notes = get_association(self.annotation, 'observation notes')
                    if notes and 'dead' in notes['link_value']:
                        self.columns['Substrate'] += ' (dead)'
                if upon['to_concept'] == 'orgcr':
                    self.columns['Substrate'] = 'Crustacea'
                    comment = get_association(self.annotation, 'comment')
                    if comment:
                        comment = comment['link_value'].split(';')[0].split(' ')
                        if comment[0] == 'on':
                            self.columns['Substrate'] = comment[1]
                else:
                    self.columns['Substrate'] = upon['to_concept']

    def set_id_ref(self, warning_messages: list):
        """
        Sets the 'IdentityReference' column with the value pulled from the annotation object. ID reference is populated
        when there are multiple annotations with the exact same animal.
        """
        identity_reference = get_association(self.annotation, 'identity-reference')
        if identity_reference:
            if identity_reference['link_value'] == '':
                self.columns['IdentityReference'] = -1
                warning_messages.append([
                    self.columns['SampleID'],
                    self.annotation['concept'],
                    self.annotation['observation_uuid'],
                    f'{Color.YELLOW}An identity-reference exists for this record, but it is empty{Color.END}'
                ])
            else:
                self.columns['IdentityReference'] = int(identity_reference['link_value'])
        else:
            self.columns['IdentityReference'] = -1

    def set_depth(self, warning_messages: list):
        """
        Sets depth based on data from annotation object. Adds a warning message if depth is missing.

        :param list warning_messages: The list of warning messages to display at the end of the script.
        """
        if 'depth_meters' in self.annotation['ancillary_data'] \
                and self.annotation['ancillary_data']['depth_meters'] != 0:
            self.columns['DepthInMeters'] = round(self.annotation['ancillary_data']['depth_meters'], 3)
        else:
            self.columns['DepthInMeters'] = NULL_VAL_INT
            warning_messages.append([
                self.columns['SampleID'],
                self.annotation['concept'],
                self.annotation['observation_uuid'],
                f'{Color.YELLOW}No depth data found for this record{Color.END}'
            ])
        self.columns['MinimumDepthInMeters'] = self.columns['DepthInMeters']
        self.columns['MaximumDepthInMeters'] = self.columns['DepthInMeters']

    def set_temperature(self, warning_messages: list):
        """
        Sets temperature based on data from annotation object. Adds a warning message if temperature is missing.

        :param list warning_messages: The list of warning messages to display at the end of the script.
        """
        if 'temperature_celsius' in self.annotation['ancillary_data']:
            self.columns['Temperature'] = round(self.annotation['ancillary_data']['temperature_celsius'], 4)
        else:
            self.columns['Temperature'] = NULL_VAL_INT
            # flag warning
            warning_messages.append([
                self.columns['SampleID'],
                self.annotation['concept'],
                self.annotation['observation_uuid'],
                'No temperature measurement included in this record'
            ])

    def set_salinity(self, warning_messages: list):
        """
        Sets salinity based on data from annotation object. Adds a warning message if salinity is missing.

        :param list warning_messages: The list of warning messages to display at the end of the script.
        """
        if 'salinity' in self.annotation['ancillary_data']:
            self.columns['Salinity'] = round(self.annotation['ancillary_data']['salinity'], 4)
        else:
            self.columns['Salinity'] = NULL_VAL_INT
            # flag warning
            warning_messages.append([
                self.columns['SampleID'],
                self.annotation['concept'],
                self.annotation['observation_uuid'],
                'No salinity measurement included in this record'
            ])

    def set_oxygen(self, warning_messages: list):
        """
        Populates the 'Oxygen' column with data from the annotation object. Adds a warning message if oxygen data is
        missing.

        :param list warning_messages: The list of warning messages to display at the end of the script.
        """
        if 'oxygen_ml_l' in self.annotation['ancillary_data']:
            self.columns['Oxygen'] = round(self.annotation['ancillary_data']['oxygen_ml_l'], 4)
        else:
            self.columns['Oxygen'] = NULL_VAL_INT
            # flag warning
            warning_messages.append([
                self.columns['SampleID'],
                self.annotation['concept'],
                self.annotation['observation_uuid'],
                'No oxygen measurement included in this record'
            ])

    def set_image_paths(self, download_highlight_images: bool, output_file_path: str, warning_messages: list):
        """
        Populates the 'ImageFilePath' and 'HighlightImageFilePath' columns with information from the annotation object.

        :param download_highlight_images: whether or not to download the highlight images and save to local machine.
        :param output_file_path: where to save the images
        :param list warning_messages: The list of warning messages to display at the end of the script.
        """
        images = self.annotation['image_references']
        image_paths = []
        for image in images:
            image_paths.append(image['url'].replace(
                'http://hurlstor.soest.hawaii.edu/imagearchive',
                'https://hurlimage.soest.hawaii.edu')
            )
        if len(image_paths) == 1:
            self.columns['ImageFilePath'] = image_paths[0]
        elif len(image_paths) > 1:
            if '.png' in image_paths[0]:
                self.columns['ImageFilePath'] = image_paths[0]
            else:
                self.columns['ImageFilePath'] = image_paths[1]

        # for old VARS :)
        photo_references = get_association(self.annotation, 'photo-reference')
        if photo_references:
            photo_references = photo_references['link_value'].split(';')
            photo_references[0] = photo_references[0].replace('http://max5kn1.soest.hawaii.edu/imagearchive/', '')
            path = photo_references[0].split('/')
            path.pop()
            path = f'https://hurlimage.soest.hawaii.edu/{"/".join(path)}'
            photo_references[0] = f'https://hurlimage.soest.hawaii.edu/{photo_references[0]}'
            for i in range(1, len(photo_references)):
                photo_references[i] = f'{path}/{photo_references[i]}'
            for image_path in photo_references:
                if self.columns['ImageFilePath'] != NULL_VAL_STRING:
                    self.columns['ImageFilePath'] += f' | {image_path}'
                else:
                    self.columns['ImageFilePath'] = image_path

        highlight_image = get_association(self.annotation, 'guide-photo')
        if highlight_image and (highlight_image['to_concept'] == '1 best' or highlight_image['to_concept'] == '2 good'):
            self.columns['HighlightImageFilePath'] = self.columns['ImageFilePath']
            if download_highlight_images:
                for image_url in self.columns['HighlightImageFilePath'].split(' | '):
                    res = requests.get(image_url)
                    if res.status_code == 200:
                        os.chdir(output_file_path)
                        with open(self.columns['ImageFilePath'].split('/')[-1], 'wb') as file:
                            file.write(res.content)
                    else:
                        warning_messages.append([
                            self.columns['SampleID'],
                            self.annotation['concept'],
                            self.annotation['observation_uuid'],
                            'Error downloading image',
                        ])

        population_density = get_association(self.annotation, 'population-density')
        if population_density and population_density['link_value'] == 'dense':
            self.columns['HighlightImageFilePath'] = self.columns['ImageFilePath']

    def set_bounding_box_uuid(self):
        """
        Sets the 'BoundingBoxID' column with the value pulled from the annotation object.
        """
        bounding_box = get_association(self.annotation, 'bounding box')
        if bounding_box:
            self.columns['BoundingBoxID'] = bounding_box['uuid']
