Public Class Form1

    Dim background As Bitmap
    Dim r As Random = New Random()
    Dim stars(100) As Star

    Class Star
        Public xpos As Integer
        Public ypos As Integer
        Public speed As Integer
    End Class

    Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load
        resize_background()
        Timer1.Start()
    End Sub

    Private Sub Timer1_Tick(ByVal sender As Object, ByVal e As System.EventArgs) Handles Timer1.Tick
        Graphics.FromImage(background).FillRectangle(Brushes.Black, 0, 0, PictureBox1.Width, PictureBox1.Height)
        For Each s As Star In stars
            s.xpos = s.xpos + s.speed
            If s.xpos > PictureBox1.Width Then
                s.xpos = 0
                s.ypos = r.Next(0, PictureBox1.Height - 1)
            End If
            Try
                background.SetPixel(s.xpos, s.ypos, Color.White)
            Catch ex As Exception
            End Try

        Next s
        PictureBox1.Refresh()
    End Sub

    Private Sub Form1_Resize(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Resize
        resize_background()
    End Sub

    Sub resize_background()
        PictureBox1.Width = Me.Width
        PictureBox1.Height = Me.Height
        background = New Bitmap(PictureBox1.Width, PictureBox1.Height)
        PictureBox1.Image = background

        For i As Integer = 0 To 100
            stars(i) = New Star
        Next
        For Each s As Star In stars
            s.xpos = r.Next(1, PictureBox1.Width - 1)
            s.ypos = r.Next(1, PictureBox1.Height - 1)
            s.speed = r.Next(1, 9)
        Next s
    End Sub
End Class
