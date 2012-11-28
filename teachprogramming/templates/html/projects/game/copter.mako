<%inherit file="_project.mako"/>

<%def name="init()">
<%
    vername = {
        'blank'          :'',
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
    self.vername = vername
%>
</%def>



<h1>Copter</h1>
demo
${parent.web_demo(self.vername['full'])}

## ----------------------------------------------
<% self.category = 'Base Compoents' %>

<%self:code_section
    prev_version   = "blank"
    target_version = "base1"
    title          = "Base"    
></%self:code_section>


<%self:code_section
    prev_version   = "base1"
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