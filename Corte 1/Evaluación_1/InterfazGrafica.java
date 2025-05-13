import javax.swing.*; //Clase para crear cuadro de diálogo
import java.awt.*; //Conjunto de clases para creación de GUI
import java.awt.event.*; //Manejo de eventos en interfaz gráfica

public class InterfazGrafica {
    private JFrame frame; //Ventana principal de aplicación con interfaz gráfica
    private CajeroAutomatico cajero;

    // Componentes de la interfaz gráfica
    private JTextField textFieldSaldo;
    private JTextField textFieldMonto;
    private JButton btnRetirar, btnDepositar, btnConsultarSaldo, btnVerSaldo;

    // Constructor
    public InterfazGrafica() {
        cajero = new CajeroAutomatico(0); //
        initialize();
    }

    // Inicializar la interfaz gráfica
    private void initialize() {
        frame = new JFrame("Cajero Automático");
        frame.setBounds(800, 250, 350, 300); //Tamaño de la interfaz gráfica
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //Cierre de la ventana
        frame.getContentPane().setLayout(new BorderLayout());

        // Panel para los botones y campos de texto
        JPanel panel = new JPanel();
        frame.getContentPane().add(panel, BorderLayout.CENTER);
        panel.setLayout(new GridLayout(6, 2));
        panel.setBackground(new Color(102, 255, 102));

        // Campo de texto para mostrar el saldo
        JLabel lblSaldo = new JLabel("Saldo:");
        panel.add(lblSaldo);
        textFieldSaldo = new JTextField();
        textFieldSaldo.setEditable(false);
        panel.add(textFieldSaldo);

        // Campo de texto para ingresar el monto
        JLabel lblMonto = new JLabel("Monto a depositar:");
        panel.add(lblMonto);
        textFieldMonto = new JTextField();
        panel.add(textFieldMonto);

        // Botón para consultar el saldo
        btnConsultarSaldo = new JButton("Consultar Saldo");
        panel.add(btnConsultarSaldo);
        btnConsultarSaldo.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                textFieldSaldo.setText(String.valueOf(cajero.consultarSaldo()));
            }
        });

        // Botón para retirar dinero
        btnRetirar = new JButton("Retirar");
        panel.add(btnRetirar);
        btnRetirar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                double monto = Double.parseDouble(textFieldMonto.getText());
                boolean exito = cajero.retirarDinero(monto);
                if (exito) {
                    JOptionPane.showMessageDialog(frame, "Retiro exitoso.");
                } else {
                    JOptionPane.showMessageDialog(frame, "No tienes saldo suficiente");
                }
                textFieldSaldo.setText(String.valueOf(cajero.consultarSaldo()));
            }
        });

        // Botón para depositar dinero
        btnDepositar = new JButton("Depositar");
        panel.add(btnDepositar);
        btnDepositar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                double monto = Double.parseDouble(textFieldMonto.getText());
                cajero.depositarDinero(monto);
                JOptionPane.showMessageDialog(frame, "Depósito exitoso.");
                textFieldSaldo.setText(String.valueOf(cajero.consultarSaldo()));
            }
        });

        // Botón adicional para ver saldo disponible
        btnVerSaldo = new JButton("Ver Saldo Disponible");
        panel.add(btnVerSaldo);
        btnVerSaldo.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                textFieldSaldo.setText(String.valueOf(cajero.consultarSaldo()));
            }
        });

        // Configurar la ventana
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        new InterfazGrafica();
    }
}
