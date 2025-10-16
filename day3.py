is_logged_in = True
is_subscribed = False
user_credits = 100
max_credits = 200
min_credits = 50
credit_valid=(user_credits>=min_credits)  and (user_credits<=max_credits) and (user_credits!=min_credits)

bonus_eligible=( is_subscribed) or(user_credits>min_credits)

user_credits+=50
user_credits-=20
user_credits*=2
user_credits/=150

power_result =user_credits**2

full_access=(is_logged_in and is_subscribed)

true_login=is_logged_in is True

access_result=is_logged_in or is_subscribed and False
print("Is Logged In:", is_logged_in)
print("Is Subscribed:", is_subscribed)
print("Credit valid:", credit_valid)
print("Bonus eligible:", bonus_eligible)
print("User credits:", user_credits)
print("Power result:", power_result)
print("Full access:", full_access)
print("True login:", true_login)
print("Access result:", access_result)

