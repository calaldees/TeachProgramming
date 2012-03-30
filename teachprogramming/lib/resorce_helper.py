import os
import teachprogramming.lib.constants as constants
import teachprogramming.lib.make_ver as make_ver

def get_projects():
    return [file.replace('.mako','') for file in os.listdir(constants.project_template_path) if not file.startswith('_')]
    
def get_project_langs(project):
    files    = [file for file in os.listdir(constants.project_path) if file.startswith('%s.' % project)]
    fileexts = [make_ver.get_fileext(file) for file in files]
    return fileexts
    
    
    

