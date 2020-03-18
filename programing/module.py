class Snake:
    # name = 'python'
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name


# object instantiation
snake = Snake('python')

print(snake.name)

snake.change_name('anaconda')
print(snake.name)