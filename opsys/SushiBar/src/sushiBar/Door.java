package sushiBar;

public class Door implements Runnable {

	private final Stats stats;
	private final ServingArea servingArea;

	public Door(Stats stats, ServingArea servingArea) {
		this.stats = stats;
		this.servingArea = servingArea;
	}

	@Override
	public void run() {
		generateCustomers();
	}

	private void generateCustomers() {
		try {
			while (SushiBar.isOpen) {
				if (SushiBar.capacity <= stats.getCurrentCustomers().size()) {
					SushiBar.write("SushiBar is full!");
					synchronized (servingArea) {
						servingArea.wait();
					}
					SushiBar.write("Now there is a free eat in the shop.");
				}
				Customer newCustomer = new Customer();
				newCustomer.waitingForSeat();
				stats.addCustomer(newCustomer);
				Thread.sleep((int) (Math.random() * 15 * SushiBar.doorWait));
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		SushiBar.write("***** NO MORE CUSTOMERS - THE SHOP IS CLOSED NOW. *****");
	}

}
