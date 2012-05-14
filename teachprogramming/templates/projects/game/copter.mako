<%inherit file="_project.mako"/>

<%
    vername = {
        'base1'          :'1',
        'background'     :'1,background',
        'copter'         :'1,background,copter',
        'colision_single':'1,background,copter,colision_single',
        'colision_multi' :'1,background,copter,colision_single,colision_multi',
        'level'          :'1,background,copter,colision_single,level',
        'physics'        :'1,background,copter,physics',
        'paralax'        :'1,background,paralax',
        'full'           :'1,background,copter,physics,colision_single,colision_multi,paralax',
    }
%>

<h1>Copter</h1>
demo
${parent.web_demo(vername['full'])}





<%self:code_section
    prev_version   = "${None}"
    target_version = "${vername['base1']}"
>
    <%def name="title()">
        <h2>Base</h2>
    </%def>
</%self:code_section>

<%self:code_section
    prev_version   = "${vername['base1']}"
    target_version = "${vername['background']}"
>
    <%def name="title()">
        <h2>Background</h2>
    </%def>
</%self:code_section>


<%self:code_section
    prev_version   = "${vername['background']}"
    target_version = "${vername['copter']}"
>
    <%def name="title()">
        <h2>Copter</h2>
    </%def>
</%self:code_section>


<%self:code_section
    prev_version   = "${vername['copter']}"
    target_version = "${vername['colision_single']}"
>
    <%def name="title()">
        <h2>Colide (Single Point)</h2>
    </%def>
</%self:code_section>


<%self:code_section
    prev_version   = "${vername['colision_single']}"
    target_version = "${vername['colision_multi']}"
>
    <%def name="title()">
        <h2>Colide (Multi Point)</h2>
    </%def>
</%self:code_section>


<%self:code_section
    prev_version   = "${vername['colision_single']}"
    target_version = "${vername['level']}"
>
    <%def name="title()">
        <h3>Level advancing</h3>
    </%def>
</%self:code_section>


<%self:code_section
    prev_version   = "${vername['copter']}"
    target_version = "${vername['physics']}"
>
    <%def name="title()">
        <h2>Physics</h2>
    </%def>
</%self:code_section>



<%self:code_section
    prev_version   = "${vername['background']}"
    target_version = "${vername['paralax']}"
>
    <%def name="title()">
        <h2>Paralax</h2>
    </%def>
</%self:code_section>




##<img src="/static/projects/images/CopterLevel1.gif">