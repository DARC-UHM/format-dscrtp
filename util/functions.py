"""
This file contains functions that are used throughout the formatting process and WoRMS check.
"""

from datetime import datetime, timedelta
from typing import Dict, Optional

from util.constants import *
from util.terminal_output import Color


def get_association(annotation: Dict, link_name: str) -> dict:
    """
    Obtains an association value from the annotation data structure.

    :param Dict annotation: The complete annotation dictionary.
    :param str link_name: The specific key we want to get the value for.
    :return dict: The matching value dict.
    """
    for association in annotation['associations']:
        if association['link_name'] == link_name:
            return association
    return {}


def get_associations_list(annotation: Dict, link_name: str) -> list:
    """
    Obtains a list of association values from the annotation data structure (for when there is more than one
    association).

    :param Dict annotation: The complete annotation dictionary.
    :param str link_name: The specific key we want to get the value for.
    :return list: A list of the matching value dicts.
    """
    association_matches = []
    for association in annotation['associations']:
        if association['link_name'] == link_name:
            association_matches.append(association)
    return association_matches


def grain_size(sub: list) -> int:
    """
    Gets the relative grain size of a substrate concept.

    :param list sub: The substrate.
    :return int: The position of the substrate in ROOTS.
    """
    for i in range(len(ROOTS)):
        if ROOTS[i] in sub:
            return i
    return len(ROOTS)


def get_date_and_time(record: Dict) -> datetime:
    """
    Returns a datetime timestamp from a completed annotation record.

    :param Dict record: The annotation record after it has been converted from an AnnotationRow to a list.
    :return datetime: A datetime object of the observation date/time.
    """
    return datetime.strptime(record[OBSERVATION_DATE] + record[OBSERVATION_TIME], '%Y-%m-%d%H:%M:%S')


def parse_datetime(timestamp: str) -> datetime:
    """
    Returns a datetime object given a timestamp string.

    :param str timestamp: The timestamp to parse.
    :return datetime: The timestamp parsed as a datetime object.
    """
    if '.' in timestamp:
        return datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
    return datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')


