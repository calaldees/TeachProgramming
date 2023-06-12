import java.util.Set;
import java.util.HashSet;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.awt.event.*;
import javax.swing.JFrame;
import java.util.concurrent.*;


class animation_base {
    public static void main(String[] args) {
        new AnimationFrame(){
            @Override 
            void loop(Graphics g, Integer frame) {
                //log(String.join(",",keys_pressed));

                g.setColor(Color.WHITE);
                g.drawString("Hello World", frame%buffer.getWidth(), 100);

                g.setColor(Color.RED);
                g.fillRect(mouse_position.x,mouse_position.y,10,10);
            }
        };
    }
}

abstract class AnimationFrame implements WindowStateListener, WindowListener, KeyListener, MouseListener, MouseMotionListener, MouseWheelListener {

    JFrame jframe;
    final Dimension size = new Dimension(320, 180);
    BufferedImage buffer;
    final Set<String> keys_pressed = new HashSet<String>();
    final Point mouse_position = new Point();
    final Integer fps = 60;

    private final GraphicsDevice screen_device = GraphicsEnvironment.getLocalGraphicsEnvironment().getDefaultScreenDevice();
    private final DisplayMode display_mode_original = screen_device.getDisplayMode();
    private static final DisplayMode display_mode_fullscreen = new DisplayMode(640,360,16,DisplayMode.REFRESH_RATE_UNKNOWN);
    
    ScheduledExecutorService timer;
    Integer frame_number = 0;


    AnimationFrame() {
        initDisplay();
        setFullScreen(false);
        startTimer();
    }

    void initDisplay(){
        if (jframe != null) {jframe.dispose();}

        jframe = new JFrame("Test");
        jframe.addKeyListener(this);
        jframe.addWindowListener(this);
        jframe.addWindowStateListener(this);

        buffer = jframe.getGraphicsConfiguration().createCompatibleImage(size.width, size.height);

        final Component c = new Component() {
            {
                setMaximumSize(size);
                setMinimumSize(size);
                setPreferredSize(size);
                setSize(size);
            }
            public void paint(Graphics g) {g.drawImage(buffer,0,0,this.getWidth(),this.getHeight(),this);}
        };
        c.addMouseListener(this);
        c.addMouseMotionListener(this);
        c.addMouseWheelListener(this);
        jframe.add(c);

    }

    void setFullScreen(Boolean fullscreen) {
        initDisplay();

        if (fullscreen) {
            try {
                jframe.setUndecorated(true);
                screen_device.setFullScreenWindow(jframe);
                //screen_device.setDisplayMode(display_mode_fullscreen);
            }
            catch (Exception e) {throw e;}
        }
        if (!fullscreen) {
            try {
                screen_device.setDisplayMode(display_mode_original);
                screen_device.setFullScreenWindow(null);
            }
            catch (Exception e) {}
            jframe.pack();
        }

        jframe.setVisible(true);
    }

    abstract void loop(Graphics g, Integer frame);

    private void startTimer() {
        if (timer == null) {
            timer = Executors.newSingleThreadScheduledExecutor();
            timer.scheduleAtFixedRate(() -> {
                final var g = buffer.getGraphics();
                g.clearRect(0,0,buffer.getWidth(), buffer.getHeight());
                loop(g, frame_number++);
                jframe.repaint();
            }, 0, 1000/fps, TimeUnit.MILLISECONDS);
        }
    }
    private void stopTimer() {
        if (timer != null) {
            timer.close(); 
            try {timer.awaitTermination(2, TimeUnit.SECONDS);} catch(InterruptedException ex) {}
            timer = null;
        }
    }
    private boolean isFullScreen() {return jframe.isUndecorated();}

    private void exit() {
        setFullScreen(false);
        stopTimer();
        jframe.dispose();
    }

    public void windowStateChanged(WindowEvent e) {
        if (e.getNewState() == JFrame.MAXIMIZED_BOTH) {setFullScreen(true);}
    }
    public void windowOpened(WindowEvent e) {}
    public void windowClosing(WindowEvent e) {exit();}
    public void windowClosed(WindowEvent e) {}
    public void windowIconified(WindowEvent e) {stopTimer();}
    public void windowDeiconified(WindowEvent e) {startTimer();}
    public void windowActivated(WindowEvent e) {}
    public void windowDeactivated(WindowEvent e) {}

    public void keyTyped(KeyEvent e) {}
    public void keyReleased(KeyEvent e) {
        keys_pressed.remove(e.getKeyText(e.getKeyCode()));
    }
    public void keyPressed(KeyEvent e) {
        keys_pressed.add(e.getKeyText(e.getKeyCode()));
        if (e.isAltDown() && e.getKeyCode() == KeyEvent.VK_ENTER) {setFullScreen(!isFullScreen());}
        if (e.isControlDown() && e.getKeyCode() == KeyEvent.VK_C) {exit();}
        if (e.getKeyCode() == KeyEvent.VK_ESCAPE) {exit();}
    }

    public void mouseClicked(MouseEvent e)  {}
    public void mousePressed(MouseEvent e)  {keys_pressed.add("Mouse"+e.getButton());}
    public void mouseReleased(MouseEvent e) {keys_pressed.remove("Mouse"+e.getButton());}
    public void mouseEntered(MouseEvent e)  {}
    public void mouseExited(MouseEvent e)   {}
    public void mouseDragged(MouseEvent e)  {updateMousePosition(e);}// mouseDragged(mouse_position.x,mouse_position.y);}
    public void mouseMoved(MouseEvent e)    {updateMousePosition(e);}// mouseMoved(mouse_position.x,mouse_position.y);}

    private void updateMousePosition(MouseEvent e) {
        mouse_position.x = (int)((e.getX()/(double)jframe.getContentPane().getWidth() )*buffer.getWidth() );
        mouse_position.y = (int)((e.getY()/(double)jframe.getContentPane().getHeight())*buffer.getHeight());
    }
        
    public void mouseWheelMoved(MouseWheelEvent e) {
        int rotation = e.getWheelRotation();
        //if      (rotation>0) {mouseWheelUp();}
        //else if (rotation<0) {mouseWheelDown();}
    }

    private void log(String s) {System.out.println(s);}

}