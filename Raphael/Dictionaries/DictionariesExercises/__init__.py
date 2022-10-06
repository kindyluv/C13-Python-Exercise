
# Create a function called word_frequency that takes in a phrase ('I love Batman because I am Batman') and returns a dictionary that shows us how many times each word is used inside of the phrase itself {'I' : 2, 'love' : 2, 'Batman' : 2, 'am': 1}

# Algorithm
# create a function
# create an empty dictionary
# turn thr phrase into a list to easily manipulate the items inside
# # loop through the list


if __name__ == '__main__':
    def word_frequency(phrase: str) -> str:
        result = {}
        words = phrase.split()
        for word in words:
            if word not in result:
                result[word] = 1
            else:
                result[word] += 1
    ree

    word_frequency('I love Batman because I am Batman')

