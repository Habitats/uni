package roundRobin;

import gui.Constants;
import gui.Gui;

public class CPU implements Constants {
	private volatile Queue cpuQueue;
	private final Gui gui;
	private final long maxCpuTime;
	private Process activeProcess;
	private final Statistics statistics;
	private final EventQueue eventQueue;

	public CPU(Queue cpuQueue, Gui gui, long maxCpuTime, Statistics statistics, EventQueue eventQueue) {
		this.cpuQueue = cpuQueue;
		this.gui = gui;
		this.maxCpuTime = maxCpuTime;
		this.statistics = statistics;
		this.eventQueue = eventQueue;
	}

	public void insertProcess(Process p, long clock) {
		cpuQueue.insert(p);
		p.leftMemoryQueue(clock);
		if (statistics.maxCpuQueueLength < cpuQueue.getQueueLength())
			statistics.maxCpuQueueLength = cpuQueue.getQueueLength();

		// if there's currently no running process
		if (getActiveProcess() == null) {
			startNextProcess(clock);
		}
	}

	public void endProcess(long clock) {
		Process p = getActiveProcess();
		p.leftCpu(clock);
		p.updateStatistics(statistics);
		setActiveProcess(null);
		startNextProcess(clock);
	}

	public void switchProcess(long clock) {
		if (getActiveProcess() != null) {
			statistics.totalProcessSwitches++;
			Process p = getActiveProcess();
			setActiveProcess(null);
			insertProcess(p, clock);
		}
		// startNextProcess(clock);
	}

	private void startNextProcess(long clock) {
		Process p = null;

		if (!cpuQueue.isEmpty()) {
			p = (Process) cpuQueue.removeNext();
			p.enteredCpu(clock);
			setActiveProcess(p);
			generateEvent(p, clock);

		}
		gui.setCpuActive(p);
	}

	private void generateEvent(Process p, long clock) {
		Event evt = null;
		if (p.getCpuTimeNeeded() <= maxCpuTime)
			evt = new Event(END_PROCESS, clock + p.getCpuTimeNeeded());
		else if (p.getCpuTimeNeeded() > maxCpuTime) {
			p.decreaseCpuTimeNeeded(maxCpuTime);
			evt = new Event(SWITCH_PROCESS, clock);
		}

		eventQueue.insertEvent(evt);
	}

	public Process getActiveProcess() {
		return activeProcess;
	}

	public void setActiveProcess(Process activeProcess) {
		this.activeProcess = activeProcess;
	}
}
