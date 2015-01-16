package agents;

import java.util.List;

/**
 * Created by Patrick on 16.01.2015.
 *
 * This agent will cooperate if unless the opponent defects twice
 */
public class TitForTwoTat implements ExtendedAgent {


  @Override
  public Action dilemma(List<Action> opponentPreviousActions) {
    if (opponentPreviousActions.size() == 0) {
      return Action.COOPERATE;
    }

    // cooperate if last action was cooperative
    Action lastAction = opponentPreviousActions.get(opponentPreviousActions.size() - 1);
    if (lastAction == Action.COOPERATE) {
      return lastAction;
    } else {
      // if opponent only has one action
      if (opponentPreviousActions.size() == 1) {
        return Action.COOPERATE;
      } else {
        // this will effectively defect if opponent defected twice, otherwise cooperate
        Action secondLastAction = opponentPreviousActions.get(opponentPreviousActions.size() - 2);
        return secondLastAction;
      }
    }
  }

  @Override
  public Action getInitialAction() {
    return Action.COOPERATE;
  }
}
