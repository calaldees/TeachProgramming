
import os

from teachprogramming.lib import make_ver, constants

def ver_string(project_type, project, format, version):
    return '\n'.join( make_ver.make_ver(constants.project_filename % (project_type, project,format), version) )


def include_file_(filename):
    source = open(filename, 'r')
    data = source.read()
    source.close()
    return data

def encode_id(title):
    """
    Safe encoder to transform 'title' string to 'id' string. Remove spaces and lowercase 
    """
    # TODO urlencode
    return title.lower().replace(' ','_').replace("'",'_')
