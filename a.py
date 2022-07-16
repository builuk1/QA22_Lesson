x = 5
y = 5
if x > 0 and y > 0:
    print('I')
elif x > 0 and y < 0:
    print('IV')
elif x > 0 and y == 0:
    print('Axis X+')
elif x < 0 and y > 0:
    print('II')
elif x < 0 and y < 0:
    print('III')
elif x < 0 and y == 0:
    print('Axis X-')
elif x == 0 and y > 0:
    print('Axis Y+')
elif x == 0 and y < 0:
    print('Axis Y-')
elif x == 0 and y == 0:
    print('Zero')
