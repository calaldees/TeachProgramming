<%inherit file="_project.mako"/>

<%
    vername = {
        'full'           :'1',
    }
%>

<h1>Whack</h1>
demo
${parent.web_demo(vername['full'])}





<%self:code_section
    prev_version   = "${None}"
    target_version = "${vername['full']}"
>
    <%def name="title()">
        <h2>Base</h2>
    </%def>
</%self:code_section>
