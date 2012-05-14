<%inherit file="_project.mako"/>

<%
    vername = {
        'base1'         :'1',
        'base2'         :'1,line',
        'base3'         :'1,line,input',
        'base4'         :'1,line,input,colide',
        '2players'      :'1,line,input,colide,player2',
        '2players_score':'1,line,input,colide,player2,score',
        'wrap'          :'1,line,input,colide,wrap',
        '2players_wrap' :'1,line,input,colide,player2,wrap,wrap2',
        'maze'          :'1,line,input,colide,maze',
        
    }
%>


<h1>Tron</h1>

demo
${parent.web_demo(vername['2players_score'])}
${parent.web_demo(vername['maze'])}


<%self:code_section
    prev_version   = "${None}"
    target_version = "${vername['base1']}"
>
    <%def name="title()">
        <h3>Base</h3>
    </%def>
    <%def name="code_before()">
        <p>before</p>
    </%def>
</%self:code_section>



<h2>Part 1: Simple Line</h2>

<%self:code_section
    prev_version   = "${vername['base1']}"
    target_version = "${vername['base2']}"
>
    <%def name="title()">
        <h3>A Line that Moves</h3>
    </%def>
    <%def name="code_before()">
        <p>before</p>
    </%def>
    <%def name="code_after()">
        <p>after</p>
    </%def>
</%self:code_section>

<%self:code_section
    prev_version   = "${vername['base2']}"
    target_version = "${vername['base3']}"
>
    <%def name="title()">
        <h3>Keyboard Input</h3>
    </%def>
    <%def name="code_before()">
        <p>Replace the ? with 0, 1 or -1</p>
    </%def>
</%self:code_section>

<%self:code_section
    prev_version   = "${vername['base3']}"
    target_version = "${vername['base4']}"
>
    <%def name="title()">
        <h2>Part 2: Collisions</h2>
    </%def>
    <%def name="code_before()">
        Get the pixel of where we are about to move to.
        If it is not black then we have hit an object so reset the players coordinate
    </%def>
</%self:code_section>






<h2>Part 3: Extras</h2>


<%self:code_section
    prev_version   = "${vername['base4']}"
    target_version = "${vername['2players']}"
>
    <%def name="title()">
        <h3>Player 2</h3>
    </%def>
    <%def name="code_before()">
        Can you add a second player?
    </%def>
</%self:code_section>




<%self:code_section
    prev_version   = "${vername['2players']}"
    target_version = "${vername['2players_score']}"
>
    <%def name="title()">
        <h3>Score</h3>
    </%def>
    <%def name="code_before()">
        Scoreing, reset after 5 deaths
    </%def>
</%self:code_section>




<h3>Background Obstacles</h3>

<h2>Part 4: Challenge Ideas</h2>


<%self:code_section
    prev_version   = "${vername['base4']}"
    target_version = "${vername['wrap']}"
>
    <%def name="title()">
        <h3>Wrap around</h3>
    </%def>
    <%def name="code_before()">
        When you go off one side of the screen you appear the other side.
    </%def>
</%self:code_section>






<h3>3 players</h3>
Add new keys (try I,J,K,L)

<h3>Boost</h3>
<pre>
Pressing a button will make your line move twice as fast
    if (isKeyPressed(KeyEvent.VK_DOWN )) {player1_x_move=0; player1_y_move=1;}
    if (isKeyPressed(KeyEvent.VK_SPACE)) {
      player1_x_move = player1_x_move*2;
      player1_y_move = player1_y_move*2;
    }
To limit people using this all the time, give them a limited about of booster fuel.
  int player1_boost_fuel = 100;

    if (isKeyPressed(KeyEvent.VK_SPACE)) {
      if (player1_boost_fuel>0) {
        player1_boost_fuel = player1_boost_fuel - 1;
        player1_x_move = player1_x_move*2;
        player1_y_move = player1_y_move*2;
      }
    }

  public void reset() {
    player1_boost_fuel = 100;
</pre>


<%self:code_section
    prev_version   = "${vername['base4']}"
    target_version = "${vername['maze']}"
>
    <%def name="title()">
        <h3>Maze levels</h3>
    </%def>
    <%def name="code_before()">
        <p>Maze is a one player game to get to the red exit.</p>
        <p>Create a set of level graphics 640 by 480 with a black or transparent background.</p>
    </%def>
    <%def name="code_after()">
        <img src="images/Maze1.gif"/>
        <img src="images/Maze2.gif"/>
        <img src="images/Maze3.gif"/>
    </%def>
</%self:code_section>

