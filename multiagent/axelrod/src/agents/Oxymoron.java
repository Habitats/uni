package agents;

import java.util.List;

/**
 * Created by Patrick on 16.01.2015.
 *
 * This agent will cooperate if the opponents last action was to cooperate. If the opponent did not cooperate, it will
 * still cooperate a percentage of the time, otherwise defect.
 */
public class Oxymoron implements Agent {

  private Agent titForTat = new TitForTat();

  @Override
  public Action dilemma(List<Action> opponentPreviousActions) {
    if (opponentPreviousActions.size() == 0) {
      return chooseAction();
    }

    int coop = 0;
    for (Action opponentsLastAction : opponentPreviousActions) {
      if (opponentsLastAction == Action.COOPERATE) {
        coop++;
      }
    }

    if (coop == 0) {
      return Action.DEFECT;
    }

    if (coop == opponentPreviousActions.size()) {
      return Action.DEFECT;
    }

    return titForTat.dilemma(opponentPreviousActions);
  }

  private Action chooseAction() {
    return (Math.random() > .2 ? Action.DEFECT : Action.COOPERATE);
  }
}
