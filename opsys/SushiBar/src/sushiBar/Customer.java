package sushiBar;

public class Customer implements Runnable {
	private int id;
	private int orders;

	volatile private boolean waiting;
	volatile private boolean done;

	public Customer() {
		done = false;
		this.id = genId();
		log("is now created.");
	}

	@Override
	public void run() {
		order();
		done = true;
	}

	public void eat() {
		log("is eating sushi now...");
		long delta = System.currentTimeMillis();
		try {
			Thread.sleep((int) (SushiBar.customerWait * (orders / 1.)));
			log("ate sushi for " + (System.currentTimeMillis() - delta) + " ms");
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}

	public boolean getSeated() {
		return done;
	}

	private void order() {
		orders = (int) ((Math.random() * 10) + 1);
		log("ordered " + orders + " meals");
		if (Math.random() > 0.5) {
			eat();
		} else
			log("ordered takeaway...");
	}

	public int getOrders() {
		return orders;
	}

	synchronized public boolean isWaiting() {
		return waiting;
	}

	synchronized private int genId() {
		return SushiBar.id++;
	}

	public boolean isDone() {
		return done;
	}

	public void waitingForSeat() {
		waiting = true;
		log("is waiting for a free seat.");
	}

	public void gotSeat() {
		waiting = false;
		log("has a seat now.");
	}

	public void leftShop() {
		log("left the shop.");
	}

	private void log(String s) {
		SushiBar.write(Thread.currentThread().getName() + ": Customer " + id + " " + s);
	}
}
