<%inherit file="_project.mako"/>

<%
    vername = {
        'base1'         :'1',
        'background'    :'1,background',
        'copter'        :'1,background,copter',
        'colision'      :'1,background,copter,colision',
        'physics'       :'1,background,copter,colision,physics',
        'paralax'       :'1,background,copter,colision,physics,paralax',
    }
%>

<h1>Copter</h1>

<h2>Base</h2>
${self.show_diff(None, vername['base1'])}

<h2>Background</h2>
${self.show_diff(vername['base1'], vername['background'])}

<h2>Copter</h2>
${self.show_diff(vername['background'], vername['copter'])}

<h2>Colide</h2>
${self.show_diff(vername['copter'], vername['colision'])}

<h2>Physics</h2>
${self.show_diff(vername['colision'], vername['physics'])}

<h2>Paralax</h2>
${self.show_diff(vername['physics'], vername['paralax'])}


<img src="/static/projects/CopterLevel1.gif">