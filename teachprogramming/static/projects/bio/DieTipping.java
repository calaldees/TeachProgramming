package britishinfomaticsolymiad;

import java.util.Scanner;

public class DieTipping {

  int[][] grid = new int[11][11];
  int dx = 5;
  int dy = 5;
  Die d = new Die();

  public DieTipping() {
    initGrid();

    Scanner console = new Scanner(System.in);
    System.out.println("enter 3x3 start grid");
    String line1 = console.nextLine();
    String line2 = console.nextLine();
    String line3 = console.nextLine();
    grid[4][4] = Integer.decode(""+line1.charAt(0));
    grid[4][5] = Integer.decode(""+line1.charAt(1));
    grid[4][6] = Integer.decode(""+line1.charAt(2));
    grid[5][4] = Integer.decode(""+line2.charAt(0));
    grid[5][5] = Integer.decode(""+line2.charAt(1));
    grid[5][6] = Integer.decode(""+line2.charAt(2));
    grid[6][4] = Integer.decode(""+line3.charAt(0));
    grid[6][5] = Integer.decode(""+line3.charAt(1));
    grid[6][6] = Integer.decode(""+line3.charAt(2));

    int n=0;
    do {
      System.out.println("Iterations? ");
      n = console.nextInt();
      for (int i=0 ; i<n ; i++) {
        calculateGrid();
        moveDice();
      }
      printGrid();
    } while (n>0 && n<=100);

    printWholeGrid();
  }

  private void moveDice() {
    int c = grid[dy][dx];
    if (c==1 || c==6) {d.move(d.last_direction);}
    if (c==2        ) {d.move(Die.nextDirectionClockwise    (d.last_direction));}
    if (c==3 || c==4) {d.move(Die.nextDirectionOpposite     (d.last_direction));}
    if (c==5        ) {d.move(Die.nextDirectionAntiClockwise(d.last_direction));}

    if (d.last_direction==0) {dy+=-1;}
    if (d.last_direction==1) {dx+= 1;}
    if (d.last_direction==2) {dy+= 1;}
    if (d.last_direction==3) {dx+=-1;}

    if (dx<0) {dx=0;}
    if (dy<0) {dy=0;}
    if (dy>grid.length-1    ) {dy=grid.length-1;}
    if (dx>grid[dy].length-1) {dx=grid[dy].length-1;}
  }

  private void calculateGrid() {
    int new_num = grid[dy][dx] + d.face;
    if (new_num>6) {new_num+=-6;}
    grid[dy][dx] = new_num;
  }

  private void printGrid() {
    System.out.println("");
    int min_y = dy-1;
    int min_x = dx-1;
    int max_y = dy+1;
    int max_x = dx+1;
    if (min_y<0) {min_y=0;}
    if (min_x<0) {min_x=0;}
    if (max_y>grid.length-1    ) {max_y=grid.length-1;}
    if (max_x>grid[dy].length-1) {max_x=grid[dy].length-1;}
    for (int y = min_y ; y <=max_y ; y++) {
      for (int x = min_x ; x <=max_x ; x++) {
        System.out.print(grid[y][x]);
      }
      System.out.println("");
    }
  }

  private void printWholeGrid() {
    System.out.println("");
    for (int y = 0 ; y <grid.length ; y++) {
      for (int x = 0 ; x <grid[y].length ; x++) {
        System.out.print(grid[y][x]);
      }
      System.out.println("");
    }
  }

  private void initGrid() {
    for (int y = 0 ; y <grid.length ; y++) {
      for (int x = 0 ; x <grid[y].length ; x++) {
        grid[y][x] = 1;
      }
    }
  }

  public static void main(String[] args) {new DieTipping();}
}

class Die {

  /* direction
   * 0 = north y- up
   * 1 = east  x+ right
   * 2 = south y+ down
   * 3 = west  x- left
   */

  public int face = 1;
  public int left = 3;
  public int right = 4;
  public int top = 2;
  public int bottom = 5;
  public int floor = 6;

  public int last_direction = 0;

  public Die() {

  }

  public static int nextDirectionOpposite     (int d) {return nextDirectionClockwise(nextDirectionClockwise(d));}
  public static int nextDirectionClockwise    (int d) {return (d+1) % 4;}
  public static int nextDirectionAntiClockwise(int d) {
    int new_d = d - 1;
    if (new_d < 0) {return 4;}
    return new_d;
  }

  public void move(int direction) {
    last_direction = direction;

    int new_face   = 0;
    int new_left   = 0;
    int new_right  = 0;
    int new_top    = 0;
    int new_bottom = 0;
    int new_floor  = 0;

    if (direction == 0) { //up
      new_face   = bottom;
      new_left   = left;
      new_right  = right;
      new_top    = face;
      new_bottom = floor;
      new_floor  = top;
    }
    if (direction == 1) { //right
      new_face   = left;
      new_left   = floor;
      new_right  = face;
      new_top    = top;
      new_bottom = bottom;
      new_floor  = right;
    }
    if (direction == 2) { //down
      new_face   = top;
      new_left   = left;
      new_right  = right;
      new_top    = floor;
      new_bottom = face;
      new_floor  = bottom;
    }
    if (direction == 3) { //left
      new_face   = right;
      new_left   = face;
      new_right  = floor;
      new_top    = top;
      new_bottom = bottom;
      new_floor  = left;
    }

    face = new_face;
    left = new_left;
    right = new_right;
    top = new_top;
    bottom = new_bottom;
    floor = new_floor;
  }
}