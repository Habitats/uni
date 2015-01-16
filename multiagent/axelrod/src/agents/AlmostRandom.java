package agents;

import java.util.List;

/**
 * Created by Patrick on 16.01.2015.
 *
 * This agent will cooperate if the opponents last action was to cooperate. If the opponent did not cooperate, it will
 * still cooperate a percentage of the time, otherwise defect.
 */
public class AlmostRandom implements ExtendedAgent {

  @Override
  public Action dilemma(List<Action> opponentPreviousActions) {
    Action opponentDefected = (Math.random() > .7 ? Action.COOPERATE : Action.DEFECT);
    Action opponentsLastAction = opponentPreviousActions.get(opponentPreviousActions.size() - 1);
    return opponentsLastAction == Action.COOPERATE ? Action.COOPERATE : opponentDefected;
  }

  @Override
  public Action getInitialAction() {
    return (Math.random() > .7 ? Action.COOPERATE : Action.DEFECT);
  }
}
