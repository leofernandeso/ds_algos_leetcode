def foo(step=0):
    for i in range(step, 4):
        print(step)
        foo(step+1)
        

foo()   
