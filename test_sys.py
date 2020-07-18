'''
python 3.x
'''

import sys
import random

name="meng"
#print(sys.path)
hello_format="hello ,{}"
print(hello_format.format(name))

#random a number
generate_number=random.random()
print("random a number with 2 decimals >>> {:.2f}".format(generate_number*100))
#random a interger number
generate_int= random.randint(1,99)
print("random a interger >>> {}".format(generate_int))
#
