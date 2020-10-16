
```vb
Public Class Form1

    Const LOOKUP_HEX() As String = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}
    Const LOOKUP_GREY() As String = {
        "0000",
        "0001",
        "0011",
        "0010",
        "0110",
        "0111",
        "0101",
        "0100",
        "1100",
        "1101",
        "1111",
        "1110",
        "1010",
        "1011",
        "1001",
        "1000",
    }


    Private Sub btnDec2Hex_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnDec2Hex.Click
        lbOutput.Text = ""
        Dim denary As Integer = Val(TextBox1.Text)
        Dim remainder As Integer
        While denary > 0
            Debug.Print("Denary=" & denary)
            remainder = denary Mod 16
            Debug.Print("Remainder=" & remainder)
            Dim lookup As String = lookupHex(remainder)
            Debug.Print("Lookup=" & lookup)
            appendOutput(lookup)
            denary = (denary - remainder) / 16
        End While
    End Sub

    Private Sub btnDec2Grey_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnDec2Grey.Click
        Dim denary = Val(TextBox1.Text)
        If (denary >= 0 And denary < 16) Then
            lbOutput.Text = grey_code_lookup(denary)
        Else
            lbOutput.Text = "Out of grey lookup range"
        End If
    End Sub

    Private Sub appendOutput(ByVal c As String)
        lbOutput.Text = c & lbOutput.Text
    End Sub

    Private Function lookupHex(ByVal i As Integer) As String
        lookupHex = hex_lookup(i)
    End Function



    Private Sub btnDec2Bin_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnDec2Bin.Click
        lbOutput.Text = ""
        Dim denary As Integer = Val(TextBox1.Text)
        Dim remainder As Integer
        While denary > 0
            remainder = denary Mod 2
            appendOutput(remainder)
            denary = (denary - remainder) / 2
        End While

    End Sub

    Private Sub btnHex2Dec_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnHex2Dec.Click
        Dim pos As Integer = TextBox1.TextLength - 1
        Dim power As Integer = 1
        Dim denary As Integer
        While (pos >= 0)
            Dim c As String = TextBox1.Text.Chars(pos)
            Debug.Print("Character=" + c + " at possition=" & pos)
            Dim n As Integer = 0
            Select Case c
                Case "[0..9]"
                    n = Val(c)
                Case "A"
                    n = 10
                Case "B"
                    n = 11
                Case "C"
                    n = 12
                Case "D"
                    n = 13
                Case "E"
                    n = 14
                Case "F"
                    n = 15
            End Select
            Debug.Print("N=" & n & " Pow=" & power)
            denary = denary + (n * power)
            Debug.Print("Denary=" & denary)
            power = power * 16
            pos = pos - 1
        End While
        lbOutput.Text = denary
    End Sub
End Class
```