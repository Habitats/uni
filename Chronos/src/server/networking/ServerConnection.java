package server.networking;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import chronos.Singleton;

import events.AuthEvent;
import events.NetworkEvent;
import events.NetworkEvent.EventType;

/**
 * Handles the connection with a single client. Event client gets it's own
 * connection on it's own thread.
 * 
 */
public class ServerConnection implements Runnable {

	private final Socket clientSocket;
	private final Server server;
	private ObjectOutputStream out;
	private ObjectInputStream in;

	private ClientConnection clientConnection;

	public ServerConnection(Socket clientSocket, Server server) {
		this.clientSocket = clientSocket;
		this.server = server;
	}

	private void initConnection() throws IOException {
		out = new ObjectOutputStream(clientSocket.getOutputStream());
		in = new ObjectInputStream(clientSocket.getInputStream());
		server.getClientConnections().add(new ClientConnection(out, clientSocket));

		NetworkEvent event;

		try {
			while ((event = (NetworkEvent) in.readObject()) != null) {
				synchronized (event) {
					Singleton.log("Server received: " + event);
					for (ClientConnection clientConnection : server.getClientConnections()) {
						if (clientConnection.getClientSocket() == clientSocket && event.getSender() != null) {
							clientConnection.setPerson(event.getSender());
							this.clientConnection = clientConnection;
							// break;
						}
					}
					// forward event to serverController that handles it
					server.getServerController().evaluateNetworkEvent(event);
					out.reset();
				}
			}
		} catch (Exception e) {
			Singleton.log("Client dropped! Cleaning up...");
			e.printStackTrace();
		}
		out.close();
		in.close();
		clientSocket.close();
		server.getServerController().evaluateNetworkEvent(new AuthEvent(EventType.LOG_OUT, clientConnection.getPerson(), null));
		server.getClientConnections().remove(clientConnection);
	}

	@Override
	public void run() {
		try {
			initConnection();
		} catch (Exception e) {
			e.printStackTrace();
			try {
				out.close();
				in.close();
				clientSocket.close();
			} catch (IOException e1) {
				e1.printStackTrace();
			}
		}
	}
}
