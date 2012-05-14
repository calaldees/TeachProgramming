import GameLib.GameFrame;
import java.awt.Color;
import java.util.ArrayList;
import java.util.Random;

public class Shoot extends GameFrame {
  
  private static final int    max_size    = 20;    //starting size of targets
  private static final double max_speed   =  1.5;  //max speed target can move
  private static final int    max_targets =  5;    //number of starting targets
  private static final int    max_split   =  3;    //when shot, break into peices
  
  private final Random            r       = new Random(); //used for generating random numbers
  private final ArrayList<Target> targets = new ArrayList<Target>(); //list of targets in play
  
  private int shoot_x;  //co-ordinate where the mouse was clicked
  private int shoot_y;
  private int shoot_effect_x;  //rember position of mouse shoot to draw shoot effect
  private int shoot_effect_y;
  private int shoot_effect_radius;
  
  public Shoot() {
    super("Shoot",320,240);
    reset();
  }
  
  public void reset() { //called to reset and ramdomise all targets
    targets.clear();  //clear all targets
    for (int count = 0; count<max_targets; count++) {  //count max_target times
      Target t = new Target();  //create new target
      t.size  = max_size;       //set target starting size
      t.x_pos = r.nextInt(getWidth()-t.size);  //random start position
      t.y_pos = r.nextInt(getHeight()-t.size);
      t.x_direction = (r.nextDouble()*max_speed*2)-max_speed; //ramdom speed
      t.y_direction = (r.nextDouble()*max_speed*2)-max_speed;
      targets.add(t); //add new target to list of targets
    }
    resetElapsedTime(); //reset time passed (for score)
  }
  
  
  public void timerEvent() {
    clearScreen();

    //Check if game is over
    if (targets.size()==0) {
      msgBox("Well Done! Time Taken:"+getElapsedTime());
      reset();
    }
    
    //Setup shooting effect if mouse has been clicked
    if (shoot_x>0 && shoot_y>0) {
      shoot_effect_x = shoot_x;
      shoot_effect_y = shoot_y;
      shoot_effect_radius = 40;
    }
    //Draw shooting effect and shrink the effect radius
    if (shoot_effect_radius>0) {
      drawCircleFilled(shoot_effect_x-(shoot_effect_radius/2),shoot_effect_y-(shoot_effect_radius/2),shoot_effect_radius,Color.RED);
      shoot_effect_radius--;
    }

    for (Target t : targets) {
      //check if target has been shot
      if (shoot_x>=t.x_pos && shoot_x<=t.x_pos+t.size && shoot_y>=t.y_pos && shoot_y<=t.y_pos+t.size) {    
        targets.remove(t); //remove the shot target
        if (t.size>15) {   //if target is big enough
          for (int count=0 ; count<max_split ; count++) { //count number of times to split
            targets.add(getRandomSmallerTarget(t));       //create new smaller targets
          }
        }
        clearShootPosition(); //this stops a shot penetrating overlapping targets, only shoot the first one
      }
      else {
        t.x_pos += t.x_direction; //move the target in it's direction
        t.y_pos += t.y_direction;
        if (t.x_pos<0 || t.x_pos+t.size>getWidth() ) {t.x_direction=-t.x_direction;}  //bounce on the edges of the screen
        if (t.y_pos<0 || t.y_pos+t.size>getHeight()) {t.y_direction=-t.y_direction;}
        drawRectangle((int)t.x_pos, (int)t.y_pos, t.size, t.size, Color.YELLOW);
      }
    }
    clearShootPosition();
    repaintScreen();
  }
  
  public void mousePressed(int x, int y) {
    shoot_x = x;
    shoot_y = y;
  }
  private void   clearShootPosition() {shoot_x = -1; shoot_y = -1;}
  
  //create new smaller targets based on the one thats been shot
  private Target getRandomSmallerTarget(Target target_old) {
    Target target_new = new Target();
    target_new.x_pos = target_old.x_pos;
    target_new.y_pos = target_old.y_pos;
    target_new.x_direction = randomDirection();
    target_new.y_direction = randomDirection(); //random direction
    target_new.size = target_old.size/2;  //this new target has half the size of parent
    return target_new;
  }
  
  private double randomDirection() {return (r.nextFloat()*max_speed*2)-max_speed;}

  
  public static void main(String[] args) {new Shoot();}
}

class Target {
  public int    size;
  public double x_pos;
  public double y_pos;
  public double x_direction;
  public double y_direction;
}