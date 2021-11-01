from Container import Container

class Player(Container):
    """
    Any data relating to the player himself should go in
    the Player class.
    Ex: location, inventory, health status, etc. etc.
    """
    def __init__(self):
        self.loc = None #what room is the player in
        self.contents = {} #Container
        
        