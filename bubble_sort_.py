
#ascending
a= [64,34,25,12,22,11,90,5]
n = len(a)
for i in range (n - 1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]

print(a)

#Descending 

a= [64,34,25,12,22,11,90,5]
n = len(a)
for i in range (n - 1):
    for j in range(n-1-i):     #if i =3  [0,7-3=4]   = [0-4]
        if a[j] < a[j+1]:
            a[j] , a[j+1] = a[j+1],a[j]

print(a)


#improvement in ascending order bubble sorting.


