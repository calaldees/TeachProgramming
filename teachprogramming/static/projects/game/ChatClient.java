import GameLib.Net.AbstractNetworkConnection;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class ChatClient extends AbstractNetworkConnection implements ActionListener {
  
  private JTextArea  text_area;
  private JTextField text_field;
  private String     username;
  
  public ChatClient(                                      ) {this("localhost"           );}
  public ChatClient(String server_address                 ) {this(server_address, "User");}
  public ChatClient(String server_address, String username) {
    this.username = username;
    JFrame frame = new JFrame("Chat Client");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    
    text_field = new JTextField();
    text_field.addActionListener(this);
    frame.add(text_field,BorderLayout.SOUTH);
    
    text_area = new JTextArea();
    text_area.setEditable(false);
    text_area.setLineWrap(true);
    JScrollPane scroll = new JScrollPane(text_area, JScrollPane.VERTICAL_SCROLLBAR_ALWAYS, JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
    frame.add(scroll,BorderLayout.CENTER);
    
    frame.pack();
    frame.setVisible(true);
    
    networkConnect(server_address);
  }
  
  public void networkRecieve(String message) {
    text_area.append(message + "\n");
    text_area.setCaretPosition(text_area.getDocument().getLength());
  }
  
  public void actionPerformed(ActionEvent event) {
    networkSend(username + ": " + text_field.getText());
    text_field.setText("");
  }
  
  public static void main(String[] args) {
    if (args==null || args.length==0) {new ChatClient(               );}
    if (              args.length==1) {new ChatClient(args[0]        );}
    if (              args.length==2) {new ChatClient(args[0],args[1]);}
  } 
}