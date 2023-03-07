'''
Write a Python program with
 builtin 
function that returns True if
 all elements of the tuple are true.
'''
tuple1=[5%2==1,'orange',0]#false
tuple2=[4,3,1]#true
tuple3=[0,1,7%2==0]#false
tuple4=[1,1,1,1,1]#true
tuple5=[True,True,False]#false
print(all(tuple1))
print(all(tuple2))
print(all(tuple3))
print(all(tuple4))
print(all(tuple5))
