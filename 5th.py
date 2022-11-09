#Print the sum of the current number and the previous number
n=int(input("enter the no:"))
pre_no=0
for i in range(n):
  x_sum =pre_no+i
  print("Current number",i,"previous number ",pre_no,"sum",x_sum)
  pre_no=i
  



