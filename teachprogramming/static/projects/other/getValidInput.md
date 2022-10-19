

```csharp
    public static string getValidChoice(string[] choices) {
        bool input_is_invalid = true;
        string input = "";
        while (input_is_invalid) {
            Console.WriteLine("Enter a valid option: " + String.Join(",", choices));
            input = Console.ReadLine();
            for (int i = 0; i < choices.Length; i=i+1) {
                //Console.WriteLine(choices[i]);
                if (choices[i] == input) {
                    //Console.WriteLine(input + " is in the list");
                    //return input;
                    input_is_invalid = false;
                }
            }
        }
        return input;
    }
```