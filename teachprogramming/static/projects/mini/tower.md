Tower
-----

Create a function that produces the following ascii shapes:

`tower(1)`
```
#
```

`tower(2)`
```
 #
###
```

`tower(3)`
```
  #
 ###
#####
```

`tower(4)`
```
   #
  ###
 #####
#######
```

`tower(n)`
```
should work for any positive integer
```

Hints
-----

Try to attempt the problem on yourself. Use the hints if you are UTTERLY stuck.

<details>
<summary>Hints: Approach</summary>

### Hints: Approach

* Get a piece of paper and a pen (Seriously do this)
* Start by printing the correct number of lines to the screen
* Consider how many `_` and how many `#` you need for each row
* Draw these on paper for different `n` (tower sizes)
* Now you have the numbers on paper - reverse engineer the maths

</details>

<details>
<summary>Hints: Technical</summary>

### Hints: Technical

* Consider the difference between `Console.Write(???)` and `Console.WriteLine(???)`
* `\n` is the character for _new line_
* You might want to research/search for a way to repeat `char`acters
</details>



<details>
<summary>Hints: Advanced</summary>

### Hints: Advanced

* Consider putting this in a function
* ```csharp
    String tower(int n) {
        return "#";
    }
    ```
* It is preferable to output a single string - this aids testing e.g.
* ```csharp
    if (tower(4) != "   #\n  ###\n #####\n#######") {Console.WriteLine($"It's broken - I got:\n{tower(4)}");}

    ```
</details>

