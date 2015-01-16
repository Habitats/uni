package axelrod;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import agents.ExtendedAgent;
import agents.AlmostRandom;
import agents.Coop;
import agents.Defect;
import agents.Mix;
import agents.TitForTat;
import agents.TitForTwoTat;

/**
 * Created by Patrick on 16.01.2015.
 */
public class Axelrod {

  public static void main(String[] args) {
    new Axelrod().run();
  }

  private void run() {
    ExtendedAgent almostRandom = new AlmostRandom();
    ExtendedAgent coop = new Coop();
    ExtendedAgent defect = new Defect();
    ExtendedAgent mix = new Mix();
    ExtendedAgent titForTat = new TitForTat();
    ExtendedAgent titForTwoTat = new TitForTwoTat();

    Set<ExtendedAgent> agents = new HashSet<ExtendedAgent>();
    agents.add(almostRandom);
    agents.add(coop);
    agents.add(defect);
    agents.add(mix);
    agents.add(titForTat);
    agents.add(titForTwoTat);

    List<Result> results = new ArrayList<Result>();
    for (ExtendedAgent agent : agents) {
      Result result = play(agent, agents, 30);
      results.add(result);

      System.out.println(agent.getClass().getSimpleName() + " - M: " + result.getM() + " - F: " + result.getF());
    }
  }

  private Result play(ExtendedAgent agent, Set<ExtendedAgent> agents, int n) {
    Result result = new Result(agent, agents.size());

    for (ExtendedAgent opponent : agents) {
      // avoid playing against itself
      if (!opponent.equals(agent)) {
        // create fresh lists of actions
        List<ExtendedAgent.Action> opponentActions = new ArrayList<ExtendedAgent.Action>();
        List<ExtendedAgent.Action> agentActions = new ArrayList<ExtendedAgent.Action>();

        agentActions.add(agent.getInitialAction());

        // do the fighting!
        for (int i = 0; i < n; i++) {
          // opponent makes an action
          ExtendedAgent.Action opponentAction = opponent.dilemma(agentActions);
          opponentActions.add(opponentAction);

          // the agent answers
          ExtendedAgent.Action agentAction = agent.dilemma(opponentActions);
          agentActions.add(agentAction);

          result.addFight(agentAction, opponentAction);
        }
      }
    }

    return result;
  }
}
