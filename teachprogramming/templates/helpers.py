import os

from teachprogramming.lib import make_ver, constants

def langs():
    """
    Tuples of ext, lang_name
    """
    return constants.file_type_to_lang.items()

def ver_string(project_type, project, lang, ver_name, ver_path=None):
    return '\n'.join( make_ver.make_ver(constants.project_filename % (project_type, project, lang), ver_name=ver_name, ver_path=ver_path) )

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

def get_templates(template_folder, template_path=constants.template_path):
    path = os.path.join(template_path, template_folder)
    return [filename.replace('.mako','') for filename in os.listdir(path) if os.path.isfile(os.path.join(path,filename)) and not filename.startswith('_')]

def get_projects(project_type):
    return get_templates(project_type, template_path=constants.project_template_path)
    
def get_project_langs(project_type=None, project=None, **kwargs):
    path     = os.path.join(constants.project_path,project_type)
    files    = [file for file in os.listdir(path) if file.startswith('%s.' % project)]
    fileexts = [make_ver.get_fileext(file) for file in files]
    return fileexts

