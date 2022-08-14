from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen 

def main(screen):

    effects = [Cycle(screen, FigletText("Have a Great Trip", font = "lean"), int(screen.height/ 2 - 8)),
        Cycle(screen, FigletText("MELANIE !!", font = "cursive", width = 500), int(screen.height / 2 + 3)),
        Cycle(screen, FigletText("I Love You <3", font = "lean"), int(screen.height / 2 + 12)),
        Stars(screen, 100)]

    screen.play([Scene(effects, 10000)])

Screen.wrapper(main)
