package sushiBar;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Stats {
	private List<Customer> currentCustomers;
	private ArrayList<Customer> totalCustomers;
	private int maxCustomers = 0;

	public Stats() {
		currentCustomers = Collections.synchronizedList(new ArrayList<Customer>());
		totalCustomers = new ArrayList<Customer>();
	}

	public void setCurrentCustomer(ArrayList<Customer> currentCustomer) {
		this.currentCustomers = currentCustomer;
	}

	synchronized public void addCustomer(Customer c) {
		totalCustomers.add(c);
		currentCustomers.add(c);
		if (currentCustomers.size() > maxCustomers)
			maxCustomers = currentCustomers.size();
	}

	synchronized public void removeCustomer(Customer c) {
		currentCustomers.remove(c);
	}

	synchronized public int totalOrders() {
		int totalOrders = 0;
		for (Customer c : totalCustomers) {
			totalOrders += c.getOrders();
		}
		return totalOrders;
	}

	synchronized public List<Customer> getCurrentCustomers() {
		return currentCustomers;
	}

	@Override
	public String toString() {
		return "Total Customers: " + totalCustomers.size() + //
				" - Current Customers: " + currentCustomers.size() + //
				" - Total Orders: " + totalOrders() + //
//				" - Average Orders pr. Customer: " + totalOrders() / (double) totalCustomers.size() + //
				" - Max Customers: " + maxCustomers //
		;
	}
}
