<%inherit file="_project.mako"/>

<%
    vername = {
        'base1'         :'1',
        'background'    :'1,background',
        'copter'        :'1,background,copter',
    }
%>

<h1>Copter</h1>

<h2>Base</h2>
${self.show_diff(None, vername['base1'])}

<h2>Background</h2>
${self.show_diff(vername['base1'], vername['background'])}

<h2>Copter</h2>
${self.show_diff(vername['background'], vername['copter'])}

<img src="/static/projects/CopterLevel1.gif">