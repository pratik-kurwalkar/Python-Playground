import test  # Importing a file will execute all of the code present outside the methods.
from test import testMethod  # Import particular method
import test as t # Import module as other name
from EmojiCoverter import make_emoji
# import testPackage
import testPackage.test2 as pack

import random

import subprocess

subprocess.run()


test.testMethod()  # Methods can be accessed using dot operator
t.testMethod()
testMethod()
print(make_emoji('Hello! :) I am sad today.. :('))

pack.printSomething()

print(random.random())  # Print random values between 0 and 1
print(random.randint(20,1000)) # Prints random values between specified numbers
myList = ['A', 'B', 'C']
print(random.choice(myList))


# We can also create packages to organize the code in a better way
# Every Python Package is a directory with a __init__.py file