<%inherit file="/_menu.mako"/>

<%!

import os

from teachprogramming.lib      import make_ver, constants

%>


<%def name='show_diff(prev_version, target_version)'>
    
    <%
        diff = make_ver.get_diff(constants.project_filename % (project_type,project,format), prev_version, target_version, hidden_line_replacement='...more...')
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

<%def name="full_code(target_version)">
    <a href="/code/${project}.${format}/${target_version}" target="_blank">Full Code</a>
    <%doc>
    <button type="button" onclick="$(this).next().toggle();">Full code</button>
    <div class="hide">
        <a href="/code/${project}.${format}/${target_version}">Version ${target_version}</a>
        <pre>${ver_string(project, format, target_version)}</pre>
    </div>
    </%doc>
</%def>


<%def name='body()'  cache_key="${project}.${format}">
    ## cached="True"
    <%
        self.files = [file for file in os.listdir(constants.project_path) if file.startswith('%s.' % project)]
    %>
    <!-- Documentation for this project -->
    ${next.body()}
    
</%def>
