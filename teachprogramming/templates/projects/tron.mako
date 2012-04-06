<%inherit file="_project.mako"/>



<h1>Tron</h1>

${self.show_diff(None, 'base1')}

<h2>Part 1: Simple Line</h2>
<h3>A Line that Moves</h3>

${self.show_diff('base1','base2')}

<h3>Keyboard Input</h3>
Replace the ? with 0, 1 or -1

${self.show_diff('base2','base3')}



<h2>Part 2: Collisions</h2>
Get the pixel of where we are about to move to.
If it is not black then we have hit an object so reset the players coordinate

${self.show_diff('base3','base4')}



<h2>Part 3: Extras</h2>

<h3>Player 2</h3>
Can you add a second player?

${self.show_diff('base4','2players')}

<h3>Score</h3>

${self.show_diff('2players','2players_score')}

<h3>Background Obstacles</h3>

<h2>Part 4: Challenge Ideas</h2>
<h3>Wrap around</h3>
When you go off one side of the screen you appear the other side.
${self.show_diff('base4','wrap')}

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
    
<h3>Maze levels</h3>

<img src="/static/projects/Maze1.gif"/>
<img src="/static/projects/Maze2.gif"/>


<pre>
Maze is a one player game to get to the red exit.
Create a set of level graphics 320 by 240 with a black background.



  int current_level = 1;

    if (Color.BLACK.equals(getPixel(player1_x_pos,player1_y_pos))) {
      putPixel(player1_x_pos,player1_y_pos,Color.YELLOW);
    }
    else if (Color.RED.equals(getPixel(player1_x_pos,player1_y_pos))) {
      current_level = current_level + 1;
      reset();
    }
    else {
      reset();
    }

  public void reset() {
    clearScreen();
    putImage(0,0,'Maze' + current_level + '.png');
</pre>