<%inherit file="_project.mako"/>


<%def name="init()">
<%
    self.titlebar_active        = 'projects'
    self.text_title             = 'Message'
    self.text_title_description = 'Run your own message board ... deal with your users, with an iron fist'

%>
</%def>


## ----------------------------------------------
<% self.section_title('Setup') %>
    <h2>Setup</h2>
    <p>Explanation of web server</p>
    
    <!--
        Setup PHP
        Setup Python
    -->
</section>



## ----------------------------------------------
<% self.category = 'Basic Webpage' %>


<%self:code_section
    prev_ver_name   = ""
    target_ver_name = "base"
    title          = "Basic Webpage"
>
</%self:code_section>


## ----------------------------------------------
<% self.category = 'Messages' %>


<%self:code_section
    prev_ver_name   = "base"
    target_ver_name = "textarea"
    title          = "Text Input"
>
</%self:code_section>

<%self:code_section
    prev_ver_name   = "textarea"
    target_ver_name = "save_message"
    title          = "Save a message"
>
</%self:code_section>

<%self:code_section
    prev_ver_name   = "save_message"
    target_ver_name = "show_messages"
    title          = "Show messages"
>
</%self:code_section>

<%self:code_section
    prev_ver_name   = "show_messages"
    target_ver_name = "username"
    title          = "Username"
>
</%self:code_section>


## ----------------------------------------------
<% self.category = 'Login System' %>

<%self:code_section
    prev_ver_name   = "username"
    target_ver_name = "login"
    title          = "Login"
>
</%self:code_section>


<%self:code_section
    prev_ver_name   = "login"
    target_ver_name = "logout"
    title          = "Logout"
>
</%self:code_section>
