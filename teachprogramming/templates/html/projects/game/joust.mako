<%inherit file="_project.mako"/>

<%def name="init()">
<%
    self.titlebar_active        = 'projects'
    self.text_title             = 'Joust'
    self.text_title_description = 'Joust'
%>
</%def>


${parent.web_demos('full')}


<% self.category = 'Base Compoents' %>

<%self:code_section
    prev_ver_name   = ""
    target_ver_name = "full"
    title          = "Full"
></%self:code_section>



<img src="/static/projects/images/JoustPlayer1.png"/>
<img src="/static/projects/images/JoustPlayer2.png"/>
<img src="/static/projects/images/JoustTitle.png"/>
