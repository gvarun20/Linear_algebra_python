#!/usr/bin/env python
# coding: utf-8

# A uniform distribution is characterized by each outcome having an equal probability of occurringImagine a spinner with numbers from 1 to 10. A uniform distribution means that when you spin the spinner, each number has an equal chance of being the result. It's like having a fair game where no number is more likely than the others. So, if you spin it many times, you'd expect each number to show up about the same number of times – that's the uniform distribution in action!

# In[1]:


import random

def spin_spinner():
    return random.randint(1, 10)

# Simulate spinning the spinner 100 times
num_spins = 100
outcomes = [spin_spinner() for _ in range(num_spins)]

# Count the occurrences of each number
counts = {number: outcomes.count(number) for number in range(1, 11)}

# Print the results
for number, count in counts.items():
    print(f"Number {number}: {count} occurrences")


# In[2]:


import random
import matplotlib.pyplot as plt

def spin_spinner():
    return random.randint(1, 10)

# Simulate spinning the spinner 100 times
num_spins = 100
outcomes = [spin_spinner() for _ in range(num_spins)]

# Count the occurrences of each number
counts = {number: outcomes.count(number) for number in range(1, 11)}

# Plot the bar graph
plt.bar(counts.keys(), counts.values())
plt.xlabel('Number on Spinner')
plt.ylabel('Occurrences')
plt.title('Uniform Distribution of Spinner Outcomes')
plt.show()


# In[ ]:




