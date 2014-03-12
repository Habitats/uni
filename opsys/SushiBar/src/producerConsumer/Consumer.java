package producerConsumer;

public class Consumer implements Runnable{
	
	private final Monitor mon;

	public Consumer(Monitor mon) {
		this.mon = mon;
	}
	
	@Override
	public void run() {
		while(true){
			String item = mon.remove();
			consume(item);
		}
	}

	private void consume(String item) {
		
	}

}
