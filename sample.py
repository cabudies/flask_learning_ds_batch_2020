from listvalues import values

completedList = list(filter(lambda singleValue: singleValue['completed'] == True, values))
print(completedList)




