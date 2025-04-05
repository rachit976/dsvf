try: 
    number = int(input("enter a number"))
    print("the number entred is"),number
except valuError as ex:
    print("exception:", ex)