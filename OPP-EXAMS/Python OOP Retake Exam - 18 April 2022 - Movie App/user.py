class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) == 0:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        result_str = [f'Username: {self.username}, Age: {self.age}', 'Liked movies:']
        if len(self.movies_liked) > 0:
            for liked in self.movies_liked:
                result_str.append(liked.details())
        else:
            result_str.append('No movies liked.')
        result_str.append('Owned movies:')
        if len(self.movies_owned) > 0:
            for owned in self.movies_owned:
                result_str.append(owned.details())
        else:
            result_str.append('No movies owned.')
        return '\n'.join(result_str)
