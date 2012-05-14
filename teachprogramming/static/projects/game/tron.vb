Public Class Form1
    Dim screen As Bitmap
    Dim background_color = Color.FromArgb(0, 0, 0)

    Dim player1_x_pos As Integer  ' VER: line
    Dim player1_y_pos As Integer  ' VER: line
    Dim player1_x_move As Integer ' VER: line
    Dim player1_y_move As Integer ' VER: line
    Dim player1_color = Color.FromArgb(255, 255, 0) ' VER: line
    ' VER: line
    Dim player2_x_pos As Integer  ' VER: player2
    Dim player2_y_pos As Integer  ' VER: player2
    Dim player2_x_move As Integer ' VER: player2
    Dim player2_y_move As Integer ' VER: player2
    Dim player2_color = Color.FromArgb(255, 0, 0) ' VER: player2
    ' VER: player2
    Dim player1_score As Integer ' VER: score
    Dim player2_score As Integer ' VER: score
    ' VER: score
    Public Sub New()
        InitializeComponent()
        Timer1.Interval = Int(1000 / 60)
        Me.MaximumSize = New System.Drawing.Size(640, 480)
        Me.MinimumSize = Me.MaximumSize
        Me.PictureBox1.Size = Me.MaximumSize
        screen = New Bitmap(PictureBox1.Width, PictureBox1.Height)
        PictureBox1.Image = screen
        reset()
    End Sub

    Sub reset()
        player1_x_pos = 100                 ' VER: line
        player1_y_pos = 100                 ' VER: line
        player1_x_move = 1                  ' VER: line
        player1_y_move = 0                  ' VER: line
        player2_x_pos = screen.Width - 100  ' VER: player2
        player2_y_pos = screen.Height - 100 ' VER: player2
        player2_x_move = -1                 ' VER: player2
        player2_y_move = 0                  ' VER: player2
        ' VER: line
        Graphics.FromImage(screen).FillRectangle(New SolidBrush(background_color), 0, 0, screen.Width, screen.Height)
        Timer1.Start()
    End Sub

    Private Sub Timer1_Tick(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Timer1.Tick
        Dim g = Graphics.FromImage(screen)
        Dim pixel As Color ' VER: colide

        player1_x_pos = player1_x_pos + player1_x_move ' VER: line
        player1_y_pos = player1_y_pos + player1_y_move ' VER: line
        player2_x_pos = player2_x_pos + player2_x_move ' VER: player2
        player2_y_pos = player2_y_pos + player2_y_move ' VER: player2
        ' VER: line
        Try                                                           ' VER: colide
            pixel = screen.GetPixel(player1_x_pos, player1_y_pos)     ' VER: colide
        Catch ex As Exception                                         ' VER: colide
            pixel = Color.White                                       ' VER: colide
        End Try                                                       ' VER: colide
        If Not background_color.Equals(pixel) Then                    ' VER: colide
            Timer1.Stop()                                             ' VER: score
            player2_score = player2_score + 1                         ' VER: score
            MsgBox("Player 1 Died " + player1_score.ToString)         ' VER: score
            reset()                                                   ' VER: colide
        End If                                                        ' VER: colide
        ' VER: colide
        Try                                                           ' VER: player2
            pixel = screen.GetPixel(player2_x_pos, player2_y_pos)     ' VER: player2
        Catch ex As Exception                                         ' VER: player2
            pixel = Color.White                                       ' VER: player2
        End Try                                                       ' VER: player2
        If Not background_color.Equals(pixel) Then                    ' VER: player2
            Timer1.Stop()                                             ' VER: score
            player1_score = player1_score + 1                         ' VER: score
            MsgBox("Player 2 Died " + player2_score.ToString)         ' VER: score
            reset()                                                   ' VER: player2
        End If                                                        ' VER: player2
        ' VER: player2
        screen.SetPixel(player1_x_pos, player1_y_pos, player1_color) ' VER: line
        screen.SetPixel(player2_x_pos, player2_y_pos, player2_color) ' VER: player2
        ' VER: line
        If player1_score = 5 Or player2_score = 5 Then ' VER: score
            Me.Close()                                 ' VER: score
        End If                                         ' VER: score
        PictureBox1.Refresh()
    End Sub

    Private Sub Form1_KeyDown(ByVal sender As Object, ByVal e As System.Windows.Forms.KeyEventArgs) Handles Me.KeyDown ' VER: input
        If e.KeyCode = Keys.Up Then    ' VER: input
            player1_x_move = 0         ' VER: input
            player1_y_move = -1        ' VER: input
        End If                         ' VER: input
        If e.KeyCode = Keys.Down Then  ' VER: input
            player1_x_move = 0         ' VER: input HIDE
            player1_y_move = 1         ' VER: input HIDE
        End If                         ' VER: input HIDE
        If e.KeyCode = Keys.Left Then  ' VER: input HIDE
            player1_x_move = -1        ' VER: input HIDE
            player1_y_move = 0         ' VER: input HIDE
        End If                         ' VER: input HIDE
        If e.KeyCode = Keys.Right Then ' VER: input HIDE
            player1_x_move = 1         ' VER: input HIDE
            player1_y_move = 0         ' VER: input HIDE
        End If                         ' VER: input HIDE
        ' VER: input
        If e.KeyCode = Keys.W Then     ' VER: player2
            player2_x_move = 0         ' VER: player2
            player2_y_move = -1        ' VER: player2
        End If ' VER: player2
        If e.KeyCode = Keys.S Then     ' VER: player2
            player2_x_move = 0         ' VER: player2 HIDE
            player2_y_move = 1         ' VER: player2 HIDE
        End If                         ' VER: player2 HIDE
        If e.KeyCode = Keys.A Then     ' VER: player2 HIDE
            player2_x_move = -1        ' VER: player2 HIDE
            player2_y_move = 0         ' VER: player2 HIDE
        End If                         ' VER: player2 HIDE
        If e.KeyCode = Keys.D Then     ' VER: player2 HIDE
            player2_x_move = 1         ' VER: player2 HIDE
            player2_y_move = 0         ' VER: player2 HIDE
        End If                         ' VER: player2 HIDE
        ' VER: player2
    End Sub                            ' VER: input
    ' VER: input
End Class