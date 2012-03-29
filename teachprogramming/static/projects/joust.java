import GameLib.GameFrame;
import java.awt.Color;
import java.awt.event.KeyEvent;

public class Joust extends GameFrame {
  
  private static final int    border_size    = 5;
  private static final double bounce_factor  = 1;
  private static final double drag_factor    = 0.01;
  private static       double gravity_factor = 0.01;
  private static final double fly_power      = 0.2;
  private static final double move_power     = 0.02;
  
  private static final String player1_image  = "JoustPlayer1.png";
  private static final String player2_image  = "JoustPlayer2.png";
  
  double player1_x;
  double player1_y;
  double player1_xspeed;
  double player1_yspeed;
  int    player1_score;
  
  double player2_x;
  double player2_y;
  double player2_xspeed;
  double player2_yspeed;
  int    player2_score;
  
  public Joust() {
    titleScreen();
  }

  public void timerEvent() {
    clearScreen();
    
    if (isKeyPressed(KeyEvent.VK_RIGHT)) {player2_xspeed+= move_power;}
    if (isKeyPressed(KeyEvent.VK_LEFT )) {player2_xspeed+=-move_power;}
    if (isKeyPressed(KeyEvent.VK_D    )) {player1_xspeed+= move_power;}
    if (isKeyPressed(KeyEvent.VK_A    )) {player1_xspeed+=-move_power;}
    
    player1_yspeed  = player1_yspeed + gravity_factor;
    player1_xspeed += player1_xspeed * -drag_factor;
    player1_yspeed += player1_yspeed * -drag_factor;
    if (player1_x<0+border_size || player1_x>getWidth() -getImageWidth (player1_image)-border_size) {player1_xspeed = -player1_xspeed * bounce_factor;}
    if (player1_y<0             || player1_y>getHeight()-getImageHeight(player1_image)            ) {player1_yspeed = -player1_yspeed * bounce_factor;}
    player1_x += player1_xspeed;
    player1_y += player1_yspeed;
    
    player2_yspeed  = player2_yspeed + gravity_factor;
    player2_xspeed += player2_xspeed * -drag_factor;
    player1_yspeed += player2_yspeed * -drag_factor;
    if (player2_x<0+border_size || player2_x>getWidth() -getImageWidth (player2_image)-border_size) {player2_xspeed = -player2_xspeed * bounce_factor;}
    if (player2_y<0             || player2_y>getHeight()-getImageHeight(player2_image)            ) {player2_yspeed = -player2_yspeed * bounce_factor;}
    player2_x += player2_xspeed;
    player2_y += player2_yspeed;

    putImage((int)player1_x,(int)player1_y,player1_image);
    putImage((int)player2_x,(int)player2_y,player2_image);
    
    repaintScreen();
    
    if (!Color.BLACK.equals(getPixel((int)player1_x+17,(int)player1_y+4)) ||
        !Color.BLACK.equals(getPixel((int)player2_x- 1,(int)player2_y+4))    ) {
      if (Math.abs(player1_y-player2_y)<1.5) {
        player1_xspeed = -player1_xspeed;
        player2_xspeed = -player2_xspeed;
      }
      else if (player1_y<player2_y) {
        player1_score++;
        msgBox("Player 1 Wins");
        titleScreen();
      }
      else if (player2_y<player1_y) {
        player2_score++;
        msgBox("Player 2 Wins");
        titleScreen();
      }
    }
  }
  
  public void keyReleased(int keycode) {
    if (keycode == KeyEvent.VK_UP) {player2_yspeed = player2_yspeed - fly_power;}
    if (keycode == KeyEvent.VK_W ) {player1_yspeed = player1_yspeed - fly_power;} 
  }
  
  public void keyPressed(int keycode) {
    if (keycode==KeyEvent.VK_F1    ) {startGame();}
    if (keycode==KeyEvent.VK_EQUALS) {gravity_factor += 0.002; titleScreen();}
    if (keycode==KeyEvent.VK_MINUS ) {gravity_factor +=-0.002; titleScreen();}
  }
  
  public void titleScreen() {
    timerPause(true);
    //clearScreen();
    putImage(0,0,"JoustTitle.png");
    drawString(100,100,"Player 1: "+player1_score);
    drawString(100,120,"Player 2: "+player2_score);
    drawString(100,140,"Gravity: " +gravity_factor);
    //play music
    repaintScreen();
  }
  
  public void startGame() {
    player1_x = border_size + 1;
    player1_y = getHeight() - getImageHeight(player1_image);
    player1_xspeed = 0;
    player1_yspeed = 0;
    
    player2_x = getWidth()  - getImageWidth (player2_image) - border_size - 1;
    player2_y = getHeight() - getImageHeight(player2_image);
    player2_xspeed = 0;
    player2_yspeed = 0;
    
    timerPause(false);
  }
  
  public static void main(String[] args) {new Joust();}
}