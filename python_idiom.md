# Writing idiomatic python

But at a deeper level, the reasoning is based on the difference between
**equality** and **identity** . Using `==` determines if two objects **have the same value**
(as defined by their `_eq` attribute). Using `is` determines if the two objects are
**actually the same object**.

Note the use of `is not` : comparisons against `None` (a singleton in Python) should always use `is` or `is not` , not `==` (from PEP8).

bytes:
bool: Flase
object: None
int(number): 0
tutple: ()
dict: {}
list: []


One of the lesser known facts about Python’s `for` loop is that it can include an
`else` clause. The `else` clause is executed after the iterator is exhausted, unless
the loop was ended prematurely due to a `break` statement.


























