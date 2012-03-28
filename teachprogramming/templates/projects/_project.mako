<%inherit file="/base.mako"/>

<%! 
import os
import teachprogramming.lib.make_ver as make_ver
%>

<%def name='show_diff(version)'>
    <%
        diff = make_ver.get_diff('teachprogramming/static/projects/%s.%s' % (project,format), version)
        line_classs = {'-':'remove', '+':'add'}
        open_section = False
    %>
    <div class='code'>
    % for line in diff:
        % if line.startswith('@@'):
            % if open_section:
        </div>
            % endif
            <% open_section = True %>
        <div class='section'>
        % elif not (line.startswith('---') or line.startswith('+++')):
            <pre class='${line_classs.get(line[0:1])}'>${line}</pre>
        % endif
    % endfor
        </div> <!-- end code section -->

    </div> <!-- end code -->
</%def>



<%def name='body()'>
    <%
        file_type_to_lang = dict(
            py   = 'Python',
            html = 'Javascript/HTML5',
            vb   = 'VB.NET',
            php  = 'PHP',
            java = 'Java',
        )
        files = [file for file in os.listdir('teachprogramming/static/projects/') if file.startswith('%s.' % project)]
    %>
    <ul>
    % for file in files:
        <% 
            fileext            = make_ver.get_fileext(file) 
            format_description = file_type_to_lang.get(fileext)
            css_class = ''
            if fileext == format:
                css_class = 'selected'
        %>
        <li><a href='/project/${project}.${fileext}' class='${css_class}'>${format_description}</a></li>
    % endfor
    </ul>
    
    ${next.body()}
    
</%def>