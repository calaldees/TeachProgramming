import GameLib.GameFrame;
import java.awt.Color;
import java.awt.Rectangle;

public class Pong extends GameFrame {
  
  private Rectangle player1_bat = new Rectangle(20,100,10,40);
  private Rectangle ball        = new Rectangle(100,100,5,5);
  private int ball_x_speed = 2;
  private int ball_y_speed = 2;

  public void timerEvent() {
    clearScreen();
    if (ball.y<0 || ball.y>getHeight()) {ball_y_speed=-ball_y_speed;}
    if (ball.x>getWidth())              {ball_x_speed=-ball_x_speed;}
    if (player1_bat.contains(ball.x,ball.y)) {ball_x_speed=-ball_x_speed;}
    if (ball.x<0) {
      msgBox("Missed");
      ball.x = 200;
      //ball.y = 200;
    }
    ball.x = ball.x + ball_x_speed;
    ball.y = ball.y + ball_y_speed;
    drawRectangle(ball,       Color.WHITE);
    drawRectangle(player1_bat,Color.WHITE);
    repaintScreen();
  }
  
  public void mouseMoved(int x, int y) {
    player1_bat.x=x;
    player1_bat.y=y;
  }
  
  public static void main(String[] args) {new Pong();}  
  
}
