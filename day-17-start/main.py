class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        # self.followers_list = []
        # self.following_list = []

    def follow(self, user):
        user.followers += 1
        self.following += 1
        # self.following_list.append(user)
        # user.followers_list.append(self)


user1 = User(1, "Mike")
user2 = User(2, "James")

user1.follow(user2)
user2.follow(user1)
print(f"{user1.username} is following: {user1.following} number of people and has {user1.followers}")
print(f"{user2.username} is following: {user2.following} number of people and has {user2.followers}")
