import sys

if len(sys.argv) == 2:
    reverse = sys.argv[1][::-1]
    print(reverse)
else:
    reverse = " ".join(sys.argv[1:])[::-1]
    print(reverse)
