/**
 Example 1B, TDT4180-2005.
 This example shows the use of an action listener by
 letting the JPanel have an innner class "MyButtonAction" that
 implements the ActionListener interface.   **/

import javax.swing.*;
import java.awt.event.*;

import javax.swing.event.*;

public class ButtonAndKeyboardExample extends JPanel {
	private JTextField myTextField, myTextField2;
	private JButton myButton;

	/** Constructor for objects of class ButtonExample_Innerclass */
	public ButtonAndKeyboardExample() {
		myButton = new JButton("Press here");
		myButton.addActionListener(new MyButtonAction());
		add(myButton);
		myTextField = new JTextField();
		myTextField.setColumns(20);
		add(myTextField);
		myTextField.setText("...");
		myTextField.addActionListener(new MyTextAction());
		myTextField.addKeyListener(new MyKeyAction());
		myTextField2 = new JTextField();
		myTextField2.setColumns(20);
		add(myTextField2);
	}

	/** Actions for myButton **/
	class MyButtonAction implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent e) {
			myTextField.setText("Hello world.");
		}
	}

	/** Actions for text **/
	class MyTextAction implements ActionListener {
		@Override
		public void actionPerformed(ActionEvent e) {
			myTextField.setText("Action");
		}
	}

	/** Actions for caret **/
	class MyKeyAction implements KeyListener {
		@Override
		public void keyTyped(KeyEvent e) {
			myTextField2.setText(myTextField.getText());
		}

		@Override
		public void keyPressed(KeyEvent e) {
			// TODO Auto-generated method stub

		}

		@Override
		public void keyReleased(KeyEvent e) {
			// TODO Auto-generated method stub

		}

	}

	public static void main(String args[]) {
		JFrame frame = new JFrame("Lexical events example with button");
		frame.getContentPane().add(new ButtonAndKeyboardExample());
		frame.pack();
		frame.setVisible(true);
	}
}