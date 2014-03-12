package producerConsumer;

import java.util.ArrayList;
import java.util.List;

public class Monitor {

	private List<String> q = new ArrayList<String>();

	private final int MAX = 1000;

	synchronized public void insert(String item) {
		if (q.size() == MAX)
			goToSleep();
		q.add(item);
		System.out.println("Added item, new size: " + q.size()); 
		if(q.size() == 1) notify();
	}

	synchronized public String remove() {
		if (q.size() == 0)
			goToSleep();
		String item = q.remove(q.size() - 1);
		System.out.println("Removed item, new size: " + q.size()); 
		if(q.size() < MAX) notify();
		return item;
	}

	private void goToSleep() {
		try {
			System.out.println(Thread.currentThread().getName() + " is going to sleep");
			wait();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
