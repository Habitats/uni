package roundRobin;

import gui.Constants;
import gui.Gui;

public class IO implements Constants {
	private Process activeProcess;
	private final Gui gui;
	private final Queue ioQueue;
	private final EventQueue eventQueue;
	private final Statistics statistics;

	public IO(Queue ioQueue, EventQueue eventQueue, Statistics statistics, Gui gui) {
		this.ioQueue = ioQueue;
		this.eventQueue = eventQueue;
		this.statistics = statistics;
		this.gui = gui;
	}

	public void startIO(Process process, long clock) {

		long future = 0;
		for (Object p : ioQueue.getList()) {
			future += ((Process) p).getTimeToNextIoOperation();
		}

		if (getActiveProcess() == null) {
			setActiveProcess(process);
			gui.setIoActive(getActiveProcess());
		} else {
			ioQueue.insert(process);
			process.enteredIoQueue(clock);

			if (ioQueue.getQueueLength() > statistics.maxIoQueueLength)
				statistics.maxIoQueueLength = ioQueue.getQueueLength();
		}

		eventQueue.insertEvent(new Event(Constants.END_IO, clock + process.getTimeToNextIoOperation() + future));
	}

	public void endIO(long clock) {

		Process p = getActiveProcess();
		System.out.println(p);
		p.leftIoQueue(clock);
		p.setTimeToIo();

		if (!this.ioQueue.isEmpty()) {
			p = (Process) ioQueue.removeNext();
			p.leftIoQueue(clock);
		} else {
			p = null;
		}
		this.gui.setIoActive(p);
		setActiveProcess(p);
	}

	public Process getActiveProcess() {
		return activeProcess;
	}

	public void setActiveProcess(Process activeProcess) {
		this.activeProcess = activeProcess;
	}

}
