import GameLib.GameFrame;
import java.awt.Color;
import java.awt.Point;


public class NetPaint extends GameFrame {
  
  private Color draw_color = Color.YELLOW;
  
  public NetPaint() {
    networkConnect("127.0.0.1");
  }
  
  public void mouseDragged(int x, int y) {
    networkSend(draw_color);
    networkSend(new Point(x,y));
  }
  
  public void networkRecieve(Object o) {
    if (o instanceof Color) {
      draw_color = (Color)o;
    }
    if (o instanceof Point) {
      Point p = (Point)o;
      putPixel(p.x,p.y,draw_color);
      repaintScreen();
    }
  }
  
  public void mouseWheelUp()   {draw_color = Color.YELLOW;}
  public void mouseWheelDown() {draw_color = Color.GREEN; }
  
  public static void main(String[] args) {new NetPaint();}  
}