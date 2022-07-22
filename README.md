# Compare two fritzing netlists

When transfering a circuit design from breadboard to strip-board it can be difficult to verify that the two designs 
are the same.

This program will (I hope) check if the two are the same, and if not, give useful indications of the differences 
between them.

## An example

Here's my 555 timer on a breadboard:

![image](http://images.rareschool.com/img/462ea248-099e-11ed-b480-01b7337f15a9-555_bb.png)

Here's the first stripboard version:

![image](http://images.rareschool.com/img/63100d66-099e-11ed-b480-01b7337f15a9-555-stripboard_bb.png)

Are they implementations of the same circuit?

I'll be writing Python code using TDD and commiting as I go.

I'll tweet progress (as @RAREblog) and will blog about issues and the algorithm at https://blog.rareschool.com/




