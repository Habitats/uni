import ov_1.UpDownCounter;

/**
 * Created by anon on 22.01.2015.
 */
public class Oo {

  // main metoden er det første som kjører når programmet starter.
  public static void main(String[] args) {

    // lag et nytt UpDownCounter-objekt, og putt den i en variabel "counter"
    // counter-objektet initisieres med verdiene start = 1, og end = 4
    UpDownCounter counter = new UpDownCounter(1, 4);

    // kall count() på counter-objektet for å øke tellingen med én
    counter.count();
    counter.count();

    // print ut hvilken verdi counter-objektet har akkurat nå
    System.out.println(counter.getCounter());
  }
}
