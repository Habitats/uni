package roundRobin;

/**
 * This class contains a lot of public variables that can be updated by other classes during a simulation, to collect information about the run.
 */
public class Statistics {
	/** The number of processes that have exited the system */
	public long nofCompletedProcesses = 0;
	/** The number of processes that have entered the system */
	public long nofCreatedProcesses = 0;
	/** The total time that all completed processes have spent waiting for memory */
	public long totalTimeSpentWaitingForMemory = 0;
	/** The time-weighted length of the memory queue, divide this number by the total time to get average queue length */
	public long memoryQueueLengthTime = 0;
	/** The largest memory queue length that has occured */
	public long memoryQueueLargestLength = 0;

	/** extra stuff */
	public long maxCpuQueueLength = 0;
	public long maxIoQueueLength = 0;

	public long totalProcessSwitches = 0;
	public long totalIoOperations = 0;

	public long totalTimeSpentInCpu = 0;
	public long totalTimeSpentInIo = 0;
	public long totalTimeSpentInReadyQueue = 0;
	public long totalTimeSpentInIoQueue = 0;
	public long totalTimeCpuIdle = 0;
	public long totalTimesInCpu = 0;

	/**
	 * Prints out a report summarizing all collected data about the simulation.
	 * 
	 * @param simulationLength
	 *            The number of milliseconds that the simulation covered.
	 */
	public void printReport(long simulationLength) {
		totalTimeCpuIdle = simulationLength - totalTimeSpentInCpu;

		System.out.println();
		System.out.println("Simulation statistics:");
		System.out.println();
		System.out.println("Number of completed processes:                                " + nofCompletedProcesses);
		System.out.println("Number of created processes:                                  " + nofCreatedProcesses);
		System.out.println();

		System.out.println("Number of (forced) process switches:                          " + totalProcessSwitches);
		System.out.println("Number of processed I/O operations:                           " + totalIoOperations);
		System.out.println("Average throughput (processes per second):                    " + ((float) nofCompletedProcesses) / simulationLength * 1000);
		System.out.println();
		System.out.println("Total CPU time spent processing:                              " + totalTimeSpentInCpu + " ms");
		System.out.println("Fraction of CPU time spent processing:                        " + ((float) totalTimeSpentInCpu) / simulationLength + "%");
		System.out.println("Total CPU time spent waiting:                                 " + totalTimeCpuIdle + " ms");
		System.out.println("Fraction of CPU time spent waiting:                           " + ((float) totalTimeCpuIdle) / simulationLength + "%");
		System.out.println();
		System.out.println("Largest occuring memory queue length:                         " + memoryQueueLargestLength);
		System.out.println("Average memory queue length:                                  " + (float) memoryQueueLengthTime / simulationLength);
		System.out.println("Largest occuring cpu queue length:                            " + maxCpuQueueLength);
		System.out.println("Average cpu queue length:                                     " + (float) totalTimeSpentInReadyQueue / simulationLength);
		System.out.println("Largest occuring I/O queue length:                            " + maxIoQueueLength);
		System.out.println("Average I/O queue length:                                     " + (float) totalTimeSpentInIoQueue / simulationLength);
		System.out.println();

		if (nofCompletedProcesses > 0) {
			System.out.println("Average # of times a process has been placed in memory queue: " + 1);
			System.out.println("Average # of times a process has been placed in cpu queue:    " + (float) totalTimesInCpu / nofCompletedProcesses);
			System.out.println("Average # of times a process has been placed in I/O queue:    " + (float) totalIoOperations / nofCompletedProcesses);
			System.out.println();

			System.out.println("Average time spent in system per process:                     " + simulationLength / nofCompletedProcesses + " ms");
			System.out.println("Average time spent waiting for memory per process:            " + totalTimeSpentWaitingForMemory / nofCompletedProcesses + " ms");
			System.out.println("Average time spent waiting for cpu per process:               " + totalTimeSpentInReadyQueue / nofCompletedProcesses + " ms");
			System.out.println("Average time spent processing per process:                    " + totalTimeSpentInCpu / nofCompletedProcesses + " ms");
			System.out.println("Average time spent waiting for I/O per process:               " + totalTimeSpentInIoQueue / nofCompletedProcesses + " ms");
			System.out.println("Average time spent in I/O per process:                        " + totalTimeSpentInIo / nofCompletedProcesses + " ms");
		}
	}
}
