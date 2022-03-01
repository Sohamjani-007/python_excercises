# solution1
x,y = map(int,input().split())
items = list(range(1,x+1,2))
items = items+items[::-1][1:]
for i in items:
    text= "WELCOME" if i == x else '.|.'*i
    print (text.center(y,'-'))

# solution2
#take rows and columns and convert both to integer using map function 
rows,columns = map(int,input().split())
#Middle row where "WELCOME" will be written
middle = rows//2+1
#Top part of door mat
for i in range(1,middle):
    #calculate number of .|. required and multiply with .|.
    center = (i*2-1)*".|."
    #Move our center pattern to center using string.center method and fill left and part with "-" 
    print(center.center(columns,"-"))
#print middle part welcome
    print("WELCOME".center(columns,"-"))

#create bottom part in reverse order like we did in the top part
    for i in reversed(range(1,middle)):
        center = (i*2-1)*".|."
        print(center.center(columns,"-"))

# solution3
if __name__ == '__main__':
        N, M = map(int, input().split(": "))

        for i in range(N):
                pattern = ".|."
                if i < (N-1)/2:
                        print((pattern * (2*i+1)).center(M, "-"))
                elif i == (N-1)/2:
                        print("WELCOME".center(M, "-"))
                else:
                        print((pattern * (2*(N-1-i)+1)).center(M, "-"))
# solution4
N, M = map(int, input().split()) 
for i in range(1,N,2): 
    print((i*'.|.').center(M,'-'))
print('WELCOME'.center(M,'-')) 
for i in range(N-2,-1,-2): 
    print((i*'.|.').center(M, '-'))

