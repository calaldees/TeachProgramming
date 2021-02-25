-- Examples from 'Computer Science' by PM Heathcoate - pg 368
-- Use Online at https://repl.it/site/blog/haskell

-- function mapping - maps a domain to a co-domain
-- domain -> co-domain

-- stateless & no-side-effects

-- First class objects are objects that
-- appear in expressions
-- be assigned to a variable
-- be assigned as an argument
-- be returned by a function call

-- Higher Order Function
-- either takes a function or returns a function or both

-- any function only takes one parameter at a time

-- argument is value or expression PASSED to a function
-- parameter is a reference declared IN a function

-- types (Bool, Char) and typeclass's
-- Num is a typeclass that includes Integer, Int, Double, Float


--addThreeIntegers :: Integer -> (Integer -> (Integer -> Integer))
addThreeIntegers a b c = a + b + c

square x = x^2
a = 4
--a = 5
addTwoNumbers x y = x + y
b = 10
doubleSmallNumber x = if x < 10
                      then x * 2
                      else x
-- Function Composition
addAndDouble x y = addTwoNumbers (doubleSmallNumber x) y

-- Integer unbounded
-- Int min/max value
-- Double
-- Float

sumOfTwo x y = x + y
-- :t sumOfTwo

sumOfSquare :: Integer -> Integer -> Integer
sumOfSquare x y = square x + square y

doubleNum :: Integer -> Integer
doubleNum x = 2 * x

isEqual :: Int -> Int -> Bool
isEqual x y = x == y

-- :t isEqual

add :: Integer -> Integer -> Integer
add x y = x + y

-- partial function
addSix :: Integer -> Integer
addSix = add 6

zz = [1,2,3,4,5]

-- length zz
-- map (max 3) zz
-- map (+5) zz
-- filter (>3) zz

isEven n = n `mod` 2 == 0

-- filter (isEven) zz

-- foldl (+) 0 zz

-- Lists --

names = ["Anna", "Bob", "Jo", "Keira", "Tom", "George"]
numbers = [3, 7, 14, 83, 2, 77]

-- head names
-- tail names
-- tail (tail (tail numbers))
-- null numbers

newList = []

-- null newList

-- 5:numbers
-- numbers ++ [100, 101]
-- length numbers