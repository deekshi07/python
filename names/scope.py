def func1():
    global x 
    x=1
    
    def func2():
        global x
        x = 2
        
    print("Before calling func2:", x)
    func2()
    print("After calling func2:", x)
func1()
print("Value of x in global scope:", x)