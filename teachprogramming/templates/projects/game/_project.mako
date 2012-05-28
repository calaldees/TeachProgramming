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

# HACK!!! THIS IS DUPLICATED FROM THE PARENT ../_project.mako!!! REMOVE DUCPLICATION CHIMP!!!
def ver_string(project_type, project, format, version):
    return '\n'.join( make_ver.make_ver(constants.project_filename % (project_type, project,format), version) )



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
    <% web_demo_code = make_web_ver(ver_string(project_type, project, 'html', target_version+',demo')) %>
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
                fileext            = make_ver.get_fileext(file) 
                format_description = constants.file_type_to_lang.get(fileext)
                css_class = ''
                if fileext == format:
                    css_class = 'selected'
            %>
            <li><a href='/project/${project}.${fileext}#${target_version}' class='${css_class}' alt='${format_description}'><span class='icon16 i_${fileext}'></span></a></li>
        % endfor
        </ul>
    </div>
</%def>



<%def name="code_section(prev_version, target_version)">
<section>
    ${format_links(target_version)}
    ${caller.title()}
    
    ${web_demo(target_version)}
    ${self.full_code(target_version)}
    
    % try:
    ${caller.code_before()}
    % except:
    % endtry
    
    ${self.show_diff(prev_version, target_version)}
    
    % try:
    ${caller.code_after()}
    % except:
    % endtry
</section>
</%def>


<%def name="body()">
${next.body()}
</%def>