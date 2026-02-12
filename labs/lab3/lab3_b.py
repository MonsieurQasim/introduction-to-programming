import matplotlib.pyplot as plt
import random
import time


A = float(input("Enter probability of customer arrival A: "))
B = float(input("Enter probability of service completion B: "))

if A < 0.0 or A > 1.0 or B < 0.0 or B > 1.0:
    print("Error: Probabilities must be between 0 and 1.")
else:
    for round in range(100):
    #  create  cashier to handle random number of customers 
        cashier = 0
        customer = 0
        ticks = 360  # Simulate 6 hours, 3600 seconds / 10 = 360 "minutes"
        #  statistics of how cashier operated during simulation
        idletime = 0
        max_cashier = 0
        numofserved = 0 
        max_idletime = 0

        while ticks > 0:
        
            if random.randint(0, 360)%5==0:  # randomly decide if a new customer arrives (every 5th = 20% chance)
                customer += 1
                cashier += 1
                if cashier > max_cashier:
                    max_cashier = cashier  # update maximum

           # time.sleep(0.1)  # Simulate passing of time
            if cashier > 0:
                idletime = 0  # Cashier has customers, reset idle time
                if random.randint(0, 3)==0:  # randomly decide if customer service is ready (1 in 3 chance)
                    cashier -= 1  # remove one customer from the queue
                    numofserved += 1
            elif cashier == 0:
                idletime += 1  # No customers in queue, increase idle time
                if idletime > max_idletime:
                    max_idletime = idletime  # Update maximum idle time  
           # print(ticks, cashier*"*")

            ticks -= 1 # remove one "minute" from simulation
        '''

        print(f"Simulation ended with {cashier} customers in queue.")
        print(f"Simulation served: {numofserved} customers.")
        print(f"Simulation's maximum number of customers in queue: {max_cashier}")
        print(f"Simulation's maximum idle time: {max_idletime} minutes.")
        '''
        plt.bar(round, numofserved, width=0.2, color='green')
        plt.bar(round, max_idletime, width=0.2, color='blue')
        plt.bar(round, max_cashier, width=0.2, color='red')
        

    plt.xlabel('Simulation')
    plt.ylabel('Number of Customers Served')
    plt.title('Cashier Simulation Results')
    plt.show()