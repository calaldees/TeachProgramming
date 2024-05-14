Public Class Form1

    Dim background As Bitmap

    Private Sub render_file(ByVal filename As String)
        Dim g As Graphics = Graphics.FromImage(background)
        Dim file As New System.IO.StreamReader(filename)
        Do While file.Peek() <> -1
            Dim s() As String = file.ReadLine().Split(",")
            Select Case s(0)
                Case "Rectangle"
                    Dim x As Integer = Val(s(1)) * background.Width
                    Dim y As Integer = Val(s(2)) * background.Height
                    Dim w As Integer = Val(s(3)) * background.Width
                    Dim h As Integer = Val(s(4)) * background.Height
                    g.FillRectangle(getColor(s(5)), x, y, w, h)
                Case "Circle"
                    Dim x As Integer = Val(s(1)) * background.Width
                    Dim y As Integer = Val(s(2)) * background.Height
                    Dim w As Integer = Val(s(3)) * background.Width
                    Dim h As Integer = Val(s(4)) * background.Height
                    g.FillEllipse(getColor(s(5)), x, y, w, h)
                Case "Line"
                    Dim x1 As Integer = Val(s(1)) * background.Width
                    Dim y1 As Integer = Val(s(2)) * background.Height
                    Dim x2 As Integer = Val(s(3)) * background.Width
                    Dim y2 As Integer = Val(s(4)) * background.Height
                    g.DrawLine(Pens.Black, x1, y1, x2, y2)
                Case "Bitmap"
                    Dim x As Integer = Val(s(1)) * background.Width
                    Dim y As Integer = Val(s(2)) * background.Height
                    Dim w As Integer = Val(s(3)) * background.Width
                    Dim h As Integer = Val(s(4)) * background.Height
                    Dim i As Image = Image.FromFile("C:\Temp\" + s(5))
                    g.DrawImage(i, x, y, w, h)
            End Select
        Loop
        file.Close()
        PictureBox1.Refresh()
    End Sub

    Private Function getColor(ByVal color_string As String) As Brush
        Select Case color_string.ToLower
            Case "red"
                getColor = Brushes.Red
            Case "yellow"
                getColor = Brushes.Yellow
            Case "green"
                getColor = Brushes.Green
            Case "blue"
                getColor = Brushes.Blue
            Case Else
                getColor = Brushes.Black
        End Select
    End Function

    Private Sub init_bitmap()
        PictureBox1.Width = Me.Width
        PictureBox1.Height = Me.Height
        background = New Bitmap(PictureBox1.Width, PictureBox1.Height)
        PictureBox1.Image = background
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        render_file("d:\vector_test.csv")
    End Sub

    Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load
        init_bitmap()
    End Sub

    Private Sub Form1_Paint(ByVal sender As Object, ByVal e As System.Windows.Forms.PaintEventArgs) Handles Me.Paint
        render_file("d:\vector_test.csv")
    End Sub

    Private Sub Form1_Resize(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Resize
        init_bitmap()
    End Sub


End Class
