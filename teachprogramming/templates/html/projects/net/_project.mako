<%inherit file="../_project.mako"/>


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


<%def name="body()">
${next.body()}
</%def>