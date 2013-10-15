package roundRobin;

import gui.Gui;

public class CPU {
	private Queue cpuQueue;
	private final Gui gui;

	public CPU(Queue cpuQueue, Gui gui) {
		this.cpuQueue = cpuQueue;
		this.gui = gui;
	}

	public void insertProcess(Process p) {
		cpuQueue.insert(p);
		runProcess(p);

	}

	private void runProcess(Process p) {
		gui.setCpuActive(p);

	}
}
