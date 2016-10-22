package agents;

import java.util.List;

/**
 * Created by Patrick on 16.01.2015.
 *
 * This agent will do whatever the opponent did last
 */
public class TitForTat implements Agent {

  @Override
  public Action dilemma(List<Action> opponentPreviousActions) {
    if (opponentPreviousActions.size() == 0) {
      return Action.COOPERATE;
    }
    return opponentPreviousActions.get(opponentPreviousActions.size() - 1);
  }


}
