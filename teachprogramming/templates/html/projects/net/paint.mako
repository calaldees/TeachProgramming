<%inherit file="_project.mako"/>


<%def name="init()">
<%
    self.titlebar_active        = 'projects'
    self.text_title             = 'Network Paint'
    self.text_title_description = 'Shared network paint'

    vername = {
        'blank'             :'',
        '1'                 :'1',
        'draw_pixel'        :'1,draw_pixel',
        'draw_line'         :'1,draw_pixel,draw_line',
        'network'           :'1,draw_pixel,draw_line',
        'draw_pixel_network':'1,draw_pixel,network,draw_pixel_network',
        'draw_line_network' :'1,draw_pixel,draw_line,network,draw_line_network',
        'select_color_keys' :'',
        'paint_images'      :'',
        'erasor'            :'',
        'text'              :'',
        #'full'              :'',
    }
    self.vername = vername
%>
</%def>

## ----------------------------------------------
<% self.section_title('Setup') %>
    <h2>Setup</h2>
    <p>Download <a href="/static/projects/net/server.py">server.py</a> (only in python, quite compicated, if you think this is discraceful then build up some code kung fu and submit additional server implementations on github)</p>
    <p><a href="#">Lesson Plan</a> for teachers</p>
</section>

##python3 ~/code/TeachProgramming/teachprogramming/lib/make_ver.py chat.html --target_version 1,send_one,send,recv,send_recv,gui,gui_recv,gui_scroll,gui_username > t.html

## ----------------------------------------------
<% self.category = 'Simple Paint' %>

<%self:code_section
    prev_version   = "blank"
    target_version = "1"
    title          = "Base"
>
</%self:code_section>


<%self:code_section
    prev_version   = "1"
    target_version = "draw_pixel"
    title          = "Draw Pixel"
>
</%self:code_section>

<%self:code_section
    prev_version   = "draw_pixel"
    target_version = "draw_line"
    title          = "Draw Lines"
>
</%self:code_section>


## ----------------------------------------------

<% self.category = 'Network' %>


<%self:code_section
    prev_version   = "draw_line"
    target_version = "network"
    title          = "Send Data over network"
>
</%self:code_section>

<%self:code_section
    prev_version   = "network"
    target_version = "draw_pixel_network"
    title          = "Draw pixel network"
>
</%self:code_section>

<%self:code_section
    prev_version   = "network"
    target_version = "draw_line_network"
    title          = "Draw line network"
>
</%self:code_section>


## ----------------------------------------------


<% self.category = 'Paint Features' %>

<%self:code_section
    prev_version   = "blank"
    target_version = "blank"
    title          = "Select Color (with keys)"
>
</%self:code_section>


<%self:code_section
    prev_version   = "blank"
    target_version = "blank"
    title          = "Erasor"
>
</%self:code_section>


<%self:code_section
    prev_version   = "blank"
    target_version = "blank"
    title          = "Clear"
>
</%self:code_section>

<%self:code_section
    prev_version   = "blank"
    target_version = "blank"
    title          = "Images"
>
</%self:code_section>

## ----------------------------------------------

<% self.category = 'Graphical User Interface' %>


<%self:code_section
    prev_version   = "blank"
    target_version = "blank"
    title          = "GUI"
>
</%self:code_section>



