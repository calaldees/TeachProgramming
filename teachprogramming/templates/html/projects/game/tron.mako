<%inherit file="_project.mako"/>

<%def name="init()">
<%
    self.titlebar_active        = 'projects'
    self.text_title             = 'Tron'
    self.text_title_description = 'Head to head line drawing action or Maze'

    vername = {
        'blank'         :'',
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
    self.vername = vername
%>
</%def>


demo
${parent.web_demo(self.vername['2players_score'])}
${parent.web_demo(self.vername['maze'])}



<%self:code_section
    prev_version   = "blank"
    target_version = "base1"
    title          = "Base"    
>
    <%def name="before_code()">
        <p>before</p>
    </%def>
</%self:code_section>

## ----------------------------------------------
<% self.category = 'Base components' %>

<h2>Part 1: Base Componenets</h2>


<%self:code_section
    prev_version   = "base1"
    target_version = "base2"
    title          = "A Line that Moves"
    heading_level  = "3"
>
    <%def name="before_code()">
        <p>before</p>
    </%def>
</%self:code_section>


<%self:code_section
    prev_version   = "base2"
    target_version = "base3"
    title          = "Keyboard Input"
    heading_level  = "3"
>
    <%def name="before_code()">
        <p>Replace the ? with 0, 1 or -1</p>
    </%def>
</%self:code_section>

<%self:code_section
    prev_version   = "base3"
    target_version = "base4"
    title          = "Part 2: Collisions"
>
    <%def name="before_code()">
        Get the pixel of where we are about to move to.
        If it is not black then we have hit an object so reset the players coordinate
    </%def>
</%self:code_section>



## ----------------------------------------------
<% self.category = 'Choices' %>

<h2>Part 2: Choices</h2>

<%self:code_section
    prev_version   = "base4"
    target_version = "2players"
    title          = "Player 2"
    heading_level  = "3"
>
    <%def name="before_code()">
        Can you add a second player?
    </%def>
</%self:code_section>

<%self:code_section
    prev_version   = "2players"
    target_version = "2players_score"
    title          = "Score"
    heading_level  = "3"
>
    <%def name="before_code()">
        Scoreing, reset after 5 deaths
    </%def>
</%self:code_section>



<%self:code_section
    prev_version   = "base4"
    target_version = "wrap"
    title          = "Wrap around"
    heading_level  = "3"
>
    <%def name="before_code()">
        When you go off one side of the screen you appear the other side.
    </%def>
</%self:code_section>



<%self:code_section
    prev_version   = "base4"
    target_version = "maze"
    title          = "Maze levels"
    heading_level  = "3"
>
    <%def name="before_code()">
        <p>Maze is a one player game to get to the red exit.</p>
        <p>Create a set of level graphics 640 by 480 with a black or transparent background.</p>
    </%def>
    <%def name="after_code()">
        <img src="images/Maze1.gif"/>
        <img src="images/Maze2.gif"/>
        <img src="images/Maze3.gif"/>
    </%def>
</%self:code_section>


## ----------------------------------------------
<% self.category = 'Advanced' %>

<h2>Part 3: Advanced</h2>

${self.section_title('3 Players')}
    <h3>3 players</h3>
    Add new keys (try I,J,K,L)
</section>

${self.section_title('Boost')}
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
</section>
