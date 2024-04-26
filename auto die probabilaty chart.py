import numpy as np

while True:
    def create_dice_matrix(num_dice, sides):
        # Initialize an empty list to store all possible outcomes of rolling each die
        dice_outcomes = []
        
        # Iterate over the number of dice and their corresponding sides
        for sides_count in sides:
            die_outcomes = np.arange(1, sides_count + 1)
            dice_outcomes.append(die_outcomes)
        
        # Use meshgrid to generate all combinations of rolling the specified number of dice
        rolls = np.meshgrid(*dice_outcomes)
        
        # Calculate the sum of each combination
        sums = np.sum(rolls, axis=0)
        
        return sums

    # Ask the user for the number of dice and sides on each die
    num_dice = int(input("Enter the number of dice to roll(2 or 3): "))
    sides = []
    for i in range(num_dice):
        sides_count = int(input(f"Enter the number of sides for die {i+1}: "))
        sides.append(sides_count)

    # Create the matrix
    matrix = create_dice_matrix(num_dice, sides)

    # get and find what number the user is looking for
    x = int(input("what number are you looking for? "))
    condition = matrix.__eq__(x)
    condition = np.count_nonzero(condition)

    print(f"multi dimentional array:\n{matrix}\n")
    print(f"how many times is {x}: {condition}\n")
    print(f"complete matrix size: {matrix.size}\n")
    print(f"what % chanse is there of roling {x}: {round(condition/matrix.size*100, 2)}%\n")