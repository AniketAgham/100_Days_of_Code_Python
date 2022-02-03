# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)
year_remaining = 90 - int(age_int)

months = year_remaining * 12
weeks = year_remaining * 52
days = year_remaining * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")









