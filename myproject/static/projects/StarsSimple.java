import GameLib.GameFrame;
import java.awt.Color;
import java.util.Random;

public class StarsSimple extends GameFrame {
  
  private final int    number_of_layers = 4;
  
  private StarX[] stars = new StarX[40];
  private Random r     = new Random();
    
  public StarsSimple() {
    super("StarsSimple",160,120);
    for (int star_number=0 ; star_number<stars.length ; star_number++) {
      StarX s = new StarX();
      s.x = r.nextInt(getWidth());
      s.y = r.nextInt(getHeight());
      s.speed = r.nextInt(number_of_layers) + 1;
      stars[star_number] = s;
    }
  }
  
  public void timerEvent() {
    clearScreen();
    
    for (StarX s : stars) {
      putPixel(s.x,s.y,Color.WHITE);
      s.x = s.x - s.speed;
      if (s.x<0) {
        s.x=getWidth();
        s.y = r.nextInt(getHeight());
      }
    }

    putImage(20,40,"ship.gif");
    repaintScreen();
  }
  
  public static void main(String[] args) {new StarsSimple();}
}

class StarX {
  public int x;
  public int y;
  public int speed;
}