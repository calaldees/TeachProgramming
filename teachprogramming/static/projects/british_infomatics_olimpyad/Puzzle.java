package britishinfomaticsolymiad;

public class Puzzle {

  public static void solvePuzzle(String... grid) {
    new Puzzle(puzzleFactory(grid));
  }

  static PuzzleBlock[][] puzzleFactoryMultiline(String grid_string) {
    return puzzleFactory(grid_string.split("\n"));
  }

  static PuzzleBlock[][] puzzleFactory(String...  grid_strings) {
    PuzzleBlock[][] grid_builder = new PuzzleBlock[grid_strings.length][];
    for (int y=0 ; y<grid_strings.length ; y++) {
      String grid_line = grid_strings[y];
      grid_builder[y] = new PuzzleBlock[grid_line.length()];
      for (int x=0 ; x<grid_line.length() ; x++) {
        grid_builder[y][x] = PuzzleBlock.blockFactory(grid_line.charAt(x));
      }
    }
    return grid_builder;
  }



  private final PuzzleBlock[][] grid_start;
  private final int[]     grid_next_drop_index;

  private final int grid_width;
  private final int grid_height;

  private PuzzleBlock[][] grid;


  public Puzzle(PuzzleBlock[][] grid_start) {
    this.grid_start = grid_start;

    grid_width  = grid_start[0].length;
    grid_height = grid_start.length;
    
    grid_next_drop_index = new int[grid_width];
    grid = new PuzzleBlock[grid_height][grid_width];

    System.out.println("TotalScore:"+solve());
  }

  private void refilGrid() {
    for (int x=0 ; x<grid_width ; x++) {
      for (int y=grid_height-1 ; y>=0 ; y--) {
        PuzzleBlock block = getBlock(x,y);
        if (block==null) {
          setBlock(x,y,getNextBlock(x));
        }
      }
    }
  }

  private PuzzleBlock getNextBlock(int col_num) {
    int drop_index = grid_next_drop_index[col_num]++;
    //System.out.println("Drop Index="+drop_index);
    return grid_start[(grid_height-1)-(drop_index%grid_height)][col_num]; //
  }

  
  private void dropGrid() {
    for (int x=0 ; x<grid_width ; x++) {
      boolean swap_took_place;
      do {
        swap_took_place = false;
        for (int y=0 ; y<grid_height ; y++) {
          PuzzleBlock block = getBlock(x,y);
          if (block==null) {
            block = takeBlock(x,y-1);
            if (block!=null) {swap_took_place = true;}
            setBlock(x,y,block);
          }
        }
      } while (swap_took_place);
    }
  }

  private int removeBlocks() {
    int total_product = 1;
    for (int x=0 ; x<grid_width ; x++) {
      for (int y=0 ; y<grid_height ; y++) {
        PuzzleBlock block_to_match = getBlock(x,y);
        int block_score = removeBlocks(x,y,block_to_match);
        if (block_score==1) {setBlock(x,y,block_to_match);} //a count of 1 is expected for all blocks, in this case remove blocks removes it, put it back
        if (block_score> 1) {
//System.out.println("TOTAL:"+total_product+" this block:"+block_score);
          total_product = total_product * block_score;
        }
      }
    }
    return total_product;
  }

  private int removeBlocks(int x, int y, PuzzleBlock block_to_match) {
    int block_count = 0;
    PuzzleBlock block_at_current_location = getBlock(x,y);
//System.out.println("check x="+x+" y="+y+ " searching_for="+b+ " found="+search);
    if (block_at_current_location!=null && block_at_current_location==block_to_match) {
      setBlock(x,y,null);
      block_count++;
      block_count += removeBlocks(x+1,y  ,block_to_match);
      block_count += removeBlocks(x-1,y  ,block_to_match);
      block_count += removeBlocks(x  ,y+1,block_to_match);
      block_count += removeBlocks(x  ,y-1,block_to_match);
//System.out.println("COUNT="+block_count);
    }
    return block_count;

  }


  private PuzzleBlock takeBlock(int x, int y) {
    PuzzleBlock block = getBlock(x,y);
    setBlock(x,y,null);
    return block;
  }

  private PuzzleBlock getBlock(int x, int y) {
    try                 {return grid[y][x];}
    catch (Exception e) {return null;}
  }

  private void setBlock(int x, int y, PuzzleBlock b) {
    try                 {grid[y][x] = b;}
    catch (Exception e) {}
  }

  private int solve() {
    int round_limit = 5;
    //System.out.println("Starting Grid");
    //System.out.println(gridToString(grid_start));
    int round_number = 1;
    int score_total  = 0;
    int score_round;
    refilGrid();
    do {
      //System.out.println("Round "+round_number);
      //System.out.println(toString());
      score_round = removeBlocks();
      System.out.println("End of Round "+round_number+" RoundScore="+score_round);
      score_total += score_round;
      System.out.println("Total so far "+score_total);
      //System.out.println(toString());
      //System.out.println("Dropping Grid");
      dropGrid();
      //System.out.println(toString());
      refilGrid();
      //System.out.println("Refil");
      //System.out.println(toString());

      
      round_number++;
    } while (score_round>1 && round_number<round_limit);
    return score_total;
  }

  public String toString() {return gridToString(grid);}

  private String gridToString(PuzzleBlock[][] grid) {
    StringBuilder grid_string = new StringBuilder();
    for (int y=0 ; y<grid.length ; y++) {
      for (int x=0 ; x<grid[y].length ; x++) {
        PuzzleBlock p = grid[y][x];
        String c = " ";
        if (p != null) {c = p.toString();}
        grid_string.append(c);
      }
      grid_string.append("\n");
    }
    return grid_string.toString();
  }

  public static void main(String[] args) {
    solvePuzzle("RRGB",
                "GRBG",
                "RRGB",
                "GBRB");
  }
}

enum PuzzleBlock {
  RED('R'),
  GREEN('G'),
  BLUE('B');

  public static PuzzleBlock blockFactory(Character c) {
    if (c=='R') {return RED;}
    if (c=='B') {return BLUE;}
    if (c=='G') {return GREEN;}
    return null;
  }

  char display_char;

  PuzzleBlock(Character c) {
    display_char = c;
  }

  public String toString() {
    return ""+display_char;
  }

}