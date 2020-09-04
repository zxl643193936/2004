a=[122,4,1,345,65,3435,23,657,76]
for i in range(len(a)-1):
	for j in range(len(a)-1):
		if a[j]>a[j+1]:
			big=a[j]
			a[j]=a[j+1]
			a[j+1]=big
print(a)
