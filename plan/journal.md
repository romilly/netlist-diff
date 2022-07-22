# Project journal for netlist-diff

## Friday 22 July 2022

I'm  developing this via TDD, and intending to publish this vi PyPi, so my
[walking skeleton](https://www.techtarget.com/whatis/definition/walking-skeleton)
will have two components.

1. I've
   1. set up the `setup.cfg` and `project.toml` files needed to **build a wheel ready for distribution**,
   2. set up my standard project structure complete with its own virtual environment,
   3. added the build and wheel packages, along with PyHamcrest which I will use for my tests,
   4. created a trivial diff.py that prints 'Hello world',
   5. and built a wheel
2. Next I'll **create a program using TDD** that implements a very thin slice of application functionality.

I've added an integration test which currently just verifies whether two files are identical or not.

That's nowhere near enough, since it's possible for two different files to represent the same circuit.

They might contain the same connections, but in a different order; there are other, more complex possibilities.
I'll need to create tests to creats those scenarios and verify correct behaviour.

There's another problem, though. The current code is very, very simple. If two files differ it says they are 
different but it gives no useful information about how they differ.

To start with, I'll write code that finds the parts used in each netlist and checks to see that both netlists use 
the same parts, list ing any differences.

I can use the current pair of data files since I know that they have slightly different parts lists.

I'm going to extend the integration test so that it fails and then write a unit test, get that to pass, and verify 
that the integration text passes.

I'll write a test that expects a line 'Missing from 555_netlist.xml: Generic female header - 2 pins'.







