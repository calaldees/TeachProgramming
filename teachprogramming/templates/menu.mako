<%inherit file="/base.mako"/>

<%!
from teachprogramming.lib import resorce_helper, constants

def selected_class(a,b):
    if a==b:
        return 'selected'
    return ''

%>

<div class="menu">
    <a href="/">Home</a>
    
    <h2>Game Projects</h2>
        <!-- Projects -->
        <ul>
        % for p in resorce_helper.get_projects():
        % if project==p:
        <li class="selected">
        % else:
        <li>
        % endif
            ${p.capitalize()}
            <% fileexts = resorce_helper.get_project_langs(p) %>
            % for lang in constants.file_type_to_lang.keys():
                % if lang in fileexts:
                    <a href="/project/${p}.${lang}" class="lang_icon lang_${lang} icon16 i_${lang}"><span>${lang}</span></a>
                % endif
            % endfor
        </tr>
        % endfor
    </table>
    
    <h2>Network Projects</h2>
    <ul>
        <li>Paint</li>
        <li>Chat</li>
        <li>NetRace</li>
        <li>NetPong</li>
        <li>NetCopter</li>
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
    git repository link
    contact@teachthisstufflikewellgood.net
</div>

<div class="main">
    ${next.body()}
</div>