package agents;

import java.util.List;

/**
 * Created by Patrick on 16.01.2015.
 *
 * This agent will return a mixture of two selected agents with a given probability
 */
public class Mix implements Agent {

  // the mix
  private Agent defect = new Defect();
  private Agent titForTat = new TitForTat();

  @Override
  public Action dilemma(List<Action> opponentPreviousActions) {
    return Math.random() > .5 ? defect.dilemma(opponentPreviousActions) : titForTat.dilemma(opponentPreviousActions);
  }
}
