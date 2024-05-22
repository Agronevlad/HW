def greet(language, number):
    """
    :param language: Language options: 'English', 'Chinese', 'Russian'
    :param number: Number of times to print the greeting
    :return: Print the greeting in the specified language for the given number of times
    """
    number = int(number)

    greetings = {
        'English': 'Hello',
        'Chinese': 'Nihao',
        'Russian': 'Privet'
    }

    if language in greetings:
        for _ in range(number):
            print(greetings[language])
    else:
        print('The language is not supported!')

if __name__ == "__main__":
    greet(language='Chinese', number=1)
    greet(language='Russian', number=2)
    greet(language='English', number=3)
