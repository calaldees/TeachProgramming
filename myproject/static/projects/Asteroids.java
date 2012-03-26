import GameLib.GameFrame;
import java.awt.Color;
import java.awt.Point;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Asteroids extends GameFrame {

  private static final int    max_targets =  5;    //number of starting targets

  private final List<Asteroid> asteroids = new ArrayList<Asteroid>(); //list of targets in play
  private final Ship           ship      = new Ship();
  private final Point          mouse     = new Point();
  
  public static void main(String[] args) {new Asteroids();}
  
  public Asteroids() {
    ship.image_name = "ship.gif";
    AsteroidObject.frame = this;
    reset();
  }
  
  public void timerEvent() {
    clearScreen();
    ship.move();
    ship.draw();
    updatePosition();
    for (Asteroid a : asteroids) {
      a.move();
      a.draw();
    }
    repaintScreen();
  }
  
  public void reset() {
    ship.x = getWidth() /2;
    ship.y = getHeight()/2;
    
    asteroids.clear();  //clear all targets
    for (int count = 0; count<max_targets; count++) {  //count max_target times
      asteroids.add(new Asteroid()); //add new target to list of targets
    }
    resetElapsedTime(); //reset time passed (for score)
  }
  
  public void mouseMoved(int x, int y) {
    mouse.x = x;
    mouse.y = y;

  }
  
  private void updatePosition() {
    ship.direction = Math.atan((ship.y-mouse.y)/(ship.x-mouse.x));
    if (mouse.x<=ship.x) {ship.direction+=Math.PI;}    
  }
  
  public void keyUp()    {ship.thrust();}

  
}

class AsteroidObject {
  public static GameFrame frame;
 
  public double x;
  public double y;
  public double x_vel;
  public double y_vel;
  public double direction;
  public String image_name;
  public int size;
  
  public void move() {
    x += x_vel; //move the target in it's direction
    y += y_vel;
    if (x<0 || (x+size)>frame.getWidth() ) {x_vel=-x_vel;}  //bounce on the edges of the screen
    if (y<0 || (y+size)>frame.getHeight()) {y_vel=-y_vel;}
  }
}

class Ship extends AsteroidObject {
  private double force_thrust = 0.02;
  private double force_slide  = 0.01;
  private double force_back   = 0.01;
  
  public void thrust() {
    x_vel += Math.sin(direction) * force_thrust;
    y_vel += Math.cos(direction) * force_thrust;
  }
  public void move() {
    super.move();
    x += x_vel;
    y += y_vel;
  }
  public void draw() {
    frame.putImage((int)x,(int)y,image_name,direction);
  }
}

class Asteroid extends AsteroidObject {
  private static final int    max_size    = 20;    //starting size of targets
  private static final double max_speed   =  1.5;  //max speed target can move
  private static final int    max_split   =  3;    //when shot, break into peices
  
  private static final Random r           = new Random(); //used for generating random numbers

  

  public double rotation_vel;
  

  public Asteroid() {
    randomize();
  }
  
  public void randomize() {
    size  = max_size;       //set target starting size
    x = r.nextInt(frame.getWidth()-size);  //random start position
    y = r.nextInt(frame.getHeight()-size);
    x_vel = (r.nextDouble()*max_speed*2)-max_speed; //ramdom speed
    y_vel = (r.nextDouble()*max_speed*2)-max_speed;
  }
  
  public void draw() {
    frame.drawRectangle((int)x, (int)y, size, size, Color.YELLOW);
  }
}