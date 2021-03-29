# Day 17 Udemy Course
class User:
    def __init__(self, user_id, username):  #Initialise the attributes
        self.user_id = user_id
        self.username = username
        self.followers = 0  # We can provide default values to start
        self.following = 0

    def follow(self, user):  #needs a self parameter
        user.followers += 1
        self.following += 1


user_1 = User("001","CJ")
user_2 = User("002" , "Jack")
print(user_1.username)
print(user_1.user_id)
print(user_1.followers)

user_1.follow(user_2)

print(user_1.followers)
print(user_2.followers)
print(user_1.following)
print(user_2.following)

