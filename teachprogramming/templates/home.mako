<%inherit file="/_menu.mako"/>


<div>
    <p>Homepage</p>
    
    <h2>Ethos</h2>
    
    <ul>
        <li>Get people creating <em>fun</em> <em>working</em> projects quickly for instant gratification and progress. Then, explore/understand how they work. People then have a <em>refernce point</em> as to what the code is actually doing.</li>
    </ul>
    
    <ul>
        <li>This site will <em>not</em> teach you every intricacy of becomming a developer.</li>
        <li>It will give you some exiting first stepping stones.</li>
    </ul>
    
    <p>Enjoy!</p>
    
    <h2>Examples</h2>
    <%namespace name="project" file="projects/_project.mako"/>
    ##${project.web_demo(vername['full'])}
</div>