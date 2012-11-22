<%inherit file="_base.mako"/>

<%doc>
<%!
from teachprogramming.lib import resorce_helper, constants

def selected_class(a,b):
    if a==b:
        return 'selected'
    return ''

%>
</%doc>


##<div class="span3">
    <div data-spy="affix" data-offset-top="130" class="span3 sidebar-nav-container">
        ##  affix-top="150" affix-bottom="0"
        <div class="well sidebar-nav">
            <ul class="nav nav-list sidebar-nav-list">
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
##</div>



<div class="offset3 span9" data-spy="scroll" data-target=".sidebar-nav-list">
    ${next.body()}
</div>


