package britishinfomaticsolymiad;

import java.util.ArrayList;
import java.util.List;

public class DigitWord {
  private static final List<String> lookup = new ArrayList<String>();

  private static void init() {
    lookup.add("ZERO");
    lookup.add("ONE");
    lookup.add("TWO");
    lookup.add("THREE");
    lookup.add("FOUR");
    lookup.add("FIVE");
    lookup.add("SIX");
    lookup.add("SEVEN");
    lookup.add("EIGHT");
    lookup.add("NINE");
  }

  public static String findDidget(String word) {
    System.out.println("Finding: "+word);
    //System.out.println("Size: "+lookup.size());
    for (int digit_number_index=0 ; digit_number_index<lookup.size() ; digit_number_index++) {
      String digit_string = lookup.get(digit_number_index);
      //System.out.println("Finding word: "+digit_string);
      int lookup_pointer = 0;
      for (int i=0 ; i<word.length() ; i++) {
        //System.out.println("Comparing "+word.charAt(i) +" with "+digit_string.charAt(lookup_pointer));
        if (word.charAt(i)==digit_string.charAt(lookup_pointer)) {
          lookup_pointer++;
          //System.out.println("Next!");
          if (lookup_pointer>=digit_string.length()) {
            return ""+digit_number_index;
          }
        }
      }
    }
    return "NO";
  }

  public static void main(String[] args) {
    init();
    System.out.println(DigitWord.findDidget("BOUNCE"));
    System.out.println(DigitWord.findDidget("ENCODE"));
    System.out.println(DigitWord.findDidget("EIGHT"));
    System.out.println(DigitWord.findDidget("BLACKJACK"));
    System.out.println(DigitWord.findDidget("FABULIOUS"));
    System.out.println(DigitWord.findDidget("EXERCISE"));
    System.out.println(DigitWord.findDidget("DRIFTWOOD"));
    System.out.println(DigitWord.findDidget("SERVICEMAN"));
    System.out.println(DigitWord.findDidget("INSIGNIFICANCE"));
    System.out.println(DigitWord.findDidget("THROWDOWN"));
  }

}
