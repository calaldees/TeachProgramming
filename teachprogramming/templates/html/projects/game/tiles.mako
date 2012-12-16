<%inherit file="_project.mako"/>

<%def name="init()">
<%
    self.titlebar_active        = 'projects'
    self.text_title             = 'Tiles'
    self.text_title_description = 'tiles n stuff and 2d arrays and stuff and stuff'

    vername = {
        'blank'         :'',
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
    self.vername = vername
%>
</%def>


demo
${parent.web_demos('full')}
${parent.web_demos('mines')}


## ----------------------------------------------
<% self.category = 'Base Compoents' %>

<%self:code_section
    prev_version   = "blank"
    target_version = "base"
    title          = "Base"
></%self:code_section>

<%self:code_section
    prev_version   = "base"
    target_version = "player"
    title          = "Player"
></%self:code_section>

<%self:code_section
    prev_version   = "player"
    target_version = "blocks"
    title          = "Blocks"
></%self:code_section>

<%self:code_section
    prev_version   = "blocks"
    target_version = "blocks_random"
    title          = "Blocks Random"
></%self:code_section>

<%self:code_section
    prev_version   = "blocks"
    target_version = "limit"
    title          = "Limit"
></%self:code_section>

<% self.category = 'Game Variations' %>

<%self:code_section
    prev_version   = "limit"
    target_version = "eat"
    title          = "Eat"
></%self:code_section>

<%self:code_section
    prev_version   = "blocks"
    target_version = "images"
    title          = "Images"
></%self:code_section>

<%self:code_section
    prev_version   = "blocks"
    target_version = "block_move"
    title          = "Block Move"
></%self:code_section>

<%self:code_section
    prev_version   = "blocks_random"
    target_version = "mines"
    title          = "Mines"
></%self:code_section>


