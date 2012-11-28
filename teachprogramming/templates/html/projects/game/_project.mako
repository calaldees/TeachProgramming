<%inherit file="../_project.mako"/>

<%! 

import re

canvas_ids = re.compile(r'<canvas.*?id=["\'](.*?)["\']')
javascript_activate_mouse = """
    canvas.addEventListener('mouseover', function(event) {start();}, true);
    canvas.addEventListener('mouseout' , function(event) {pause();}, true);
"""

from teachprogramming.lib      import make_ver, constants
from teachprogramming.lib.misc import random_string



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
    source = re.sub('<!--<canvas','<canvas', source) # AllanC - SWEET HOLY HACK!!!! I needed a way to have the tron.html working as a static file, so I HAD to rem the 320,240 canvas out, this just makes it visible again
    
    return source
%>





<%def name="web_demo(target_version)">
    % try:
    <% web_demo_code = make_web_ver(h.ver_string(project_type, project, 'html', target_version+',demo')) %>
    <div class="demo">
        <div class="demo_placeholder">
            <p>Hover mouse for demo</p>
            <p>(press escape to stop and reset)</p>
        </div>
        ${web_demo_code | n}
    </div>
    % except Exception as e:
        <p>BROKEN!! ${e}</p>
    % endtry    
</%def>


<%def name="format_links(target_version='')">
    <div class="format_links">
        <a name="${target_version}"></a>
        <!-- List all formats for this version -->
        <ul>
        % if not self.files:
        No versions?
        % endif
        % for file in self.files:
            <% 
                fileext            = h.make_ver.get_fileext(file) 
                format_description = h.constants.file_type_to_lang.get(fileext)
                css_class = ''
                if fileext == format:
                    css_class = 'selected'
            %>
            ## TODO: use route path? code_url = request.route_path('project_code', project_type=project_type, project=project, format=format, version=target_version)
            <li><a href='/project/${project_type}/${project}.${fileext}#${target_version}' class='${css_class}' alt='${format_description}'><span class='icon16 i_${fileext}'></span></a></li>
        % endfor
        </ul>
    </div>
</%def>


<%def name="code_section(prev_version, target_version, title, heading_level=2)">
<%
    try   : category = self.category
    except: category = None
    self.sidebar_content.append((title,category))
%>
<section id='${h.encode_id(title)}'>
    <h${heading_level}>${title.capitalize()}</h${heading_level}>
    
    ${web_demo(self.vername[target_version])}
    ${self.full_code(self.vername[target_version])}

    % try:
    ${caller.before_code()}
    % except:
    % endtry
    
    ${self.show_diff(self.vername[prev_version], self.vername[target_version])}
    
    % try:
    ${caller.after_code()}
    % except:
    % endtry
</section>
</%def>


<%def name="body()">
${next.body()}
</%def>