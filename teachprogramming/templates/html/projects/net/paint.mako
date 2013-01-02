<%inherit file="_project.mako"/>


<%def name="init()">
<%
    self.titlebar_active        = 'projects'
    self.text_title             = 'Network Paint'
    self.text_title_description = 'Shared network paint'

%>
</%def>

## ----------------------------------------------
<% self.section_title('Setup') %>
    <h2>Setup</h2>
    <p>Download <a href="/static/projects/net/server.py">server.py</a> (only in python, quite compicated, if you think this is discraceful then build up some code kung fu and submit additional server implementations on github)</p>
    <p><a href="#">Lesson Plan</a> for teachers</p>
</section>

##python3 ~/code/TeachProgramming/teachprogramming/lib/make_ver.py chat.html --target_ver_name 1,send_one,send,recv,send_recv,gui,gui_recv,gui_scroll,gui_username > t.html

## ----------------------------------------------
<% self.category = 'Simple Paint' %>

<%self:code_section
    prev_ver_name   = ""
    target_ver_name = "base"
    title          = "Base"
>
</%self:code_section>


<%self:code_section
    prev_ver_name   = "base"
    target_ver_name = "draw_pixel"
    title          = "Draw Pixel"
>
</%self:code_section>

<%self:code_section
    prev_ver_name   = "draw_pixel"
    target_ver_name = "draw_line"
    title          = "Draw Lines"
>
</%self:code_section>


## ----------------------------------------------

<% self.category = 'Network' %>


<%self:code_section
    prev_ver_name   = "draw_line"
    target_ver_name = "network"
    title          = "Send Data over network"
>
</%self:code_section>


<%self:code_section
    prev_ver_name   = "network"
    target_ver_name = "draw_line_network"
    title          = "Draw line network"
>
</%self:code_section>


## ----------------------------------------------


<% self.category = 'Paint Features' %>

<%self:code_section
    prev_ver_name   = "base"
    target_ver_name = "base"
    title          = "Select Color (with keys)"
>
</%self:code_section>


<%self:code_section
    prev_ver_name   = "base"
    target_ver_name = "base"
    title          = "Erasor"
>
</%self:code_section>


<%self:code_section
    prev_ver_name   = "base"
    target_ver_name = "base"
    title          = "Clear"
>
</%self:code_section>

<%self:code_section
    prev_ver_name   = "base"
    target_ver_name = "base"
    title          = "Images"
>
</%self:code_section>

## ----------------------------------------------

<% self.category = 'Graphical User Interface' %>


<%self:code_section
    prev_ver_name   = "base"
    target_ver_name = "base"
    title          = "GUI"
>
</%self:code_section>



