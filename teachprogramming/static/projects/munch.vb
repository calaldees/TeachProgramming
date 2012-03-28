Public Class Form1

    'Dim image_smile As Image = Image.FromFile("smile.gif")
    'Dim image_brick As Image = Image.FromFile("brick.gif")

    Const grid_size As Integer = 20
    Dim grid(grid_size, grid_size) As Integer

    Dim x_pos = 0
    Dim y_pos = 0

    Private Sub Form1_KeyDown(ByVal sender As Object, ByVal e As System.Windows.Forms.KeyEventArgs) Handles Me.KeyDown
        grid(x_pos, y_pos) = 0
        If e.KeyCode = Keys.Up Then y_pos += -1
        If e.KeyCode = Keys.Down Then y_pos += 1
        If e.KeyCode = Keys.Left Then x_pos += -1
        If e.KeyCode = Keys.Right Then x_pos += 1
        grid(x_pos, y_pos) = 2
        Debug.Print("New X=" & x_pos & " Y=" & y_pos)
        Me.Refresh()
    End Sub

    Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load
        grid(1, 1) = 1
        grid(2, 2) = 1
        grid(3, 3) = 1
        grid(5, 8) = 1
        grid(9, 9) = 1
        grid(8, 8) = 1
        grid(1, 8) = 1
        grid(8, 7) = 1
        grid(2, 7) = 1
    End Sub


    Private Sub Form1_Paint(ByVal sender As Object, ByVal e As System.Windows.Forms.PaintEventArgs) Handles Me.Paint
        Dim g As Graphics = e.Graphics
        Dim x As Integer
        Dim y As Integer

        For y = 0 To grid_size
            For x = 0 To grid_size
                If grid(x, y) = 1 Then
                    'g.DrawImage(image_brick, x * grid_size, y * grid_size)
                    g.FillRectangle(Brushes.Chocolate, x * grid_size, y * grid_size, grid_size, grid_size)
                End If
                If grid(x, y) = 2 Then
                    'g.DrawImage(image_smile, x * grid_size, y * grid_size)
                    g.FillRectangle(Brushes.Crimson, x * grid_size, y * grid_size, grid_size, grid_size)
                End If
            Next
        Next
    End Sub



End Class
