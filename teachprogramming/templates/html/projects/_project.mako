<%inherit file="../_sidebar.mako"/>



<%def name='show_diff(prev_version, target_version)'>

    <%
        diff = h.make_ver.get_diff(h.constants.project_filename % (project_type,project,format), prev_version, target_version, hidden_line_replacement='...more...')
        line_classs = {'-':'code_remove', '+':'code_add'}
        open_section = False
    %>
    ##<div class='code'>
<pre>
    % for line in diff:
        % if line.startswith('@@'):
            % if open_section:
</pre>
<pre>
        ##</pre></div>
            % endif
            <% open_section = True %>
        ##<div class='code_section'><pre>
        % elif not (line.startswith('---') or line.startswith('+++')):
##<p class='${line_classs.get(line[0:1])}'>${line}</p>
<span class="${line_classs.get(line[0:1])}">${line[1:]}</span>
        % endif
    % endfor
        ##</pre></div> <!-- end code section -->
    ##</div> <!-- end code -->
</pre>
</%def>

<%def name="full_code(target_version=None, code_inline=False)">
    <% 
        #code_url = "/code/%(project_type)s/%(project)s.%(format)s/%(target_version)s" % {'project_type':project_type, 'project':project, 'format':format, 'target_version':target_version}
        code_url = request.route_path('project_code', project_type=project_type, project=project, format=format, version=target_version)
    %>
    <a href="${code_url}" target="_blank">Full Code</a>
    % if code_inline:
    <button type="button" onclick="$(this).next().toggle();">Full code</button>
    <div class="hide">
        <a href="${code_url}">Version ${target_version}</a>
        <pre>${h.ver_string(project_type, project, format, target_version)}</pre>
    </div>
    % endif
</%def>

<%def name="t_include_file(filename)">
    <pre>${include_file_(filename)}</pre>
</%def>


<%def name="section_title(title)"><%
    try   : category = self.category
    except: category = None
    self.sidebar_content.append((title,category))
%>
<section id='${h.encode_id(title)}'>
</%def>


<%def name="code_section(prev_version, target_version, title, heading_level=2)">
<% self.section_title(title) %>
    <h${heading_level}>${title.capitalize()}</h${heading_level}>
    
    ${self.full_code(self.vername[target_version])}
    
    % try:
    ${caller.before_code()}
    % except:
    % endtry
    
    ${self.show_diff(self.vername[prev_version], self.vername[target_version])}
    
    % try:
    ${caller.after_code()}
    % except:
    % endtry
</section>
</%def>



<%def name='body()'  cache_key="%{project_type}/${project}.${format}">
    ## cached="True"
    ##<%
    ##    self.files = [file for file in os.listdir(os.path.join(h.constants.project_path,project_type)) if file.startswith('%s.' % project)]
    ##%>
    <!-- Documentation for this project -->
    ${next.body()}
    
</%def>
