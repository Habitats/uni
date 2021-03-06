package a.agents;

import a.misc.Problem;
import util.Log;

/**
 * A simple agent for executing division
 */
public class DivisionSolver extends AbstractSolverAgent {

  @Override
  protected int getExecutionEstimate(String content) {
    return super.getExecutionEstimate(content) + EXECUTION_CONSTANT;
  }

  @Override
  protected void problemReceived(Problem problem) {
    problem.solve();
    Log.v(getTag(), "Returning answer: " + problem);
  }

  @Override
  protected String getServiceName() {
    return Operator.DIVISION.get();
  }

}
