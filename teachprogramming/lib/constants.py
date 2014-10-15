
#AllanC - TODO! Move paths to config! ... they are not constants!
template_path         = 'teachprogramming/templates/html/'
project_path          = 'teachprogramming/static/projects/'
project_template_path = 'teachprogramming/templates/html/projects/'

project_filename      = project_path + '%s/%s.%s'
project_filename_dict = project_path + '{project_type}/{project}.{selected_lang}'

file_type_to_lang = dict(
    py   = 'Python',
    html = 'Javascript/HTML5',
    #js   = 'Javascript',
    vb   = 'VB.NET',
    php  = 'PHP',
    java = 'Java',
)

LANGAUAGES = {
    'python',
    'javascript',
    'php',
    'ruby',
    'java',
    'vb',
}
