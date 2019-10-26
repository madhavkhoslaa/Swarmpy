class Robo():
    def __init__(self, initial_position):
        assert isinstance(initial_position, tuple)
        self.initial_position= initial_position
        self.position= self.initial_position
    
    def update_position(self, x, y):
        self.position= self.position[0]+ x, self.position[1]
        