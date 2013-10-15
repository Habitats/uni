package sushiBar;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class SushiBar {
	// SushiBar settings:
	// These parameters have to be changed to check that the program works in all situations.

	public static int capacity = 3;
	private static int duration = 5; // Simulation time
	public static int maxOrder = 10; // Maximum number of orders for each customer
	public static int customerWait = 1000; // coefficient of eating time for customers
	public static int doorWait = 100; // coefficient of waiting time for door for creating next customer

	public static int id = 1;

	public static boolean isOpen = true;

	// Creating the log file
	private static File log;
	private static String path = "./";
	public static int customers = 0;

	private Stats stats;
	private Door door;

	public static void main(String[] args) {
		log = new File(path + "log.txt");

		// To be completed
		new Clock(duration);
		new SushiBar().init();
	}

	private void init() {
		stats = new Stats();
		ServingArea servingArea = new ServingArea(stats);
		door = new Door(stats,servingArea);
		new Thread(door).start();
		new Thread(servingArea).start();

	}

	// Writes actions in the log file and console
	synchronized public static void write(String str) {
		try {
			FileWriter fw = new FileWriter(log.getAbsoluteFile(), true);
			BufferedWriter bw = new BufferedWriter(fw);
			bw.write(Clock.getTime() + ", " + str + "\n");
			bw.close();
			System.out.println(Clock.getTime() + ", " + str);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
