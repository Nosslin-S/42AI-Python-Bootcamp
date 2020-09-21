import sys

if not sys.argv[2].isdigit() or not sys.argv[1].isalpha():
    print("ERROR")
else:
    print(
        [
            word.strip(";,:.")
            for word in sys.argv[1].split()
            if len(word.strip(";,:.")) > int(sys.argv[2])
        ]
    )

