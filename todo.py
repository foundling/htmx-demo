class Todo():

    _id = 0

    def __init__(self, title):

        Todo._id += 1

        self.title = title
        self.id = Todo._id

    def __repr__(self):
        return '<class Todo {}>'.format(self.title)
