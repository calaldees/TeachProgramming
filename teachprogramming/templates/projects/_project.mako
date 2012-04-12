<%inherit file="/menu.mako"/>

<%! 
import os
import re
from teachprogramming.lib.misc import random_string
from teachprogramming.lib      import make_ver, constants

def ver_string(project, format, version):
    return '\n'.join( make_ver.make_ver(constants.project_filename % (project,format), version) )


canvas_ids = re.compile(r'<canvas.*?id=["\'](.*?)["\']')
javascript_activate_mouse = """
    canvas.addEventListener('mouseover', function(event) {start();}, true);
    canvas.addEventListener('mouseout' , function(event) {pause();}, true);
"""

def make_web_ver(source):
    """
    Takes an html/javascript raw file and processes it so it can work indipendently in an html page with other examples
    
    Takes a source file in the format
    <canvas id="thing" ...>
    <script>
        //some script stuff
        start();
    </script>
    
    and returns
    <canvas id="thing_XRANDOMX">
    <script>
    (function (canvas_id) {
        //some script stuff
        //  all use of 'thing' now 'thing_XRANDOMX'
        canvas.Eventstuff(to pause and start when mouse rolled over);
    })();
    </script>
    
    The source canvas id's are pattern matched and those strings are REPLACED in the source below,
    the canvas.id name string should not appear ANYWHERE in the script code unless it is to be replaced
    
    """
    replace_strings = []
    for canvas_match in canvas_ids.finditer(source):
        replace_strings.append(canvas_match.group(1))
        
    for s in replace_strings:
        source = re.sub(s,"%s_%s"%(s,random_string()),source)
    
    source = re.sub( '<script>','<script>(function () {', source)
    source = re.sub('start\(\);\s*</script>',javascript_activate_mouse+'})();</script>', source)
    
    return source
%>



<%def name='show_diff(prev_version, target_version)'>
    <%
        diff = make_ver.get_diff(constants.project_filename % (project,format), prev_version, target_version, hidden_line_replacement='...more...')
        line_classs = {'-':'remove', '+':'add'}
        open_section = False
    %>
    <div class='code'>
    % for line in diff:
        % if line.startswith('@@'):
            % if open_section:
        </div>
            % endif
            <% open_section = True %>
        <div class='section'>
        % elif not (line.startswith('---') or line.startswith('+++')):
            <pre class='${line_classs.get(line[0:1])}'>${line}</pre>
        % endif
    % endfor
        </div> <!-- end code section -->

    </div> <!-- end code -->
    
    <button type="button" onclick="$(this).next().toggle();">Full code</button>
    <div class="hide">
        <a href="/code/${project}.${format}/${target_version}">Version ${target_version}</a>
        <pre>${ver_string(project, format, target_version)}</pre>
    </div>
    
    ${web_demo(target_version)}
</%def>


<%def name="web_demo(target_version)">
    <div class="demo">
        <div class="demo_placeholder">
            <p>Hover mouse for demo</p>
            <p>(press escape to stop and reset)</p>
        </div>
        ${make_web_ver(ver_string(project, 'html', target_version+',demo')) | n}
    </div>
</%def>


<%def name='body()'>
    <!-- List all formats for this project -->
    <%
        files = [file for file in os.listdir(constants.project_path) if file.startswith('%s.' % project)]
    %>
    <ul>
    % for file in files:
        <% 
            fileext            = make_ver.get_fileext(file) 
            format_description = constants.file_type_to_lang.get(fileext)
            css_class = ''
            if fileext == format:
                css_class = 'selected'
        %>
        <li><a href='/project/${project}.${fileext}' class='${css_class}'><span class='icon16 i_${fileext}'></span>${format_description}</a></li>
    % endfor
    </ul>
    
    <!-- Documentation for this project -->
    ${next.body()}
    
</%def>