"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
   return record[1]


def convert_coordinate(coordinate):
    return (coordinate[0], coordinate[1])


def compare_records(azara_record, rui_record):
    return convert_coordinate(azara_record[1]) == rui_record[1]


def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    else:
        return 'not a match'


def clean_up(combined_record_group):
    output = ''
    for record in combined_record_group:
        trimmed = (record[0], record[2], record[3], record[4])
        output += f"{repr(trimmed)}\n"
    return output
