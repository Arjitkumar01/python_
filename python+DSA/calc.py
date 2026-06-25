def calc(a,b,op):
    if op=="sum":
        return f"sum of both no:{a+b}"
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    else:
        if b==0:
            return f"Error"
        else:
            return a/b

a=int(input("enter first num:"))
b=int (input("enter sec num:"))
op=input("enter the operator:")
print(calc(a,b,op))
        
    