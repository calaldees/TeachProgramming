import GameLib.GameFrame;
import java.awt.Color;
import java.awt.Point;

public class TronNet extends GameFrame {

  private Point player_point = new Point();
  int player_x_move = 1;
  int player_y_move = 0;
  
  public TronNet() {
    String server = inputBox("Server IP Address");
    if (server==null) {server = "localhost";}
    networkConnect(server);
    reset();
  }
  
  public void timerEvent() {
    player_point.x = player_point.x + player_x_move;
    player_point.y = player_point.y + player_y_move;
    networkSend(new Point(player_point));
    repaintScreen();
  }
  
  public void networkRecieve(Object o) {
    if (o instanceof Point) {
      Point p = (Point)o;
      if (!Color.BLACK.equals(getPixel(p.x,p.y))) {networkSend("crash");}
      if (p.equals(player_point)) {putPixel(p.x,p.y,Color.YELLOW);}
      else                        {putPixel(p.x,p.y,Color.WHITE); }
    }
    if (o instanceof String) {
      String message = (String)o;
      if (message.equals("crash")) {reset();}
      else                         {msgBox(message);}
    }
  }
  
  public void reset() {
    player_point.setLocation( (int)(Math.random()*getWidth()) , (int)(Math.random()*getHeight()) );
    clearScreen();
  }
  
  public void keyUp()    {player_x_move= 0; player_y_move=-1;}
  public void keyDown()  {player_x_move= 0; player_y_move= 1;}  
  public void keyLeft()  {player_x_move=-1; player_y_move= 0;}
  public void keyRight() {player_x_move= 1; player_y_move= 0;}
  
  public static void main(String[] args) {new TronNet();}
}