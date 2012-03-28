import GameLib.GameFrame;
import java.awt.Color;
import java.awt.event.KeyEvent;

public class Tron extends GameFrame {

  int player1_x_pos;
  int player1_y_pos;
  int player1_x_move;
  int player1_y_move;
  
  int player2_x_pos;
  int player2_y_pos;
  int player2_x_move;
  int player2_y_move;
  
  int player1_deaths = 0;
  int player2_deaths = 0;
  
  public Tron() {
    reset();
  }
  
  public void timerEvent() {
    if (isKeyPressed(KeyEvent.VK_LEFT )) {player1_x_move=-1; player1_y_move= 0;}
    if (isKeyPressed(KeyEvent.VK_RIGHT)) {player1_x_move= 1; player1_y_move= 0;}
    if (isKeyPressed(KeyEvent.VK_UP   )) {player1_x_move= 0; player1_y_move=-1;}
    if (isKeyPressed(KeyEvent.VK_DOWN )) {player1_x_move= 0; player1_y_move= 1;}
   
    if (isKeyPressed(KeyEvent.VK_A    )) {player2_x_move=-1; player2_y_move= 0;}
    if (isKeyPressed(KeyEvent.VK_D    )) {player2_x_move= 1; player2_y_move= 0;}
    if (isKeyPressed(KeyEvent.VK_W    )) {player2_x_move= 0; player2_y_move=-1;}
    if (isKeyPressed(KeyEvent.VK_S    )) {player2_x_move= 0; player2_y_move= 1;}

    player1_x_pos = player1_x_pos + player1_x_move;
    player1_y_pos = player1_y_pos + player1_y_move;
    
    player2_x_pos = player2_x_pos + player2_x_move;
    player2_y_pos = player2_y_pos + player2_y_move;
    
    if (!Color.BLACK.equals(getPixel(player1_x_pos,player1_y_pos))) {
      msgBox("Player1 Crashed");
      player1_deaths = player1_deaths + 1;
      reset();
    }
    else {putPixel(player1_x_pos,player1_y_pos,Color.YELLOW);}
    
    if (!Color.BLACK.equals(getPixel(player2_x_pos,player2_y_pos))) {
      msgBox("Player2 Crashed");
      player2_deaths = player2_deaths + 1;
      reset();
    }
    else {putPixel(player2_x_pos,player2_y_pos,Color.RED);}
    
    if (player1_deaths+player2_deaths>=5) {
      msgBox("Game Over Player1Deaths:"+player1_deaths+" Player2Deaths:"+player2_deaths);
      exitFinal();
    }
    
    repaintScreen();
  }
  
  public void reset() {
    player1_x_pos = 50;
    player1_y_pos = 50;
    player2_x_pos = getWidth()-50;
    player2_y_pos = getHeight()-50;
    player1_x_move = 1;
    player1_y_move = 0;
    player2_x_move =-1;
    player2_y_move = 0;
    clearScreen();
  }
      
  public static void main(String[] args) {new Tron();}
  
}
