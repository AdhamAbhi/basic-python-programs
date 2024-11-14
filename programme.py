import math 
scrores=[70,90,60,50,25,65,85]
sum=0 
for num in scrores:
          sum=sum+num
          avg=sum/len(scrores)
          maximum=max(scrores)
avgC=math.ceil(avg)
avgF=math.floor(avg)
print('Here the sum of the list items is :',sum)
print('Here the average of the list items is :',avg)
print('Here the maximum of the list items is :',maximum)
print('The ceiling value of average is :', avgC)
print('The Floor value of average is :', avgF)
maxi=scrores[0]
for num in scrores:
          if num>maxi :
                    maxi=num
                    print("Inside if")
          else:
                    print("Inside else")
print('Here the maximum of the list items is :',maxi)
def find_max(items):
          maximum1=items[0]
          for number in items:
                    if number>maximum1:
                              maximum1=number
          print('Here the maximum of the list items is :',maximum1)
find_max([70,10,50,80,900])
find_max([70,10,500,80,90])