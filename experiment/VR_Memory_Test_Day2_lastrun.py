#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on May 12, 2024, at 19:25
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'VR_Memory_Test_Day2'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'version': 'ESY',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'd2data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Jun\\OneDrive\\桌面\\Final Project\\VR_Test_Git\\Social_Navigation_VR\\VR_Memory_Test_Day2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1820, 1000], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "intro" ---
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='TestD21.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.76, 0.99),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()
# Run 'Begin Experiment' code from startup_code
# The only way to win... is to play the game, actually


excelnumber = int(expInfo['session'])


#order_num = int(random.random() * 50)
#order = f"{order_num:03}"
#order_file = f"orders/session{expInfo['session']}/order{order}.csv"
#t_order_file = f"orders/session{expInfo['session']}/secorder{order}.csv"

if expInfo['version'] == 'ESY':
    rate_file = 'ratepic_ESY.xlsx'
    arrange_file = 'Arrange_ESY.xlsx'
else:
    rate_file = 'ratepic.xlsx'
    arrange_file = 'Arrange.xlsx'
    


# --- Initialize components for Routine "trial1" ---
landmark = visual.ImageStim(
    win=win,
    name='landmark', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(0.8, 0.08), pos=(0, -0.3), units=None,
    labels=[1,2,3,4,5,6,7], ticks=(1, 2, 3, 4, 5,6,7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)
status_mouse = event.Mouse(win=win)
x, y = [None, None]
status_mouse.mouseClock = core.Clock()
vtxt = visual.TextStim(win=win, name='vtxt',
    text=None,
    font='Arial',
    pos=(0, -0.45), height=0.04, wrapWidth=None, ori=0.0, 
    color=[-1.0000, 1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='一点也不喜欢                                                       非常喜欢',
    font='Arial',
    pos=(-0.01, -0.23), height=0.04, wrapWidth=2.0, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "fixation" ---
iti = visual.ShapeStim(
    win=win, name='iti', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=0.0, interpolate=True)

# --- Initialize components for Routine "intro2" ---
key_resp = keyboard.Keyboard()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='TestD22.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.76, 0.99),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "tr2_1" ---
tmouse_2 = event.Mouse(win=win)
x, y = [None, None]
tmouse_2.mouseClock = core.Clock()
# Run 'Begin Experiment' code from drg2
## code for py->js
#shuffle = util.shuffle
#win = psychoJS.window
#thisExp = psychoJS.experiment
count = 1



polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2',
    size=(0.8, 0.8), vertices='circle',
    ori=0.0, pos=(0.04, 0), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=1.0, depth=-2.0, interpolate=True)
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='grid.png', mask=None, anchor='center',
    ori=0.0, pos=(0.04, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
cmark = visual.ImageStim(
    win=win,
    name='cmark', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.04, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
cmark2 = visual.ImageStim(
    win=win,
    name='cmark2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.04, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
cmark3 = visual.ImageStim(
    win=win,
    name='cmark3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.04, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
cmark4 = visual.ImageStim(
    win=win,
    name='cmark4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.04, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
cmark5 = visual.ImageStim(
    win=win,
    name='cmark5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.04, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
cmark6 = visual.ImageStim(
    win=win,
    name='cmark6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.04, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
btn_2 = visual.ButtonStim(win, 
    text='Finish', font='Arial',
    pos=(0.77, -0.37),
    letterHeight=0.05,
    size=(0.18,0.06), borderWidth=0.0,
    fillColor=[0.0353, 1.0000, 0.4588], borderColor=None,
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='btn_2'
)
btn_2.buttonClock = core.Clock()
# Run 'Begin Experiment' code from code_3
grid_size = 0.1
grid_r = 4

text_list = [
    '压力','高唤醒','激动',
    '不愉快','', '愉快',
    '压抑','低唤醒','放松']
text_components = []
text_pos_x = 0
text_pos_y = 0
for i in range(9):
    text_pos_x = (i % 3 - 1) * grid_r * (grid_size + 0.015)+0.04
    text_pos_y = np.floor(i / 3 - 1) * grid_r * (grid_size + 0.005)
    text_components.append(
        visual.TextStim(
            win=win,
            text=text_list[i],
            pos=(text_pos_x, text_pos_y),
            height=0.03))

# --- Initialize components for Routine "intro2" ---
key_resp = keyboard.Keyboard()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='TestD22.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.76, 0.99),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "tr2" ---
tmouse = event.Mouse(win=win)
x, y = [None, None]
tmouse.mouseClock = core.Clock()
# Run 'Begin Experiment' code from drg
## code for py->js
#shuffle = util.shuffle
#win = psychoJS.window
#thisExp = psychoJS.experiment
count = 1



polygon = visual.ShapeStim(
    win=win, name='polygon',
    size=(0.8, 0.8), vertices='circle',
    ori=0.0, pos=(0.04, 0), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=1.0, depth=-2.0, interpolate=True)
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='grid.png', mask=None, anchor='center',
    ori=0.0, pos=(0.04, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
lmark1 = visual.ImageStim(
    win=win,
    name='lmark1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.04, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
lmark2 = visual.ImageStim(
    win=win,
    name='lmark2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
btn = visual.ButtonStim(win, 
    text='Finish', font='Arial',
    pos=(0.75, -0.37),
    letterHeight=0.05,
    size=(0.18,0.06), borderWidth=0.0,
    fillColor=[0.0353, 1.0000, 0.4588], borderColor=None,
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='btn'
)
btn.buttonClock = core.Clock()
lmark3 = visual.ImageStim(
    win=win,
    name='lmark3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
lmark4 = visual.ImageStim(
    win=win,
    name='lmark4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
lmark5 = visual.ImageStim(
    win=win,
    name='lmark5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
lmark6 = visual.ImageStim(
    win=win,
    name='lmark6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
lmark7 = visual.ImageStim(
    win=win,
    name='lmark7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
lmark8 = visual.ImageStim(
    win=win,
    name='lmark8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)

# --- Initialize components for Routine "intro3" ---
key_resp_2 = keyboard.Keyboard()
image_n = visual.ImageStim(
    win=win,
    name='image_n', 
    image='TestM3.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.76, 0.99),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "tr3" ---
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='arrang2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.76, 0.99),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
# Run 'Begin Experiment' code from drag
## code for py->js
#shuffle = util.shuffle
#win = psychoJS.window
#thisExp = psychoJS.experiment

scene = visual.ImageStim(
    win=win,
    name='scene', 
    image='p.png', mask=None, anchor='center',
    ori=0.0, pos=(0.1, 0), size=(0.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
label1 = visual.ImageStim(
    win=win,
    name='label1', 
    image='material2/1_flower.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
label2 = visual.ImageStim(
    win=win,
    name='label2', 
    image='material2/2_bin.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.08, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
label3 = visual.ImageStim(
    win=win,
    name='label3', 
    image='material2/3_sofa.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
label4 = visual.ImageStim(
    win=win,
    name='label4', 
    image='material2/4_plant.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
label5 = visual.ImageStim(
    win=win,
    name='label5', 
    image='material2/5_mail.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
label6 = visual.ImageStim(
    win=win,
    name='label6', 
    image='material2/6_wash.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
label7 = visual.ImageStim(
    win=win,
    name='label7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.13, 0.13),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
label8 = visual.ImageStim(
    win=win,
    name='label8', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.13, 0.13),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
label9 = visual.ImageStim(
    win=win,
    name='label9', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.13, 0.13),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
label10 = visual.ImageStim(
    win=win,
    name='label10', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.13, 0.13),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
label11 = visual.ImageStim(
    win=win,
    name='label11', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
label12 = visual.ImageStim(
    win=win,
    name='label12', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
label13 = visual.ImageStim(
    win=win,
    name='label13', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.11, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
label14 = visual.ImageStim(
    win=win,
    name='label14', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.11, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
button = visual.ButtonStim(win, 
    text='Finish', font='Arial',
    pos=(0.75, -0.37),
    letterHeight=0.05,
    size=(0.18,0.06), borderWidth=0.0,
    fillColor=[0.0353, 1.0000, 0.4588], borderColor=None,
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button'
)
button.buttonClock = core.Clock()

# --- Initialize components for Routine "thanks" ---
key_resp_3 = keyboard.Keyboard()
thankstext = visual.TextStim(win=win, name='thankstext',
    text='您现在已经完成了上机部分的实验。\n\n请按任意键结束本部分的实验。\n\n请您休息一会儿，谢谢您的参与~！',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "intro" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    introComponents = [image_4, key_resp_4]
    for thisComponent in introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "intro" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_4* updates
        if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_4.started')
            image_4.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=None, waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intro" ---
    for thisComponent in introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials_3.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials_3.addData('key_resp_4.rt', key_resp_4.rt)
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(rate_file),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "trial1" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        landmark.setImage(image)
        slider.reset()
        # Run 'Begin Routine' code from code
        is_pressed = False
        # setup some python lists for storing info about the status_mouse
        status_mouse.x = []
        status_mouse.y = []
        status_mouse.leftButton = []
        status_mouse.midButton = []
        status_mouse.rightButton = []
        status_mouse.time = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        trial1Components = [landmark, slider, status_mouse, vtxt, text_2]
        for thisComponent in trial1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial1" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *landmark* updates
            if landmark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                landmark.frameNStart = frameN  # exact frame index
                landmark.tStart = t  # local t and not account for scr refresh
                landmark.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(landmark, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'landmark.started')
                landmark.setAutoDraw(True)
            
            # *slider* updates
            if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider.frameNStart = frameN  # exact frame index
                slider.tStart = t  # local t and not account for scr refresh
                slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider.started')
                slider.setAutoDraw(True)
            # Run 'Each Frame' code from code
            vall = slider.markerPos
            if vall != None:
            
                vtxt.text = "当前您的评分： "+ str(round(vall,3)) 
            
            #    vtxt.text = "当前的奖金分配选择：\n您的奖金 : 对方的奖金 = " + str(yours) + " : " + str(oppos)
            #    您选择：\n{:,.2f}:{:,.2f} 分配方式\n您将得到：￥{:,.2f}\n对方将得到：￥{:,.2f}'.format(yours,oppos,yourm,oppsm)
            if not is_pressed and status_mouse.getPressed()[0]:
                is_pressed = True
                slider.fillColor = "blue"
                timer = core.CountdownTimer(0.3)
            
            # if slider has been clicked
            if is_pressed:
                if timer.getTime() <= 0:
                    continueRoutine = False
            else:
                slider.fillColor = "red"
                slider.markerPos = slider._posToRating(slider.mouse.getPos())
                slider.recordRating(slider.markerPos)
            # *status_mouse* updates
            if status_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                status_mouse.frameNStart = frameN  # exact frame index
                status_mouse.tStart = t  # local t and not account for scr refresh
                status_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(status_mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('status_mouse.started', t)
                status_mouse.status = STARTED
                prevButtonState = status_mouse.getPressed()  # if button is down already this ISN'T a new click
            if status_mouse.status == STARTED:  # only update if started and not finished!
                x, y = status_mouse.getPos()
                status_mouse.x.append(x)
                status_mouse.y.append(y)
                buttons = status_mouse.getPressed()
                status_mouse.leftButton.append(buttons[0])
                status_mouse.midButton.append(buttons[1])
                status_mouse.rightButton.append(buttons[2])
                status_mouse.time.append(globalClock.getTime())
            
            # *vtxt* updates
            if vtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                vtxt.frameNStart = frameN  # exact frame index
                vtxt.tStart = t  # local t and not account for scr refresh
                vtxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vtxt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'vtxt.started')
                vtxt.setAutoDraw(True)
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                text_2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial1" ---
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('slider.response', slider.getRating())
        trials.addData('slider.rt', slider.getRT())
        # Run 'End Routine' code from code
        is_pressed = False
        thisExp.addData("stage","rate")
        # store data for trials (TrialHandler)
        trials.addData('status_mouse.x', status_mouse.x)
        trials.addData('status_mouse.y', status_mouse.y)
        trials.addData('status_mouse.leftButton', status_mouse.leftButton)
        trials.addData('status_mouse.midButton', status_mouse.midButton)
        trials.addData('status_mouse.rightButton', status_mouse.rightButton)
        trials.addData('status_mouse.time', status_mouse.time)
        # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [iti]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        while continueRoutine and routineTimer.getTime() < 1.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *iti* updates
            if iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                iti.frameNStart = frameN  # exact frame index
                iti.tStart = t  # local t and not account for scr refresh
                iti.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(iti, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'iti.started')
                iti.setAutoDraw(True)
            if iti.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > iti.tStartRefresh + 1.2-frameTolerance:
                    # keep track of stop time/frame for later
                    iti.tStop = t  # not accounting for scr refresh
                    iti.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'iti.stopped')
                    iti.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.200000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "intro2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    intro2Components = [key_resp, image_2]
    for thisComponent in intro2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "intro2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2.started')
            image_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intro2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intro2" ---
    for thisComponent in intro2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_3.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_3.addData('key_resp.rt', key_resp.rt)
    # the Routine "intro2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "tr2_1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # setup some python lists for storing info about the tmouse_2
    tmouse_2.x = []
    tmouse_2.y = []
    tmouse_2.leftButton = []
    tmouse_2.midButton = []
    tmouse_2.rightButton = []
    tmouse_2.time = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from drg2
    # define scene terms
    thisExp.addData("stage","Preference")
    
    
    def shuffle_twolist(list1, list2):
        b =  [i for i in range(len(list1))]
        np.random.shuffle(b)
        sorted_list1 = [t[1] for t in sorted(zip(b, list1), key=lambda x: x[0]) ]
        sorted_list2 = [t[1] for t in sorted(zip(b, list2), key=lambda x: x[0]) ]
        return sorted_list1, sorted_list2
    
    scenes = [cmark, cmark2, cmark3, cmark4, cmark5, cmark6]
    scene_value = ['1_flower', '2_bin', '3_sofa', '4_plant', '5_mail', '6_wash']
    
    new_scenes,new_scene_value = shuffle_twolist(scenes, scene_value)
    #new_scenes,new_scene_value = scenes, scene_value
    print(new_scenes)
    print(new_scene_value)
    
    #shuffle(scenes)
    thisExp.addData('scenes', new_scene_value)
    
    # set pos of different figures
    for pointer in range(len(new_scenes)):
        # 0 1 2 3 / 4 5 6 7 
        # 0.45/0.15/-0.25/-0.45 0.15*(x % 4)-0.45
        x = -0.8+(pointer // 6)*0.1
        y = 0.15*(pointer % 6)-0.37
        new_scenes[pointer].setPos([x, y])
        wid, hei = new_scenes[pointer].size
        print("wid: ",wid)
    
        print(new_scene_value[pointer],'(',x,',',y,')' )
        
    
    
    
    drg_in_process = False
    clicked_stim = None
    
    thisExp.nextEntry()
    
    cmark.setSize((0.12,0.12))
    cmark.setImage('material2/1_flower.PNG')
    cmark2.setSize((0.12,0.12))
    cmark2.setImage('material2/2_bin.PNG')
    cmark3.setSize((0.12,0.12))
    cmark3.setImage('material2/3_sofa.PNG')
    cmark4.setSize((0.12,0.12))
    cmark4.setImage('material2/4_plant.PNG')
    cmark5.setSize((0.12,0.12))
    cmark5.setImage('material2/5_mail.PNG')
    cmark6.setSize((0.12,0.12))
    cmark6.setImage('material2/6_wash.PNG')
    # Run 'Begin Routine' code from code_3
    for i in range(9):
        text_components[i].setAutoDraw(True)
    # keep track of which components have finished
    tr2_1Components = [tmouse_2, polygon_2, image_7, cmark, cmark2, cmark3, cmark4, cmark5, cmark6, btn_2]
    for thisComponent in tr2_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "tr2_1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *tmouse_2* updates
        if tmouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tmouse_2.frameNStart = frameN  # exact frame index
            tmouse_2.tStart = t  # local t and not account for scr refresh
            tmouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tmouse_2, 'tStartRefresh')  # time at next scr refresh
            tmouse_2.status = STARTED
            tmouse_2.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if tmouse_2.status == STARTED:  # only update if started and not finished!
            x, y = tmouse_2.getPos()
            tmouse_2.x.append(x)
            tmouse_2.y.append(y)
            buttons = tmouse_2.getPressed()
            tmouse_2.leftButton.append(buttons[0])
            tmouse_2.midButton.append(buttons[1])
            tmouse_2.rightButton.append(buttons[2])
            tmouse_2.time.append(tmouse_2.mouseClock.getTime())
        # Run 'Each Frame' code from drg2
        if not drg_in_process:
            for i in range(len(new_scenes)):
                if tmouse_2.isPressedIn(new_scenes[i]):
                    # drag start
                    drg_in_process = True
                    clicked_stim = new_scenes[i]
                    thisExp.addData('scene', new_scene_value[i])
                    # clear list
                    tmouse_2.x = []
                    tmouse_2.y = []
                    tmouse_2.time = []
                    break
        if tmouse_2.getPressed()[0] == 1:
            # set stimulus pos
            if drg_in_process:
                clicked_stim.pos = tmouse_2.getPos()
        else:
            # drag end
            if drg_in_process:
                # record stimulus pos and time
                thisExp.addData('item.x', tmouse_2.x)
                thisExp.addData('item.y', tmouse_2.y)
                thisExp.addData('item.time', tmouse_2.time)
                thisExp.nextEntry()
            drg_in_process = False
        
        
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_2.started')
            polygon_2.setAutoDraw(True)
        
        # *image_7* updates
        if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_7.frameNStart = frameN  # exact frame index
            image_7.tStart = t  # local t and not account for scr refresh
            image_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_7.started')
            image_7.setAutoDraw(True)
        
        # *cmark* updates
        if cmark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cmark.frameNStart = frameN  # exact frame index
            cmark.tStart = t  # local t and not account for scr refresh
            cmark.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cmark, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cmark.started')
            cmark.setAutoDraw(True)
        
        # *cmark2* updates
        if cmark2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cmark2.frameNStart = frameN  # exact frame index
            cmark2.tStart = t  # local t and not account for scr refresh
            cmark2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cmark2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cmark2.started')
            cmark2.setAutoDraw(True)
        
        # *cmark3* updates
        if cmark3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cmark3.frameNStart = frameN  # exact frame index
            cmark3.tStart = t  # local t and not account for scr refresh
            cmark3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cmark3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cmark3.started')
            cmark3.setAutoDraw(True)
        
        # *cmark4* updates
        if cmark4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cmark4.frameNStart = frameN  # exact frame index
            cmark4.tStart = t  # local t and not account for scr refresh
            cmark4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cmark4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cmark4.started')
            cmark4.setAutoDraw(True)
        
        # *cmark5* updates
        if cmark5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cmark5.frameNStart = frameN  # exact frame index
            cmark5.tStart = t  # local t and not account for scr refresh
            cmark5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cmark5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cmark5.started')
            cmark5.setAutoDraw(True)
        
        # *cmark6* updates
        if cmark6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cmark6.frameNStart = frameN  # exact frame index
            cmark6.tStart = t  # local t and not account for scr refresh
            cmark6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cmark6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cmark6.started')
            cmark6.setAutoDraw(True)
        
        # *btn_2* updates
        if btn_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            btn_2.frameNStart = frameN  # exact frame index
            btn_2.tStart = t  # local t and not account for scr refresh
            btn_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(btn_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'btn_2.started')
            btn_2.setAutoDraw(True)
        if btn_2.status == STARTED:
            # check whether btn_2 has been pressed
            if btn_2.isClicked:
                if not btn_2.wasClicked:
                    btn_2.timesOn.append(btn_2.buttonClock.getTime()) # store time of first click
                    btn_2.timesOff.append(btn_2.buttonClock.getTime()) # store time clicked until
                else:
                    btn_2.timesOff[-1] = btn_2.buttonClock.getTime() # update time clicked until
                if not btn_2.wasClicked:
                    
                    continueRoutine = False
                btn_2.wasClicked = True  # if btn_2 is still clicked next frame, it is not a new click
            else:
                btn_2.wasClicked = False  # if btn_2 is clicked next frame, it is a new click
        else:
            btn_2.wasClicked = False  # if btn_2 is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tr2_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "tr2_1" ---
    for thisComponent in tr2_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('tmouse_2.x', tmouse_2.x)
    trials_3.addData('tmouse_2.y', tmouse_2.y)
    trials_3.addData('tmouse_2.leftButton', tmouse_2.leftButton)
    trials_3.addData('tmouse_2.midButton', tmouse_2.midButton)
    trials_3.addData('tmouse_2.rightButton', tmouse_2.rightButton)
    trials_3.addData('tmouse_2.time', tmouse_2.time)
    # Run 'End Routine' code from drg2
    ## record end time
    #thisExp.addData('end_time', mouse.mouseClock.getTime())
    #thisExp.nextEntry()
    
    screenshot = win.getMovieFrame()
    
    screenshot.save('d2data/'+expInfo['participant']+'_count_'+str(count)+'_markmove.png') 
    count += 1
    win.clearBuffer()
    
    drg_in_process = False
    clicked_stim = None
    
    thisExp.nextEntry()
    trials_3.addData('btn_2.numClicks', btn_2.numClicks)
    if btn_2.numClicks:
       trials_3.addData('btn_2.timesOn', btn_2.timesOn)
       trials_3.addData('btn_2.timesOff', btn_2.timesOff)
    else:
       trials_3.addData('btn_2.timesOn', "")
       trials_3.addData('btn_2.timesOff', "")
    # Run 'End Routine' code from code_3
    for i in range(9):
        text_components[i].setAutoDraw(False)
    # the Routine "tr2_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'trials_3'


# --- Prepare to start Routine "intro2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
intro2Components = [key_resp, image_2]
for thisComponent in intro2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_2.started')
        image_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro2" ---
for thisComponent in intro2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "intro2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(arrange_file),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "tr2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # setup some python lists for storing info about the tmouse
    tmouse.x = []
    tmouse.y = []
    tmouse.leftButton = []
    tmouse.midButton = []
    tmouse.rightButton = []
    tmouse.time = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from drg
    # define scene terms
    thisExp.addData("stage","Emotion_Preference")
    
    
    def shuffle_twolist(list1, list2):
        b =  [i for i in range(len(list1))]
        np.random.shuffle(b)
        sorted_list1 = [t[1] for t in sorted(zip(b, list1), key=lambda x: x[0]) ]
        sorted_list2 = [t[1] for t in sorted(zip(b, list2), key=lambda x: x[0]) ]
        return sorted_list1, sorted_list2
    
    scenes = [lmark1, lmark2, lmark3, lmark4, lmark5, lmark6,lmark7, lmark8]
    scene_value = ['CaseAvatar1', 'CaseAvatar2', 'CaseAvatar3', 'CaseAvatar4', 'CaseAvatar5', 'CaseAvatar6', 'CaseAvatar7', 'CaseAvatar8']
    
    new_scenes,new_scene_value = shuffle_twolist(scenes, scene_value)
    #new_scenes,new_scene_value = scenes, scene_valueprint(new_scene_value)
    
    #shuffle(scenes)
    thisExp.addData('scenes', new_scene_value)
    
    # set pos of different figures
    for pointer in range(len(new_scenes)):
        # 0 1 2 3 / 4 5 6 7 
        # 0.45/0.15/-0.25/-0.45 0.15*(x % 4)-0.45
        x = -0.8+(pointer // 6)*0.1
        y = 0.15*(pointer % 6)-0.37
        new_scenes[pointer].setPos([x, y])
        wid, hei = new_scenes[pointer].size
        
        print("wid: ",wid)
    #    if wid > 0.1:
    #        new_scenes[pointer].setSize([new_size, new_size])
        if new_scene_value[pointer].startswith("CaseAvatar"):
            new_scenes[pointer].setSize([new_size, new_size])
        print("V: ",new_scene_value[pointer],'(',x,',',y,')' )
    
    
    
    
    drg_in_process = False
    clicked_stim = None
    
    thisExp.nextEntry()
    
    lmark1.setSize((0.12,0.12))
    lmark1.setImage(t1)
    lmark2.setSize((0.12,0.12))
    lmark2.setImage(t2)
    # Run 'Begin Routine' code from code_2
    for i in range(9):
        text_components[i].setAutoDraw(True)
    lmark3.setSize((0.12,0.12))
    lmark3.setImage(t3)
    lmark4.setSize((0.12,0.12))
    lmark4.setImage(t4)
    lmark5.setSize((0.12,0.12))
    lmark5.setImage(t5)
    lmark6.setSize((0.12,0.12))
    lmark6.setImage(t6)
    lmark7.setSize((0.12,0.12))
    lmark7.setImage(t7)
    lmark8.setSize((0.12,0.12))
    lmark8.setImage(t8)
    # keep track of which components have finished
    tr2Components = [tmouse, polygon, image_6, lmark1, lmark2, btn, lmark3, lmark4, lmark5, lmark6, lmark7, lmark8]
    for thisComponent in tr2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "tr2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *tmouse* updates
        if tmouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tmouse.frameNStart = frameN  # exact frame index
            tmouse.tStart = t  # local t and not account for scr refresh
            tmouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tmouse, 'tStartRefresh')  # time at next scr refresh
            tmouse.status = STARTED
            tmouse.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if tmouse.status == STARTED:  # only update if started and not finished!
            x, y = tmouse.getPos()
            tmouse.x.append(x)
            tmouse.y.append(y)
            buttons = tmouse.getPressed()
            tmouse.leftButton.append(buttons[0])
            tmouse.midButton.append(buttons[1])
            tmouse.rightButton.append(buttons[2])
            tmouse.time.append(tmouse.mouseClock.getTime())
        # Run 'Each Frame' code from drg
        if not drg_in_process:
            for i in range(len(new_scenes)):
                if tmouse.isPressedIn(new_scenes[i]):
                    # drag start
                    drg_in_process = True
                    clicked_stim = new_scenes[i]
                    thisExp.addData('scene', new_scene_value[i])
                    # clear list
                    tmouse.x = []
                    tmouse.y = []
                    tmouse.time = []
                    break
        if tmouse.getPressed()[0] == 1:
            # set stimulus pos
            if drg_in_process:
                clicked_stim.pos = tmouse.getPos()
        else:
            # drag end
            if drg_in_process:
                # record stimulus pos and time
                thisExp.addData('item.x', tmouse.x)
                thisExp.addData('item.y', tmouse.y)
                thisExp.addData('item.time', tmouse.time)
                thisExp.nextEntry()
            drg_in_process = False
        
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon.started')
            polygon.setAutoDraw(True)
        
        # *image_6* updates
        if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_6.frameNStart = frameN  # exact frame index
            image_6.tStart = t  # local t and not account for scr refresh
            image_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_6.started')
            image_6.setAutoDraw(True)
        
        # *lmark1* updates
        if lmark1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lmark1.frameNStart = frameN  # exact frame index
            lmark1.tStart = t  # local t and not account for scr refresh
            lmark1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lmark1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lmark1.started')
            lmark1.setAutoDraw(True)
        
        # *lmark2* updates
        if lmark2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lmark2.frameNStart = frameN  # exact frame index
            lmark2.tStart = t  # local t and not account for scr refresh
            lmark2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lmark2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lmark2.started')
            lmark2.setAutoDraw(True)
        
        # *btn* updates
        if btn.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            btn.frameNStart = frameN  # exact frame index
            btn.tStart = t  # local t and not account for scr refresh
            btn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(btn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'btn.started')
            btn.setAutoDraw(True)
        if btn.status == STARTED:
            # check whether btn has been pressed
            if btn.isClicked:
                if not btn.wasClicked:
                    btn.timesOn.append(btn.buttonClock.getTime()) # store time of first click
                    btn.timesOff.append(btn.buttonClock.getTime()) # store time clicked until
                else:
                    btn.timesOff[-1] = btn.buttonClock.getTime() # update time clicked until
                if not btn.wasClicked:
                    continueRoutine = False  # end routine when btn is clicked
                    
                    continueRoutine = False
                btn.wasClicked = True  # if btn is still clicked next frame, it is not a new click
            else:
                btn.wasClicked = False  # if btn is clicked next frame, it is a new click
        else:
            btn.wasClicked = False  # if btn is clicked next frame, it is a new click
        
        # *lmark3* updates
        if lmark3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lmark3.frameNStart = frameN  # exact frame index
            lmark3.tStart = t  # local t and not account for scr refresh
            lmark3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lmark3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lmark3.started')
            lmark3.setAutoDraw(True)
        
        # *lmark4* updates
        if lmark4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lmark4.frameNStart = frameN  # exact frame index
            lmark4.tStart = t  # local t and not account for scr refresh
            lmark4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lmark4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lmark4.started')
            lmark4.setAutoDraw(True)
        
        # *lmark5* updates
        if lmark5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lmark5.frameNStart = frameN  # exact frame index
            lmark5.tStart = t  # local t and not account for scr refresh
            lmark5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lmark5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lmark5.started')
            lmark5.setAutoDraw(True)
        
        # *lmark6* updates
        if lmark6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lmark6.frameNStart = frameN  # exact frame index
            lmark6.tStart = t  # local t and not account for scr refresh
            lmark6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lmark6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lmark6.started')
            lmark6.setAutoDraw(True)
        
        # *lmark7* updates
        if lmark7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lmark7.frameNStart = frameN  # exact frame index
            lmark7.tStart = t  # local t and not account for scr refresh
            lmark7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lmark7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lmark7.started')
            lmark7.setAutoDraw(True)
        
        # *lmark8* updates
        if lmark8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lmark8.frameNStart = frameN  # exact frame index
            lmark8.tStart = t  # local t and not account for scr refresh
            lmark8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lmark8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'lmark8.started')
            lmark8.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tr2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "tr2" ---
    for thisComponent in tr2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('tmouse.x', tmouse.x)
    trials_2.addData('tmouse.y', tmouse.y)
    trials_2.addData('tmouse.leftButton', tmouse.leftButton)
    trials_2.addData('tmouse.midButton', tmouse.midButton)
    trials_2.addData('tmouse.rightButton', tmouse.rightButton)
    trials_2.addData('tmouse.time', tmouse.time)
    # Run 'End Routine' code from drg
    ## record end time
    #thisExp.addData('end_time', mouse.mouseClock.getTime())
    #thisExp.nextEntry()
    
    screenshot = win.getMovieFrame()
    
    screenshot.save('d2data/'+expInfo['participant']+'_count_'+str(count)+'_markmove.png') 
    count += 1
    win.clearBuffer()
    
    thisExp.nextEntry()
    trials_2.addData('btn.numClicks', btn.numClicks)
    if btn.numClicks:
       trials_2.addData('btn.timesOn', btn.timesOn)
       trials_2.addData('btn.timesOff', btn.timesOff)
    else:
       trials_2.addData('btn.timesOn', "")
       trials_2.addData('btn.timesOff', "")
    # Run 'End Routine' code from code_2
    for i in range(9):
        text_components[i].setAutoDraw(False)
    # the Routine "tr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(arrange_file),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "intro3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    intro3Components = [key_resp_2, image_n]
    for thisComponent in intro3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "intro3" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image_n* updates
        if image_n.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_n.frameNStart = frameN  # exact frame index
            image_n.tStart = t  # local t and not account for scr refresh
            image_n.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_n, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_n.started')
            image_n.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intro3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intro3" ---
    for thisComponent in intro3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials_4.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_4.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "intro3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "tr3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from drag
    # define scene terms
    thisExp.addData("stage","Arrangement")
    
    
    def shuffle_twolist(list1, list2):
        b =  [i for i in range(len(list1))]
        np.random.shuffle(b)
        sorted_list1 = [t[1] for t in sorted(zip(b, list1), key=lambda x: x[0]) ]
        sorted_list2 = [t[1] for t in sorted(zip(b, list2), key=lambda x: x[0]) ]
        return sorted_list1, sorted_list2
    
    scenes = [label1, label2, label3, label4, label5, label6,label7, label8,label9,label10,label11,label12,label13,label14]
    scene_value = ['flower','bin','sofa','plant','mailbox','wash','CaseAvatar1', 'CaseAvatar2', 'CaseAvatar3', 'CaseAvatar4', 'CaseAvatar5', 'CaseAvatar6', 'CaseAvatar7', 'CaseAvatar8']
    
    new_scenes,new_scene_value = shuffle_twolist(scenes, scene_value)
    #new_scenes,new_scene_value = scenes, scene_value
    print(new_scenes)
    print(new_scene_value)
    
    #shuffle(scenes)
    thisExp.addData('scenes', new_scene_value)
    
    
    
    # set pos of different figures
    for pointer in range(len(new_scenes)):
        # 0 1 2 3 / 4 5 6 7 
        # 0.45/0.15/-0.25/-0.45 0.15*(x % 4)-0.45
        x = -0.8+(pointer // 6)*0.1
        y = 0.15*(pointer % 6)-0.37
        new_scenes[pointer].setPos([x, y])
        wid, hei = new_scenes[pointer].size
        print("wid: ",wid)
        if new_scene_value[pointer].startswith("CaseAvatar"):
            new_scenes[pointer].setSize([new_size, new_size])
    
    #    if wid > 0.125 or wid < 0.115:
    #        new_scenes[pointer].setSize([new_size, new_size])
        print(new_scene_value[pointer],'(',x,',',y,')' )
    
    drag_in_process = False
    clicked_stim = None
    
    
    thisExp.nextEntry()
    ## textstime list
    #stimuli = []
    #x_pos = [-0.7, -0.6, -0.5]
    #for i in range(len(scenes)):
    #    stimuli.append(visual.TextStim(win=win, name=str(i), text=scenes[i], 
    #    font='Open Sans', pos=(x_pos[int(i / 4)], 0.3 - 0.1 * (i % 4)),
    #    height=0.03, color='red', colorSpace='rgb'))
    #    stimuli[i].setAutoDraw(True)
    #
    ## used in each frame
    
    #
    ##event.clearEvents()
    label7.setImage(t1)
    label8.setImage(t2)
    label9.setImage(t3)
    label10.setImage(t4)
    label11.setImage(t5)
    label12.setImage(t6)
    label13.setImage(t7)
    label14.setImage(t8)
    # keep track of which components have finished
    tr3Components = [image_3, mouse, scene, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, button]
    for thisComponent in tr3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "tr3" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3.started')
            image_3.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse.status == STARTED:  # only update if started and not finished!
            x, y = mouse.getPos()
            mouse.x.append(x)
            mouse.y.append(y)
            buttons = mouse.getPressed()
            mouse.leftButton.append(buttons[0])
            mouse.midButton.append(buttons[1])
            mouse.rightButton.append(buttons[2])
            mouse.time.append(mouse.mouseClock.getTime())
        # Run 'Each Frame' code from drag
        if not drag_in_process:
            for i in range(len(new_scenes)):
                if mouse.isPressedIn(new_scenes[i]):
                    # drag start
                    drag_in_process = True
                    clicked_stim = new_scenes[i]
                    thisExp.addData('scene', new_scene_value[i])
                    # clear list
                    mouse.x = []
                    mouse.y = []
                    mouse.time = []
                    break
        if mouse.getPressed()[0] == 1:
            # set stimulus pos
            if drag_in_process:
                clicked_stim.pos = mouse.getPos()
        else:
            # drag end
            if drag_in_process:
                # record stimulus pos and time
                thisExp.addData('item.x', mouse.x)
                thisExp.addData('item.y', mouse.y)
                thisExp.addData('item.time', mouse.time)
                thisExp.nextEntry()
            drag_in_process = False
        
        
        # *scene* updates
        if scene.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scene.frameNStart = frameN  # exact frame index
            scene.tStart = t  # local t and not account for scr refresh
            scene.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scene, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'scene.started')
            scene.setAutoDraw(True)
        
        # *label1* updates
        if label1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label1.frameNStart = frameN  # exact frame index
            label1.tStart = t  # local t and not account for scr refresh
            label1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label1.started')
            label1.setAutoDraw(True)
        
        # *label2* updates
        if label2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label2.frameNStart = frameN  # exact frame index
            label2.tStart = t  # local t and not account for scr refresh
            label2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label2.started')
            label2.setAutoDraw(True)
        
        # *label3* updates
        if label3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label3.frameNStart = frameN  # exact frame index
            label3.tStart = t  # local t and not account for scr refresh
            label3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label3.started')
            label3.setAutoDraw(True)
        
        # *label4* updates
        if label4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label4.frameNStart = frameN  # exact frame index
            label4.tStart = t  # local t and not account for scr refresh
            label4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label4.started')
            label4.setAutoDraw(True)
        
        # *label5* updates
        if label5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label5.frameNStart = frameN  # exact frame index
            label5.tStart = t  # local t and not account for scr refresh
            label5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label5.started')
            label5.setAutoDraw(True)
        
        # *label6* updates
        if label6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label6.frameNStart = frameN  # exact frame index
            label6.tStart = t  # local t and not account for scr refresh
            label6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label6.started')
            label6.setAutoDraw(True)
        
        # *label7* updates
        if label7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label7.frameNStart = frameN  # exact frame index
            label7.tStart = t  # local t and not account for scr refresh
            label7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label7.started')
            label7.setAutoDraw(True)
        
        # *label8* updates
        if label8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label8.frameNStart = frameN  # exact frame index
            label8.tStart = t  # local t and not account for scr refresh
            label8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label8.started')
            label8.setAutoDraw(True)
        
        # *label9* updates
        if label9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label9.frameNStart = frameN  # exact frame index
            label9.tStart = t  # local t and not account for scr refresh
            label9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label9.started')
            label9.setAutoDraw(True)
        
        # *label10* updates
        if label10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label10.frameNStart = frameN  # exact frame index
            label10.tStart = t  # local t and not account for scr refresh
            label10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label10.started')
            label10.setAutoDraw(True)
        
        # *label11* updates
        if label11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label11.frameNStart = frameN  # exact frame index
            label11.tStart = t  # local t and not account for scr refresh
            label11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label11.started')
            label11.setAutoDraw(True)
        
        # *label12* updates
        if label12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label12.frameNStart = frameN  # exact frame index
            label12.tStart = t  # local t and not account for scr refresh
            label12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label12.started')
            label12.setAutoDraw(True)
        
        # *label13* updates
        if label13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label13.frameNStart = frameN  # exact frame index
            label13.tStart = t  # local t and not account for scr refresh
            label13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label13.started')
            label13.setAutoDraw(True)
        
        # *label14* updates
        if label14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            label14.frameNStart = frameN  # exact frame index
            label14.tStart = t  # local t and not account for scr refresh
            label14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'label14.started')
            label14.setAutoDraw(True)
        
        # *button* updates
        if button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button.frameNStart = frameN  # exact frame index
            button.tStart = t  # local t and not account for scr refresh
            button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button.started')
            button.setAutoDraw(True)
        if button.status == STARTED:
            # check whether button has been pressed
            if button.isClicked:
                if not button.wasClicked:
                    button.timesOn.append(button.buttonClock.getTime()) # store time of first click
                    button.timesOff.append(button.buttonClock.getTime()) # store time clicked until
                else:
                    button.timesOff[-1] = button.buttonClock.getTime() # update time clicked until
                if not button.wasClicked:
                    
                    continueRoutine = False
                button.wasClicked = True  # if button is still clicked next frame, it is not a new click
            else:
                button.wasClicked = False  # if button is clicked next frame, it is a new click
        else:
            button.wasClicked = False  # if button is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tr3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "tr3" ---
    for thisComponent in tr3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('mouse.x', mouse.x)
    trials_4.addData('mouse.y', mouse.y)
    trials_4.addData('mouse.leftButton', mouse.leftButton)
    trials_4.addData('mouse.midButton', mouse.midButton)
    trials_4.addData('mouse.rightButton', mouse.rightButton)
    trials_4.addData('mouse.time', mouse.time)
    # Run 'End Routine' code from drag
    ## record end time
    #thisExp.addData('end_time', mouse.mouseClock.getTime())
    #thisExp.nextEntry()
    screenshot = win.getMovieFrame()
    screenshot.save('d2data/'+expInfo['participant']+'_'+str(pictype)+'_arrangement.png') 
    win.clearBuffer()
    trials_4.addData('button.numClicks', button.numClicks)
    if button.numClicks:
       trials_4.addData('button.timesOn', button.timesOn)
       trials_4.addData('button.timesOff', button.timesOff)
    else:
       trials_4.addData('button.timesOn', "")
       trials_4.addData('button.timesOff', "")
    # the Routine "tr3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_4'


# --- Prepare to start Routine "thanks" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
thanksComponents = [key_resp_3, thankstext]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "thanks" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_3.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_3.tStop = t  # not accounting for scr refresh
            key_resp_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
            key_resp_3.status = FINISHED
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *thankstext* updates
    if thankstext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thankstext.frameNStart = frameN  # exact frame index
        thankstext.tStart = t  # local t and not account for scr refresh
        thankstext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thankstext, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thankstext.started')
        thankstext.setAutoDraw(True)
    if thankstext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thankstext.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            thankstext.tStop = t  # not accounting for scr refresh
            thankstext.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thankstext.stopped')
            thankstext.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "thanks" ---
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
