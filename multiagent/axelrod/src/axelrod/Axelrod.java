package axelrod;

import java.util.ArrayList;
import java.util.List;

import agents.Oxymoron;
import agents.Coop;
import agents.Defect;
import agents.Agent;
import agents.Mix;
import agents.TitForTat;
import agents.TitForTwoTat;

/**
 * Created by Patrick on 16.01.2015.
 *
 * This is the Axelrod Tournament main class
 */
public class Axelrod {

  public static void main(String[] args) {
    new Axelrod().run();
  }

  private void run() {
    // create and initialize the agents
    Agent almostRandom = new Oxymoron();
    Agent coop = new Coop();
    Agent defect = new Defect();
    Agent mix = new Mix();
    Agent titForTat = new TitForTat();
    Agent titForTwoTat = new TitForTwoTat();

    List<Agent> agents = new ArrayList<Agent>();
    agents.add(almostRandom);
    agents.add(coop);
    agents.add(defect);
    agents.add(mix);
    agents.add(titForTat);
    agents.add(titForTwoTat);

    List<Result> results = new ArrayList<Result>();

    // for every tournament
    for (int tournament = 1; tournament <= 3; tournament++) {
      System.out.println("\n\nRound: " + tournament);

      // for every round
      for (int n = 10; n <= 1000; n += 10) {
        System.out.println("\nN: " + n);

        for (Agent agent : agents) {
          Result result = play(agent, agents, n);
          results.add(result);

          // format it pretty
          System.out
              .format("%13s - F: %.3f - M: %s%n", agent.getClass().getSimpleName(), result.getF(), result.getMString());
        }
      }
    }
  }

  private Result play(Agent agent, List<Agent> agents, int n) {

    Result result = new Result(agent, agents.size());
    for (Agent opponent : agents) {
      double m = 0;
      // avoid playing against itself
      if (!opponent.equals(agent)) {
        // create fresh lists of actions
        List<Agent.Action> opponentActions = new ArrayList<Agent.Action>();
        List<Agent.Action> agentActions = new ArrayList<Agent.Action>();

        // do the fighting!
        for (int i = 0; i < n; i++) {
          Agent.Action agentAction = agent.dilemma(opponentActions);
          agentActions.add(agentAction);

          Agent.Action opponentAction = opponent.dilemma(agentActions);
          opponentActions.add(opponentAction);

          result.addFight(agentAction, opponentAction, opponent);
        }
      }
    }

    return result;
  }
}
