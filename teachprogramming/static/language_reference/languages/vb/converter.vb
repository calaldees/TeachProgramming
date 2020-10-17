Imports System.Collections.Generic  ' required for Dictionary


Module VisualBasic

    Function Dec2Bin(ByVal denary as Integer) As String
        Dim output As String = ""
        While denary > 0
            Const remainder As Integer = denary Mod 2
            output = remainder & output
            denary = (denary - remainder) / 2
        End While
        Dec2Bin = output
    End Function

    Dim LOOKUP_INTEGER_TO_HEX() as String = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}
    Function Dec2Hex(ByVal denary as Integer) As String
        Dim output as String = ""
        While denary > 0
            Const remainder As Integer = denary Mod 16
            output = LOOKUP_INTEGER_TO_HEX(remainder) & output
            denary = (denary - remainder) / 16
        End While
        Dec2Hex = output
    End Function

    Dim LOOKUP_GREY() as String = {
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
        "1000"
    }
    Function Dec2Grey(ByVal denary as Integer) As String
        If (denary >= 0 And denary < 16) Then
            Dec2Grey = LOOKUP_GREY(denary)
        Else
            Dec2Grey = "Out of grey lookup range"
        End If
    End Function

    ' dicts cant be set at compile time in vb<10
    ' https://stackoverflow.com/questions/3771922/add-keys-values-to-dictionary-at-declaration
    Dim LOOKUP_HEX_TO_INTEGER = New Dictionary(Of String, Integer) 'From {{ "Test1", 1 }, { "Test1", 2}}
    Function Hex2Dec(ByRef s As String) as Integer
        Dim dec as Integer = 0
        For i As Integer = 0 To s.Length-1
            dec = dec + (LOOKUP_HEX_TO_INTEGER(s(s.Length-1-i)) * 16 ^ i)
        Next
        Hex2Dec = dec
    End Function


    Sub Main()
        ' Populate LOOKUP_HEX_TO_INTEGER at runtime as dicts cant be set at compile-time in vb<10
        For i As Integer = 0 to LOOKUP_INTEGER_TO_HEX.Length-1
            LOOKUP_HEX_TO_INTEGER(LOOKUP_INTEGER_TO_HEX(i)) = i
        Next

        Console.WriteLine("Hello " + Dec2Bin(9))
        Console.WriteLine("Hello " + Dec2Hex(23487))
        Console.WriteLine("Hello " + Hex2Dec("5BBF").toString())
        Console.WriteLine("Hello " + Hex2Dec("101").toString())
    End Sub
End Module
