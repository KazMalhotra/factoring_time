'''This program is free software. It is licensed under the Apache 2.0 license. Original author: Kaz Malhotra'''
#https://xkcd.com/247/

from datetime import datetime #import stuff
import math
import time

def primeFactors(n): 
      
   
    while n % 2 == 0:  # Print 2 the number of times it goes into n
        print (2), 
        n = n / 2
          
   

    for i in range(3,int(math.sqrt(n))+1,2):  # n is odd now
          
        
        while n % i== 0: # while i divides n , print i and divide n 
            print (i), 
            n = n / i 
                  
    if n > 2: 
        print (n) 

while True:
  now = datetime.now()  #define now
  current_time = now.strftime("%H%M") #define current time. (it is only hours and minutes.)
  n = int(current_time)  #define n to current time converted to an integer

  if n > 1300: #this is for 12 hour time 
     n = n - 1300 #convert from 24h time to 12h time     

  print("Current Time =", n) #display the time
  print("Factored:") 
  primeFactors(n) # process n through prime factors
  time.sleep(1) #wait a second and then repeat!
