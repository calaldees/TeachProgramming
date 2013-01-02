<%inherit file="_project.mako"/>

<%def name="init()">
<%
    self.titlebar_active        = 'projects'
    self.text_title             = 'Tiles'
    self.text_title_description = 'tiles n stuff and 2d arrays and stuff and stuff'
%>
</%def>



${parent.web_demos('full','mines')}


## ----------------------------------------------
<% self.category = 'Base Compoents' %>

<%self:code_section
    prev_ver_name   = ""
    target_ver_name = "base"
    title          = "Base"
></%self:code_section>

<%self:code_section
    prev_ver_name   = "base"
    target_ver_name = "player"
    title          = "Player"
></%self:code_section>

<%self:code_section
    prev_ver_name   = "player"
    target_ver_name = "blocks"
    title          = "Blocks"
></%self:code_section>

<%self:code_section
    prev_ver_name   = "blocks"
    target_ver_name = "blocks_random"
    title          = "Blocks Random"
></%self:code_section>

<%self:code_section
    prev_ver_name   = "blocks"
    target_ver_name = "limit"
    title          = "Limit"
></%self:code_section>

<% self.category = 'Game Variations' %>

<%self:code_section
    prev_ver_name   = "limit"
    target_ver_name = "eat"
    title          = "Eat"
></%self:code_section>

<%self:code_section
    prev_ver_name   = "blocks"
    target_ver_name = "images"
    title          = "Images"
></%self:code_section>

<%self:code_section
    prev_ver_name   = "blocks"
    target_ver_name = "block_move"
    title          = "Block Move"
></%self:code_section>

<%self:code_section
    prev_ver_name   = "blocks_random"
    target_ver_name = "mines"
    title          = "Mines"
></%self:code_section>


