weight=int(input('weight : '))
c=0
unit=input('L(bs) or K(g) : ')
if unit.upper()=='L':
    c=weight *0.45
    print(f'you are {c} kilos ')
else:
    c=weight/0.45
    print(f'you are {c} pounds ')

