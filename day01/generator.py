def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""
    splitted = text.split(sep)
    if option == "shuffle":
        shuffled = set(splitted)
        for word in shuffled:
            yield word
    if option == "unique":
        unique = list(set(splitted))
        yield unique
    if option == "ordered":
        ordered = sorted(splitted)
        for word in ordered:
            yield word


text = "Lorem Ipsum is fake is"

for word in generator(text, sep=" ", option="ordered"):
    print(word)
