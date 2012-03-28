Public Class Gravity

    Class Mass
        Public x As Single
        Public y As Single
        Public x_vel As Single = 0
        Public y_vel As Single = 0
        Public size As Integer
    End Class

    Private Const max_size As Integer = 30
    Dim r As Random = New Random()
    Dim blocks(50) As Mass
    Dim background As Bitmap
    Dim background_color As Color

    Dim score As Integer

    Dim px As Integer
    Dim py As Integer

    Sub reset()
        px = PictureBox1.Width / 2
        py = PictureBox1.Height / 2
        For i As Integer = 0 To blocks.Length - 1
            Dim m As Mass = New Mass()
            m.size = r.Next(0, max_size) + 5
            m.x = r.NextDouble() * (PictureBox1.Width  - m.size())
            m.y = r.NextDouble() * (PictureBox1.Height - m.size())
            blocks(i) = m
        Next
        Timer1.Start()
        score = 0
    End Sub

    Private Sub Timer1_Tick(ByVal sender As Object, ByVal e As System.EventArgs) Handles Timer1.Tick
        score += 1
        Graphics.FromImage(background).FillRectangle(Brushes.Black, 0, 0, PictureBox1.Width, PictureBox1.Height)
        For Each m As Mass In blocks
            If m.x < 0 Or (m.x + m.size) > PictureBox1.Width Then m.x_vel = -(m.x_vel / 3)
            If m.y < 0 Or (m.y + m.size) > PictureBox1.Height Then m.y_vel = -(m.y_vel / 3)
            m.x_vel += -(m.x - px) / m.size / 500
            m.y_vel += -(m.y - py) / m.size / 500
            m.x += m.x_vel
            m.y += m.y_vel
            Graphics.FromImage(background).FillRectangle(Brushes.Yellow, m.x, m.y, m.size, m.size)
        Next m

        If Not background_color.Equals(background.GetPixel(px, py)) Then
            Timer1.Stop()
            MsgBox("score=" + score.ToString)
            reset()
        Else
            Graphics.FromImage(background).FillRectangle(Brushes.White, px - 3, py - 3, 6, 6)
            PictureBox1.Refresh()
        End If

    End Sub


    Private Sub Gravity_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load
        background = New Bitmap(PictureBox1.Width, PictureBox1.Height)
        PictureBox1.Image = background
        background.SetPixel(0, 0, Color.Black)
        background_color = background.GetPixel(0, 0)
        reset()
    End Sub


    Private Sub PictureBox1_MouseMove(ByVal sender As Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles PictureBox1.MouseMove
        px = e.X
        py = e.Y
    End Sub
End Class
