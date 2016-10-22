package agents;


import java.util.List;

/**
 * Created by Patrick on 16.01.2015.
 *
 * This agent will always defect
 */
public class Defect implements Agent {

  @Override
  public Action dilemma(List<Action> opponentPreviousActions) {
    return Action.DEFECT;
  }

}
