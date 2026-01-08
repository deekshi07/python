def outer_function():
    global a
    a = 2

    def inner_function():
        global a
        a = 30
        print('a= ',a)
    print('a = ',a )

    inner_function()
    print('a = ',a)
a= 10
print('a = ',a )
outer_function()
print('a = ',a )

