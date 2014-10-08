'Visual Basic                                        ' VER: title
'Visual Basic .NET Express                           ' VER: download
'http://www.microsoft.com/express/vb/Default.aspx    ' VER: download
'www.dreamspark.com
'http://www.homeandlearn.co.uk/                      ' VER: help
'http://www.functionx.com/vbnet/                     ' VER: help
Imports System.Collections.Generic

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
        Dim line_to_write as String = "Append to end of file"                   ' VER: file_write
        Dim f As New System.IO.StreamWriter("out.txt", False)                   ' VER: file_write
        f.WriteLine(line_to_write)                                              ' VER: file_write
        f.Close()                                                               ' VER: file_write
        
        'Alternate
        FileOpen(1, "out.txt", OpenMode.Append)
        WriteLine(1, line_to_write.ToCharArray)
        FileClose(1)
    End Sub
    
    Sub file_read()
        Dim line_count as Integer = 0                                           ' VER: file_read
        FileOpen(1, "in.txt", OpenMode.Input)                                   ' VER: file_read
        Do While Not EOF(1)                                                     ' VER: file_read
          Console.WriteLine("Line " + line_count + ": " + LineInput(1))         ' VER: file_read
          line_count += 1                                                       ' VER: file_read
        Loop                                                                    ' VER: file_read
        FileClose(1)                                                            ' VER: file_read
    End Sub
    
    Sub file_read_alternate()
        'Alternate way of reading file                                          ' VER: file_read
        Dim line_count as Integer = 0                                           ' VER: file_read
        Dim file As New System.IO.StreamReader("in.txt")                        ' VER: file_read
        Do While file.Peek() <> -1                                              ' VER: file_read
          Console.WriteLine("Line " + line_count + ": " + file.ReadLine())      ' VER: file_read
          line_count += 1                                                       ' VER: file_read
        Loop                                                                    ' VER: file_read
        file.Close()                                                            ' VER: file_read
    End Sub
    
    Sub string_concatination()
        Dim fullname, forename, surname as String
        fullname = forename & " " & surname         ' VER: string_concatination
    End Sub
    
    Sub convert_string_to_interger_and_back()
        Dim sum as Integer = val("5") + val(Console.ReadLine())     ' VER: convert_string_to_interger_and_back
        Console.WriteLine(CStr(sum))                                ' VER: convert_string_to_interger_and_back
    End Sub
    
    Sub convert_double_to_string_and_back()
        'CInt
        'Cdbl
        'todo
    End Sub

    Sub sayHello()                      ' VER: function
        Console.WriteLine("Hello")      ' VER: function
        Console.WriteLine("Goodbye")    ' VER: function
    End Sub                             ' VER: function

    Sub _function()
        sayHello()
    End Sub

    Function biggest(ByVal a as Integer, ByVal b as Integer) As Integer    ' VER: function_with_return_value
        If a > b Then                                                       ' VER: function_with_return_value
            biggest = a                                                     ' VER: function_with_return_value
        Else                                                                ' VER: function_with_return_value
            biggest = b                                                     ' VER: function_with_return_value
        End if                                                              ' VER: function_with_return_value
    End Function

    Sub function_with_return_value()
        'Dim biggest, a, b as Integer
        biggest(0, 1)
    End Sub

    Sub addMonkeyByRef(ByRef name as String)  'Pass a reference to name         ' VER: function_with_params_by_reference
        name = name + " is a monkey"                                            ' VER: function_with_params_by_reference
    End Sub                                                                     ' VER: function_with_params_by_reference
    
    Sub function_with_params_by_reference()
        Dim text as String = "Brian"                                            ' VER: function_with_params_by_reference
        addMonkeyByRef(text)                                                    ' VER: function_with_params_by_reference
        Console.WriteLine(text) 'print 'Brian is a monkey'                      ' VER: function_with_params_by_reference
    End Sub

    Sub addMonkeyByVal(ByVal name as String)  'use a Copy the text name         ' VER: function_with_params_by_value
      name = name + " is a monkey"                                              ' VER: function_with_params_by_value
    End Sub                                                                     ' VER: function_with_params_by_value
    
    Sub function_with_params_by_value()
        Dim text as String = "Brian"                                            ' VER: function_with_params_by_value
        addMonkeyByVal(text)                                                    ' VER: function_with_params_by_value
        Console.WriteLine(text) 'Brian .. is not a monkey!                      ' VER: function_with_params_by_value
    End Sub
    
    Sub define_fixed_array()
        Dim names(3) As String                              ' VER: define_fixed_array
        names(0) = "Bob"                                    ' VER: define_fixed_array
        names(1) = "Foo"                                    ' VER: define_fixed_array
        names(2) = "Rah"                                    ' VER: define_fixed_array
        For Each name As String In names                    ' VER: define_fixed_array
          Console.WriteLine(name)                           ' VER: define_fixed_array
        Next                                                ' VER: define_fixed_array
        Console.WriteLine("array size is " + names.Length)  ' VER: define_fixed_array
    End Sub
    
    Sub define_2d_arrays()
        Dim grid(10,10) as Integer  ' VER: define_2d_arrays
        grid(5,5) = 1               ' VER: define_2d_arrays
    End Sub
    
    Sub linked_list()
        Dim list As New LinkedList(Of String)           ' VER: linked_list
        list.AddLast("Bill")                            ' VER: linked_list
        list.AddLast("Ben")                             ' VER: linked_list
        list.AddLast("Bob")                             ' VER: linked_list
        list.Remove("Ben")                              ' VER: linked_list
        list.RemoveLast()                               ' VER: linked_list
        list.AddFirst("Kim")                            ' VER: linked_list
        For Each item as String In list                 ' VER: linked_list
          Console.WriteLine(item)                       ' VER: linked_list
        Next                                            ' VER: linked_list
        Console.WriteLine("list size is " + list.Count) ' VER: linked_list
        
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
        Dim dict As New Dictionary(Of String, String)
        dict.Add("Joe", 77)
        dict.Add("Jane", 51)
        For Each key as String In dict.Keys
          Console.WriteLine("Key: " + key + " Value: " + dict(key))
        Next
    End Sub
    
    Sub error_handling()
        Try                                 ' VER: error_handling
          'thing that may error             ' VER: error_handling
        Catch ex As Exception               ' VER: error_handling
          'what to do if things go wrong    ' VER: error_handling
        End Try                             ' VER: error_handling
    End Sub
    
    Sub split_strings()
        Const csv_line_test as String = "Jane,09/09/1989,Female,Blue"   ' VER: split_strings
        Dim line_split As String() = csv_line_test.Split(",")                       ' VER: split_strings
    End Sub
    
    Sub random_number()
        Dim random_generator As Random = New Random             ' VER: random_number
        Dim new_num As Integer = random_generator.Next(0, 100)  ' VER: random_number
        'Dim new_fraction As Double = random_generator.         ' VER: random_number
    End Sub
    
    Sub switch()
        Dim nCPU as Integer
        Select Case nCPU
            Case 0
                'No CPU!
            Case 1
                'Single CPU
            Case 2
                'Dual CPU machine
            Case 4
                'Quad CPU machine
            Case 3, 5 To 8
                '3, 5, 6, 7, 8 CPU's
            Case Else
                'Something more than 8
        End Select
    End Sub

    Class Star                      ' VER: _class
        Public x As Integer         ' VER: _class
        Public y As Integer         ' VER: _class
        Public speed As Integer     ' VER: _class
    End Class                       ' VER: _class

    Sub _class()
        Dim s as Star = New Star()  ' VER: _class
        s.x = 100                   ' VER: _class
    End Sub
    
    Sub read_csv_into_array_of_classs()
    'Module Module1
      'Class Student
      '    Public forname As String
      '    Public surname As String
      '    Public dob As Date
      'End Class
    
      'Const filename As String = "c:\test.csv"
      'Dim students As New LinkedList(Of Student)
    
        'Sub Main()
       '   Dim objReader As New System.IO.StreamReader(filename)
       '   Do While objReader.Peek() <> -1
       '       Dim line_split() = objReader.ReadLine().Split(",")
       '       Dim new_student As Student = New Student()
       '       new_student.forname = line_split(0)
       '       new_student.surname = line_split(1)
       '       new_student.dob = Date.Parse(line_split(2))
       '       students.AddLast(new_student)
       '   Loop
       '   objReader.Close()
       '   Console.WriteLine("Loaded "&students.Count&" students")
        'End Sub
    'End Module
    End Sub
    
    Sub sleep()
        Threading.Thread.Sleep(1000)    ' VER: sleep
    End Sub
    
    '---------------------------------------------------------------------------
    
    Sub Main()
        hello_world()
        function_with_params_by_reference()
        function_with_params_by_value()
    End Sub

End Module