package ladder;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.LinkedList;

public class FibonacciAdder {

  private long ans;
  private int max;
  private long evenAns;
  private ArrayList<Integer> numArr = new ArrayList<Integer>();
  private LinkedList<Integer> evenArr = new LinkedList<Integer>();

  public static void main(String[] args) {
    FibonacciAdder fib = new FibonacciAdder();

    fib.getFibSeq();
  }

  public void getFibSeq() {

    numArr.add(0);
    numArr.add(1);
    double start = System.nanoTime();
    int ans = 0;

    while (ans < 4000000) {
      ans = numArr.get(numArr.size() - 2) + numArr.get(numArr.size() - 1);
      numArr.add(ans);
      // System.out.println(ans);
      if (ans % 2 == 0) {
        evenArr.add(ans);
      }
    }
    System.out.println(ans);
    System.out.println("Computation time: " + (System.nanoTime() - start) + " ns");
    evenAns = 0;

    for (long l : evenArr) {
      evenAns += l;
      System.out.println(l);
    }
    System.out.println(evenAns);
  }
}
