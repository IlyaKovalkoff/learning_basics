def glr_outer():
    x = 2
    print ('x equals ', x)

    def glr_inner():
        nonlocal x
        x = 5
        print(x)
    glr_inner()
    print ('local x changed to ', x)
glr_outer()
#print(x)