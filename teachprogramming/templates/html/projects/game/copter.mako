<%inherit file="_project.mako"/>

<%def name="init()">
<%
    self.titlebar_active        = 'projects'
    self.text_title             = 'Copter'
    self.text_title_description = 'Classic cave flying action'

%>
</%def>


demo
${parent.web_demos('full')}

## ----------------------------------------------
<% self.category = 'Base Compoents' %>

<%self:code_section
    prev_ver_name    = ""
    target_ver_name = "base"
    title          = "Base"
></%self:code_section>


<%self:code_section
    prev_ver_name   = "base"
    target_ver_name = "background"
    title          = "Background"
></%self:code_section>


<%self:code_section
    prev_ver_name   = "background"
    target_ver_name = "copter"
    title          = "Copter"
></%self:code_section>


<%self:code_section
    prev_ver_name   = "copter"
    target_ver_name = "colision_single"
    title          = "Colide (Single Point)"
></%self:code_section>


## ----------------------------------------------
<% self.category = 'Choices' %>


<%self:code_section
    prev_ver_name   = "colision_single"
    target_ver_name = "level"
    title          = "Level advancing"
></%self:code_section>


<%self:code_section
    prev_ver_name   = "copter"
    target_ver_name = "physics"
    title          = "Physics"
></%self:code_section>


## ----------------------------------------------
<% self.category = 'Advanced' %>


<%self:code_section
    prev_ver_name   = "background"
    target_ver_name = "paralax"
    title          = "Paralax"
></%self:code_section>

<%self:code_section
    prev_ver_name   = "colision_single"
    target_ver_name = "colision_multi"
    title          = "Colide (Multi Point)"
></%self:code_section>

## ----------------------------------------------

##<img src="/static/projects/images/CopterLevel1.gif">