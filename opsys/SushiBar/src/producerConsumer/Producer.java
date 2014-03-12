package producerConsumer;

public class Producer implements Runnable{

	private final Monitor mon;

	public Producer(Monitor mon) {
		this.mon = mon;
	}

	@Override
	public void run() {
		while(true){
			String item = produce();
			mon.insert(item);
		}
	}
	
	private String produce(){
		return "bitch";
	}

}
