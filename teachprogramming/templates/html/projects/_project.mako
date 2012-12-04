<%inherit file="../_sidebar.mako"/>



<%def name='show_diff(prev_version, target_version)'>
    <%
        prev_version   = self.vername[prev_version]
        target_version = self.vername[target_version]
    
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
        target_version = self.vername[target_version]
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
    
    ${self.full_code(target_version)}
    
    <%
        def render_by_method_name(method_name_prefix):
            """
            Reflect on the 'caller' to find+execute methods named
            'before_code_py' or 'before_code_vb'
            This enabled templates to define langauge level messages
            """
            for render_method_name in [method_name_prefix+'_'+format, method_name_prefix]:
                try:
                    getattr(caller, render_method_name)()
                except:
                    pass
            return ''
    %>
    
    ${render_by_method_name('before_code')}
    ${self.show_diff(prev_version, target_version)}
    ${render_by_method_name('after_code')}
</section>
</%def>



<%def name='body()'  cache_key="project/%{project_type}/${project}.${format}">
    ## cached="True"
    <!-- Documentation for this project -->
    ${next.body()}
    
</%def>
