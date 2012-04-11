import re

from teachprogramming.lib.misc import random_string

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
    <canvas id="thing_1" ... mouseover=  mouseout= >
    <script>
    (function (canvas_id) {
    })('thing_1');
    </script>
    
    The source canvas id's are pattern matched and those strings are REPLACED in the source below,
    the canvas.id name string should not appear ANYWHERE in the script code unless it is to be replaced
    
(function (canvas_id) {
  var start = null;
  var timer = setTimeout(rar);
  function hello () {
    start = new Date();
    console.log(start);
    window.document.getElementById('canvas_' + canvas_id);
  }
  hello();
})(1);

console.log(start);
    
    
    """
    replace_strings = []
    for canvas_match in canvas_ids.finditer(source):
        replace_strings.append(canvas_match.group(1))
        
    for s in replace_strings:
        source = re.sub(s,"%s_%s"%(s,random_string()),source)
    
    source = re.sub( '<script>','<script>(function () {', source)
    source = re.sub('start\(\);\s*</script>',javascript_activate_mouse+'})();</script>', source)
    
    return source