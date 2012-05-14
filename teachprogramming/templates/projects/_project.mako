<%inherit file="/_menu.mako"/>

<%!

import os

from teachprogramming.lib import make_ver, constants

def ver_string(project_type, project, format, version):
    return '\n'.join( make_ver.make_ver(constants.project_filename % (project_type, project,format), version) )

def include_file_(filename):
    source = open(filename, 'r')
    data = source.read()
    source.close()
    return data

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

<%def name="full_code(target_version=None, code_inline=False)">
    <% 
        code_url = "/code/%(project_type)s/%(project)s.%(format)s/%(target_version)s" % {'project_type':project_type, 'project':project, 'format':format, 'target_version':target_version}
    %>
    <a href="${code_url}" target="_blank">Full Code</a>
    % if code_inline:
    <button type="button" onclick="$(this).next().toggle();">Full code</button>
    <div class="hide">
        <a href="${code_url}">Version ${target_version}</a>
        <pre>${ver_string(project_type, project, format, target_version)}</pre>
    </div>
    % endif
</%def>

<%def name="t_include_file(filename)">
    <pre>${include_file_(filename)}</pre>
</%def>

<%def name='body()'  cache_key="${project}.${format}">
    ## cached="True"
    <%
        self.files = [file for file in os.listdir(constants.project_path) if file.startswith('%s.' % project)]
    %>
    <!-- Documentation for this project -->
    ${next.body()}
    
</%def>
