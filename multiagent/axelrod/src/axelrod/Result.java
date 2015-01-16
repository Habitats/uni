package axelrod;

import agents.Agent;

/**
 * Created by Patrick on 16.01.2015.
 */
public class Result {

  public final Agent agent;
  private int numAgents;
  private int sum = 0;
  private int numFights = 0;

  public Result(Agent agent, int numAgents) {
    this.agent = agent;
    this.numAgents = numAgents;
  }

  public void addFight(Agent.Action agentAction, Agent.Action opponentAction) {
    if (agentAction == Agent.Action.COOPERATE && opponentAction == Agent.Action.COOPERATE) {
      sum += 3;
    } else if (agentAction == Agent.Action.COOPERATE && opponentAction == Agent.Action.DEFECT) {
      sum += 0;
    } else if (agentAction == Agent.Action.DEFECT && opponentAction == Agent.Action.DEFECT) {
      sum += 2;
    } else if (agentAction == Agent.Action.DEFECT && opponentAction == Agent.Action.COOPERATE) {
      sum += 5;
    }

    numFights++;
  }

  public double getM() {
    return (double) sum / numFights;
  }

  public double getF() {
    return getM() / numAgents;
  }
}
