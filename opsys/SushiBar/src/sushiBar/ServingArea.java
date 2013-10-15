package sushiBar;

public class ServingArea implements Runnable {
	private final Stats stats;

	public ServingArea(Stats stats) {
		this.stats = stats;
	}

	@Override
	public void run() {
		init();
	}

	private void init() {

		while (stats.getCurrentCustomers().size() > 0 || SushiBar.isOpen) {
			int i = 0;
			while (i <= stats.getCurrentCustomers().size()) {
				Customer currentCustomer;
				if (stats.getCurrentCustomers().size() > i)
					currentCustomer = stats.getCurrentCustomers().get(i);
				else
					break;
				synchronized (currentCustomer) {
					if (stats.getCurrentCustomers().size() <= SushiBar.capacity && currentCustomer.isWaiting()) {
						join(currentCustomer);
						Thread customerThread = new Thread(currentCustomer);
						customerThread.start();
					} else if (currentCustomer.isDone())
						leave(currentCustomer);
				}
				i++;
			}
		}
		finished();
	}

	private void join(Customer c) {
		c.gotSeat();
	}

	private void leave(Customer c) {
		stats.removeCustomer(c);
		c.leftShop();
		synchronized (this) {
			notifyAll();
		}
	}

	public void finished() {
		SushiBar.write(stats.toString());
	}
}
