#Write a Python program that takes a list 
#of strings as input and outputs the number of times 
#each string appears in the list, using a dictionary and
#conditional statements.
def count_frequent(list):
    list = ['banana', 'pineaple', 'apple', 'orange', 'banana', 'apple']
    frequency = {}
    for item in list:
        if item in frequency:
            frequency[item] +=1
        else:
            frequency[item] = 1
    return frequency
print(count_frequent(list))

#Write a Python program that takes a list of 
#numbers as input and outputs
#the median of the numbers
def count_median(nums):
    nums.sort()
    length = len(nums)
    if length % 2==0:
        median = (nums[length//2] + nums[length//2 - 1])/2
    else:
        median = nums[length//2]
    return median

nums = [2,4,3,5,6,7,8,10]
median = count_median(nums)
print("Median of", nums, "is", median)

#Write a Python program that takes a list 
#of numbers as input and outputs the second largest number
#in the list using conditional statements and a for loop.
# num_list = list(map(int, input("Enter a list of numbers: ").split()))
# largest = num_list[0]
# second_largest = num_list[1]
# for num in num_list:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num < largest:
#         second_largest = num
#         numbers=[12,100,500,230,300,400]
# print("The second largest number in the list is:", second_largest)


#Write a Python program that takes a
#year as input and determines if it is a leap year.
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year  % 400 == 0:
                return True
            else:
                return False
year = 2016
if is_leap_year(year):
 print(f"{is_leap_year} is a leap year")
else:
 print(f"{year} is not a leap year")

 #Write a Python program that takes a string as input
 #and checks if it is a palindrome (reads the same forwards and backwards), 
 #ignoring spaces and punctuation.
 def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum())
    s = s.lower()
    return s == s[::-1]
s = input("madam")
if is_palindrome(s):
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
print(is_palindrome(s))