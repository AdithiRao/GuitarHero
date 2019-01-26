import pygame, time
# from pygameButton import retu
import pygameButton

class PygameGame2(object):

    def init(self):
        pass

    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def keyPressed(self, keyCode, modifier):
        for note in self.listOfNotes:
            if keyCode == 97:
                    if type(note) == redNote and self.height - 160 <= note.y <= self.height - 120:
                        note.y = self.height - 140
                        if note.tailLength <= 40:
                            try:
                                self.listOfNotes.remove(note)
                            except:
                                pass
                        else:
                            note.spd = 0
                            note.tailLength -= 5
            elif keyCode == 115:
                    if type(note) == yellowNote and self.height - 160 <= note.y <= self.height - 120:
                        note.y = self.height - 140
                        if note.tailLength <= 40:
                            try:
                                self.listOfNotes.remove(note)
                            except:
                                pass
                        else:
                            note.spd = 0
                            note.tailLength -= 5
            elif keyCode == 100:
                    if type(note) == blueNote and self.height - 160 <= note.y <= self.height - 120:
                        note.y = self.height - 140
                        if note.tailLength <= 40:
                            try:
                                self.listOfNotes.remove(note)
                            except:
                                pass
                        else:
                            note.spd = 0
                            note.tailLength -= 5
            elif keyCode == 102:
                   if type(note) == greenNote and self.height - 160 <= note.y <= self.height - 120:
                        note.y = self.height - 140
                        if note.tailLength <= 40:
                            try:
                                self.listOfNotes.remove(note)
                            except:
                                pass
                        else:
                            note.spd = 0
                            note.tailLength -= 5




    def timerFired(self, dt):
        for note in self.listOfNotes:
            note.moveDown()
            if note.y > self.height:
                try:
                    self.listOfNotes.remove(note)
                except:
                    pass
            if note.spd == 0:
                if type(note) == redNote and self.isKeyPressed(97):
                    if note.tailLength >= 10:
                        note.tailLength -= 10
                    else:
                        try:
                            self.listOfNotes.remove(note)
                        except:
                            pass
                elif type(note) == redNote and not self.isKeyPressed(97):
                    try:
                        self.listOfNotes.remove(note)
                    except:
                        pass
                elif type(note) == yellowNote and self.isKeyPressed(115):
                    if note.tailLength >= 10:
                        note.tailLength -= 10
                    else:
                        try:
                            self.listOfNotes.remove(note)
                        except:
                            pass
                elif type(note) == yellowNote and not self.isKeyPressed(117):
                    try:
                        self.listOfNotes.remove(note)
                    except:
                        pass
                elif type(note) == blueNote and self.isKeyPressed(100):
                    if note.tailLength >= 10:
                        note.tailLength -= 10
                    else:
                        try:
                            self.listOfNotes.remove(note)
                        except:
                            pass
                elif type(note) == blueNote and not self.isKeyPressed(100):
                    try:
                        self.listOfNotes.remove(note)
                    except:
                        pass
                elif type(note) == greenNote and self.isKeyPressed(102):
                    if note.tailLength >= 10:
                        note.tailLength -= 10
                    else:
                        try:
                            self.listOfNotes.remove(note)
                        except:
                            pass
                elif type(note) == greenNote and not self.isKeyPressed(102):
                    try:
                        self.listOfNotes.remove(note)
                    except:
                        pass

    def drawNoteLines(self, screen):
        redX = 0.2*self.width - 40
        yellowX = 0.4*self.width - 40
        blueX = 0.6*self.width - 40
        greenX = 0.8*self.width - 40

        red, redStart, redEnd= (255, 0, 0), (redX + 39, 0), (redX + 39, self.height)
        pygame.draw.line(screen, red, redStart, redEnd, 2)
        blue, blueStart, blueEnd = (0, 0, 255), (blueX + 39, 0), (blueX + 39, self.height)
        pygame.draw.line(screen, blue, blueStart, blueEnd, 2)
        green, greenStart, greenEnd = (11, 102, 35), (greenX + 39, 0), (greenX + 39, self.height)
        pygame.draw.line(screen, green, greenStart, greenEnd, 2)
        yellow, yellowStart, yellowEnd = (255, 255, 0), (yellowX + 39, 0), (yellowX + 39, self.height)
        pygame.draw.line(screen, yellow, yellowStart, yellowEnd, 2)

        silver = (192,192,192)
        for num in range(200, 800, 100):
            silverStart, silverEnd = (0, self.height - num), (self.width, self.height - num)
            pygame.draw.line(screen, silver, silverStart, silverEnd, 1)
        silverStart, silverEnd = (0, self.height - 100), (self.width, self.height - 100)
        pygame.draw.line(screen, silver, silverStart, silverEnd, 5)

    def drawNotes(self, screen):
        for note in self.listOfNotes:
            note.drawTail(screen)
            screen.blit(note.noteImg, (note.x, note.y))

    def drawBackGround(self, screen):
        screen.blit(self.flames, (0, 0))
        #screen.blit(self.gh, (0, 0))
        pass

    def redrawAll(self, screen):
        self.drawNoteLines(screen)
        self.drawNotes(screen)
        #pygame.display.flip()

    def __init__(self, width=1000, height=2000, fps=200, title="Guitar Hero!!!!!!!!!"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (0, 0, 0)
        self.listOfNotes = [] #added
        self.flames = pygame.image.load("flames.png")
        #self.gh = pygame.image.load("Guitar_hero_logo.png)")
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()

        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            #print(pygame.time.Clock.get_time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False

            screen.fill(self.bgColor)
            self.drawBackGround(screen)
            screen.blit(self.flames, (0, 0))
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()

class Note(object): #superclass for all notes
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.spd = 15
        self.tailLength = tailLength
        self.color = (255, 0, 0)
        self.struck = False

    def moveDown(self):
        self.y += self.spd
        #pygame.display.update()

    def drawTail(self, screen):
        pygame.draw.rect(screen, (255,255,255), (self.x+ 34, self.y + 40, 11, -self.tailLength -1), 2)
        pygame.draw.rect(screen, self.color, (self.x+ 35, self.y + 40, 10, -self.tailLength))

class redNote(Note):
    def __init__(self, y, spd, width, tailLength = 0):
        self.x = int(0.2*width - 40)
        self.y = y
        self.pos = (self.x, self.y)
        self.noteImg = pygame.image.load("redNoteB.png")
        self.spd = spd
        self.tailLength = tailLength
        self.color = (255, 0, 0)

class blueNote(Note):
    def __init__(self, y, spd, width, tailLength = 0):
        self.x = int(0.6*width - 40)
        self.y = y
        self.pos = (self.x, self.y)
        self.noteImg = pygame.image.load("blueNoteB.png")
        self.spd = spd
        self.tailLength = tailLength
        self.color = (0, 0, 255)

class greenNote(Note):
    def __init__(self, y, spd, width, tailLength = 0):
        self.x = int(0.8*width - 40)
        self.y = y
        self.pos = (self.x, self.y)
        self.noteImg =pygame.image.load("greenNoteB.png")
        self.spd = spd
        self.tailLength = tailLength
        #self.color = (0, 255, 0)
        self.color = (11, 102, 35)

class yellowNote(Note):
    def __init__(self, y, spd, width, tailLength = 0):
        self.x = int(0.4*width - 40)
        self.y = y
        self.pos = (self.x, self.y)
        self.noteImg = pygame.image.load("yellowNoteB.png")
        self.spd = spd
        self.tailLength = tailLength
        self.color = (255, 255, 0)

def main():
    retu = pygameButton.retu
    print("helloooo", retu)
    guitarHero = PygameGame2()
    speed = 10
    for el in retu:
        y_pos = -1*80*(el[1] - 1.3875)
        if el[0] == "B":
            if el[1] == el[2]:
                guitarHero.listOfNotes.append(blueNote(y_pos, speed, guitarHero.width, 0))
            else:
                bar = 5000*(el[2]- el[1])
                guitarHero.listOfNotes.append(blueNote(y_pos, speed, guitarHero.width, int(bar)))
        if el[0] == "Y":
            if el[1] == el[2]:
                guitarHero.listOfNotes.append(yellowNote(y_pos, speed, guitarHero.width, 0))
            else:
                bar = 5000*(el[2]- el[1])
                guitarHero.listOfNotes.append(yellowNote(y_pos, speed, guitarHero.width, int(bar)))
        if el[0] == "G":
            if el[1] == el[2]:
                guitarHero.listOfNotes.append(greenNote(y_pos, speed, guitarHero.width, 0))
            else:
                bar = 5000*(el[2]- el[1])
                guitarHero.listOfNotes.append(greenNote(y_pos, speed, guitarHero.width, int(bar)))
        if el[0] == "R":
            if el[1] == el[2]:
                guitarHero.listOfNotes.append(redNote(y_pos, speed, guitarHero.width, 0))
            else:
                bar = 5000*(el[2]- el[1])
                guitarHero.listOfNotes.append(redNote(y_pos, speed, guitarHero.width, int(bar)))

#     guitarHero.run()
#
#     #All pieces should appear at a height of -80 or higher, they must travel 740 pixels down
#     #from that point to get their centers to hit the white line, this takes ~1.3875 seconds
#
#
# if _name_ == '_main_':
#     main()
