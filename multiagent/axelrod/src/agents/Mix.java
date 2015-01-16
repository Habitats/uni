package agents;

import java.util.List;

/**
 * Created by Patrick on 16.01.2015.
 *
 * This agent will return a mixture of two selected agents with a given probability
 */
public class Mix implements ExtendedAgent {

  // the mix
  private Agent coop = new Coop();
  private Agent titForTat = new TitForTat();

  @Override
  public Action dilemma(List<Action> opponentPreviousActions) {
    return Math.random() > .5 ? coop.dilemma(opponentPreviousActions) : titForTat.dilemma(opponentPreviousActions);
  }

  @Override
  public Action getInitialAction() {
    return Action.COOPERATE;
  }
}
