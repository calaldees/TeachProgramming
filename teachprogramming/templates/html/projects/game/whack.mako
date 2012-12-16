<%inherit file="_project.mako"/>

<%def name="init()">
<%
    self.titlebar_active        = 'projects'
    self.text_title             = 'Whack'
    self.text_title_description = 'Whack a wham'

    vername = {
        'blank'          :'',
        'full'           :'1',
    }
    self.vername = vername
%>
</%def>


demo
${parent.web_demos('full')}


<% self.category = 'Base Compoents' %>

<%self:code_section
    prev_version   = "blank"
    target_version = "full"
    title          = "Full"
></%self:code_section>

