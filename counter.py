import time

def counter(counting):
   
    for count in range(1,counting):
     
        time.sleep(1)
        print("""+----------+""")
        print(" ", " ", " ",count)
        print("""+----------+""")
    
user_input = int(input('Enter Seconds : '))
counter(counting=user_input+1)
time.sleep(1)
print("""
+--------------------+
|   Your Time's Up   |                    
|       Buddy!       |
|                    |
+--------------------+
""")


# import time

# def counter(c):
#     for i in range(1, c):
#         time.sleep(1)
#         print(i)

# counter(c=int(input('Enter the seconds')) + 1)