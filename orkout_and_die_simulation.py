
import random

# Task 1: Simulate Rolling a Six-Sided Die (At least 20 times)
def roll_die():
    # Initialize counters
    count_6 = 0
    count_1 = 0
    count_consecutive_6s = 0
    previous_roll = None

    # Simulate rolling the die 20 times
    for roll in range(1, 21):
        die_roll = random.randint(1, 6)

        # Count occurrences of 6 and 1
        if die_roll == 6:
            count_6 += 1
        if die_roll == 1:
            count_1 += 1

        # Count consecutive 6s
        if previous_roll == 6 and die_roll == 6:
            count_consecutive_6s += 1

        # Update the previous roll
        previous_roll = die_roll

    # Print the statistics
    print("\nTask 1: Die Rolling Statistics")
    print(f"Times rolled a 6: {count_6}")
    print(f"Times rolled a 1: {count_1}")
    print(f"Times rolled two 6s in a row: {count_consecutive_6s}")

# Task 2: Workout Routine (Jumping Jacks)
def workout_routine():
    total_jumping_jacks = 100
    completed_jumping_jacks = 0

    # Loop to ask for 10 jumping jacks at a time
    print("\nTask 2: Workout Routine (Jumping Jacks)")
    while completed_jumping_jacks < total_jumping_jacks:
        completed_jumping_jacks += 10
        print(f"You completed {completed_jumping_jacks} jumping jacks.")

        # Ask if the user is tired
        tired = input("Are you tired? (yes/y or no/n): ").strip().lower()

        if tired == "yes" or tired == "y":
            skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()

            if skip == "yes" or skip == "y":
                print(f"You completed a total of {completed_jumping_jacks} jumping jacks.")
                break
        else:
            remaining = total_jumping_jacks - completed_jumping_jacks
            if remaining > 0:
                print(f"{remaining} jumping jacks remaining.")
            else:
                print("Congratulations! You completed the workout.")
                break

# Main function to run both tasks
def main():
    roll_die()
    workout_routine()

# Run the program
if __name__ == "__main__":
    main()


# this is my final code , task 05 < lets run it /.....................
