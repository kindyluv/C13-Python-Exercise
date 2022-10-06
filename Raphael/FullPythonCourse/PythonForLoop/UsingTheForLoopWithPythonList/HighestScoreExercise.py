# WAP that calculates the highest score from a List of scores using for loop. You are not allowed to use the max or min function.

if __name__ == '__main__':
    scores = list(range(56, 89, 3))
    highest_score = 0
    for score in scores:
        if score > highest_score:
            highest_score = score

    print(highest_score)

