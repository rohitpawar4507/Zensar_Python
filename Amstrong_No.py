# Assignment
no=int(input('Enter a number : '))
sum=0
temp=no
while(temp>0):
    digit=temp%10
    sum+=digit**3
    temp=temp//10
if no==sum:
    print('Amstrong Number :',no)
else:
    print('Not Amstrong No:',no)
