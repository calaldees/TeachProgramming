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
    prev_version   = ""
    target_version = "base"
    title          = "Base"
></%self:code_section>


<%self:code_section
    prev_version   = "base"
    target_version = "background"
    title          = "Background"
></%self:code_section>


<%self:code_section
    prev_version   = "background"
    target_version = "copter"
    title          = "Copter"
></%self:code_section>


<%self:code_section
    prev_version   = "copter"
    target_version = "colision_single"
    title          = "Colide (Single Point)"
></%self:code_section>


## ----------------------------------------------
<% self.category = 'Choices' %>


<%self:code_section
    prev_version   = "colision_single"
    target_version = "level"
    title          = "Level advancing"
></%self:code_section>


<%self:code_section
    prev_version   = "copter"
    target_version = "physics"
    title          = "Physics"
></%self:code_section>


## ----------------------------------------------
<% self.category = 'Advanced' %>


<%self:code_section
    prev_version   = "background"
    target_version = "paralax"
    title          = "Paralax"
></%self:code_section>

<%self:code_section
    prev_version   = "colision_single"
    target_version = "colision_multi"
    title          = "Colide (Multi Point)"
></%self:code_section>

## ----------------------------------------------

##<img src="/static/projects/images/CopterLevel1.gif">