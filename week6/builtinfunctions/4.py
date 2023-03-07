'''
Write a Python program that invoke square root function after specific milliseconds.
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
'''
import time,math
def delay(number,milliseconds):
    seconds=milliseconds/1000
    answer=math.sqrt(number)
    time.sleep(seconds)
    print('Square root of '+str(number)+' after '+str(milliseconds)+' milliseconds is '+str(answer))
delay(25100,2123)
delay(25,5000)