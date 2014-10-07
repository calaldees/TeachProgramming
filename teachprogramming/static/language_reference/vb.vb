'Visual Basic                                        ' VER: title
'Visual Basic .NET Express                           ' VER: download
'http://www.microsoft.com/express/vb/Default.aspx    ' VER: download
'www.dreamspark.com
'http://www.homeandlearn.co.uk/                      ' VER: help
'http://www.functionx.com/vbnet/                     ' VER: help

Module VisualBasic
    Sub hello_world()
    'Module Module1                             ' VER: hello_world
    '    Sub Main()                             ' VER: hello_world
            Console.WriteLine("Hello World")    ' VER: hello_world
    '    End Sub                                ' VER: hello_world
    'End Module                                 ' VER: hello_world
    End Sub

    Sub read_line_from_console()
        'Dim username as String               ' VER: read_line_from_console
        'username = Console.ReadLine()       ' VER: read_line_from_console
    End Sub
    
    Sub comment()
        'This is a comment      ' VER: comment
    End Sub

    Sub define_variables()    
        Dim count as Integer = 0            ' VER: define_variables
        Dim username as String = "Betty"    ' VER: define_variables
        Dim distance as Double = "3.14"     ' VER: define_variables
        Dim email_errors as Boolean = True  ' VER: define_variables
    End Sub
    
    Sub define_constants()
        Const GRAVITY As Double = 9.81      ' VER: define_constants
    End Sub
    
    Sub arithmetic()
        Dim xpos as Integer
        Dim distance as Double
        Dim quant as Integer = 0
        Dim total_cost as Double
        Dim remainder as Integer
        Dim count as Integer
        Dim item_price as Double = 0

        xpos = xpos + 1                     ' VER: arithmetic
        distance = 3 / 4                    ' VER: arithmetic
        total_cost = item_price * quant     ' VER: arithmetic
        remainder = 14 mod 11               ' VER: arithmetic
        count += 1                          ' VER: arithmetic
    End Sub

    Sub if_statement()
        Dim count as Integer
        Dim username as String

        If count>=5 and username = "Jim" Then   ' VER: if_statement
          Console.WriteLine("Yes")              ' VER: if_statement
        Else If username = "admin"              ' VER: if_statement
          Console.WriteLine("Admin")            ' VER: if_statement
        Else                                    ' VER: if_statement
          Console.WriteLine("No")               ' VER: if_statement
        End If                                  ' VER: if_statement
    End Sub
    
    Sub for_loop()
        Dim username as String = "bob"              ' VER: for_loop
        For i As Integer = 0 To username.Length - 1 ' VER: for_loop
          Console.WriteLine(username.Chars(i))      ' VER: for_loop
        Next                                        ' VER: for_loop
    End Sub

    Sub while_loop()
        Dim count as Integer = 0                    ' VER: while_loop
        Do While count < 10                         ' VER: while_loop
          Console.WriteLine("Count is " + count)    ' VER: while_loop
          count = count + 2                         ' VER: while_loop
        Loop                                        ' VER: while_loop
    End Sub

    Sub until_loop()
        Dim word as String = "gibber"   ' VER: until_loop
        Do                              ' VER: until_loop
          word = word + word            ' VER: until_loop
        Loop Until word.Length < 10     ' VER: until_loop
    End Sub
    
    Sub for_each_loop()
        Dim names() as String = {"Bob","Ben","Bill","Borris","Bin"} ' VER: for_each_loop
        For Each name As String In names                            ' VER: for_each_loop
          Console.WriteLine(name)                                   ' VER: for_each_loop
        Next name                                                   ' VER: for_each_loop
    End Sub
    
    Sub file_write()
        Dim line_to_write as String = "Append to end of file"
        Dim f As New System.IO.StreamWriter("out.txt", False)
        f.WriteLine(line_to_write)
        f.Close()
        
        'Alternate
        FileOpen(1, "out.txt", OpenMode.Append)
        WriteLine(1, line_to_write.ToCharArray)
        FileClose(1)
    End Sub
    
    Sub file_read()
        Dim line_count as Integer = 0
        FileOpen(1, "in.txt", OpenMode.Input)
        Do While Not EOF(1)
          Console.WriteLine("Line " + line_count + ": " + LineInput(1))
          line_count += 1
        Loop
        FileClose(1)
    End Sub
    
    Sub file_read_alternate()
        'Alternate way of reading file
        Dim line_count as Integer = 0
        Dim file As New System.IO.StreamReader("in.txt")
        Do While file.Peek() <> -1
          Console.WriteLine("Line " + line_count + ": " + file.ReadLine())
          line_count += 1
        Loop
        file.Close()
    End Sub
    
    Sub string_concatination()
        Dim fullname, forename, surname as String
        fullname = forename & " " & surname
    End Sub
    
    Sub convert_string_to_interger_and_back()
        Dim sum as Integer = val("5") + val(Console.ReadLine())
        Console.WriteLine(CStr(sum))
    End Sub
    
    Sub convert_double_to_string_and_back()
        'CInt
        'Cdbl
        'todo
    End Sub
    
    Sub _function()
        'Sub sayHello()
          Console.WriteLine("Hello")
          Console.WriteLine("Goodbye")
        'End Sub
    End Sub
    
    Sub function_with_return_value()
        Dim biggest, a, b as Integer
        'Function biggest(ByVal a as Integer, ByVal b as Integer) As Integer    ' VER: function_with_return_value
            If a > b Then                                                       ' VER: function_with_return_value
                biggest = a                                                     ' VER: function_with_return_value
            Else                                                                ' VER: function_with_return_value
                biggest = b                                                     ' VER: function_with_return_value
            End if                                                              ' VER: function_with_return_value
        'End Function
    End Sub
    
    Sub function_with_params_by_reference()
        'Sub addMonkey(ByRef name as String)  'Pass a reference to name
        '  name = name + " is a monkey"
        'End Sub
        'Console.WriteLine(addMonkey("Brian")) 'Brian is a monkey
    End Sub
    
    Sub function_with_params_by_value()
        'Sub addMonkey(ByVal name as String)  'use a Copy the text name
        '  name = name + " is a monkey"
        'End Sub
        'Console.WriteLine(addMonkey("Brian")) 'Brian .. is not a monkey!
    End Sub
    
    Sub define_fixed_array()
        Dim names(3) As String
        names(0) = "Bob"
        names(1) = "Foo"
        names(2) = "Rah"
        For Each name As String In names
          Console.WriteLine(name)
        Next
        Console.WriteLine("array size is " + names.Length)
    End Sub
    
    Sub define_2d_arrays()
        Dim grid(10,10) as Integer
        grid(5,5) = 1
    End Sub
    
    Sub linked_list()
        Dim list As New LinkedList(Of String)
        list.AddLast("Bill")
        list.AddLast("Ben")
        list.AddLast("Bob")
        list.Remove("Ben")
        list.RemoveLast()
        list.AddFirst("Kim")
        For Each item In list
          Console.WriteLine(item)
        Next
        Console.WriteLine("list size is " + list.Count)
        
        'Alternate – notes old redim way – more needed
        'ReDim Preserve ArrayName(LowerValue To HigherValue)
        'Dim dict As New Dictionary(Of String, String)
        'dict.Add("Joe", 77)
        'dict.Add("Jane", 51)
        'For Each key In dict.Keys
        '  Console.WriteLine("Key: " + key + " Value: " + dict(key))
        'Next
    End Sub
    
    Sub define_map()
    End Sub
    
    Sub error_handling()
    End Sub
    
    Sub split_strings()
    End Sub
    
    Sub random_number()
    End Sub
    
    Sub switch()
    End Sub
    
    Sub _class()
    End Sub
    
    Sub read_csv_into_array_of_classs()
    End Sub
    
    Sub sleep()
    End Sub
    
    '---------------------------------------------------------------------------
    
    Sub Main()
        hello_world()
    End Sub

End Module