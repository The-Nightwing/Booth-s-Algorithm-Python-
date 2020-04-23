
def convertToBinary(n): 
    if(int(n)>=0):
	    return positivenum(int(n))
    else:
        return twoscompliment(int(n))


def positivenum(n):         #converting a postitive number to binary number
    p=list(bin(int(n)).replace("0b", ""))
    p.insert(0,'0')
    return "".join(p)


def twoscompliment(n):      #returning two's compliment of a number in form of list
    arr=[]
    n=n*-1
    for i in positivenum(n):
        if i=='1':
            arr.append('0')
        elif i=='0':
            arr.append('1')
    temp=arr
    temp.reverse()

    if(temp[0]=='0'):
        temp[0]='1'
    else:
        temp[0]='0'
        for j in range(1,len(arr)):
            if(temp[j]=='0'):
                temp[j]='1'
                break
            else:
                temp[j]='0'
    temp.reverse()
    return "".join(temp) 




def shiftToRight(shift):  #right shifting 
    s=shift[0]
    s1=shift[:-1]
    s1="".join(s1)
    s2=s+s1
    return s2


def adding(b1,b2):  #adding two binary  numbers
    add = []
    carry = 0
    for x in range(len(b1)-1, -1, -1):               
        if b1[x] == '1' and b2[x] == '1':
            if carry == 1:
                add.append('1')
            else:
                add.append('0')
                carry = 1
        elif b1[x] == '0' and b2[x] == '0':
            if carry == 1:
                add.append('1')
                carry = 0
            else:
                add.append('0')  
        elif (b1[x] == '0' and b2[x] == '1') or (b1[x] == '1' and b2[x] == '0'):
            if carry == 1:
                add.append('0')
            else:
                add.append('1')
    add.reverse()
    return "".join(add)

def btoD(n):
    print()
    print("The answer is:",end=" ")
    c=int(n,2)
    c=c*-1
    print(str(c))


def binaryToDecimal(n): 
    if(n[0]=='0'):
        print()
        print("The Answer is:",end=" ")
        print(int(n,2))
    elif(n[0]=='1'):
        arr=[]
        for i in range(len(n)):
            if n[i]=='1':
                arr.append('0')
            elif n[i]=='0':
                arr.append('1')
        temp=arr
        temp.reverse()

        if(temp[0]=='0'):
            temp[0]='1'
        else:
            temp[0]='0'
            for j in range(1,len(arr)):
                if(temp[j]=='0'):
                    temp[j]='1'
                    break
                else:
                    temp[j]='0'
        temp.reverse()
        btoD("".join(temp))


def booth(b1,b2):
    m=int(b1)
    l1=convertToBinary(b1)
    r=int(b2)
    m1=m*-1
    if(m>=0):
        l=convertToBinary(m)
        x=len(l)
        A=list(convertToBinary(m))
        A.insert(0,'0')
        S=list(convertToBinary(m1))
        S.insert(0,'1')
    else:
        p=m*-1
        l=convertToBinary(p)
        x=len(l)
        A=list(convertToBinary(m))
        A.insert(0,'1')
        S=list(convertToBinary(m1))
        S.insert(0,'0')
    if(r>=0):
        l=convertToBinary(r)
        y=len(l)
        P=list(convertToBinary(r))
    else:
        r=r*-1
        l=convertToBinary(r)
        y=len(l)
        P=list(convertToBinary(r*-1))
    for i in range(y+1):
        A.append('0')
        S.append('0')
    for j in range(0,x):
        P.insert(j,'0')

    P.insert(0,'0')
    P.append('0')
    
   
    count=0
    while(count!=y):
        qneg1=P[len(P)-1]
        q1=P[len(P)-2]
        if(q1=='0' and qneg1=='1'):
            s=adding(P,A)
            print("P="+str("".join(P)),end=" ")
            print("the last two bits are "+str(P[len(P)-2])+str(P[len(P)-1]))
            print(str("".join(P))+"."+"P=P+S")
            P=shiftToRight(s)
            print(str("".join(P))+"."+"Right Shift")
        if(q1=='1' and qneg1=='0'):
            s=adding(P,S)
            print("P="+str("".join(P)),end=" ")
            print("the last two bits are "+str(P[len(P)-2])+str(P[len(P)-1]))
            print(str("".join(P))+"."+"P=P+S")
            P=shiftToRight(s)
            print(str("".join(P))+"."+"Right Shift")

        if((q1=='0' and qneg1=='0') or (q1=='1' and qneg1=='1')):
            print("P="+str("".join(P)),end=" ")
            print("the last two bits are "+str(P[len(P)-2])+str(P[len(P)-1]))
            print("After right shift: ",end=" ")
            P=shiftToRight(P)
            print(str("".join(P)))
        count=count+1   

    binaryToDecimal(P[1:len(P)-1])

        

if __name__ == '__main__': 
    num1=input("Enter first number")
    num2=input("Enter second number")
    if(int(num1)==0 or int(num2)==0):
        print(0)
    else:
        booth(num1,num2)
    
    

