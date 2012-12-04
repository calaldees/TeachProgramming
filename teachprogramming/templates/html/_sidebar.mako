<%inherit file="_base.mako"/>

<%doc>
<%!

def selected_class(a,b):
    if a==b:
        return 'selected'
    return ''

%>
</%doc>

<% self.sidebar_content = [] %>

<% body_capture = capture(next.body) %>

% if self.sidebar_content:
<div data-spy="affix" data-offset-top="130" class="span3 sidebar-nav-container">
    ##  affix-top="150" affix-bottom="0"
    <div class="well well-small">
        ##sidebar-nav
        <ul class="nav nav-list">
            ##sidebar-nav-list
            <%def name="sidebar()">
                <% current_category = None %>
                % for title, category in  self.sidebar_content :
                    % if category != current_category:
                    <% current_category = category %>
                    <li class="nav-header">${current_category}</li>
                    % endif
                    <li><a href="#${h.encode_id(title)}">${title}</a></li>
                    ##class="active"
                % endfor
            </%def>
            ${self.sidebar()}
        </ul>
    </div><!--/.well -->
</div>

<div class="offset3 span9" data-spy="scroll" data-target=".sidebar-nav-list">
    ${body_capture | n}
</div>
% else:
<div class="span12">
    ${body_capture | n}
</div>
% endif

