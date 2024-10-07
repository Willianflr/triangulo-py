def triangulo(y):
#    x = 0 
#    for i in range(1, y + 1):
#        x = i + (x * 10)
#        print(f'{x:.>{y}}')
#
    x = 0 
    for i in range(1, y + 1):
        x = i + (x * 10)
        print(f'{x: >{y}} {x: <{y}}')

triangulo(10)