package agents;

import java.util.List;

/**
 * Created by Patrick on 16.01.2015.
 *
 * This agent will always cooperate
 */
public class Coop implements ExtendedAgent {

  @Override
  public Action dilemma(List<Action> opponentPreviousActions) {
    return Action.COOPERATE;
  }

  @Override
  public Action getInitialAction() {
    return Action.COOPERATE;
  }
}
