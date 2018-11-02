#Copyright 2018 B Doubior
# This file was created by Ben Doubior in 31.10.2018.
#
# This program is a private software; you can redistribute it and/or modify
# it under the permission of B Doubior - bendoubior@gmail.com
#
# This program was created in the hope to make the "Tips" procces faster.

print("Tips Calculator")
print("*******************")
totalTips = float(input())
numOfWaiters = int(input())


hoursOfWork = [float((input()))]
totalHours = hoursOfWork[0]
for i in range(1,int(numOfWaiters)):
	hoursOfWork.append(float(input(
	)))
	totalHours += hoursOfWork[i]

if(float(totalTips)*0.9/(float(totalHours)) < 30):
	print("No hafrasha")
else:
	print("Hafrasha bar : "+ str(totalTips* 0.05)+" NIS")
	print("Hafrasha kitchen : "+ str(totalTips* 0.05)+" NIS")
	totalTips*=0.9

tipsPerHour = totalTips/totalHours
print("Tips per hour : "+ str(round(tipsPerHour,1))+" NIS")
print("Basis : "+ str(totalHours* 20)+" NIS")
currentTips = 0
for i in range(0,numOfWaiters):
    currentTips = round((tipsPerHour-20) * hoursOfWork[i],1)
    print("Tips Waiter "+str(i+1)+": "+str(currentTips)+" NIS")