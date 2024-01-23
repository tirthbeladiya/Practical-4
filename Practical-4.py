fh = open('Practical-4.txt','w')
number_list=[30,50,20,10,40]
i=0
sum=0
while i<len(number_list):
    sum+=number_list[i]
    i+=1
avg=sum/len(number_list)
fh.write('The average of a list of numbers is: '+str(avg))
fh.close()
