def text_analyzer(text):
    """
    This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.
    """
    count = 0
    count_upper = 0
    count_lower = 0
    count_punctuation = 0
    count_space = 0
    if len(text) == 0:
        print("Please enter some text")
        return None
    for char in text:
        count += 1
        if char.isupper():
            count_upper += 1
        elif char in [",", ";", ".", ":", "!", "?"]:
            count_punctuation += 1
        elif char == " ":
            count_space += 1
        elif char.islower():
            count_lower += 1
    print("The text contains " + "{}".format(count) + " characters")
    print("- " + "{}".format(count_upper) + " upper letters")
    print("- " + "{}".format(count_lower) + " lower letters")
    print("- " + "{}".format(count_punctuation) + " punctuation marks")
    print("- " + "{}".format(count_space) + " spaces")


text_analyzer("")

