import GameLib.GameFrame;
import java.awt.Color;
import java.awt.event.KeyEvent;
import java.util.Random;

public class Stars extends GameFrame {
  
  private final int    number_of_layers = 4;
  private final double move_speed       = 0.1;
  
  private Star[] stars = new Star[40];
  private Random r     = new Random();
  
  private double image_x_pos = 60;
  private double image_y_pos = 45;
  private double image_x_speed = 0;
  private double image_y_speed = 0;
  
  private int text_scroll_x_pos = 100;
  private int text_scroll_y_pos = 100;
  
  public Stars() {
    super("Stars",160,120);
    for (int star_number=0 ; star_number<stars.length ; star_number++) {
      Star s = new Star();
      s.x = r.nextInt(getWidth());
      s.y = r.nextInt(getHeight());
      s.speed = r.nextInt(number_of_layers) + 1;
      stars[star_number] = s;
    }
  }
  
  public void timerEvent() {
    clearScreen();
    
    if (isKeyPressed(KeyEvent.VK_LEFT )) {image_x_speed+=-move_speed;}
    if (isKeyPressed(KeyEvent.VK_RIGHT)) {image_x_speed+= move_speed;}
    if (isKeyPressed(KeyEvent.VK_UP   )) {image_y_speed+=-move_speed;}
    if (isKeyPressed(KeyEvent.VK_DOWN )) {image_y_speed+= move_speed;}
    
    if (text_scroll_x_pos<-100) {
      text_scroll_x_pos = 200;
      text_scroll_y_pos = r.nextInt(getHeight());
    }
    text_scroll_x_pos+=-1;
    drawString(text_scroll_x_pos,text_scroll_y_pos,"A-Level Computing");
    
    for (Star s : stars) {
      putPixel(s.x,s.y,Color.WHITE);
      s.x = s.x - s.speed;
      if (s.x<0) {
        s.x=getWidth();
        s.y = r.nextInt(getHeight());
      }
    }
    
    image_x_speed += ((getWidth() /4) - image_x_pos)/3000;
    image_y_speed += ((getHeight()/2) - image_y_pos)/2000;
    
    image_x_pos += image_x_speed;
    image_y_pos += image_y_speed;
    
    putImage((int)image_x_pos,(int)image_y_pos,"ship.gif");
    repaintScreen();
  }
  
  public void mouseDragged(int x, int y) {
    image_x_pos = x;
    image_y_pos = y;
  }
  
  public static void main(String[] args) {new Stars();}
}

class Star {
  public int x;
  public int y;
  public int speed;
}