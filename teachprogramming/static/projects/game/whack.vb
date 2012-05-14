Public Class Hopper

    Dim background As Bitmap
    Dim shape As Rectangle = New Rectangle(0, 0, 50, 50)
    Dim r As Random = New Random()

    Private Sub Hopper_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load
        background = New Bitmap(PictureBox1.Width, PictureBox1.Height)
        PictureBox1.Image = background
        Timer1.Start()
    End Sub

    Private Sub Timer1_Tick(ByVal sender As Object, ByVal e As System.EventArgs) Handles Timer1.Tick
        shape.X = r.Next(Me.Width - shape.Width)
        shape.Y = r.Next(Me.Height - shape.Height)
        Graphics.FromImage(background).FillRectangle(Brushes.Black, 0, 0, PictureBox1.Width, PictureBox1.Height)
        Graphics.FromImage(background).FillRectangle(Brushes.Yellow, shape)
        PictureBox1.Refresh()
    End Sub

    Private Sub PictureBox1_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles PictureBox1.Click
        MsgBox(e.ToString)
        'if shape.Contains()
    End Sub
End Class
