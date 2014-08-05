'www.dreamspark.com
'Visual Studio 200?
'http://www.microsoft.com/express/vb/Default.aspx
'Visual Basic .NET Express
'http://www.homeandlearn.co.uk/
'http://www.functionx.com/vbnet/

Module Module1                              ' VER: hello_world
    Sub Main()                              ' VER: hello_world
        Console.WriteLine("Hello World")    ' VER: hello_world
    End Sub                                 ' VER: hello_world

    Sub read_line_from_console()
        username = Console.ReadLine()       ' VER: read_line_from_console
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
        xpos = xpos + 1                     ' VER: arithmetic
        distance = 3 / 4                    ' VER: arithmetic
        total_cost = item_price * quant     ' VER: arithmetic
        remainder = 14 mod 11               ' VER: arithmetic
        count += 1                          ' VER: arithmetic
    End Sub

    Sub if_statement()
        If count>=5 and username = "Jim" Then   ' VER: if_statement
          Console.WriteLine("Yes")              ' VER: if_statement
        Else If username = "admin"              ' VER: if_statement
          Console.WriteLine("Admin")            ' VER: if_statement
        Else                                    ' VER: if_statement
          Console.WriteLine("No")               ' VER: if_statement
        End If                                  ' VER: if_statement
    End Sub

<> or
For i As Integer = 0 To username.Length – 1
  Console.WriteLine(username.Chars(i))
Next
Dim count as Integer = 0;
Do While count < 10
  Console.WriteLine("Count is " + count)
  count = count + 2
Loop
Dim word as String = "gibber"
Do
  word = word + word
Loop Until word.Length < 10
Dim names() as String = {"Bob","Ben","Bill","Borris","Bin"}
For Each name As String In names
  Console.WriteLine(name)
Next name
Dim line_to_write as String = "Append to end of file"
Dim f As New System.IO.StreamWriter("out.txt", False)
f.WriteLine(line_to_write)
f.Close()

'Alternate
FileOpen(1, "out.txt", OpenMode.Append)
WriteLine(1, line_to_write.ToCharArray)
FileClose(1)

Dim line_count as Integer = 0
FileOpen(1, "in.txt", OpenMode.Input)
Do While Not EOF(1)
  Console.WriteLine("Line " + line_count + ": " + LineInput(1))
  line_count += 1
Loop
FileClose(1)

'Alternate way of reading file
Dim line_count as Integer = 0
Dim file As New System.IO.StreamReader("in.txt")
Do While file.Peek() <> -1
  Console.WriteLine("Line " + line_count + ": " + file.ReadLine())
  line_count += 1
Loop
file.Close()
fullname = forename & " " & surname
Dim sum as Integer = val("5") + val(Console.ReadLine())
Console.WriteLine(CStr(sum))
CInt
Cdbl
todo
Like[0-9]
Sub sayHello()
  Console.WriteLine("Hello")
  Console.WriteLine("Goodbye")
End Sub
Function biggest(ByVal a as Integer, ByVal b as Integer) As Integer
  If a > b Then  
    biggest = a
  Else
    biggest = b
  End if
End Function
Sub addMonkey(ByRef name as String)  'Pass a reference to name
  name = name + " is a monkey"
End Sub
Console.WriteLine(addMonkey("Brian")) 'Brian is a monkey
Sub addMonkey(ByVal name as String)  'use a Copy the text name
  name = name + " is a monkey"
End Sub
Console.WriteLine(addMonkey("Brian")) 'Brian .. is not a monkey!
Dim names(3) As String
names(0) = "Bob"
names(1) = "Foo"
names(2) = "Rah"
For Each name As String In names
  Console.WriteLine(name)
Next
Console.WriteLine("array size is " + names.Length)
Dim grid(10,10) as Inetger
grid(5,5) = 1
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
ReDim Preserve ArrayName(LowerValue To HigherValue)
Dim dict As New Dictionary(Of String, String)
dict.Add("Joe", 77)
dict.Add("Jane", 51)
For Each key In dict.Keys
  Console.WriteLine("Key: " + key + " Value: " + dict(key))
Next
Try
  'thing that may error
Catch ex As Exception
  'what to do if things go wrong
End Try
Const csv_line_test as String = "Jane,09/09/1989,Female,Blue"
Dim line_split() = csv_line_test.Split(",")

Dim random_generator As Random = New Random

Dim new_num As Integer = random_generator.Next(0, 100)
Dim new_fraction As Double = random_generator.
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
Class Star
    Public x As Integer
    Public y As Integer
    Public speed As Integer
End Class
...
Dim s as Star = New Star()
s.x = 100
Module Module1
  Class Student
      Public forname As String
      Public surname As String
      Public dob As Date
  End Class

  Const filename As String = "c:\test.csv"
  Dim students As New LinkedList(Of Student)

  Sub Main()
      Dim objReader As New System.IO.StreamReader(filename)
      Do While objReader.Peek() <> -1
          Dim line_split() = objReader.ReadLine().Split(",")
          Dim new_student As Student = New Student()
          new_student.forname = line_split(0)
          new_student.surname = line_split(1)
          new_student.dob = Date.Parse(line_split(2))
          students.AddLast(new_student)
      Loop
      objReader.Close()
      Console.WriteLine("Loaded "&students.Count&" students")
  End Sub
End Module
Threading.Thread.Sleep(1000)
