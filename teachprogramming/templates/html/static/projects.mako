<%inherit file="../_base.mako"/>


<%def name="init()"><%
    self.titlebar_active        = 'projects'
    self.text_title             = 'Projects'
    self.text_title_description = 'Pick a project and get coding!'
%></%def>

<% format='py' %>

    <h2>Game Projects</h2>
        <!-- Projects -->
    <ul>
        % for p in h.get_projects('game'):
        <li>
            <a href="${request.route_path('project', project_type='game', project=p, format=format)}">${p.capitalize()}</a>
        </li>
        % endfor
    </ul>
    
    <h2>Network Projects</h2>
    <ul>
        % for p in h.get_projects('net'):
        <li>
            <a href="${request.route_path('project', project_type='net', project=p, format=format)}">${p.capitalize()}</a>
        </li>
        % endfor
        <li>Paint</li>
        <li>NetRace</li>
        <li>NetPong</li>
        <li>NetCopter</li>
    </ul>
    
    <h2>Web Projects</h2>
    <ul>
        % for p in h.get_projects('web'):
        <li>
            <a href="${request.route_path('project', project_type='web', project=p, format=format)}">${p.capitalize()}</a>
        </li>
        % endfor
        ##<li><a href="/project/web/php.html">Simple Messagbord</a><li>
        <li>Quiz Graphs<li>
        <li>Regex: rip from URL's</li>
        <li>Mobile App (jQueryMobile)</li>
    </ul>
    
    <h2>Activities</h2>
    <ul>
        <li>SMTP</li>
        <li>HTTP</li>
        <li>iCal</li>
        <li>Google Maps</li>
    </ul>
    