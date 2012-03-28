
import GameLib.GameFrame;

public class SpaceshipTest extends GameFrame {

  private final double move_speed  = 0.10;
  private final double drag_factor = 0.001;

  private double ship_x_pos = 60;
  private double ship_y_pos = 45;
  private double ship_x_speed = 0;
  private double ship_y_speed = 0;
  
  private double ship_rotation = 0;

  public void timerEvent() {
    clearScreen();

    ship_x_speed += ship_x_speed * -drag_factor;
    ship_y_speed += ship_y_speed * -drag_factor;
    
    ship_y_speed = ship_y_speed + 0.01;
    
    if (ship_y_pos > getHeight()) {ship_y_speed = -ship_y_speed;}
    
    ship_x_pos += ship_x_speed;
    ship_y_pos += ship_y_speed;
    
    putImage((int)ship_x_pos,(int)ship_y_pos,"ship.gif",ship_rotation);
    repaintScreen();
  }

  public void keyUp()    {ship_y_speed+=-move_speed;}
  public void keyDown()  {ship_y_speed+=+move_speed;}  
  public void keyLeft()  {ship_x_speed+=-move_speed;}
  public void keyRight() {ship_x_speed+=+move_speed;}
  public void keySpace() {ship_rotation += 0.01;}
  
  public static void main(String[] args) {new SpaceshipTest();}

}