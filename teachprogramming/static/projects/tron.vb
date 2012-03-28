Public Class Form1

    Dim background As Bitmap
    Dim background_color As Color

    Dim xpos_1 As Integer
    Dim ypos_1 As Integer
    Dim xdirection_1 As Integer
    Dim ydirection_1 As Integer

    Dim xpos_2 As Integer
    Dim ypos_2 As Integer
    Dim xdirection_2 As Integer
    Dim ydirection_2 As Integer

    Dim score_1 As Integer
    Dim score_2 As Integer

    Public Sub New()
        InitializeComponent()
        reset()
    End Sub

    Sub reset()
        xpos_1 = 50
        ypos_1 = 50
        xdirection_1 = 1
        ydirection_1 = 0

        xpos_2 = PictureBox1.Width - 50
        ypos_2 = PictureBox1.Width - 50
        xdirection_2 = -1
        ydirection_2 = 0

        setsize()
        Timer1.Start()
    End Sub

    Sub setsize()
        PictureBox1.Width = Me.Width
        PictureBox1.Height = Me.Height
        background = New Bitmap(PictureBox1.Width, PictureBox1.Height)
        PictureBox1.Image = background
        background_color = background.GetPixel(0, 0)
    End Sub

    Private Sub Timer1_Tick(ByVal sender As Object, ByVal e As System.EventArgs) Handles Timer1.Tick
        Dim c As Color

        '---------------------Player 1--------------------------
        xpos_1 = xpos_1 + xdirection_1
        ypos_1 = ypos_1 + ydirection_1
        Try
            c = background.GetPixel(xpos_1, ypos_1)
        Catch ex As Exception
            'do nothing
        End Try
        If background_color.Equals(c) Then
            background.SetPixel(xpos_1, ypos_1, Color.Blue)
        Else
            Timer1.Stop()
            score_2 = score_2 + 1
            MsgBox("Player 1 Died " + score_1.ToString)
            reset()
        End If


        '---------------------Player 2--------------------------
        xpos_2 = xpos_2 + xdirection_2
        ypos_2 = ypos_2 + ydirection_2
        Try
            c = background.GetPixel(xpos_2, ypos_2)
        Catch ex As Exception
            'do nothing
        End Try

        If background_color.Equals(c) Then
            background.SetPixel(xpos_2, ypos_2, Color.Red)
        Else
            Timer1.Stop()
            score_1 = score_1 + 1
            MsgBox("Player 2 Died " + score_1.ToString)
            reset()
        End If

        PictureBox1.Refresh()
    End Sub

    Private Sub Form1_KeyDown(ByVal sender As Object, ByVal e As System.Windows.Forms.KeyEventArgs) Handles Me.KeyDown
        If e.KeyCode = Keys.Up Then
            xdirection_1 = 0
            ydirection_1 = -1
        End If
        If e.KeyCode = Keys.Down Then
            xdirection_1 = 0
            ydirection_1 = 1
        End If
        If e.KeyCode = Keys.Left Then
            xdirection_1 = -1
            ydirection_1 = 0
        End If
        If e.KeyCode = Keys.Right Then
            xdirection_1 = 1
            ydirection_1 = 0
        End If

        If e.KeyCode = Keys.W Then
            xdirection_2 = 0
            ydirection_2 = -1
        End If
        If e.KeyCode = Keys.S Then
            xdirection_2 = 0
            ydirection_2 = 1
        End If
        If e.KeyCode = Keys.A Then
            xdirection_2 = -1
            ydirection_2 = 0
        End If
        If e.KeyCode = Keys.D Then
            xdirection_2 = 1
            ydirection_2 = 0
        End If
    End Sub

    Private Sub Form1_ResizeEnd(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.ResizeEnd
        reset()
    End Sub
End Class