package producerConsumer;

public class ProducerConsumer {
	public static void main(String[] args) {
		Monitor mon = new Monitor();

		Producer p = new Producer(mon);
		Consumer c = new Consumer(mon);

		Thread pThread = new Thread(p);
		Thread cThread = new Thread(c);

		pThread.setName("Producer");
		cThread.setName("Consumer");

		pThread.start();
		cThread.start();

	}

}
