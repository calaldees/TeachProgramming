import os
import teachprogramming.lib.constants as constants
import teachprogramming.lib.make_ver as make_ver

def get_templates(template_folder, template_path=constants.template_path):
    path = os.path.join(template_path, template_folder)
    return [filename.replace('.mako','') for filename in os.listdir(path) if os.path.isfile(os.path.join(path,filename)) and not filename.startswith('_')]

def get_projects(project_type):
    return get_templates(project_type, template_path=constants.project_template_path)
    
def get_project_langs(project_type, project):
    files    = [file for file in os.listdir(os.path.join(constants.project_path,project_type)) if file.startswith('%s.' % project)]
    fileexts = [make_ver.get_fileext(file) for file in files]
    return fileexts
    
    
    

