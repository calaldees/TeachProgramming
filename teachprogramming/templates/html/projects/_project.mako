<%inherit file="../_sidebar.mako"/>



<%def name='show_diff(prev_ver_name, target_ver_name)'>
    <%
        ##prev_version   = self.vername[prev_version]
        ##target_version = self.vername[target_version]
    
        diff = h.make_ver.get_diff(
            h.constants.project_filename % (project_type,project,selected_lang),
            prev_ver_name  ,
            target_ver_name,
            hidden_line_replacement='...more...'
        )
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
##${line[1:]}
<span class="${line_classs.get(line[0:1])}">${line[1:]}</span>
        % endif
    % endfor
        ##</pre></div> <!-- end code section -->
    ##</div> <!-- end code -->
</pre>
</%def>

<%def name="full_code(ver_name=None, code_inline=False)">
    <%
        #target_version = self.vername[target_version]
        code_url = request.route_path('project_code', project_type=project_type, project=project, selected_lang=selected_lang, version=ver_name)
    %>
    <a href="${code_url}" target="_blank">Full Code</a>
    % if code_inline:
    <button type="button" onclick="$(this).next().toggle();">Full code</button>
    <div class="hide">
        <a href="${code_url}">Version ${target_version}</a>
        <pre>${h.ver_string(project_type, project, selected_lang, target_version)}</pre>
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


<%def name="code_section(prev_ver_name, target_ver_name, title, heading_level=2)">
<% self.section_title(title) %>
    <h${heading_level}>${title.capitalize()}</h${heading_level}>
    
    ${self.full_code(target_ver_name)}
    
    <%
        def render_by_method_name(method_name_prefix):
            """
            Reflect on the 'caller' to find+execute methods named
            'before_code_py' or 'before_code_vb'
            This enabled templates to define langauge level messages
            """
            for render_method_name in [method_name_prefix+'_'+selected_lang, method_name_prefix]:
                try:
                    getattr(caller, render_method_name)()
                except:
                    pass
            return ''
    %>
    
    ${render_by_method_name('before_code')}
    ${self.show_diff(prev_ver_name, target_ver_name)}
    ${render_by_method_name('after_code')}
</section>
</%def>



<%def name='body()'  cache_key="project/%{project_type}/${project}.${selected_lang}">
    ## cached="True"
    <!-- Documentation for this project -->
    <% project_langs = h.get_project_langs(project_type, project) %>
    % if selected_lang in project_langs:
        ${next.body()}
    % else:
    <p>This project is avalable in</p>
        <ul>
            % for lang in project_langs:
            <li><a href="${request.route_path('project', project_type=project_type, project=project, selected_lang=lang)}">${h.constants.file_type_to_lang[lang]}</a></li>
            % endfor
        </ul>
    % endif
</%def>
