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
            int x = 100;
            int y = 100;

            Image image = loadImage("images/block.gif");

            @Override 
            void loop(Graphics g, Integer frame) {
                //log(String.join(",",keys_pressed));

                //g.setColor(Color.WHITE);
                //g.drawString("Hello World", frame % buffer.getWidth(), 100);

                int t = frame % buffer.getWidth();
                Color color = new Color((int) Long.parseLong("FFf0b000", 16));
                g.setColor(color);
                g.fillRect(t,10,120,80);

                t = frame % buffer.getHeight();
                g.setColor(Color.RED);
                //pen.Width = 5;  //??
                g.drawLine(t,t,t+10,t+10);

                g.drawImage(image,mouse_position.x,mouse_position.y,jframe);
                //g.setColor(Color.RED);
                //g.fillRect(mouse_position.x,mouse_position.y,10,10);

                if (keys_pressed.contains("Up")) { y += -1; }
                if (keys_pressed.contains("Down")) { y += 1; }
                if (keys_pressed.contains("Left")) { x += -1; }
                if (keys_pressed.contains("Right")) { x += 1; }
                g.drawImage(image,x,y,jframe);
                //g.setColor(Color.YELLOW);
                //g.fillRect(x,y,10,10);
            }
        };
    }
}

abstract class AnimationFrame implements WindowStateListener, WindowListener, KeyListener, MouseListener, MouseMotionListener, MouseWheelListener {

    final Dimension size;
    final Integer fps;

    final Set<String> keys_pressed = new HashSet<String>();
    final Point mouse_position = new Point();
    
    private final GraphicsDevice screen_device = GraphicsEnvironment.getLocalGraphicsEnvironment().getDefaultScreenDevice();
    private final DisplayMode display_mode_original = screen_device.getDisplayMode();
    private static final DisplayMode display_mode_fullscreen = new DisplayMode(640,360,16,DisplayMode.REFRESH_RATE_UNKNOWN);
    
    JFrame jframe;
    BufferedImage buffer;
    ScheduledExecutorService timer;
    Integer frame_number = 0;


    AnimationFrame() {this(new Dimension(320, 180), 60);}
    AnimationFrame(Dimension size, Integer fps) {
        this.size = size;
        this.fps = fps;
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
        if (fullscreen) {try {
            jframe.setUndecorated(true);
            screen_device.setFullScreenWindow(jframe);
            //screen_device.setDisplayMode(display_mode_fullscreen);
        } catch (Exception e) {throw e;}}
        if (!fullscreen) {try {
                screen_device.setDisplayMode(display_mode_original);
                screen_device.setFullScreenWindow(null);
            } catch (Exception e) {}
            jframe.pack();
        }
        jframe.setVisible(true);
    }

    abstract void loop(Graphics g, Integer frame);

    private void startTimer() {
        if (timer == null) {
            timer = Executors.newSingleThreadScheduledExecutor();
            timer.scheduleAtFixedRate(() -> {try {
                final var g = buffer.getGraphics();
                g.clearRect(0,0,buffer.getWidth(), buffer.getHeight());
                loop(g, frame_number++);
                jframe.repaint();
            }catch (Exception ex){ex.printStackTrace(System.out); System.exit(1);}}, 0, 1000/fps, TimeUnit.MILLISECONDS);
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
        jframe = null;
    }

    public void windowStateChanged(WindowEvent e) {
        if (e.getNewState() == JFrame.MAXIMIZED_BOTH) {setFullScreen(true);}
    }
    public void windowOpened(WindowEvent e) {}
    public void windowClosing(WindowEvent e) {exit();}
    public void windowClosed(WindowEvent e) {}
    public void windowIconified(WindowEvent e) {}
    public void windowDeiconified(WindowEvent e) {}
    public void windowActivated(WindowEvent e) {startTimer();}
    public void windowDeactivated(WindowEvent e) {stopTimer();}

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
    public void mouseDragged(MouseEvent e)  {updateMousePosition(e);}
    public void mouseMoved(MouseEvent e)    {updateMousePosition(e);}

    private void updateMousePosition(MouseEvent e) {
        mouse_position.x = (int)((e.getX()/(double)jframe.getContentPane().getWidth() )*buffer.getWidth() );
        mouse_position.y = (int)((e.getY()/(double)jframe.getContentPane().getHeight())*buffer.getHeight());
    }
        
    public void mouseWheelMoved(MouseWheelEvent e) {
        int rotation = e.getWheelRotation();
        //if      (rotation>0) {mouseWheelUp();}
        //else if (rotation<0) {mouseWheelDown();}
    }

    Image loadImage(String filename) {
        try {
            Image i = java.awt.Toolkit.getDefaultToolkit().getImage(filename);
            MediaTracker load_tracker = new MediaTracker(jframe);
            load_tracker.addImage(i, 0);
            load_tracker.waitForID(0);
            if (load_tracker.isErrorID(0)) {i=null;}
            return i;
        }
        catch (Exception ex) {throw new IllegalStateException("Unable to load Image: "+filename);}  // this is not printing anything?! debug this
    }

    private void log(String s) {System.out.println(s);}

}