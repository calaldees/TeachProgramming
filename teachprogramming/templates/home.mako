<%inherit file="/_sidebar.mako"/>


<%def name="init()"><%
    #self.titlebar_active        = 'about'
    self.text_title             = 'Programming! Its Badass!!'
    self.text_title_description = 'Ever dreamed of kicking ass ... well now you can.'
%></%def>

<div>
    <p>TeachProgramming</p>
    
    <h2>What</h2>
        <p>Build up games in steps with previews in Javascript/HTML5, Python, Java and VB.NET</p>
        <p>Programming reference, other activities, chat system, message boards, SMTP, regex + more</p>
        <p>(Eventually, with print styles) These activities can be printed and used offline as well. (the original concept was 1 page of A4 printed 2 to a page and duplex and handed to kids)</p>
            
        <h3>Dymistify the preconceptions</h3>
        <ul>
            <li>This site will <em>not</em> teach you every intricacy of becoming a developer.</li>
            <li>It will give you some exiting first stepping stone examples.</li>
        </ul>


    <h2>How</h2>
        <ul>
            <li>
                <p>Get people creating <em>fun</em> <em>working</em> projects quickly for instant gratification and progress.</p>
                <p>People then have a <em>context</em> as to what the code is actually doing.</p>
                <p>Then, a teacher professional can help the learner explore/understand how they work.</p>
            </li>
            <li>
                By creating the same game in multiple languages the learner can experience the similarities/differences of each language.
            </li>
            <li>
                By using the raw industry languages, learners have real progression paths. Rather than binding them to an abstract point and click interface.
            </li>
        </ul>


    <h3>Why</h3>
        <ul>
            <li>Fun</li>
            <li>Government wants Computing back on the agenda</li>
            <li>Teachers are too busy to explore all langauges in detail to create these games from scatch themselfs</li>
            <li>Learning real industry tools/skills is important</li>
            <li>Actually building something! (With HTML5/Javascript learners can take the games home on a mobile phone and show people their creations)</li>
            <li>It's just rewarding and creative</li>
        </ul>

    
    <h3>Who</h3>
        <ul>
            <li>Learners can just come to site of there own accord and create some cool stuff. People of all ages, who are curious about coding stuff</li>
            <li>Teachers (with minimal knowledge) can point class's at the resources</li>
            <li>Teachers can lead cool sessions (lesson plans coming soon, because i'm a teacher too!)</li>
        </ul>
    
    
    <p>Enjoy!</p>
    
    <h2>Examples of the stuff you can build</h2>
    <%namespace name="project" file="projects/_project.mako"/>
    ##${project.web_demo(vername['full'])}
</div>