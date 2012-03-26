import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class Calculator implements ActionListener {

  private JTextField input1 = new JTextField(5);
  private JTextField input2 = new JTextField(5);
  private JTextField output = new JTextField(5);
  
  public Calculator() {
    setupGUI();
  }

  public static void main(String[] args) {
    new Calculator();
  }

  private void setupGUI() {
    JFrame frame = new JFrame("Calculator");
    JPanel panel = new JPanel();
    
    panel.add(input1);
    panel.add(input2);
    panel.add(makeJButton("add"));
    panel.add(makeJButton("sub"));
    panel.add(makeJButton("div"));
    panel.add(makeJButton("multiply"));
    panel.add(output);
    
    frame.add(panel);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.pack();
    frame.setVisible(true);
  }
  
  private JButton makeJButton(String name) {
    JButton button = new JButton(name);
    button.setActionCommand(name);
    button.addActionListener(this);
    return button;
  }

  public void actionPerformed(ActionEvent e) {
    String command = e.getActionCommand();
    double input_number_1 = Double.parseDouble(input1.getText());
    double input_number_2 = Double.parseDouble(input2.getText());
    double output_calculated = 0;
    if      (command.equals("add"))      {output_calculated = input_number_1 + input_number_2;}
    else if (command.equals("sub"))      {output_calculated = input_number_1 - input_number_2;}
    else if (command.equals("div"))      {output_calculated = input_number_1 / input_number_2;}
    else if (command.equals("multiply")) {output_calculated = input_number_1 * input_number_2;}
    output.setText(""+output_calculated);
  }
}