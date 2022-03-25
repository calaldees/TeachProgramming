# AQA-75161-QP-JUN16.PDF) Q5.1 (8 marks)

"""
The algorithm, represented using pseudo-code in Figure 4, describes a method to 
calculate the additive or multiplicative persistence of a two-digit integer. The 
examples below illustrate how additive and multiplicative persistence are
calculated.
Example: calculating the additive persistence of 87
8 + 7 = 15
1 + 5 = 6
After 2 steps the method results in a one digit answer so the additive 
persistence of 87 is 2.
Example: calculating the multiplicative persistence of 39
3 * 9 = 27
2 * 7 = 14
1 * 4 = 4
After 3 steps the method results in a one digit answer so the multiplicative 
persistence of 39 is 3.
"""

"""
OUTPUT "Enter integer (0-99): " 
INPUT Value 
OUTPUT "Calculate additive or multiplicative persistence (a or m)? " 
INPUT Operation 
Count  0 
WHILE Value > 9 
 IF Operation = "a" THEN 
 Value  (Value DIV 10) + (Value MOD 10) 
 ELSE 
 Value  (Value DIV 10) * (Value MOD 10) 
 ENDIF 
 Count  Count + 1 
ENDWHILE 
OUTPUT "The persistence is: " 
OUTPUT Count
"""

# My process
# Copy and paste all code -> replace with python equivalents 
# (not really thinking about what the code is doing, just replacing syntax)
# Ran program - found that it crashs due to performing maths on a string - cast it to integer

def q5():
    print("Enter integer (0-99): ")
    Value = int(input())
    print("Calculate additive or multiplicative persistence (a or m)? ")
    Operation = input()
    Count = 0 
    while Value > 9:
        if Operation == "a": 
            Value = (Value // 10) + (Value % 10) 
        else:
            Value = (Value // 10) * (Value % 10) 
        Count = Count + 1
    print("The persistence is: ")
    print(Count)

if __name__ == "__main__":
    q5()
