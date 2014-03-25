package ladder;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;

public class Ladder {
  public static void main(String[] args) {
    new Ladder().run();
  }

  // Et oppned-tall er et tall som leses likt når det blir rotert 180°. Eksempler på dette er 181,
  // 916 og 8008.
  //
  // Hvor mange oppned-tall mindre enn 100 000 finnes det?

  private class Child {

  }

  private void run() {
    regular();
    // isPalindrome("heieh");
  }

  private void regular() {
    HashSet<Integer> yo = new HashSet<Integer>();
    int count = 0;
    for (int i = 0; i < 100000; i++) {
      if (isUpsideDown(i)) {
        count++;
        yo.add(i);
        System.out.println(i);
      }
    }
    System.out.println(count);
    System.out.println(yo.size());
  }

  private boolean isUpsideDown(int i) {
    String num = Integer.toString(i);
    if (num.contains("2") || num.contains("3") || num.contains("4") || num.contains("5")
        || num.contains("7")) {
      return false;
    }
    if (num.contains("9") || num.contains("6")) {
      num = swap(num);
      if (isPalindrome(num)) {
        // System.out.println(num);
        return true;
      }
    } else if (num.contains("0") || num.contains("8") || num.contains("1")) {
      if (isPalindrome(num)) {
        System.out.println(num);
        return true;
      }
    }
    return false;
  }

  private String swap(String num) {
    StringBuilder newNum = new StringBuilder();
    int max = num.length() / 2;
    int count = 0;
    for (char s : num.toCharArray()) {
      if (count < max) {
        if (s == '9') {
          newNum.append('6');
        } else if (s == '6') {
          newNum.append('9');
        } else {
          newNum.append(s);
        }
      } else {
        newNum.append(s);
      }
      count++;
    }
    // for (int i = 0; i < num.length() / 2; i++) {
    // String ni = Character.toString(num.charAt(i));
    // newNum.append(b)
    // }
    return newNum.toString();
  }

  private boolean isPalindrome(String num) {
    if (num.length() % 2 != 0) {
      num = num.substring(0, (num.length() / 2)) + num.substring((num.length() / 2) + 1);
    }
    String left = num.substring(0, num.length() / 2);
    String right = num.substring(num.length() / 2);
    right = new StringBuilder(right).reverse().toString();

    if (left.equals(right)) {
      // System.out.println(num + " " + left.equals(right));
    }
    return (left.equals(right));
  }
}
