try:
    a="ABC"
except ValueError:
    print("You cannot force String to behave like Integer")
else:
    print("No error found")
finally:
    print("This will always print")