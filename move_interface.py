from enum import Enum, auto
from pynput import keyboard

class MoveInterface:

   # @abstractmethod    
    def nextDirection(self):    
        pass

    class Direction(Enum):
        NORTH = auto()
        SOUTH = auto()
        WEST = auto()
        EAST = auto()

class KeyboardInterface(MoveInterface):
    def __init__(self):
        self.listener = keyboard.Listener(on_release = self.on_release)
        self.last_released = MoveInterface.Direction.SOUTH
    
    def on_release(self, key):    
        if key == keyboard.Key.left:
            self.last_released = MoveInterface.Direction.WEST
        elif key == keyboard.Key.right:
            self.last_released = MoveInterface.Direction.EAST
        elif key == keyboard.Key.up:
            self.last_released = MoveInterface.Direction.NORTH
        elif key == keyboard.Key.down:
            self.last_released = MoveInterface.Direction.SOUTH
        
    def nextDirection(self):
        return self.last_released

