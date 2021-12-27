a=[1,2,3,4,5,6,7]
print(a)
for i in range(5):
 temp=a[0]
 for j in range(len(a)-1):
   a[j]=a[j+1]
 a[len(a)-1]=temp
 print(a)

