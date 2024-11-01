```python
aa = [1,2,3]
bb = [4,5,6]
cc = aa
cc.append(7)

# evaluates to
aa == [1,2,3,7]
bb == [4,5,6]
cc == [1,2,3,7]

# aa and cc point to the same list
aa = [8,9,10]
# evaluates to
aa == [8,9,10]
bb == [4,5,6]
cc == [1,2,3,7]
# because you only changed the list aa points to

aa = cc # lets get our state back
aa == [1,2,3,7]
bb == [4,5,6]
cc == [1,2,3,7]

# time for our in place selector!
aa[:] = [8,9,10]
# evaluates to
aa == [8,9,10]
bb == [4,5,6]
cc == [8,9,10]
# we have modified the list in place that aa points to. and cc points to the same list object

>>> id([1,2,3])
4373703616
>>> id([4,5,6])
4374371648
>>> id([1,2,3])
4375747136

# The id's of the list objects are different
# The `[]` syntax is an object constructor
```