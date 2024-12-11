# method is a function which is inside function and used with objects
# it can modify multiple obejects
class User:
    def __init__(
        self, id
    ):  # if you dont wanna modify any attribute or pre-assign any value of any attribute, don't pass it in constructor. Just modify that inside the constructor
        self.name = id
        self.followers = 0
        self.following = 0
        # initially every account has 0 follwoers and following

    def follow(self, userID):
        self.following += 1
        userID.followers += 1

    def unfollow(self, userID):
        self.following -= 1
        userID.followers -= 1


user1 = User("wasi20210201")
user2 = User("igotYuandme")
user3 = User("iamfineRYU")
user1.follow(user2)
user1.follow(user3)
user2.follow(user3)
user3.follow(user2)

print(
    f"{user1.name} follows: {user1.following} people and is followed by {user1.followers}\n{user2.name} follows: {user2.following} people and is followed by {user2.followers}\n{user3.name} follows: {user3.following} people and is followed by {user3.followers}\n\n"
)

user3.unfollow(user2)

print(
    f"{user1.name} follows: {user1.following} people and is followed by {user1.followers}\n{user2.name} follows: {user2.following} people and is followed by {user2.followers}\n{user3.name} follows: {user3.following} people and is followed by {user3.followers}\n\n"
)
