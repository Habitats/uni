package ov_1;

/**
 * Created by anon on 22.01.2015.
 */
public class UpDownCounter {


  // konstante felter, derfor final, disse feltene skal aldri endre verdi
  private final int end;
  private final int start;

  // er felt som holder styr på hvor counteren er akkurat nå, dette kan endres
  private int count;

  // konstruktøren. denne initiseres med verdiene start og end
  public UpDownCounter(int start, int end) {
    // om start == end, skal man krasje programmet med en IllegalArgumentException
    if (start == end) {
      throw new IllegalArgumentException();
    }

    // sett DETTE objektet (altså, counteren) sine start og end-verdier, og sett nåværende counter-posisjon til å være det samme som start (siden det er her den skal starte å telle)
    // this.x brukes for å hente ut DETTE objektet sine felter. this.start er IKKE det samme som start
    this.count = start;
    this.start = start;
    this.end = end;
  }

  // en metode for å returnere hvor counteren er akkurat nå
  public int getCounter() {
    return count;
  }

  // en boolean metode som returnerer true om telleren ikke har nådd maksimum (end)
  public boolean count() {
    // om start er mindre enn end, så har vi en teller som teller oppover, altså, man øker telleren med én
    if (start < end && count < end) {
      // dette er en snarvei for å skrive: count = count + 1
      count++;
    }
    // om start er større enn end, så har vi en teller som teller nedover, altså, man minker verdien med én
    else if (start > end && count > end) {
      // dette er en snarvei for å skrvie: count = count - 1
      count--;
    }

    // om count er ulik end, altså, om count ikke har kommet frem til end, så returnerer denne true. om telleren har kommet til end, returnerer den false
    // dette er det samme som å skrive:
    // if(count == end){
    //     return false;
    // else{
    //     return true;
    // }
    return count != end;
  }
}
