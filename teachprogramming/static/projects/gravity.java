import GameLib.GameFrame;
import java.awt.Color;
import java.awt.Rectangle;
import java.util.Random;

public class Gravity extends GameFrame {

  private static final int max_size = 30;
  
  private Rectangle player = new Rectangle(100,100,10,10);
  private Mass[]    blocks = new Mass[50];

  public Gravity() {
    super("Gravity",640,480);
    reset();
  }

  public void timerEvent() {
    clearScreen();

    for (Mass m : blocks) {
      if (m.x_pos<0 || m.x_pos>getWidth())  {m.x_vel=-(m.x_vel/3);}
      if (m.y_pos<0 || m.y_pos>getHeight()) {m.y_vel=-(m.y_vel/3);}
      m.x_vel += -(m.x_pos-player.x)/m.size/500;
      m.y_vel += -(m.y_pos-player.y)/m.size/500;
      m.x_pos+=m.x_vel;
      m.y_pos+=m.y_vel;
      drawRectangle((int)m.x_pos, (int)m.y_pos, m.size, m.size, Color.YELLOW);
    }

    if (!Color.BLACK.equals(getPixel(player.x,player.y))) {msgBox("Score: "+getElapsedTime()); reset();}
    
    drawRectangle(player, Color.WHITE);
    repaintScreen();
  }
  
  public void reset() {
    Random r = new Random();
    for (int count = 0; count<blocks.length; count++) {
      Mass mass = new Mass();
      mass.x_pos = r.nextFloat()*getWidth();
      mass.y_pos = r.nextFloat()*getHeight();
      mass.size  = r.nextInt(max_size)+5;
      blocks[count] = mass;
    }
    resetElapsedTime();
  }
  
  public void mouseMoved(int x, int y) {
    player.x = x;
    player.y = y;
  }
  
  public static void main(String[] args) {new Gravity();}
  
}

class Mass {
  public float x_pos;
  public float y_pos;
  public float x_vel = 0;
  public float y_vel = 0;
  public int   size;
}