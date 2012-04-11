<%inherit file="_project.mako"/>

<%
    vername = {
        'base1'          :'1',
        'background'     :'1,background',
        'copter'         :'1,background,copter',
        'colision_single':'1,background,copter,colision_single',
        'colision_multi' :'1,background,copter,colision_single,colision_multi',
        'level'          :'1,background,copter,colision_single,level',
        'physics'        :'1,background,copter,colision_single,physics',
        'paralax'        :'1,background,paralax',
        'full'           :'1,background,copter,physics,colision_single,colision_multi,paralax',
    }
%>

<h1>Copter</h1>
demo
${parent.web_demo(vername['full'])}


<h2>Base</h2>
${self.show_diff(None, vername['base1'])}

<h2>Background</h2>
${self.show_diff(vername['base1'], vername['background'])}

<h2>Copter</h2>
${self.show_diff(vername['background'], vername['copter'])}

<h2>Colide (Single Point)</h2>
${self.show_diff(vername['copter'], vername['colision_single'])}

<h2>Colide (Multi Point)</h2>
${self.show_diff(vername['colision_single'], vername['colision_multi'])}


<h3>Level advancing</h3>
${self.show_diff(vername['colision_single'], vername['level'])}

<h2>Physics</h2>
${self.show_diff(vername['copter'], vername['physics'])}

<h2>Paralax</h2>
${self.show_diff(vername['background'], vername['paralax'])}


<img src="/static/projects/CopterLevel1.gif">