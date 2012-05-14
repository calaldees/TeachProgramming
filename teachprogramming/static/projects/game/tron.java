import GameLib.GameFrame;
import java.awt.Color;
import java.awt.event.KeyEvent;

public class Tron extends GameFrame {

  int   player1_x_pos;  // Ver: 2
  int   player1_y_pos;  // Ver: 2
  int   player1_x_move; // Ver: 2
  int   player1_y_move; // Ver: 2
  Color player1_color = Color.YELLOW; // Ver: 2
                        // Ver: 2
  int   player2_x_pos;  // Ver: 5
  int   player2_y_pos;  // Ver: 5
  int   player2_x_move; // Ver: 5
  int   player2_y_move; // Ver: 5
  Color player2_color = Color.RED; // Ver: 5
                        // Ver: 5
  int player1_deaths = 0; // Ver: 6
  int player2_deaths = 0; // Ver: 6
                          // Ver: 6
  public void reset() {
    player1_x_pos = 100;            // Ver: 2
    player1_y_pos = 100;            // Ver: 2
    player1_x_move = 1;             // Ver: 2
    player1_y_move = 0;             // Ver: 2
    player2_x_pos = getWidth() -100;// Ver: 5
    player2_y_pos = getHeight()-100;// Ver: 5
    player2_x_move =-1;             // Ver: 5
    player2_y_move = 0;             // Ver: 5
    clearScreen();
  }
  
  public void timerEvent() {
    if (isKeyPressed(KeyEvent.VK_UP   )) {player1_x_move= 0; player1_y_move=-1;} // Ver: 3
    if (isKeyPressed(KeyEvent.VK_DOWN )) {player1_x_move= 0; player1_y_move= 1;} // Ver: 3 hidden
    if (isKeyPressed(KeyEvent.VK_LEFT )) {player1_x_move=-1; player1_y_move= 0;} // Ver: 3 hidden
    if (isKeyPressed(KeyEvent.VK_RIGHT)) {player1_x_move= 1; player1_y_move= 0;} // Ver: 3 hidden

                                                                                 // Ver: 3
    if (isKeyPressed(KeyEvent.VK_A    )) {player2_x_move=-1; player2_y_move= 0;} // Ver: 5
    if (isKeyPressed(KeyEvent.VK_D    )) {player2_x_move= 1; player2_y_move= 0;} // Ver: 5 hidden
    if (isKeyPressed(KeyEvent.VK_W    )) {player2_x_move= 0; player2_y_move=-1;} // Ver: 5 hidden
    if (isKeyPressed(KeyEvent.VK_S    )) {player2_x_move= 0; player2_y_move= 1;} // Ver: 5 hidden
                                                                                 // Ver: 5
    player1_x_pos = player1_x_pos + player1_x_move; // Ver: 2
    player1_y_pos = player1_y_pos + player1_y_move; // Ver: 2
                                                    // Ver: 2
    player2_x_pos = player2_x_pos + player2_x_move; // Ver: 5
    player2_y_pos = player2_y_pos + player2_y_move; // Ver: 5
                                                    // Ver: 5
    if (!Color.BLACK.equals(getPixel(player1_x_pos,player1_y_pos))) { // Ver: 4
      msgBox("Player1 Crashed");                                      // Ver: 4
      player1_deaths = player1_deaths + 1;                            // Ver: 6
      reset();                                                        // Ver: 4
    }                                                                 // Ver: 4
                                                                      // Ver: 4
    if (!Color.BLACK.equals(getPixel(player2_x_pos,player2_y_pos))) { // Ver: 5
      msgBox("Player2 Crashed");                                      // Ver: 5
      player2_deaths = player2_deaths + 1;                            // Ver: 6
      reset();                                                        // Ver: 5
    }                                                                 // Ver: 5
                                                                      // Ver: 5
    putPixel(player1_x_pos,player1_y_pos,player1_color); // Ver: 2
    putPixel(player2_x_pos,player2_y_pos,player2_color); // Ver: 5
                                                         // Ver: 2
    if (player1_deaths+player2_deaths>=5) {                                               // Ver: 6
      msgBox("Game Over Player1Deaths:"+player1_deaths+" Player2Deaths:"+player2_deaths); // Ver: 6
      exitFinal();                                                                        // Ver: 6
    }                                                                                     // Ver: 6
                                                                                          // Ver: 6
    repaintScreen();
  }  

  public static void main(String[] args) {new Tron();}
  
  public Tron() {
    reset();
  }
}
