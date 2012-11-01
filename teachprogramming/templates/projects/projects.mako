<%inherit file="/_base.mako"/>

<%
    self.text_title             = 'Projects'
    self.text_title_description = 'Pick a project and get coding!'
%>



    <h2>Game Projects</h2>
        <!-- Projects -->
        <ul>
        % for p in resorce_helper.get_projects('game'):
        % if project==p:
        <li class="selected">
        % else:
        <li>
        % endif
            ${p.capitalize()}
        </li>
        % endfor
    </ul>
    
    <h2>Network Projects</h2>
    <ul>
        <li>Paint</li>
        <li><a href="/project/net/chat.html">Chat</a></li>
        <li>NetRace</li>
        <li>NetPong</li>
        <li>NetCopter</li>
    </ul>
    
    <h2>Web Projects</h2>
    <ul>
        <li><a href="/project/web/php.html">Simple Messagbord</a><li>
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
    