def extract_time(json_object: Dict) -> Optional[datetime]:
    """
    Used to sort json objects by timestamp, given the json object.

    :param Dict json_object: A json object with the time we want to sort by.
    :return datetime: A datetime object of the timestamp from the json object.
    """
    if not json_object:
        return None
    if '.' in json_object['recorded_timestamp']:
        timestamp = datetime.strptime(json_object['recorded_timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')
        if timestamp.microsecond >= 500000:
            return timestamp.replace(microsecond=0) + timedelta(seconds=1)
        return timestamp.replace(microsecond=0)
    return datetime.strptime(json_object['recorded_timestamp'], '%Y-%m-%dT%H:%M:%SZ')


def extract_uuid(json_object: Dict) -> str:
    """
    Used for sorting annotations by UUID (for testing).

    :param Dict json_object: A json object with the UUID we want to sort by.
    :return str: The UUID.
    """
    return json_object['observation_uuid']


def add_meters(accuracy: str) -> str:
    """
    Takes input and appends an 'm' to the end, if one is not there already.

    :param str accuracy: The accuracy string, e.g. '50m' or '50'.
    :return str: The string with an 'm' on the end.
    """
    if accuracy[-1:] != 'm':
        accuracy = accuracy + 'm'
    return accuracy


def convert_username_to_name(vars_username: str) -> str:
    """
    Converts format of VARS username: [FirstnameLastname] -> [Lastname, FirstName]
    Assumes VARS usernames are formatted 'FirstnameLastname'
    Some exceptions added for old VARS usernames

    :param str vars_username: VARS username, e.g. 'SarahBingo'.
    :return str: The converted name string, e.g. 'Bingo, Sarah'.
    """
    if vars_username == 'christopherkelley':
        return 'Kelly, Christopher'
    if vars_username == 'janeculp':
        return 'Culp, Jane'
    for i in range(1, len(vars_username)):
        if vars_username[i].isupper():
            return vars_username[i:] + ', ' + vars_username[0:i]
    return vars_username


def translate_substrate_code(code: str) -> str:
    """
    Translates substrate codes into human language.

    :param str code: The VARS code of the substrate, e.g. 'peb'.
    :return str: The translated code, e.g. 'pebble'.
    """
    code = code.strip()
    if code in SAMES:
        return code
    if code == 'hp':  # condition for old VARS, where hp was not only a suffix
        return 'hydrothermal precipitate'
    substrate_word_list = []
    r = ''
    man_or_forms = []
    for root in ROOTS:
        if root in code:
            substrate_word_list.append(SUB_CONCEPTS[root])
            r = SUB_CONCEPTS[root]
            code = code.replace(root, '')
            if code == '':
                if r == 'man-made':
                    return 'man-made object'
                else:
                    return r
            break
    for affix in ALL_AFFIXES:
        if affix in code:
            if affix == 'pi':
                if r == 'bedrock' or r == 'block':
                    substrate_word_list.insert(0, SUB_CONCEPTS[affix][0])
                else:
                    substrate_word_list.append(SUB_CONCEPTS[affix][1])
            elif affix in SUFFIXES and r in substrate_word_list:
                substrate_word_list.insert(substrate_word_list.index(r) + 1, SUB_CONCEPTS[affix])
            elif affix in SUFFIXES_FORMS or affix in SUFFIXES_MAN:
                substrate_word_list.append(SUB_CONCEPTS[affix])
                man_or_forms.append(affix)
            elif affix in SUFFIXES_DEAD:
                substrate_word_list.append(SUB_CONCEPTS[affix])
            elif affix in PREFIXES and r in substrate_word_list:
                substrate_word_list.insert(substrate_word_list.index(r), SUB_CONCEPTS[affix])
            code = code.replace(affix, '')
            if code == '':
                if len(man_or_forms) >= 2:
                    substrate_word_list.insert(-1, 'and')
                subs = ' '.join(substrate_word_list)
                if subs[:4] == 'dead':
                    subs = f'{subs[5:]} (dead)'
                return subs
    return ''


def collapse_id_records(report_records: list) -> int:
    """
    Collapses records with the same identity-reference. Returns number of records collapsed.

    :param list report_records: A list of annotation rows (i.e., a list of every annotation in a dive).
    :return int: The number of records collapsed.
    """
    identity_references = {}
    dupes_removed = 0
    num_records = len(report_records)
    i = 0
    while i < num_records:
        id_ref = report_records[i][IDENTITY_REF]
        if id_ref != -1:
            if id_ref not in identity_references:
                # add a new key to identity_references with the current annotation as the value
                identity_references[id_ref] = report_records[i]
            else:
                # collapse the values in the current annotation into the annotation in identity_references
                for j in [ID_COMMENTS, HABITAT, SUBSTRATE, INDV_COUNT, VERBATIM_SIZE, OCCURRENCE_COMMENTS,
                          CMECS_GEO_FORM]:
                    if identity_references[id_ref][j] == NULL_VAL_STRING and report_records[i][j] != NULL_VAL_STRING:
                        identity_references[id_ref][j] = report_records[i][j]
                for j in [MIN_SIZE, MAX_SIZE]:
                    if identity_references[id_ref][j] == NULL_VAL_INT and report_records[i][j] != NULL_VAL_INT:
                        identity_references[id_ref][j] = report_records[i][j]
                for j in [IMAGE_PATH, HIGHLIGHT_IMAGE, BOUNDING_BOX_ID]:
                    if report_records[i][j] != NULL_VAL_STRING:
                        if identity_references[id_ref][j] != NULL_VAL_STRING and \
                                report_records[i][j] not in identity_references[id_ref][j]:
                            identity_references[id_ref][j] += f' | {report_records[i][j]}'
                        else:
                            identity_references[id_ref][j] = report_records[i][j]
                if int(identity_references[id_ref][INDV_COUNT]) < int(report_records[i][INDV_COUNT]):
                    identity_references[id_ref][INDV_COUNT] = report_records[i][INDV_COUNT]
                del report_records[i]  # remove the duplicate record
                i -= 1  # to account for the record that was just deleted
                num_records -= 1  # ^
                dupes_removed += 1
        i += 1

    return dupes_removed


def find_associated_taxa(report_records: list, concepts: Dict, warning_messages: list):
    """
    Fills in the AssociatedTaxa fields: retrieves records from the output table that have another VARS concept listed
    as a substrate.

    :param list report_records: A list of annotation rows (i.e., a list of every annotation in a dive).
    :param Dict concepts: Dictionary of all locally saved concepts.
    :param list warning_messages: The list of warning messages to display at the end of the script.
    """
    for i in range(len(report_records)):
        associate_record = report_records[i]
        if associate_record[UPON_IS_CREATURE]:
            # the associate's 'upon' is indeed a creature
            host_concept_name = associate_record[SUBSTRATE]  # VARS name for host
            if host_concept_name in concepts:
                # host concept is in local concepts file
                observation_time = get_date_and_time(associate_record)  # timestamp at which the associate was recorded
                found = False
                for j in range(i + 10, -1, -1):
                    """
                    Checks backward, looking for the most recent host w/ matching name. We start at i + 10 because
                    there can be multiple records with the exact same timestamp, and one of those records could be
                    the 'upon'
                    """
                    # to catch index out of range exception
                    while j >= len(report_records):
                        j -= 1
                    host_record = report_records[j]
                    host_time = get_date_and_time(host_record)
                    if i == j or host_time > observation_time:
                        # host record won't be recorded after associate record, so ignore this record
                        # i == j: record shouldn't be associated with itself, ignore
                        pass
                    elif host_record[SAMPLE_ID][:-9] != associate_record[SAMPLE_ID][:-9]:
                        # dive names don't match, stop the search
                        break
                    else:
                        if host_record[VARS_CONCEPT_NAME] == host_concept_name:
                            # the host record's name is equal to the host concept name (associate's 'upon' name)
                            if host_record[ASSOCIATED_TAXA] == NULL_VAL_STRING:
                                # if the host's 'associated taxa' field is blank, add the associate's concept name
                                host_record[ASSOCIATED_TAXA] = associate_record[COMBINED_NAME_ID]
                            elif associate_record[COMBINED_NAME_ID] not in host_record[ASSOCIATED_TAXA]:
                                # otherwise, append the concept name if it's not already there
                                host_record[ASSOCIATED_TAXA] += f' | {associate_record[COMBINED_NAME_ID]}'
                            if host_record[OCCURRENCE_COMMENTS] == NULL_VAL_STRING:
                                # add touch to occurrence comments
                                host_record[OCCURRENCE_COMMENTS] = 'associate touching host'
                            elif 'associate touching host' not in host_record[OCCURRENCE_COMMENTS]:
                                host_record[OCCURRENCE_COMMENTS] += ' | associate touching host'
                            time_diff = observation_time - host_time
                            if time_diff.seconds > 300:
                                # flag warning
                                warning_messages.append([
                                    associate_record[SAMPLE_ID],
                                    associate_record[VARS_CONCEPT_NAME],
                                    associate_record[TRACKING_ID],
                                    f'{Color.RED}Time between record and upon record greater than 5 minutes {Color.END}'
                                    f'({time_diff.seconds} seconds)'
                                ])
                            elif time_diff.seconds > 60:
                                # flag for review
                                warning_messages.append([
                                    associate_record[SAMPLE_ID],
                                    associate_record[VARS_CONCEPT_NAME],
                                    associate_record[TRACKING_ID],
                                    f'{Color.YELLOW}Time between record and upon record greater than 1 minute {Color.END}'
                                    f'({time_diff.seconds} seconds)'
                                ])
                            found = True
                            break
                if not found:
                    # flag error
                    warning_messages.append([
                        associate_record[SAMPLE_ID],
                        associate_record[VARS_CONCEPT_NAME],
                        associate_record[TRACKING_ID],
                        f'{Color.RED}Upon not found in previous records{Color.END}'
                    ])
            else:
                # flag error
                warning_messages.append([
                    associate_record[SAMPLE_ID],
                    associate_record[VARS_CONCEPT_NAME],
                    associate_record[TRACKING_ID],
                    f'{Color.RED}"{associate_record[SUBSTRATE]}" is host for this record, but that concept name '
                    f'was not found in concepts.{Color.END}'
                ])
