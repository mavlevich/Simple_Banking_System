import random


random.seed(3)
# call the function here
alpha = 0.9
beta = 0.1
beta_distribution = random.betavariate(alpha, beta)
print(beta_distribution)
