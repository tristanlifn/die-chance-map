import numpy as np

while True:
    # Create arrays representing the possible outcomes of rolling one die
    h = int(input("what first die do you want? "))
    f = int(input("what second die do you want? "))
    g = int(input("what third die do you want? "))
    die_outcome_1 = np.arange(1, f+1)
    die_outcome_2 = np.arange(1, g+1)
    die_outcome_3 = np.arange(1, h+1)

    # Use meshgrid to generate all combinations of rolling three dice
    roll1, roll2, roll3 = np.meshgrid(die_outcome_1, die_outcome_2, die_outcome_3)

    # Calculate the sum of each combination
    sums = roll1 + roll2 + roll3

    # Enter what number you are looking for
    x = int(input("what number are you looking for? "))
    condition = sums.__eq__(x)
    condition = np.count_nonzero(condition)

    # Print the resulting matrix and probabilety outecome.
    print(f"multi dimentional array:\n{sums}\n")
    print(f"how many times is {x}: {condition}\n")
    print(f"complete matrix size: {sums.size}\n")
    print(f"what % chanse is there of roling {x}: {round(condition/sums.size*100, 2)}%\n")