<%inherit file="/_base.mako"/>

<%!
from teachprogramming.lib import resorce_helper, constants

def selected_class(a,b):
    if a==b:
        return 'selected'
    return ''

%>


<div id="menu_affix" data-spy="affix" data-offset-top="200" class="span3">
    <div class="well sidebar-nav">
        <ul class="nav nav-list">
            ${self.sidebar()}
        </ul>
    </div><!--/.well -->
</div>


<div class="span9">
    ${next.body()}
</div>


<%def name="sidebar()">
            <li class="nav-header">Sidebar</li>
            <li class="active"><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
            <li class="nav-header">Sidebar</li>
            <li><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
            <li class="nav-header">Sidebar</li>
            <li><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
</%def>

<%doc>
<div class="menu">
    <a href="/">Home</a>
    
    
    
</div>

<div class="main">
    ${next.body()}
</div>
</%doc>