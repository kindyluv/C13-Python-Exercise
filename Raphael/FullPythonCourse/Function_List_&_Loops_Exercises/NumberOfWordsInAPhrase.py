# Create a function count_words that counts and returns the number of words in the phrase: 'Hi my name is Raphael'

# Algorithm:
# 1. define the function
# 2. call the method .split() to split the phrase by empty spaces
# 3. call the len() function on .split()
# 4.
if __name__ == '__main__':

    def count_words(phrase: str) -> int:
        return len((phrase.split()))

    print(count_words('Hi my name is Raphael Ekpei'))
