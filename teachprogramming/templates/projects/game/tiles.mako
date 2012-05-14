<%inherit file="_project.mako"/>

<%
    vername = {
        'base'          :'1',
        'player'        :'1,player',
        'blocks'        :'1,player,blocks',
        'blocks_random' :'1,player,blocks,blocks_random',
        'limit'         :'1,player,blocks,limit',
        'eat'           :'1,player,blocks,limit,eat',
        'images'        :'1,player,blocks,images',
        'block_move'    :'1,player,blocks,block_move',
        'full'          :'1,player,blocks,blocks_random,block_move,limit,images',
        'mines'         :'1,player,blocks,blocks_random,mines',
    }
%>



<h1>Tiles</h1>

${parent.web_demo(vername['full'])}
${parent.web_demo(vername['mines'])}


<%self:code_section
    prev_version   = "${None}"
    target_version = "${vername['base']}"
>
    <%def name="title()">
        <h2>Base</h2>
    </%def>
</%self:code_section>


<%self:code_section
    prev_version   = "${vername['base']}"
    target_version = "${vername['player']}"
>
    <%def name="title()">
        <h2>Player</h2>
    </%def>
</%self:code_section>


<%self:code_section
    prev_version   = "${vername['player']}"
    target_version = "${vername['blocks']}"
>
    <%def name="title()">
        <h2>Blocks</h2>
    </%def>
</%self:code_section>





<%self:code_section
    prev_version   = "${vername['blocks']}"
    target_version = "${vername['blocks_random']}"
>
    <%def name="title()">
        <h3>Blocks Random</h3>
    </%def>
</%self:code_section>




<%self:code_section
    prev_version   = "${vername['blocks']}"
    target_version = "${vername['limit']}"
>
    <%def name="title()">
        <h2>limit</h2>
    </%def>
</%self:code_section>


<%self:code_section
    prev_version   = "${vername['limit']}"
    target_version = "${vername['eat']}"
>
    <%def name="title()">
        <h2>eat</h2>
    </%def>
</%self:code_section>



<%self:code_section
    prev_version   = "${vername['blocks']}"
    target_version = "${vername['images']}"
>
    <%def name="title()">
        <h2>images</h2>
    </%def>
</%self:code_section>


<%self:code_section
    prev_version   = "${vername['blocks']}"
    target_version = "${vername['block_move']}"
>
    <%def name="title()">
        <h2>block_move</h2>
    </%def>
</%self:code_section>



<%self:code_section
    prev_version   = "${vername['blocks_random']}"
    target_version = "${vername['mines']}"
>
    <%def name="title()">
        <h2>mines</h2>
    </%def>
</%self:code_section>

