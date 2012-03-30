<%inherit file="/base.mako"/>

<%!
import teachprogramming.lib.resorce_helper as resorce_helper
%>

<h2>Game Projects</h2>
<ul>
    % for project in resorce_helper.get_projects():
        <li>${project.capitalize()}
        % for fileext in resorce_helper.get_project_langs(project):
            <a href="/project/${project}.${fileext}">${fileext}</a>
        % endfor
        </li>
    % endfor
</ul>

<h2>Network Projects</h2>
<ul>
    <li>Paint</li>
    <li>Chat</li>
</ul>

<h2>Activities</h2>
<ul>
    <li>SMTP</li>
    <li>HTTP</li>
    <li>Regex: rip from URL's</li>
    <li>iCal</li>
    <li>Google Maps</li>
</ul>

<h2>Reference</h2>
<p>These will be replaced with html dynamic versions in time</p>
<ul>
    <li><a href="/static/docs/LanguageCheetSheet.odt">Language Cheet Sheet</a> Do the same stuff in VB.NET, Python, Java, PHP</li>
    <li><a href="/static/docs/unit1-projects.odt">Projects for A-Level spec</a></li>
</ul>

<h2>Kinesthetic Activities</h2>
<p>examples of talks and conveying concepts of computing in a physical way</p>

<h2>Setup</h2>
<p>How to setup/install the langauges for use on this site
<ul>
    <li>VB.NET</li>
    <li>Java</li>
    <li>Javascript/HTML5</li>
    <li>Python</li>
    <li>PHP</li>
</ul>

<h2>Contribute</h2>
git repository
contact@teachthisstufflikewellgood.net
