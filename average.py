# python
# copyEdid

# average function
def calculate_average(numbers):
    # initial total is 0
    total = 0
    print(f"initial total: {total}")
    # let initiate number of numbers to be omitted incase a not a number is entered
    lenNotNumber = 0
    # when we call the function we pass the numbers to add
    # loop through the numbers while adding to total
    for num in numbers:
        # let test if type number add else don't add but alert user
        res = isinstance(num, float) | isinstance(num, int)
        print(f"{num} is a number" if res else f"{num} is not a number, note that it won't be included in calculating avarage")
        if res :
            total += num
            print(f"added {num} to total. New total: {total}")
        else:
            lenNotNumber += 1
            print(f"{num} was not added since is not a number. New total: {total}")
    
    # to remove bug we condition. if total is 0 we return 0 else we return average
    print("testing total and calculating average")
    # on calculating avg lets deduct len of not number from len numbers
    avgNumber = lenNotNumber - len(numbers) if  lenNotNumber > len(numbers)  else len(numbers) - lenNotNumber 
    # use the avgNumber in average
    average = total / avgNumber if total > 0 else 0
    print("average calculated and returned")
    print(f'Total: {total}. \nLength of numbers {avgNumber}.\n{lenNotNumber} numbers were omitted ')
    return average
# Test the function
print(calculate_average([1,2,2, "12", "1"]))
