package britishinfomaticsolymiad;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;


public class Anagram {

  Scanner console = new Scanner(System.in);

  List<Character> num_list = new ArrayList<Character>();

  public Anagram() {
    boolean found_anagram = false;
    System.out.println("Enter an anagram number");
    String input = console.nextLine();
    Integer num = Integer.decode(input);
    if (num <0 && num>123456789) {
      System.out.println("Not valid number");
    }
    else {
      // Convert String to num list
      for (int i = 0; i < input.length(); i++) {
        num_list.add(input.charAt(i));
      }
      for (int a = 2 ; a <= 9 ; a++) {
        String new_num_string = "" + (num * a);
        List<Character> copy_of_num_list = new ArrayList<Character>(num_list);
        for (int i = 0; i < new_num_string.length(); i++) {
          Character char_to_seek = new_num_string.charAt(i);
          if (!copy_of_num_list.remove(char_to_seek)) {break;}
        }
        if (copy_of_num_list.size() == 0) {
          System.out.print(""+a+" ");
          found_anagram = true;
        }
      }
      if (found_anagram==false) {
        System.out.println("NO");
      }

    }
  }

  public static void main(String[] args) {new Anagram();}

}
