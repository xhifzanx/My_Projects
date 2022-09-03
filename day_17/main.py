class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0
    def follow(self, user):
        self.following+=1
        user.followers+=1

user_1 = User("001", "hifzan")
user_2 = User("002", "hifzan2")
print(f"User id = {user_1.user_id} and User Name = {user_1.user_name}")

user_2.follow(user_1)
print(f" {user_1.user_name}'s following {user_1.following} no. of people.")
print(f" {user_1.user_name}'s followers are {user_1.followers} no. of people.")

print(f"User id = {user_2.user_id} and User Name = {user_2.user_name}")

print(f" {user_2.user_name}'s following {user_2.following} no. of people.")
print(f" {user_2.user_name}'s followers are {user_2.followers} no. of people.")