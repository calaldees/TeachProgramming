
import GameLib.GameFrame;

public class GameTest extends GameFrame {
    
  public void mousePressed(int x, int y) {
    putImage(x,y,"ship.gif");
    repaintScreen();
  }
  
  public static void main(String[] args) {new GameTest();}
  
}
