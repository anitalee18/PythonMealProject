# Create and define main method, asking for input of time
def main():
    x = input("What time is it right now? ")
    x = convert(x)
    if 7.00 <= x <= 8.00:
        print("breakfast time")
    elif 12.00 <= x <= 13.00:
        print("lunch time")
    elif 18.00 <= x <= 19.00:
        print("dinner time")
    else:
        print("Not time for a meal")


# Create and define method to convert time string into a float
def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes)/60
    time = float(hours) + minutes
    return time

# Use conditionals to call upon main method
if __name__ == "__main__":
    main()
