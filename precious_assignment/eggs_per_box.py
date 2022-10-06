"""
(Eggs per Box) Typically 6 eggs fit in one box. Write a script to calculate the number of boxes a farmer
needs to store 28 eggs. The script will also determine how many eggs are placed in the last uncompleted box,
and how many additional eggs are needed to fill this last box.
"""
if __name__ == '__main__':
    eggs = int(input("Enter the number of eggs: "))
    boxes = int(eggs / 6)
    uncompleted = eggs % 6

    if uncompleted <= 5:
        boxes += 1

    needed = 6 - uncompleted

    print(f"The completed egg boxes is {boxes}\n"
          f"The number of eggs in the uncompleted box is {uncompleted}\nThe number of eggs "
          f"needed to fill up the last box is {needed}")