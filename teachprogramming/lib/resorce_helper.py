import os
import teachprogramming.lib.constants as constants
import teachprogramming.lib.make_ver as make_ver

def get_projects(project_type):
    return [file.replace('.mako','') for file in os.listdir(os.path.join(constants.project_template_path, project_type)) if not file.startswith('_')]
    
def get_project_langs(project_type, project):
    files    = [file for file in os.listdir(os.path.join(constants.project_path,project_type)) if file.startswith('%s.' % project)]
    fileexts = [make_ver.get_fileext(file) for file in files]
    return fileexts
    
    
    

