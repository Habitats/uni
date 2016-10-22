package axelrod;

import java.util.HashMap;
import java.util.Map;

import agents.Agent;

/**
 * Created by Patrick on 16.01.2015.
 */
public class Result {

  public final Agent agent;
  private Map<Agent, Integer> mScores;
  private Map<Agent, Integer> numFights;

  public Result(Agent agent, int numAgents) {
    this.agent = agent;
    mScores = new HashMap<Agent, Integer>();
    numFights = new HashMap<Agent, Integer>();
  }

  public void addFight(Agent.Action agentAction, Agent.Action opponentAction, Agent opponent) {
    if (!mScores.containsKey(opponent)) {
      mScores.put(opponent, 0);
    }
    if (!numFights.containsKey(opponent)) {
      numFights.put(opponent, 0);
    }

    int score = 0;
    if (agentAction == Agent.Action.COOPERATE && opponentAction == Agent.Action.COOPERATE) {
      score += 3;
    } else if (agentAction == Agent.Action.COOPERATE && opponentAction == Agent.Action.DEFECT) {
      score += 0;
    } else if (agentAction == Agent.Action.DEFECT && opponentAction == Agent.Action.DEFECT) {
      score += 2;
    } else if (agentAction == Agent.Action.DEFECT && opponentAction == Agent.Action.COOPERATE) {
      score += 5;
    }

    mScores.put(opponent, mScores.get(opponent) + score);
    numFights.put(opponent, numFights.get(opponent) + 1);
  }

  public double getM(Agent opponent) {
    return ((double) mScores.get(opponent)) / numFights.get(opponent);
  }

  public double getF() {
    double sum = 0;
    for (Agent opponent : mScores.keySet()) {
      sum += getM(opponent);
    }
    return sum / mScores.size();
  }

  public String getMString() {
    StringBuilder sb = new StringBuilder();
    for (Agent opponent : mScores.keySet()) {
      sb.append(String.format("%13s", opponent.getClass().getSimpleName())).append(" ")
          .append(String.format("%.3f", getM(opponent))).append(" - ");
    }

    return sb.toString().substring(0, sb.length() - 2);
  }
}
