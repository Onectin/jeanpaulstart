from jeanpaulstart import file_io
from jeanpaulstart.constants import *


TASK_COMMAND = 'copy'


def validate(user_data):
    return OK, ""


def normalize_after_split(splitted):
    splitted['arguments']['force'] = splitted['arguments'].get('force', True)
    splitted['arguments']['replace'] = splitted['arguments'].get('replace', False)
    return splitted


def apply_(src, dest, force, replace):
    file_io.copy(src, dest, force, replace)

    return OK
