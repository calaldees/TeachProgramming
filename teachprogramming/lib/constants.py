
#AllanC - TODO! Move paths to config! ... they are not constants!
project_path          = 'teachprogramming/static/projects/'
project_template_path = 'teachprogramming/templates/projects/'

project_filename      = project_path + '%s.%s'
project_filename_dict = project_path + '%(project)s.%(format)s'

file_type_to_lang = dict(
    py   = 'Python',
    html = 'Javascript/HTML5',
    js   = 'Javascript',
    vb   = 'VB.NET',
    php  = 'PHP',
    java = 'Java',
)