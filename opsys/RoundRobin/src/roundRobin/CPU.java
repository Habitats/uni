package roundRobin;

public class CPU {
	private Queue cpuQueue;

	public CPU(Queue cpuQueue) {
		this.cpuQueue = cpuQueue;
	}

	public void insertProcess(Process p) {
		cpuQueue.insert(p);

	}

}
