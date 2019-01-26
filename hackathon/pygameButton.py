import module_manager
module_manager.review()
import pygame
pygame.init()
import pyaudio
import wave
import aubio
import numpy as num
import time
import copy
from pygamegame import PygameGame
from combine import record
retu = None

class button():
    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        if outline:
            pygame.draw.rect(win,outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            font = pygame.font.SysFont("comiscsans", 30)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x+ (self.width/2 - text.get_width()/2), self.y + (self.height/2 -text.get_height()/2)))

    def isOver(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] <self.y + self.height:
                return True
        return False

def redrawWindow():
    win.fill((0,0,0))
    recordButton.draw(win)
    stopButton.draw(win)
    recordButton2.draw(win)
    playButton.draw(win)

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

    def keyReleased(self, keyCode, modifier):
        pass


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

    def __init__(self, width=600, height=800, fps=200, title="Guitar Hero!!!!!!!!!"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (0, 0, 0)
        self.listOfNotes = [] #added
        self.flames = pygame.image.load("flames.png")
        #self.gh = pygame.image.load("Guitar_hero_logo.png)")
        pygame.init()
        pygame.mixer.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)
        music = pygame.mixer.Sound("recordedFile2.wav")
        music.play()

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        speed = 6
        for el in retu:
            y_pos = -1*80*(el[1] - 1.3875)
            if el[0] == "B":
                if el[1] == el[2]:
                    self.listOfNotes.append(blueNote(y_pos, speed, self.width, 0))
                else:
                    bar = 5000*(el[2]- el[1])
                    self.listOfNotes.append(blueNote(y_pos, speed, self.width, int(bar)))
            if el[0] == "Y":
                if el[1] == el[2]:
                    self.listOfNotes.append(yellowNote(y_pos, speed, self.width, 0))
                else:
                    bar = 5000*(el[2]- el[1])
                    self.listOfNotes.append(yellowNote(y_pos, speed, self.width, int(bar)))
            if el[0] == "G":
                if el[1] == el[2]:
                    self.listOfNotes.append(greenNote(y_pos, speed, self.width, 0))
                else:
                    bar = 5000*(el[2]- el[1])
                    self.listOfNotes.append(greenNote(y_pos, speed, self.width, int(bar)))
            if el[0] == "R":
                if el[1] == el[2]:
                    self.listOfNotes.append(redNote(y_pos, speed, self.width, 0))
                else:
                    bar = 5000*(el[2]- el[1])
                    self.listOfNotes.append(redNote(y_pos, speed, self.width, int(bar)))
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

