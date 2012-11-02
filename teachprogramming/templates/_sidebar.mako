<%inherit file="/_base.mako"/>

<%doc>
<%!
from teachprogramming.lib import resorce_helper, constants

def selected_class(a,b):
    if a==b:
        return 'selected'
    return ''

%>
</%doc>

<div class="span3 sidebar">
    <div data-spy="affix" data-offset-top="30" affix-top="100" affix-bottom="100">
        <div class="well sidebar-nav">
            <ul class="nav nav-list">
                <%def name="sidebar()">
                <li class="nav-header">Example Heading</li>
                <li class="active"><a href="#">to be overridden</a></li>
                <li><a href="#">Link</a></li>
                <li class="nav-header">Sidebar</li>
                <li><a href="#">Link</a></li>
                </%def>
                ${self.sidebar()}
            </ul>
        </div><!--/.well -->
    </div>
</div>

<div class="span9" data-spy="scroll" data-target=".sidebar">
    ${next.body()}
</div>


