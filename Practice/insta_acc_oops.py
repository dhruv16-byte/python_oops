class User:
    def __init__(self, username):
        self.username = username
        self.followers = []
        self.following = []
        self.posts = []

    def follow(self, obj_user):
        if obj_user == self:
            print("Invalid Request. You cannot follow yourself.")
            return
        if self in obj_user.followers:
            print("Invalid request. You already follow this person")
            return
        self.following.append(obj_user)
        obj_user.followers.append(self)

    def unfollow(self, obj_user):
        if obj_user == self:
            print("Invalid Request. You cannot unfollow yourself.")
            return
        if self not in obj_user.followers:
            print("Invalid request. You do not follow this person")
            return
        self.following.remove(obj_user)
        obj_user.followers.remove(self)

    def create_post(self, obj):
        self.posts.append(obj)

    def display_profile(self):
        print(f"Username : {self.username}")
        print(f"Followers : ")
        for follow in self.followers:
            print(follow.username)
        print(f"Following : ")
        for follown in self.following:
            print(follown.username)

        print("POSTS :")
        for posts in self.posts:
            print(
                f"Author : {posts.author.username}\n{posts.content}\nLikes : {len(posts.likes)}\nWho liked the post :"
            )
            for user in posts.likes:
                print(user.username)


class Post:
    def __init__(self, content, author):
        self.author = author
        self.content = content
        self.likes = []

    def like(self, obj_user):
        if obj_user in self.likes:
            print("You've already liked this post")
        else:
            self.likes.append(obj_user)

    def unlike(self, obj_user):
        if obj_user not in self.likes:
            print("You've not liked the post to dislike it")
        else:
            self.likes.remove(obj_user)

    def display_post(self):
        print(
            f"Author : {self.author.username}\n{self.content}\nNo. of likes :", end=""
        )
        print(len(self.likes))