class Game(PygameGame):
    def init(self):
        self.recordButton = button((255,128,0), 125, 100, 350, 100, "Click to Record Guitar Solo!")
        self.stopButton = button((255,128,0), 125, 200, 350, 100, "Stop Recording Guitar Solo!")
        self.record2Button = button((255,128,0), 125, 300, 350, 100, "Click to Record Full Song!")
        self.playButton = button((255,128,0), 125, 400, 350, 100, "Play game!")
        self.bool = False
        self.Recordframes = []
        self.pitchList = []
        self.recorded = False
        self.donePitching = False
        self.retu = []

    def mouseMotion(self, x, y):
        if self.recordButton.isOver((x,y)):
            self.recordButton.color = (255,85,0)
        else:
            self.recordButton.color = (255,128,0)
        if self.stopButton.isOver((x,y)):
            self.stopButton.color = (255,85,0)
        else:
            self.stopButton.color = (255,128,0)
        if self.record2Button.isOver((x,y)):
            self.record2Button.color = (255,85,0)
        else:
            self.record2Button.color = (255,128,0)
        if self.playButton.isOver((x,y)):
            self.playButton.color = (255,85,0)
        else:
            self.playButton.color = (255,128,0)

    def mousePressed(self, x, y):
        if self.recordButton.isOver((x,y)):
            self.pitchList = []
            self.bool = True
            self.initTimeRec = 0
            print ("recording started")
        if self.stopButton.isOver((x,y)):
            self.bool = False
            self.donePitching = True
            self.retu = self.convertToRetu()
            global retu
            retu = self.retu

        if self.record2Button.isOver((x,y)):
            if self.donePitching == True:
                lengthOfSong = self.pitchList[len(self.pitchList)-1][0]
                record(lengthOfSong)
                self.recorded = True

        elif self.playButton.isOver((x,y)):
            if self.recorded == True and self.donePitching == True:
                guitarHero = PygameGame2(600,800)
                guitarHero.run()


    def pitching(self):
        FORMAT = pyaudio.paFloat32
        CHANNELS = 1
        RATE = 44100
        CHUNK = 1024
        WAVE_OUTPUT_FILENAME = "recordedFile.wav"
        device_index = 2
        p = pyaudio.PyAudio()
        index = 0
        pDetection = aubio.pitch("default", 2048,
            2048//2, 44100)
        # Set unit.
        pDetection.set_unit("Hz")
        pDetection.set_silence(-40)
        stream = p.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,input_device_index = index,
                        frames_per_buffer=CHUNK)

        data = stream.read(CHUNK)
        samples = num.fromstring(data,
        dtype=aubio.float_type)
        pitch = pDetection(samples)[0]
        print(pitch)
        self.pitchList.append((self.initTimeRec,pitch))
        # self.Recordframes.append(data) #we want to record this every 1 ms

        stream.stop_stream()
        stream.close()
        p.terminate()

    def convertToRetu(self):
        pitchList = self.pitchList
        # parse pitchList
        # remove 0s from pitchList
        copyPitch = copy.copy(pitchList)
        copyPitch = [x for x in pitchList if x[1] != 0]

        minn = copyPitch[0][1]
        maxx = copyPitch[0][1]
        for x in copyPitch:
            if x[1] > maxx:
                maxx = x[1]
            if x[1] < minn:
                minn = x[1]
        range_interval = (maxx - minn)//4

        retu = []
        newBlue = []
        copyPitch = copy.copy(pitchList)
        for c in range (len(pitchList)):
            # RED RANGE
            boo = False
            if pitchList[c] != None and minn <= pitchList[c][1] < minn + range_interval:   #blue range
                i = c
                summ = pitchList[c][0]
                while i+1 <= len(pitchList)-1 and abs(pitchList[c][0] - pitchList[i+1][0]) < 2 and abs(pitchList[i][1] - pitchList[i+1][1]) < 40:
                    boo = True
                    summ = pitchList[i+1][0]
                    pitchList[i+1] = pitchList[i]
                    i+= 1
                newBlue.append(("R", pitchList[c][0], summ))
                if c< len(newBlue):
                    if boo and pitchList[c][0] == newBlue[c][2]:
                        newBlue.pop(c)

            # YELLOW RANGE
            boo = False
            if pitchList[c] != None and minn + range_interval <= pitchList[c][1] < minn + 2*range_interval:
                i = c
                summ = pitchList[c][0]
                while i+1 <= len(pitchList)-1 and abs(pitchList[c][0] - pitchList[i+1][0]) < 2 and abs(pitchList[i][1] - pitchList[i+1][1]) < 40:
                    boo = True
                    summ = pitchList[i+1][0]
                    pitchList[i+1] = pitchList[i]
                    i+= 1
                newBlue.append(("Y", pitchList[c][0], summ))
                if c< len(newBlue):
                    if boo and pitchList[c][0] == newBlue[c][2]:
                        newBlue.pop(c)

            # BLUE RANGE
            boo = False
            if pitchList[c] != None and minn + 2*range_interval <= pitchList[c][1] < minn + 3*range_interval:
                i = c
                summ = pitchList[c][0]
                while i+1 <= len(pitchList)-1 and abs(pitchList[c][0] - pitchList[i+1][0]) < 2 and abs(pitchList[i][1] - pitchList[i+1][1]) < 40:
                    boo = True
                    summ = pitchList[i+1][0]
                    pitchList[i+1] = pitchList[i]
                    i+= 1
                newBlue.append(("B", pitchList[c][0], summ))
                if c< len(newBlue):
                    if boo and pitchList[c][0] == newBlue[c][2]:
                        newBlue.pop(c)

            # GREEN RANGE
            boo = False
            if pitchList[c] != None and minn + 3*range_interval <= pitchList[c][1] <= maxx:
                i = c
                summ = pitchList[c][0]
                while i+1 <= len(pitchList)-1 and abs(pitchList[c][0] - pitchList[i+1][0]) < 2 and abs(pitchList[i][1] - pitchList[i+1][1]) < 40:
                    boo = True
                    summ = pitchList[i+1][0]
                    pitchList[i+1] = pitchList[i]
                    i+= 1
                newBlue.append(("G", pitchList[c][0], summ))
                if c< len(newBlue):
                    if boo and pitchList[c][0] == newBlue[c][2]:
                        newBlue.pop(c)

        # getting rid of repeats
        dictB = {}
        retu = []
        for x in newBlue:
            if x[0] == "B":
                if x[1] not in dictB:
                    dictB[x[1]] = x[2]
                else:
                    if dictB[x[1]] < x[2]:
                        dictB[x[1]] = x[2]
        for y in dictB.keys():
            retu.append(("B", y, dictB[y]))

        dictB = {}
        for x in newBlue:
            if x[0] == "G":
                if x[1] not in dictB:
                    dictB[x[1]] = x[2]
                else:
                    if dictB[x[1]] < x[2]:
                        dictB[x[1]] = x[2]
        for y in dictB.keys():
            retu.append(("G", y, dictB[y]))

        dictB = {}
        for x in newBlue:
            if x[0] == "R":
                if x[1] not in dictB:
                    dictB[x[1]] = x[2]
                else:
                    if dictB[x[1]] < x[2]:
                        dictB[x[1]] = x[2]
        for y in dictB.keys():
            retu.append(("R", y, dictB[y]))

        dictB = {}
        for x in newBlue:
            if x[0] == "Y":
                if x[1] not in dictB:
                    dictB[x[1]] = x[2]
                else:
                    if dictB[x[1]] < x[2]:
                        dictB[x[1]] = x[2]
        for y in dictB.keys():
            retu.append(("Y", y, dictB[y]))

        # sort by times
        retu = sorted(retu, key=lambda x: x[1])
        return retu



    def timerFired(self, dt):
        if self.bool:
            self.initTimeRec += .1 *2
            self.pitching()


    def redrawAll(self, screen):
        screen.fill((0,0,0))
        self.recordButton.draw(screen)
        self.stopButton.draw(screen)
        self.record2Button.draw(screen)
        self.playButton.draw(screen)

# loadScreen = Game(600, 800)
# loadScreen.run()
# retu = loadScreen.retu

def main():
    loadScreen = Game(600, 800)
    loadScreen.run()
    print(retu)
    guitarHero = PygameGame2()


if __name__ == '__main__':
    main()
