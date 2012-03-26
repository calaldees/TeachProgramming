import GameLib.GameFrame;
import java.awt.Color;
import java.awt.event.KeyEvent;

public class Race extends GameFrame {

  private static final double move_power = 0.01;
  
  double player1_x;
  double player1_y;
  double player1_xspeed;
  double player1_yspeed;
  
  public Race() {
    reset();
  }
  
  public void timerEvent() {
    if (isKeyPressed(KeyEvent.VK_LEFT )) {player1_xspeed+=-move_power;}
    if (isKeyPressed(KeyEvent.VK_RIGHT)) {player1_xspeed+= move_power;}
    if (isKeyPressed(KeyEvent.VK_UP   )) {player1_yspeed+=-move_power;}
    if (isKeyPressed(KeyEvent.VK_DOWN )) {player1_yspeed+= move_power;}    
    putImage(0,0,"Track1.png");

    player1_x = player1_x + player1_xspeed;
    player1_y = player1_y + player1_yspeed;
    if (Color.BLACK.equals(getPixel((int)player1_x+8,(int)player1_y+8))) {
    }
    else {
      if (player1_xspeed>0.05) {player1_xspeed=0.05;}
      if (player1_yspeed>0.05) {player1_yspeed=0.05;}
      if (player1_xspeed<-0.05) {player1_xspeed=-0.05;}
      if (player1_yspeed<-0.05) {player1_yspeed=-0.05;}
    }
    putImage((int)player1_x,(int)player1_y,"Race1.png");
    repaintScreen();
  }
  
  public void reset() {
    player1_x = 100;
    player1_y = 100;
    player1_xspeed = 0;
    player1_yspeed = 0;
  }
  
  public static void main(String[] args) {new Race();}
}
