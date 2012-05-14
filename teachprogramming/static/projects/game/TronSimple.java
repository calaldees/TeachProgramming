import GameLib.GameFrame;
import java.awt.Color;
import java.awt.event.KeyEvent;

public class TronSimple extends GameFrame {

  int player1_x_pos = 50;
  int player1_y_pos = 50;
  int player1_x_move = 1;
  int player1_y_move = 0;

  public void timerEvent() {
    if (isKeyPressed(KeyEvent.VK_LEFT )) {player1_x_move=-1; player1_y_move= 0;}
    if (isKeyPressed(KeyEvent.VK_RIGHT)) {player1_x_move= 1; player1_y_move= 0;}
    if (isKeyPressed(KeyEvent.VK_UP   )) {player1_x_move= 0; player1_y_move=-1;}
    if (isKeyPressed(KeyEvent.VK_DOWN )) {player1_x_move= 0; player1_y_move= 1;}
    
    player1_x_pos = player1_x_pos + player1_x_move;
    player1_y_pos = player1_y_pos + player1_y_move;
    putPixel(player1_x_pos,player1_y_pos,Color.YELLOW);
    repaintScreen();
  }

  public static void main(String[] args) {new TronSimple();}

}