n=int(input("Enter the number of elements to be inserted: "))
Enter the number of elements to be inserted: 3
a=[]
for i in range(0,n):
	elem=int(input("Enter element: "))
	a.append(elem)
Enter element: 1
Enter element: 2
Enter element: 3
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))