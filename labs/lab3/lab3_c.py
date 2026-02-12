'''
for this exercise it was used Chat GBT to generate the code with the given prompt:

make this exercise :  The simulation asks a user to enter the probabilities A for a customer to enter the shop and

B  the customer’s service to be ready. If the given numbers are not between 0.0 – 1.0 the program closes.

The simulation mimics a situation where every minute a customer enters the cashier’s queue (probability A),

the number of customers in a queue is updated, the customer is randomly served (probability B),

and when served, removed from the queue.

If there are no customers in the queue, the cashier is idle.

Simulation is run 100 times.

The program keeps track for each simulation round the total number of customers,

the longest queue, and the idle time during the simulation.

In the end, the program draws a bar chart showing the total number of customers, the longest queue,

 and the maximum idle time for each simulation round.

The final plot x-axis range is from 1 to the number of rounds and each x-point has 3 bars.

 

Plotting a green bar to x=1, y=20 (see: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)

plt.bar(1, 20, width=0.2, color='green')
 

the code should: program asks the user to input 2 probabilities
given  numbers are casted to floats
given numbers range is checked
simulation rounds plot the results as 3 bars	
invalid numbers result to closing the program
'''


import random
import sys
import matplotlib.pyplot as plt

# --- USER INPUT ---
try:
    A = float(input("Enter probability A (customer enters queue): "))
    B = float(input("Enter probability B (customer is served): "))
except ValueError:
    print("Invalid input. Closing program.")
    sys.exit()

# Check probability range
if not (0.0 <= A <= 1.0 and 0.0 <= B <= 1.0):
    print("Probabilities must be between 0.0 and 1.0. Closing program.")
    sys.exit()

# --- SIMULATION SETTINGS ---
ROUNDS = 100
MINUTES = 100  # each simulation lasts 100 minutes

total_customers_list = []
longest_queue_list = []
idle_time_list = []

# --- RUN SIMULATION ---
for _ in range(ROUNDS):
    queue = 0
    total_customers = 0
    longest_queue = 0
    idle_time = 0

    for _ in range(MINUTES):

        # Customer enters queue with probability A
        if random.random() < A:
            queue += 1
            total_customers += 1

        # If queue is empty → cashier idle
        if queue == 0:
            idle_time += 1
        else:
            # Customer served with probability B
            if random.random() < B:
                queue -= 1

        # Track longest queue
        if queue > longest_queue:
            longest_queue = queue

    total_customers_list.append(total_customers)
    longest_queue_list.append(longest_queue)
    idle_time_list.append(idle_time)

# --- PLOT RESULTS ---
x = list(range(1, ROUNDS + 1))
width = 0.25

plt.figure(figsize=(14, 6))

plt.bar([i - width for i in x], total_customers_list, width=width, color='green', label='Total Customers')
plt.bar(x, longest_queue_list, width=width, color='blue', label='Longest Queue')
plt.bar([i + width for i in x], idle_time_list, width=width, color='red', label='Idle Time')

plt.xlabel("Simulation Round")
plt.ylabel("Value")
plt.title("Queue Simulation Results")
plt.legend()
plt.tight_layout()
plt.show()
