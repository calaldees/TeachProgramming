Public Class Form1
    Dim screen As Bitmap
    Dim background_color = Color.FromArgb(0, 0, 0)

    Dim player1_x_pos As Integer  ' Ver: 2
    Dim player1_y_pos As Integer  ' Ver: 2
    Dim player1_x_move As Integer ' Ver: 2
    Dim player1_y_move As Integer ' Ver: 2
    Dim player1_color = Color.FromArgb(255, 255, 0) ' Ver: 2
    ' Ver: 2
    Dim player2_x_pos As Integer  ' Ver: 5
    Dim player2_y_pos As Integer  ' Ver: 5
    Dim player2_x_move As Integer ' Ver: 5
    Dim player2_y_move As Integer ' Ver: 5
    Dim player2_color = Color.FromArgb(255, 0, 0) ' Ver: 5
    ' Ver: 5
    Dim player1_score As Integer ' Ver: 6
    Dim player2_score As Integer ' Ver: 6
    ' Ver: 6
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
        player1_x_pos = 100                 ' Ver: 2
        player1_y_pos = 100                 ' Ver: 2
        player1_x_move = 1                  ' Ver: 2
        player1_y_move = 0                  ' Ver: 2
        player2_x_pos = screen.Width - 100  ' Ver: 5
        player2_y_pos = screen.Height - 100 ' Ver: 5
        player2_x_move = -1                 ' Ver: 5
        player2_y_move = 0                  ' Ver: 5
        ' Ver: 2
        Graphics.FromImage(screen).FillRectangle(New SolidBrush(background_color), 0, 0, screen.Width, screen.Height)
        Timer1.Start()
    End Sub

    Private Sub Timer1_Tick(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Timer1.Tick
        Dim g = Graphics.FromImage(screen)
        Dim pixel As Color ' Ver: 4

        player1_x_pos = player1_x_pos + player1_x_move ' Ver: 2
        player1_y_pos = player1_y_pos + player1_y_move ' Ver: 2
        player2_x_pos = player2_x_pos + player2_x_move ' Ver: 5
        player2_y_pos = player2_y_pos + player2_y_move ' Ver: 5
        ' Ver: 2
        Try                                                           ' Ver: 4
            pixel = screen.GetPixel(player1_x_pos, player1_y_pos)     ' Ver: 4
        Catch ex As Exception                                         ' Ver: 4
            pixel = Color.White                                       ' Ver: 4
        End Try                                                       ' Ver: 4
        If Not background_color.Equals(pixel) Then                    ' Ver: 4
            Timer1.Stop()                                             ' Ver: 6
            player2_score = player2_score + 1                         ' Ver: 6
            MsgBox("Player 1 Died " + player1_score.ToString)         ' Ver: 6
            reset()                                                   ' Ver: 4
        End If                                                        ' Ver: 4
        ' Ver: 4
        Try                                                           ' Ver: 5
            pixel = screen.GetPixel(player2_x_pos, player2_y_pos)     ' Ver: 5
        Catch ex As Exception                                         ' Ver: 5
            pixel = Color.White                                       ' Ver: 5
        End Try                                                       ' Ver: 5
        If Not background_color.Equals(pixel) Then                    ' Ver: 5
            Timer1.Stop()                                             ' Ver: 6
            player1_score = player1_score + 1                         ' Ver: 6
            MsgBox("Player 2 Died " + player2_score.ToString)         ' Ver: 6
            reset()                                                   ' Ver: 5
        End If                                                        ' Ver: 5
        ' Ver: 5
        screen.SetPixel(player1_x_pos, player1_y_pos, player1_color) ' Ver: 2
        screen.SetPixel(player2_x_pos, player2_y_pos, player2_color) ' Ver: 5
        ' Ver: 2
        If player1_score = 5 Or player2_score = 5 Then ' Ver: 6
            Me.Close()                                 ' Ver: 6
        End If                                         ' Ver: 6
        PictureBox1.Refresh()
    End Sub

    Private Sub Form1_KeyDown(ByVal sender As Object, ByVal e As System.Windows.Forms.KeyEventArgs) Handles Me.KeyDown ' Ver: 3
        If e.KeyCode = Keys.Up Then    ' Ver: 3
            player1_x_move = 0         ' Ver: 3
            player1_y_move = -1        ' Ver: 3
        End If                         ' Ver: 3
        If e.KeyCode = Keys.Down Then  ' Ver: 3
            player1_x_move = 0         ' Ver: 3
            player1_y_move = 1         ' Ver: 3
        End If                         ' Ver: 3
        If e.KeyCode = Keys.Left Then  ' Ver: 3
            player1_x_move = -1        ' Ver: 3
            player1_y_move = 0         ' Ver: 3
        End If                         ' Ver: 3
        If e.KeyCode = Keys.Right Then ' Ver: 3
            player1_x_move = 1         ' Ver: 3
            player1_y_move = 0         ' Ver: 3
        End If                         ' Ver: 3
        ' Ver: 5
        If e.KeyCode = Keys.W Then     ' Ver: 5
            player2_x_move = 0         ' Ver: 5
            player2_y_move = -1        ' Ver: 5
        End If ' Ver: 5
        If e.KeyCode = Keys.S Then     ' Ver: 5
            player2_x_move = 0         ' Ver: 5
            player2_y_move = 1         ' Ver: 5
        End If                         ' Ver: 5
        If e.KeyCode = Keys.A Then     ' Ver: 5
            player2_x_move = -1        ' Ver: 5
            player2_y_move = 0         ' Ver: 5
        End If                         ' Ver: 5
        If e.KeyCode = Keys.D Then     ' Ver: 5
            player2_x_move = 1         ' Ver: 5
            player2_y_move = 0         ' Ver: 5
        End If                         ' Ver: 5
        ' Ver: 3
    End Sub                            ' Ver: 3
    ' Ver: 3
End Class