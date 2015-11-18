import funcynum as fn
import sys

# redirect all print functions to our txt file to read
f = open('funcynum_TEST_print_outputs.txt', 'w')
sys.stdout = f

#no extra lines between what is printed for each number
#...or there shouldn't be at least
#there will be one line between changes in number e.g. 0's then \n 1's
#all numbers should be 5 tall
#all examples pulled from Joes comments (DISCLAIMER!!)
#each change in number starts with the standard 5 wide
#first will come 5 wide then should be 2x 3 wide

#check zero

def test_print_zero():
    fn.print_zero('*', 5) 
    fn.print_zero('*', 3)#looks really dumb
    fn.print_zero('*', 1)#still dumb

#check one 

def test_print_one():
    fn.print_one('*', 5) 
    fn.print_one('X', 3) 
    fn.print_one('$', 1) 

#check two

def test_print_two():
    fn.print_two('*', 5) 
    fn.print_two('*', 3)
    fn.print_two('*', 1)

def test_print_three():
    fn.print_three('*', 5)
    fn.print_three('*', 3)
    fn.print_three('*', 1)

def test_print_four():
    fn.print_four('*', 5)
    fn.print_four('*', 3)
    fn.print_four('*', 1)
    
def test_print_five():
    fn.print_five('*', 5)
    fn.print_five('*', 3)
    fn.print_five('*', 1)

def test_print_six():
    fn.print_six('*', 5)
    fn.print_six('*', 3)
    fn.print_six('*', 1)

def test_print_seven():
    fn.print_seven('*', 5)
    fn.print_seven('*', 3)
    fn.print_seven('*', 1)

def test_print_eight():
    fn.print_eight('*', 5)
    fn.print_eight('*', 3)
    fn.print_eight('*', 1)

def test_print_nine():
    fn.print_nine('*', 5)
    fn.print_nine('*', 3)
    fn.print_nine('*', 1)

def test_print_plus():
    fn.print_plus('*', 5)
    fn.print_plus('*', 3)
    fn.print_plus('*', 1)

def test_print_minus():
    fn.print_minus('*', 5)
    fn.print_minus('*', 3)
    fn.print_minus('*', 1)
    
if __name__ == '__main__':
    
    test_print_zero()
    print()

    test_print_one()
    print()

    test_print_two()
    print()

    test_print_three()
    print()
    
    test_print_four()
    print()

    test_print_five()
    print()

    test_print_six()
    print()
    
    test_print_seven()
    print()
    
    test_print_eight()
    print()
    
    test_print_nine()
    print()

    test_print_plus()
    print()

    test_print_minus()

    
