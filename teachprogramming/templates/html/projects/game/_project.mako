<%inherit file="../_project.mako"/>

<%! 

import re

from teachprogramming.lib      import make_ver, constants
from teachprogramming.lib.misc import random_string


canvas_ids = re.compile(r'<canvas.*?id=["\'](.*?)["\']')
javascript_activate_mouse = """
    canvas.addEventListener('mouseover', function(event) {start();}, true);
    canvas.addEventListener('mouseout' , function(event) {pause();}, true);
    timerEvent();
"""

def make_web_ver(source):
    """
    Takes an html/javascript raw file and processes it so it can work indipendently in an html page with other examples
    
    Takes a source file in the format
    <canvas id="thing" ...>
    <script>
        //some script stuff
        function timerEvent() {
            ...
        }
        //
        start();
    </script>
    
    and returns
    <canvas id="thing_XRANDOMX">
    <script>
    (function (canvas_id) {
        //some script stuff
        //  all use of 'thing' now 'thing_XRANDOMX'
        canvas.Eventstuff(to pause and start when mouse rolled over);
        timerEvent(); // this is to tick ONE timer to poplate the first frame
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

## Demos ---------------------------------------

<%def name="web_demos(*target_ver_names)">
    <ul class="thumbnails">
    % for target_ver_name in target_ver_names:
        <li class="span4"><div class="thumbnail">
        ${web_demo(target_ver_name)}
        </div></li>
    % endfor
    </ul>
</%def>

<%def name="web_demo(ver_name)">
    % try:
        <div class="demo">
            <div class="demo_placeholder">
                <p>Hover mouse for demo</p>
                <p>(press escape to stop and reset)</p>
            </div>
            ${make_web_ver(h.ver_string(project_type, project, 'html', ver_name=ver_name, ver_path='demo')) | n}
            <p>${self.full_code(ver_name)}</p>
        </div>
    % except Exception as e:
        <p>BROKEN!! ${str(e)}</p>
    % endtry
</%def>




<%def name="code_section(prev_ver_name, target_ver_name, title, heading_level=2)">
<% self.section_title(title) %>
<h${str(heading_level)}>${str(title.capitalize())}</h${str(heading_level)}>
<div class="row">
    <div class="span6">
        % try:
        ${caller.before_code()}
        % except:
        % endtry
        
        ${self.show_diff(prev_ver_name, target_ver_name)}
        
        % try:
        ${caller.after_code()}
        % except:
        % endtry
    </div>
    <div class="span3">
        ${web_demo(target_ver_name)}
        ##${self.full_code(target_ver_name)}
    </div>
</div>
</section>
</%def>


<%def name="body()">
${next.body()}
</%def>