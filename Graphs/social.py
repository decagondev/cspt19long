import random
import math
import time

class Queue():
    def __init__(self):
        self.storage = []
    def enqueue(self, value):
        self.storage.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.storage.pop(0)
        else:
            return None
    def size(self):
        return len(self.storage)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            return False # print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False # print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    # def populate_graph(self, num_users, avg_friendships):
    #     """
    #     Takes a number of users and an average number of friendships
    #     as arguments
    #     Creates that number of users and a randomly distributed friendships
    #     between those users.
    #     The number of users must be greater than the average number of friendships.
    #     """
    #     # Reset graph
    #     self.last_id = 0
    #     self.users = {}
    #     self.friendships = {}
    #     # !!!! IMPLEMENT ME

    #     # Add users
    #     # iterate over 0 to num users
    #         # add user 

    #     # Create friendships
    #     # generate all possible friendships.

    #     # to avoid dupelecates, makes user user1 is smaller than user2

    #     # shuffle the friendships

    #     # take n number of friends from the from the front of the list
    #     # by using the equasion num_users * avg_friendships // 2 (a for loop)
    def populate_graph(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)
        x = 0
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def populate_graph_l(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # create a target friendships variable of (num_users * avg_friendships)
        target_friendships = (num_users * avg_friendships)
        # create a total_friendships counter and set it to zero
        total_friendships = 0
        # creat a collision counter and set it to zero
        collision_counter = 0

        # while our total friendships is less than our target friendships
        while total_friendships < target_friendships:
            # create a random user id
            user_id = random.randint(1, self.last_id)
            # create a random friend id
            friend_id = random.randint(1, self.last_id)

            # add a friendship between them checking if there is a collision
            if self.add_friendship(user_id, friend_id):
                # increment our total friendships
                total_friendships += 1
            # otherwise
            else:
                # increment our collision counter
                collision_counter += 1
        # print the number of collision
        print(f"Collisions: {collision_counter}")


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}
        q = Queue()
        q.enqueue([user_id])
        while q.size() > 0:
            path = q.dequeue()
            newuser_id = path[-1]
            if newuser_id not in visited:
                visited[newuser_id] = path
                for friend_id in self.friendships[newuser_id]:
                    if friend_id not in visited:
                        new_path = list(path)
                        new_path.append(friend_id)
                        q.enqueue(new_path)
        return visited


if __name__ == '__main__':
    num = 1000
    friends = 5
    sg = SocialGraph()

    # # start time
    start_time = time.time()
    sg.populate_graph(num, friends)
    # set an end time
    end_time = time.time()
    # print the difference
    print(f"Quadratic Runtime: {end_time - start_time} seconds")

    # sg = SocialGraph()

    # # start time
    # start_time = time.time()
    # sg.populate_graph_l(num, friends)
    # # set an end time
    # end_time = time.time()
    # # print the difference
    # print(f"Linear Runtime: {end_time - start_time} seconds")
    # # print(sg.friendships)

    connections = sg.get_all_social_paths(1)
    # print(connections)
    # keep track of a total number of connections.
    total = 0

    # iterate over connections.
    for user_id in connections:
        # increment the total by the length connections at the current user id.
        total += len(connections[user_id]) - 1
    
    # print the length of the connections.
    print(len(connections))
    # print the total divided by the length of the connections.
    print(total / len(connections))

    # total connections counter and set it to zero
    total_connections = 0
    # total degrees counter and set it to zero.
    total_degrees = 0
    # number of iterations set to 10
    number_of_iterations = 10

    # iterate over number_of_iterations
    for _ in range(0, number_of_iterations):

        # populate the graph.
        sg.populate_graph(num, friends)
        # update the connections
        connections = sg.get_all_social_paths(1)
        # reset total to zero.
        total = 0
        # iterate over connections.
        for user_id in connections:
            # increment the total by the length connections at the current user id.
            total += len(connections[user_id]) - 1

        # print the length of the connections.
        total_connections += len(connections)
        # print the total divided by the length of the connections.
        total_degrees += total / len(connections)
    
    # print the total_connections / number_of_iterations.
    print(f"connections: {total_connections / number_of_iterations}")
    # print the total degrees / divided
    print(f"Degrees: {total / number_of_iterations}")



    """
    1: 2, 3, 4, 5, 6, 7, 8, 9, 10
    2: 3, 4, 5, 6, 7, 8, 9, 10 
    3: 4, 5, 6, 7, 8, 9, 10
    4: 5, 6, 7, 8, 9, 10
    5: 6, 7, 8, 9, 10
    6: 7, 8, 9, 10
    7: 8, 9, 10
    8: 9, 10
    9: 10
    10

    """