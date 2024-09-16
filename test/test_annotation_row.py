from annotation.annotation_row import AnnotationRow
from annotation.timestamp_processor import TimestampProcessor
from test.data_for_tests import annotations, dive_dict, concepts
from util.constants import HEADERS, NULL_VAL_STRING, NULL_VAL_INT


class TestAnnotationRow:

    def test_init(self):
        test_row = AnnotationRow(annotation=annotations[0], reporter='test', reporter_email='test@test.com')
        i = 0
        for key in test_row.columns.keys():
            assert key == HEADERS[i]
            i += 1
        for val in test_row.columns.values():
            assert val == NULL_VAL_STRING
        assert test_row.annotation == annotations[0]
        assert test_row.reporter == 'test'
        assert test_row.reporter_email == 'test@test.com'
        assert test_row.recorded_time.timestamp == \
               TimestampProcessor(test_row.annotation['recorded_timestamp']).timestamp
        assert test_row.observation_time.timestamp == \
               TimestampProcessor(test_row.annotation['observation_timestamp']).timestamp

    def test_simple_static_data(self):
        test_row = AnnotationRow(annotation=annotations[1], reporter='Bingo, Sarah', reporter_email='sarahr6@hawaii.edu')
        test_row.set_simple_static_data()
        assert test_row.columns['VARSConceptName'] == 'Paralepididae'
        assert test_row.columns['TrackingID'] == '0d9133d7-1d49-47d5-4b6d-6e4fb25dd41e'
        assert test_row.columns['AphiaID'] == NULL_VAL_INT
        assert test_row.columns['IdentifiedBy'] == 'Putts, Meagan'
        assert test_row.columns['IdentificationDate'] == test_row.observation_time.timestamp.strftime('%Y-%m-%d')
        assert test_row.columns['IdentificationVerificationStatus'] == 1
        assert test_row.columns['DepthMethod'] == 'reported'
        assert test_row.columns['ObservationDate'] == test_row.recorded_time.timestamp.strftime('%Y-%m-%d')
        assert test_row.columns['ObservationTime'] == test_row.recorded_time.timestamp.strftime('%H:%M:%S')
        assert test_row.columns['OtherData'] == 'CTD'
        # skip checking 'Modified' column (initialized to current time)
        assert test_row.columns['Reporter'] == 'Bingo, Sarah'
        assert test_row.columns['ReporterEmail'] == 'sarahr6@hawaii.edu'
        assert test_row.columns['EntryDate'] == ''
        assert test_row.columns['SampleAreaInSquareMeters'] == NULL_VAL_INT
        assert test_row.columns['Density'] == NULL_VAL_INT
        assert test_row.columns['Cover'] == NULL_VAL_INT
        assert test_row.columns['WeightInKg'] == NULL_VAL_INT
        assert test_row.columns['SampleAreaInSquareMeters'] == NULL_VAL_INT
        assert test_row.columns['Density'] == NULL_VAL_INT
        assert test_row.columns['WeightInKg'] == NULL_VAL_INT

    def test_set_ancillary_data(self):
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        warnings = []
        test_row.set_ancillary_data(warnings)
        assert test_row.columns['Latitude'] == round(38.793148973388, 8)
        assert test_row.columns['Longitude'] == round(-72.992393976812, 8)
        assert test_row.columns['VerbatimLatitude'] == 38.793148973388
        assert test_row.columns['VerbatimLongitude'] == -72.992393976812
        assert warnings == []

    def test_set_ancillary_data_missing_location(self):
        test_row = AnnotationRow(annotation=annotations[0], reporter='test', reporter_email='test')
        warnings = []
        test_row.set_ancillary_data(warnings)
        assert test_row.columns['Latitude'] == NULL_VAL_INT
        assert test_row.columns['Longitude'] == NULL_VAL_INT
        assert test_row.columns['VerbatimLatitude'] == NULL_VAL_INT
        assert test_row.columns['VerbatimLongitude'] == NULL_VAL_INT
        assert len(warnings) == 1

    def test_set_ancillary_data_missing_data(self):
        test_row = AnnotationRow(annotation=annotations[5], reporter='test', reporter_email='test')
        warnings = []
        test_row.set_ancillary_data(warnings)
        assert len(warnings) == 1

    def test_set_sample_id(self):
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.set_sample_id('my test dive :)')
        assert test_row.columns['SampleID'] == 'my_test_dive_:)_' + test_row.recorded_time.get_formatted_timestamp()

    def test_set_dive_info(self):
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.set_dive_info(dive_dict)
        assert test_row.columns['Citation'] == ''
        assert test_row.columns['Repository'] == \
               'Ocean Exploration Trust | University of Hawaii Deep-sea Animal Research Center'
        assert test_row.columns['Locality'] == \
               'Papah_naumoku_kea Marine National Monument (PMNM) | Northwestern Hawaiian Islands | Unnamed Seamount A'
        assert test_row.columns['Ocean'] == 'North Pacific'
        assert test_row.columns['LargeMarineEcosystem'] == 'Insular Pacific-Hawaiian'
        assert test_row.columns['Country'] == 'USA'
        assert test_row.columns['FishCouncilRegion'] == 'Western Pacific'
        assert test_row.columns['SurveyID'] == 'NA134'
        assert test_row.columns['Vessel'] == 'Nautilus'
        assert test_row.columns['PI'] == 'Kelley, Christopher; Kosaki, Randy; Orcutt, Beth; Petruncio, Emil'
        assert test_row.columns['PIAffiliation'] == 'NA'
        assert test_row.columns['Purpose'] == 'Document whether these underwater mountains support vibrant coral ' \
                                              'and sponge communities like others in the region'
        assert test_row.columns['Station'] == 'NA134-H1884'
        assert test_row.columns['EventID'] == 'NA134-H1884'
        assert test_row.columns['SamplingEquipment'] == 'ROV'
        assert test_row.columns['VehicleName'] == 'Hercules'
        assert test_row.columns['LocationAccuracy'] == '50m'
        assert test_row.columns['NavType'] == 'USBL'
        assert test_row.columns['WebSite'] == 'https://nautiluslive.org/cruise/na134'
        assert test_row.columns['DataProvider'] == 'Ocean Exploration Trust; University of Hawaiʻi'
        assert test_row.columns['DataContact'] == 'Bingo, Sarah; sarahr6@hawaii.edu'

    def test_set_concept_info_no_descriptors(self):
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.set_concept_info(concepts, warning_messages=[])
        assert test_row.columns['ScientificName'] == 'Paralepididae'
        assert test_row.columns['VernacularName'] == 'barracudinas'
        assert test_row.columns['TaxonRank'] == 'Family'
        assert test_row.columns['AphiaID'] == 125447
        assert test_row.columns['LifeScienceIdentifier'] == 'urn:lsid:marinespecies.org:taxname:125447'
        assert test_row.columns['Kingdom'] == 'Animalia'
        assert test_row.columns['Phylum'] == 'Chordata'
        assert test_row.columns['Class'] == 'Teleostei'
        assert test_row.columns['Subclass'] == NULL_VAL_STRING
        assert test_row.columns['Order'] == 'Aulopiformes'
        assert test_row.columns['Suborder'] == NULL_VAL_STRING
        assert test_row.columns['Family'] == 'Paralepididae'
        assert test_row.columns['Subfamily'] == NULL_VAL_STRING
        assert test_row.columns['Genus'] == NULL_VAL_STRING
        assert test_row.columns['Subgenus'] == NULL_VAL_STRING
        assert test_row.columns['Species'] == NULL_VAL_STRING
        assert test_row.columns['Subspecies'] == NULL_VAL_STRING
        assert test_row.columns['ScientificNameAuthorship'] == 'Bonaparte, 1835'
        assert test_row.columns['CombinedNameID'] == 'Paralepididae'
        assert test_row.columns['Morphospecies'] == NULL_VAL_STRING
        assert test_row.columns['Synonyms'] == NULL_VAL_STRING

    def test_set_concept_info_descriptors(self):
        test_row = AnnotationRow(annotation=annotations[3], reporter='test', reporter_email='test')
        test_row.set_concept_info(concepts, warning_messages=[])
        assert test_row.columns['ScientificName'] == 'Demospongiae'
        assert test_row.columns['VernacularName'] == 'demosponges | horny sponges'
        assert test_row.columns['TaxonRank'] == 'Class'
        assert test_row.columns['AphiaID'] == 164811
        assert test_row.columns['LifeScienceIdentifier'] == 'urn:lsid:marinespecies.org:taxname:164811'
        assert test_row.columns['Kingdom'] == 'Animalia'
        assert test_row.columns['Phylum'] == 'Porifera'
        assert test_row.columns['Class'] == 'Demospongiae'
        assert test_row.columns['Subclass'] == NULL_VAL_STRING
        assert test_row.columns['Order'] == NULL_VAL_STRING
        assert test_row.columns['Suborder'] == NULL_VAL_STRING
        assert test_row.columns['Family'] == NULL_VAL_STRING
        assert test_row.columns['Subfamily'] == NULL_VAL_STRING
        assert test_row.columns['Genus'] == NULL_VAL_STRING
        assert test_row.columns['Subgenus'] == NULL_VAL_STRING
        assert test_row.columns['Species'] == NULL_VAL_STRING
        assert test_row.columns['Subspecies'] == NULL_VAL_STRING
        assert test_row.columns['ScientificNameAuthorship'] == 'Sollas, 1885'
        assert test_row.columns['CombinedNameID'] == 'Demospongiae encrusting'
        assert test_row.columns['Morphospecies'] == 'encrusting'
        assert test_row.columns['Synonyms'] == 'hehe | test'

    def test_set_media_type(self):
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.columns['ScientificName'] = 'this was a triumph'
        test_row.set_media_type('im making a note here, huge success')  # it's hard to overstate my satisfaction
        assert test_row.columns['RecordType'] == 'im making a note here, huge success'
        assert test_row.columns['IdentificationQualifier'] == 'ID by expert from image'

    def test_set_media_type_no_name(self):
        test_row = AnnotationRow(annotation=annotations[4], reporter='test', reporter_email='test')
        test_row.set_media_type('still image')
        assert test_row.columns['RecordType'] == 'still image'
        assert test_row.columns['IdentificationQualifier'] == NULL_VAL_STRING

    def test_set_id_comments_maybe(self):
        test_row = AnnotationRow(annotation=annotations[2], reporter='test', reporter_email='test')
        test_row.columns['ScientificName'] = 'test'
        test_row.columns['IdentificationQualifier'] = 'ID by expert from taste'
        test_row.set_id_comments()
        assert test_row.columns['IdentificationQualifier'] == 'ID by expert from taste | ID Uncertain'
        assert test_row.columns['IdentificationComments'] == NULL_VAL_STRING

    def test_set_id_comments_other(self):
        test_row = AnnotationRow(annotation=annotations[6], reporter='test', reporter_email='test')
        test_row.columns['ScientificName'] = 'test'
        test_row.columns['IdentificationQualifier'] = 'ID by expert from smell'
        test_row.set_id_comments()
        assert test_row.columns['IdentificationQualifier'] == 'ID by expert from smell'
        assert test_row.columns['IdentificationComments'] == 'small head | long ribbon body'

    def test_set_id_comments_none(self):
        test_row = AnnotationRow(annotation=annotations[4], reporter='test', reporter_email='test')
        test_row.set_id_comments()
        assert test_row.columns['IdentificationQualifier'] == NULL_VAL_STRING
        assert test_row.columns['IdentificationComments'] == NULL_VAL_STRING

    def test_set_indv_count(self):
        test_row = AnnotationRow(annotation=annotations[5], reporter='test', reporter_email='test')
        test_row.set_indv_count_and_cat_abundance()
        assert test_row.columns['IndividualCount'] == '2'
        assert test_row.columns['CategoricalAbundance'] == NULL_VAL_STRING

    def test_set_cat_abundance(self):
        test_row = AnnotationRow(annotation=annotations[7], reporter='test', reporter_email='test')
        test_row.set_indv_count_and_cat_abundance()
        assert test_row.columns['IndividualCount'] == NULL_VAL_INT
        assert test_row.columns['CategoricalAbundance'] == '\u003e100'

    def test_set_indv_count_and_cat_abundance_none(self):
        test_row = AnnotationRow(annotation=annotations[4], reporter='test', reporter_email='test')
        test_row.set_indv_count_and_cat_abundance()
        assert test_row.columns['IndividualCount'] == NULL_VAL_INT
        assert test_row.columns['CategoricalAbundance'] == NULL_VAL_STRING

    def test_set_size(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[8], reporter='test', reporter_email='test')
        test_row.set_size(warnings)
        assert test_row.columns['VerbatimSize'] == '50-100 cm'
        assert test_row.columns['MinimumSize'] == '50'
        assert test_row.columns['MaximumSize'] == '100'
        assert warnings == []

    def test_set_size_no_size(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[4], reporter='test', reporter_email='test')
        test_row.set_size(warnings)
        assert test_row.columns['VerbatimSize'] == NULL_VAL_STRING
        assert test_row.columns['MinimumSize'] == NULL_VAL_INT
        assert test_row.columns['MaximumSize'] == NULL_VAL_INT
        assert warnings == []

    def test_set_size_no_match(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[7], reporter='test', reporter_email='test')
        test_row.set_size(warnings)
        assert test_row.columns['VerbatimSize'] == '51000000 cm'
        assert test_row.columns['MinimumSize'] == NULL_VAL_INT
        assert test_row.columns['MaximumSize'] == NULL_VAL_INT
        assert len(warnings) == 1

    def test_set_condition_comment(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.columns['ScientificName'] = 'Magikarp'
        test_row.set_condition_comment(warnings)
        assert test_row.columns['Condition'] == 'Live'
        assert warnings == []

    def test_set_condition_comment_none(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.set_condition_comment(warnings)
        assert test_row.columns['Condition'] == NULL_VAL_STRING
        assert warnings == []

    def test_set_condition_comment_damaged(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[7], reporter='test', reporter_email='test')
        test_row.set_condition_comment(warnings)
        assert test_row.columns['Condition'] == 'Damaged'
        assert warnings == []

    def test_set_condition_comment_dead(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[8], reporter='test', reporter_email='test')
        test_row.set_condition_comment(warnings)
        assert test_row.columns['Condition'] == 'Dead'
        assert len(warnings) == 1

    def test_set_comments_simple_remark(self):
        test_row = AnnotationRow(annotation=annotations[6], reporter='test', reporter_email='test')
        test_row.set_comments_and_sample()
        assert test_row.columns['OccurrenceComments'] == 'in water column on descent'

    def test_set_comments_simple_size(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[8], reporter='test', reporter_email='test')
        test_row.set_size(warnings)
        test_row.set_comments_and_sample()
        assert test_row.columns['OccurrenceComments'] == 'size is estimated greatest length of individual in cm. Size estimations placed into size category bins'

    def test_set_comments_simple_sample(self):
        test_row = AnnotationRow(annotation=annotations[9], reporter='test', reporter_email='test')
        test_row.columns['TrackingID'] = '1234'
        test_row.set_comments_and_sample()
        assert test_row.columns['OccurrenceComments'] == 'sampled by manipulator'
        assert test_row.columns['TrackingID'] == '1234 | NA134-158-B-MCZ'

    def test_set_comments_and_sample_none(self):
        test_row = AnnotationRow(annotation=annotations[2], reporter='test', reporter_email='test')
        test_row.set_comments_and_sample()
        assert test_row.columns['OccurrenceComments'] == NULL_VAL_STRING

    def test_set_comments_and_sample(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.set_size(warnings)
        test_row.set_comments_and_sample()
        assert test_row.columns['OccurrenceComments'] == \
               'in water column on descent | another remark | size is estimated greatest length of individual in cm. ' \
               'Size estimations placed into size category bins | comment: loose talus | sampled by manipulator'

    def test_set_comments_old_vars(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[10], reporter='test', reporter_email='test')
        test_row.set_size(warnings)
        test_row.set_comments_and_sample()
        assert test_row.columns['OccurrenceComments'] == 'notes: 363;; | comment: karstic'

    def test_set_cmecs_geo(self):
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.set_cmecs_geo('get out of my swamp')
        assert test_row.columns['CMECSGeoForm'] == 'get out of my swamp'

    def test_set_habitat_s1(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[5], reporter='test', reporter_email='test')
        test_row.set_habitat(warnings)
        assert test_row.columns['Habitat'] == 'primarily: sediment'
        assert warnings == []

    def test_set_habitat_s1_none(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[6], reporter='test', reporter_email='test')
        test_row.columns['ScientificName'] = 'Gyarados'
        test_row.set_habitat(warnings)
        assert test_row.columns['Habitat'] == NULL_VAL_STRING
        assert len(warnings) == 1

    def test_set_habitat_s1_fail(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[8], reporter='test', reporter_email='test')
        test_row.set_habitat(warnings)
        assert NULL_VAL_STRING in test_row.columns['Habitat']
        assert len(warnings) == 1

    def test_set_habitat_one_s2(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[3], reporter='test', reporter_email='test')
        test_row.set_habitat(warnings)
        assert test_row.columns['Habitat'] == 'primarily: bedrock / secondary: sediment'
        assert warnings == []

    def test_set_habitat_multiple_s2(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[2], reporter='test', reporter_email='test')
        test_row.set_habitat(warnings)
        assert test_row.columns['Habitat'] == 'primarily: sediment / secondary: boulder; bedrock'
        assert warnings == []

    def test_set_habitat_s2_fail(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[8], reporter='test', reporter_email='test')
        test_row.set_habitat(warnings)
        assert NULL_VAL_STRING in test_row.columns['Habitat']
        assert len(warnings) == 1

    def test_set_habitat_comment(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.set_habitat(warnings)
        print(f'"{test_row.columns["Habitat"]}"')
        print('"primarily: sediment / secondary: man-made trash / comments: loose talus"')
        assert test_row.columns['Habitat'] == 'primarily: sediment / secondary: man-made trash / comments: loose talus'
        assert warnings == []

    def test_set_upon_not_creature(self):
        test_row = AnnotationRow(annotation=annotations[0], reporter='test', reporter_email='test')
        test_row.set_upon()
        assert test_row.columns['UponIsCreature'] is False
        assert test_row.columns['Substrate'] == 'sediment'

    def test_set_upon_is_creature(self):
        test_row = AnnotationRow(annotation=annotations[9], reporter='test', reporter_email='test')
        test_row.set_upon()
        assert test_row.columns['UponIsCreature'] is True
        assert test_row.columns['Substrate'] == 'some creature'

    def test_set_upon_no_upon(self):
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.set_upon()
        assert test_row.columns['UponIsCreature'] is False
        assert test_row.columns['Substrate'] == NULL_VAL_STRING

    def test_set_id_ref(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[9], reporter='test', reporter_email='test')
        test_row.set_id_ref(warnings)
        assert test_row.columns['IdentityReference'] == 51
        assert len(warnings) == 0

    def test_set_id_ref_none(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.set_id_ref(warnings)
        assert test_row.columns['IdentityReference'] == -1
        assert len(warnings) == 0

    def test_set_id_ref_blank(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[10], reporter='test', reporter_email='test')
        test_row.set_id_ref(warnings)
        assert test_row.columns['IdentityReference'] == -1
        assert len(warnings) == 1

    def test_set_depth(self):
        test_row = AnnotationRow(annotation=annotations[0], reporter='test', reporter_email='test')
        warnings = []
        test_row.set_depth(warnings)
        assert test_row.columns['DepthInMeters'] == round(668.458984375, 4)
        assert test_row.columns['MinimumDepthInMeters'] == 668.459
        assert test_row.columns['MaximumDepthInMeters'] == 668.459
        assert warnings == []

    def test_set_depth_missing(self):
        test_row = AnnotationRow(annotation=annotations[2], reporter='test', reporter_email='test')
        warnings = []
        test_row.set_depth(warnings)
        assert test_row.columns['DepthInMeters'] == NULL_VAL_INT
        assert test_row.columns['MinimumDepthInMeters'] == NULL_VAL_INT
        assert test_row.columns['MaximumDepthInMeters'] == NULL_VAL_INT
        assert len(warnings) == 1

    def test_set_temperature(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.set_temperature(warnings)
        assert test_row.columns['Temperature'] == 5.126
        assert warnings == []

    def test_set_temperature_none(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[4], reporter='test', reporter_email='test')
        test_row.set_temperature(warnings)
        assert test_row.columns['Temperature'] == NULL_VAL_INT
        assert len(warnings) == 1

    def test_set_salinity(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.set_salinity(warnings)
        assert test_row.columns['Salinity'] == 35.8649
        assert warnings == []

    def test_set_salinity_none(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[4], reporter='test', reporter_email='test')
        test_row.set_salinity(warnings)
        assert test_row.columns['Salinity'] == NULL_VAL_INT
        assert len(warnings) == 1

    def test_set_oxygen(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.set_oxygen(warnings)
        assert test_row.columns['Oxygen'] == 7.3196
        assert warnings == []

    def test_set_oxygen_none(self):
        warnings = []
        test_row = AnnotationRow(annotation=annotations[4], reporter='test', reporter_email='test')
        test_row.set_oxygen(warnings)
        assert test_row.columns['Oxygen'] == NULL_VAL_INT
        assert len(warnings) == 1

    def test_set_image_paths_one_no_hl(self):
        test_row = AnnotationRow(annotation=annotations[7], reporter='test', reporter_email='test')
        test_row.set_image_paths(download_highlight_images=False, output_file_path='', warning_messages=[])
        assert test_row.columns['ImageFilePath'] == 'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1895/cam1_20211130090725.png'
        assert test_row.columns['HighlightImageFilePath'] == NULL_VAL_STRING

    def test_set_image_paths_one_hl_best(self):
        test_row = AnnotationRow(annotation=annotations[6], reporter='test', reporter_email='test')
        test_row.set_image_paths(download_highlight_images=False, output_file_path='', warning_messages=[])
        assert test_row.columns['ImageFilePath'] == 'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/D2photos/EX1404photos/EX1404L2_DIVE01_20140905/EX1404L2_IMG_20140905T135040Z_ROVHD_NICE_EEL_BOTTOM.png'
        assert test_row.columns['HighlightImageFilePath'] == 'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/D2photos/EX1404photos/EX1404L2_DIVE01_20140905/EX1404L2_IMG_20140905T135040Z_ROVHD_NICE_EEL_BOTTOM.png'

    def test_set_image_paths_one_hl_dense(self):
        test_row = AnnotationRow(annotation=annotations[8], reporter='test', reporter_email='test')
        test_row.set_image_paths(download_highlight_images=False, output_file_path='', warning_messages=[])
        assert test_row.columns['ImageFilePath'] == 'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1895/cam1_20211130080700.png'
        assert test_row.columns['HighlightImageFilePath'] == 'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1895/cam1_20211130080700.png'

    def test_set_image_paths_multiple(self):
        test_row = AnnotationRow(annotation=annotations[9], reporter='test', reporter_email='test')
        test_row.set_image_paths(download_highlight_images=False, output_file_path='', warning_messages=[])
        assert test_row.columns['ImageFilePath'] == 'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/Hphotos/NA134photos/H1895/cam1_20211130145709.png'
        assert test_row.columns['HighlightImageFilePath'] == NULL_VAL_STRING

    def test_old_vars_image_paths(self):
        test_row = AnnotationRow(annotation=annotations[10], reporter='test', reporter_email='test')
        test_row.set_image_paths(download_highlight_images=False, output_file_path='', warning_messages=[])
        assert test_row.columns['ImageFilePath'] == 'https://hurlimage.soest.hawaii.edu/SupplementalPhotos/P5photos/P5-653/P5-653-042.tif | https://hurlimage.soest.hawaii.edu/SupplementalPhotos/P5photos/P5-653/P5-653-d3-13238a1.tif | https://hurlimage.soest.hawaii.edu/SupplementalPhotos/P5photos/P5-653/P5-653-d3-13238a2.tif'
        assert test_row.columns['HighlightImageFilePath'] == NULL_VAL_STRING

    def test_set_bounding_box_uuid_single(self):
        test_row = AnnotationRow(annotation=annotations[0], reporter='test', reporter_email='test')
        test_row.set_bounding_box_uuid()
        assert test_row.columns['BoundingBoxID'] == 'b860c165-078e-4715-8bc3-491039679b67'

    def test_set_bounding_box_uuid_none(self):
        test_row = AnnotationRow(annotation=annotations[1], reporter='test', reporter_email='test')
        test_row.set_bounding_box_uuid()
        assert test_row.columns['BoundingBoxID'] == NULL_VAL_STRING
