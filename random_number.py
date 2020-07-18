import random


'''
generate a random number from start to end
'''
def  generate_number(start,end):
   int_number= random.randint(start,end)
   return int_number


'''
generate N random number
'''
def generate_number_list(length):

    #initialize list value to 0
    random_number_list=[0]*length

    #generate random number into list
    for index in range(length):
        random_number_list[index]=generate_number(1, 999)

    return random_number_list

'''
test scope
'''
list=generate_number_list(30)
print(list)
