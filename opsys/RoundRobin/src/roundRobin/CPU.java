package roundRobin;

import javax.swing.plaf.SliderUI;

import gui.Gui;

public class CPU {
	private volatile Queue cpuQueue;
	private final Gui gui;
	private final long maxCpuTime;
	private final Simulator simulator;
	private final Memory memory;

	public CPU(Queue cpuQueue, Gui gui, long maxCpuTime, Simulator simulator, Memory memory) {
		this.cpuQueue = cpuQueue;
		this.gui = gui;
		this.maxCpuTime = maxCpuTime;
		this.simulator = simulator;
		this.memory = memory;
		Robin robin = new Robin();
		new Thread(robin).start();
	}

	public void insertProcess(Process p) {
		cpuQueue.insert(p);
	}

	private class Robin implements Runnable {

		private void robinLoop() {
			Process p;
			System.out.println("loopin");
			while (true) {
				if (!cpuQueue.isEmpty()) {
					p = (Process) cpuQueue.removeNext();
					runProcess(p);
				}
			}
		}

		private void runProcess(Process p) {
			gui.setCpuActive(p);
			long computationalTime = p.getCpuTimeNeeded();
			try {
				if (computationalTime >= maxCpuTime) {
					p.decreaseCpuTimeNeeded(maxCpuTime);
					Thread.sleep(maxCpuTime);
					cpuQueue.insert(p);
				} else if (p.getCpuTimeNeeded() < maxCpuTime) {
					Thread.sleep(computationalTime);
					gui.setCpuActive(null);
					memory.processCompleted(p);
					Thread.sleep(maxCpuTime - computationalTime);
				}
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}

		@Override
		public void run() {
			robinLoop();
		}
	}
}
