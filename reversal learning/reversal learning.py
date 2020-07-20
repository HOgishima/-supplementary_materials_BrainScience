#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Mon Nov 20 10:08:53 2017
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'reversal learning'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
image = visual.ImageStim(win=win, name='image',units='pix', 
    image='./rl_instruction_rev.png', mask=None,
    ori=0, pos=[0, 0], size=[1366, 768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blank"
blankClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
cross1 = visual.Rect(win=win, name='cross1',units='pix', 
    width=[5, 50][0], height=[5, 50][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1,depth=0.0, 
interpolate=True)
closs2 = visual.Rect(win=win, name='closs2',units='pix', 
    width=[5, 50][0], height=[5, 50][1],
    ori=90, pos=[0, 0],
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
squre_right = visual.Rect(win=win, name='squre_right',units='pix', 
    width=[300, 250][0], height=[300, 250][1],
    ori=0, pos=[400, 0],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1,depth=-4.0, 
interpolate=True)
squre_left = visual.Rect(win=win, name='squre_left',units='pix', 
    width=[300, 250][0], height=[300, 250][1],
    ori=0, pos=[-400, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,depth=-5.0, 
interpolate=True)
squre_top = visual.Rect(win=win, name='squre_top',units='pix', 
    width=[300, 250][0], height=[300, 250][1],
    ori=0, pos=[0, 200],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1,depth=-6.0, 
interpolate=True)
squre_bottom = visual.Rect(win=win, name='squre_bottom',units='pix', 
    width=[300, 250][0], height=[300, 250][1],
    ori=0, pos=[0, -200],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1,depth=-7.0, 
interpolate=True)
circle1 = visual.Polygon(win=win, name='circle1',units='pix', 
    edges = 40, size=[250, 250],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='green', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1,depth=-8.0, 
interpolate=True)
circle2 = visual.Polygon(win=win, name='circle2',units='pix', 
    edges = 40, size=[250, 250],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1,depth=-9.0, 
interpolate=True)


# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
textFeedback = visual.TextStim(win=win, ori=0, name='textFeedback',
    text='default text',    font='Arial',
    units='pix', pos=[0, 0], height=50, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Please click the enter',    font='Arial',
    units='pix', pos=[0, -120], height=36, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
image = visual.ImageStim(win=win, name='image',units='pix', 
    image='./rl_instruction_rev.png', mask=None,
    ori=0, pos=[0, 0], size=[1366, 768],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blank"
blankClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
cross1 = visual.Rect(win=win, name='cross1',units='pix', 
    width=[5, 50][0], height=[5, 50][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1,depth=0.0, 
interpolate=True)
closs2 = visual.Rect(win=win, name='closs2',units='pix', 
    width=[5, 50][0], height=[5, 50][1],
    ori=90, pos=[0, 0],
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
squre_right = visual.Rect(win=win, name='squre_right',units='pix', 
    width=[300, 250][0], height=[300, 250][1],
    ori=0, pos=[400, 0],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1,depth=-4.0, 
interpolate=True)
squre_left = visual.Rect(win=win, name='squre_left',units='pix', 
    width=[300, 250][0], height=[300, 250][1],
    ori=0, pos=[-400, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,depth=-5.0, 
interpolate=True)
squre_top = visual.Rect(win=win, name='squre_top',units='pix', 
    width=[300, 250][0], height=[300, 250][1],
    ori=0, pos=[0, 200],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1,depth=-6.0, 
interpolate=True)
squre_bottom = visual.Rect(win=win, name='squre_bottom',units='pix', 
    width=[300, 250][0], height=[300, 250][1],
    ori=0, pos=[0, -200],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1,depth=-7.0, 
interpolate=True)
circle1 = visual.Polygon(win=win, name='circle1',units='pix', 
    edges = 40, size=[250, 250],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='green', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1,depth=-8.0, 
interpolate=True)
circle2 = visual.Polygon(win=win, name='circle2',units='pix', 
    edges = 40, size=[250, 250],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1,depth=-9.0, 
interpolate=True)


# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
textFeedback = visual.TextStim(win=win, ori=0, name='textFeedback',
    text='default text',    font='Arial',
    units='pix', pos=[0, 0], height=50, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Please click the enter',    font='Arial',
    units='pix', pos=[0, -120], height=36, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
cross1 = visual.Rect(win=win, name='cross1',units='pix', 
    width=[5, 50][0], height=[5, 50][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1,depth=0.0, 
interpolate=True)
closs2 = visual.Rect(win=win, name='closs2',units='pix', 
    width=[5, 50][0], height=[5, 50][1],
    ori=90, pos=[0, 0],
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
squre_right = visual.Rect(win=win, name='squre_right',units='pix', 
    width=[300, 250][0], height=[300, 250][1],
    ori=0, pos=[400, 0],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1,depth=-4.0, 
interpolate=True)
squre_left = visual.Rect(win=win, name='squre_left',units='pix', 
    width=[300, 250][0], height=[300, 250][1],
    ori=0, pos=[-400, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,depth=-5.0, 
interpolate=True)
squre_top = visual.Rect(win=win, name='squre_top',units='pix', 
    width=[300, 250][0], height=[300, 250][1],
    ori=0, pos=[0, 200],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1,depth=-6.0, 
interpolate=True)
squre_bottom = visual.Rect(win=win, name='squre_bottom',units='pix', 
    width=[300, 250][0], height=[300, 250][1],
    ori=0, pos=[0, -200],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1,depth=-7.0, 
interpolate=True)
circle1 = visual.Polygon(win=win, name='circle1',units='pix', 
    edges = 40, size=[250, 250],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='green', lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1,depth=-8.0, 
interpolate=True)
circle2 = visual.Polygon(win=win, name='circle2',units='pix', 
    edges = 40, size=[250, 250],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1,depth=-9.0, 
interpolate=True)


# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
textFeedback = visual.TextStim(win=win, ori=0, name='textFeedback',
    text='default text',    font='Arial',
    units='pix', pos=[0, 0], height=50, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Please click the enter',    font='Arial',
    units='pix', pos=[0, -120], height=36, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='Thank you for your participation.',    font='Arial',
    units='pix', pos=[0, 0], height=36, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
instructionComponents = []
instructionComponents.append(image)
instructionComponents.append(key_resp_5)
for thisComponent in instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instruction"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if t >= 0.0 and image.status == NOT_STARTED:
        # keep track of start time/frame for later
        image.tStart = t  # underestimates by a little under one frame
        image.frameNStart = frameN  # exact frame index
        image.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        key_resp_5.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['return', 'num_enter'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
   key_resp_5.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "blank"-------
t = 0
blankClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = []
blankComponents.append(text_3)
for thisComponent in blankComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "blank"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blankClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    if text_3.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "blank"-------
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('stim_pos_practice.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_correct = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_correct.status = NOT_STARTED
    key_resp_faulse = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_faulse.status = NOT_STARTED
    circle1.setPos([stim1_posx, stim1_posy])
    circle2.setPos([stim2_posx, stim2_posy])
    
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_6.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(cross1)
    trialComponents.append(closs2)
    trialComponents.append(key_resp_correct)
    trialComponents.append(key_resp_faulse)
    trialComponents.append(squre_right)
    trialComponents.append(squre_left)
    trialComponents.append(squre_top)
    trialComponents.append(squre_bottom)
    trialComponents.append(circle1)
    trialComponents.append(circle2)
    trialComponents.append(key_resp_3)
    trialComponents.append(key_resp_6)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross1* updates
        if t >= 0.0 and cross1.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross1.tStart = t  # underestimates by a little under one frame
            cross1.frameNStart = frameN  # exact frame index
            cross1.setAutoDraw(True)
        if cross1.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            cross1.setAutoDraw(False)
        
        # *closs2* updates
        if t >= 0.0 and closs2.status == NOT_STARTED:
            # keep track of start time/frame for later
            closs2.tStart = t  # underestimates by a little under one frame
            closs2.frameNStart = frameN  # exact frame index
            closs2.setAutoDraw(True)
        if closs2.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            closs2.setAutoDraw(False)
        
        # *key_resp_correct* updates
        if t >= 3 and key_resp_correct.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_correct.tStart = t  # underestimates by a little under one frame
            key_resp_correct.frameNStart = frameN  # exact frame index
            key_resp_correct.status = STARTED
            # AllowedKeys looks like a variable named `correctAns`
            if not 'correctAns' in locals():
                logging.error('AllowedKeys variable `correctAns` is not defined.')
                core.quit()
            if not type(correctAns) in [list, tuple, np.ndarray]:
                if not isinstance(correctAns, basestring):
                    logging.error('AllowedKeys variable `correctAns` is not string- or list-like.')
                    core.quit()
                elif not ',' in correctAns: correctAns = (correctAns,)
                else:  correctAns = eval(correctAns)
            # keyboard checking is just starting
            key_resp_correct.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_correct.status == STARTED:
            theseKeys = event.getKeys(keyList=list(correctAns))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_correct.keys = theseKeys[-1]  # just the last key pressed
                key_resp_correct.rt = key_resp_correct.clock.getTime()
                # was this 'correct'?
                if (key_resp_correct.keys == str(correctAns)) or (key_resp_correct.keys == correctAns):
                    key_resp_correct.corr = 1
                else:
                    key_resp_correct.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *key_resp_faulse* updates
        if t >= 3 and key_resp_faulse.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_faulse.tStart = t  # underestimates by a little under one frame
            key_resp_faulse.frameNStart = frameN  # exact frame index
            key_resp_faulse.status = STARTED
            # AllowedKeys looks like a variable named `faulseAns`
            if not 'faulseAns' in locals():
                logging.error('AllowedKeys variable `faulseAns` is not defined.')
                core.quit()
            if not type(faulseAns) in [list, tuple, np.ndarray]:
                if not isinstance(faulseAns, basestring):
                    logging.error('AllowedKeys variable `faulseAns` is not string- or list-like.')
                    core.quit()
                elif not ',' in faulseAns: faulseAns = (faulseAns,)
                else:  faulseAns = eval(faulseAns)
            # keyboard checking is just starting
            key_resp_faulse.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_faulse.status == STARTED:
            theseKeys = event.getKeys(keyList=list(faulseAns))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_faulse.keys = theseKeys[-1]  # just the last key pressed
                key_resp_faulse.rt = key_resp_faulse.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *squre_right* updates
        if t >= 3 and squre_right.status == NOT_STARTED:
            # keep track of start time/frame for later
            squre_right.tStart = t  # underestimates by a little under one frame
            squre_right.frameNStart = frameN  # exact frame index
            squre_right.setAutoDraw(True)
        
        # *squre_left* updates
        if t >= 3 and squre_left.status == NOT_STARTED:
            # keep track of start time/frame for later
            squre_left.tStart = t  # underestimates by a little under one frame
            squre_left.frameNStart = frameN  # exact frame index
            squre_left.setAutoDraw(True)
        
        # *squre_top* updates
        if t >= 3 and squre_top.status == NOT_STARTED:
            # keep track of start time/frame for later
            squre_top.tStart = t  # underestimates by a little under one frame
            squre_top.frameNStart = frameN  # exact frame index
            squre_top.setAutoDraw(True)
        
        # *squre_bottom* updates
        if t >= 3 and squre_bottom.status == NOT_STARTED:
            # keep track of start time/frame for later
            squre_bottom.tStart = t  # underestimates by a little under one frame
            squre_bottom.frameNStart = frameN  # exact frame index
            squre_bottom.setAutoDraw(True)
        
        # *circle1* updates
        if t >= 3 and circle1.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle1.tStart = t  # underestimates by a little under one frame
            circle1.frameNStart = frameN  # exact frame index
            circle1.setAutoDraw(True)
        
        # *circle2* updates
        if t >= 3 and circle2.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle2.tStart = t  # underestimates by a little under one frame
            circle2.frameNStart = frameN  # exact frame index
            circle2.setAutoDraw(True)
        
        
        # *key_resp_3* updates
        if t >= 3 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            key_resp_3.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', '4', '6', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
                # was this 'correct'?
                if (key_resp_3.keys == str(num_correnctAns)) or (key_resp_3.keys == num_correnctAns):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *key_resp_6* updates
        if t >= 3 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t  # underestimates by a little under one frame
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            key_resp_6.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', '4', '6', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6.keys = theseKeys[-1]  # just the last key pressed
                key_resp_6.rt = key_resp_6.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_correct.keys in ['', [], None]:  # No response was made
       key_resp_correct.keys=None
       # was no response the correct answer?!
       if str(correctAns).lower() == 'none': key_resp_correct.corr = 1  # correct non-response
       else: key_resp_correct.corr = 0  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('key_resp_correct.keys',key_resp_correct.keys)
    trials_3.addData('key_resp_correct.corr', key_resp_correct.corr)
    if key_resp_correct.keys != None:  # we had a response
        trials_3.addData('key_resp_correct.rt', key_resp_correct.rt)
    # check responses
    if key_resp_faulse.keys in ['', [], None]:  # No response was made
       key_resp_faulse.keys=None
    # store data for trials_3 (TrialHandler)
    trials_3.addData('key_resp_faulse.keys',key_resp_faulse.keys)
    if key_resp_faulse.keys != None:  # we had a response
        trials_3.addData('key_resp_faulse.rt', key_resp_faulse.rt)
    if  key_resp_correct.keys:
        feedbackMsg = u'true'
    else:
        feedbackMsg = u'false'
    
    
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
       key_resp_3.keys=None
       # was no response the correct answer?!
       if str(num_correnctAns).lower() == 'none': key_resp_3.corr = 1  # correct non-response
       else: key_resp_3.corr = 0  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('key_resp_3.keys',key_resp_3.keys)
    trials_3.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        trials_3.addData('key_resp_3.rt', key_resp_3.rt)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
       key_resp_6.keys=None
    # store data for trials_3 (TrialHandler)
    trials_3.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        trials_3.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    textFeedback.setText(feedbackMsg)
    # keep track of which components have finished
    feedbackComponents = []
    feedbackComponents.append(key_resp_2)
    feedbackComponents.append(textFeedback)
    feedbackComponents.append(text_2)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['return', 'num_enter'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *textFeedback* updates
        if t >= 0.0 and textFeedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            textFeedback.tStart = t  # underestimates by a little under one frame
            textFeedback.frameNStart = frameN  # exact frame index
            textFeedback.setAutoDraw(True)
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
    # store data for trials_3 (TrialHandler)
    trials_3.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_3.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


#------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
instructionComponents = []
instructionComponents.append(image)
instructionComponents.append(key_resp_5)
for thisComponent in instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instruction"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if t >= 0.0 and image.status == NOT_STARTED:
        # keep track of start time/frame for later
        image.tStart = t  # underestimates by a little under one frame
        image.frameNStart = frameN  # exact frame index
        image.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        key_resp_5.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['return', 'num_enter'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
   key_resp_5.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "blank"-------
t = 0
blankClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = []
blankComponents.append(text_3)
for thisComponent in blankComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "blank"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blankClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    if text_3.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "blank"-------
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('stim_pos.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_correct = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_correct.status = NOT_STARTED
    key_resp_faulse = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_faulse.status = NOT_STARTED
    circle1.setPos([stim1_posx, stim1_posy])
    circle2.setPos([stim2_posx, stim2_posy])
    
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_6.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(cross1)
    trialComponents.append(closs2)
    trialComponents.append(key_resp_correct)
    trialComponents.append(key_resp_faulse)
    trialComponents.append(squre_right)
    trialComponents.append(squre_left)
    trialComponents.append(squre_top)
    trialComponents.append(squre_bottom)
    trialComponents.append(circle1)
    trialComponents.append(circle2)
    trialComponents.append(key_resp_3)
    trialComponents.append(key_resp_6)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross1* updates
        if t >= 0.0 and cross1.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross1.tStart = t  # underestimates by a little under one frame
            cross1.frameNStart = frameN  # exact frame index
            cross1.setAutoDraw(True)
        if cross1.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            cross1.setAutoDraw(False)
        
        # *closs2* updates
        if t >= 0.0 and closs2.status == NOT_STARTED:
            # keep track of start time/frame for later
            closs2.tStart = t  # underestimates by a little under one frame
            closs2.frameNStart = frameN  # exact frame index
            closs2.setAutoDraw(True)
        if closs2.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            closs2.setAutoDraw(False)
        
        # *key_resp_correct* updates
        if t >= 3 and key_resp_correct.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_correct.tStart = t  # underestimates by a little under one frame
            key_resp_correct.frameNStart = frameN  # exact frame index
            key_resp_correct.status = STARTED
            # AllowedKeys looks like a variable named `correctAns`
            if not 'correctAns' in locals():
                logging.error('AllowedKeys variable `correctAns` is not defined.')
                core.quit()
            if not type(correctAns) in [list, tuple, np.ndarray]:
                if not isinstance(correctAns, basestring):
                    logging.error('AllowedKeys variable `correctAns` is not string- or list-like.')
                    core.quit()
                elif not ',' in correctAns: correctAns = (correctAns,)
                else:  correctAns = eval(correctAns)
            # keyboard checking is just starting
            key_resp_correct.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_correct.status == STARTED:
            theseKeys = event.getKeys(keyList=list(correctAns))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_correct.keys = theseKeys[-1]  # just the last key pressed
                key_resp_correct.rt = key_resp_correct.clock.getTime()
                # was this 'correct'?
                if (key_resp_correct.keys == str(correctAns)) or (key_resp_correct.keys == correctAns):
                    key_resp_correct.corr = 1
                else:
                    key_resp_correct.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *key_resp_faulse* updates
        if t >= 3 and key_resp_faulse.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_faulse.tStart = t  # underestimates by a little under one frame
            key_resp_faulse.frameNStart = frameN  # exact frame index
            key_resp_faulse.status = STARTED
            # AllowedKeys looks like a variable named `faulseAns`
            if not 'faulseAns' in locals():
                logging.error('AllowedKeys variable `faulseAns` is not defined.')
                core.quit()
            if not type(faulseAns) in [list, tuple, np.ndarray]:
                if not isinstance(faulseAns, basestring):
                    logging.error('AllowedKeys variable `faulseAns` is not string- or list-like.')
                    core.quit()
                elif not ',' in faulseAns: faulseAns = (faulseAns,)
                else:  faulseAns = eval(faulseAns)
            # keyboard checking is just starting
            key_resp_faulse.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_faulse.status == STARTED:
            theseKeys = event.getKeys(keyList=list(faulseAns))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_faulse.keys = theseKeys[-1]  # just the last key pressed
                key_resp_faulse.rt = key_resp_faulse.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *squre_right* updates
        if t >= 3 and squre_right.status == NOT_STARTED:
            # keep track of start time/frame for later
            squre_right.tStart = t  # underestimates by a little under one frame
            squre_right.frameNStart = frameN  # exact frame index
            squre_right.setAutoDraw(True)
        
        # *squre_left* updates
        if t >= 3 and squre_left.status == NOT_STARTED:
            # keep track of start time/frame for later
            squre_left.tStart = t  # underestimates by a little under one frame
            squre_left.frameNStart = frameN  # exact frame index
            squre_left.setAutoDraw(True)
        
        # *squre_top* updates
        if t >= 3 and squre_top.status == NOT_STARTED:
            # keep track of start time/frame for later
            squre_top.tStart = t  # underestimates by a little under one frame
            squre_top.frameNStart = frameN  # exact frame index
            squre_top.setAutoDraw(True)
        
        # *squre_bottom* updates
        if t >= 3 and squre_bottom.status == NOT_STARTED:
            # keep track of start time/frame for later
            squre_bottom.tStart = t  # underestimates by a little under one frame
            squre_bottom.frameNStart = frameN  # exact frame index
            squre_bottom.setAutoDraw(True)
        
        # *circle1* updates
        if t >= 3 and circle1.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle1.tStart = t  # underestimates by a little under one frame
            circle1.frameNStart = frameN  # exact frame index
            circle1.setAutoDraw(True)
        
        # *circle2* updates
        if t >= 3 and circle2.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle2.tStart = t  # underestimates by a little under one frame
            circle2.frameNStart = frameN  # exact frame index
            circle2.setAutoDraw(True)
        
        
        # *key_resp_3* updates
        if t >= 3 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            key_resp_3.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', '4', '6', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
                # was this 'correct'?
                if (key_resp_3.keys == str(num_correnctAns)) or (key_resp_3.keys == num_correnctAns):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *key_resp_6* updates
        if t >= 3 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t  # underestimates by a little under one frame
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            key_resp_6.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', '4', '6', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6.keys = theseKeys[-1]  # just the last key pressed
                key_resp_6.rt = key_resp_6.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_correct.keys in ['', [], None]:  # No response was made
       key_resp_correct.keys=None
       # was no response the correct answer?!
       if str(correctAns).lower() == 'none': key_resp_correct.corr = 1  # correct non-response
       else: key_resp_correct.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_correct.keys',key_resp_correct.keys)
    trials.addData('key_resp_correct.corr', key_resp_correct.corr)
    if key_resp_correct.keys != None:  # we had a response
        trials.addData('key_resp_correct.rt', key_resp_correct.rt)
    # check responses
    if key_resp_faulse.keys in ['', [], None]:  # No response was made
       key_resp_faulse.keys=None
    # store data for trials (TrialHandler)
    trials.addData('key_resp_faulse.keys',key_resp_faulse.keys)
    if key_resp_faulse.keys != None:  # we had a response
        trials.addData('key_resp_faulse.rt', key_resp_faulse.rt)
    if  key_resp_correct.keys:
        feedbackMsg = u'true'
    else:
        feedbackMsg = u'false'
    
    
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
       key_resp_3.keys=None
       # was no response the correct answer?!
       if str(num_correnctAns).lower() == 'none': key_resp_3.corr = 1  # correct non-response
       else: key_resp_3.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    trials.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
       key_resp_6.keys=None
    # store data for trials (TrialHandler)
    trials.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        trials.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    textFeedback.setText(feedbackMsg)
    # keep track of which components have finished
    feedbackComponents = []
    feedbackComponents.append(key_resp_2)
    feedbackComponents.append(textFeedback)
    feedbackComponents.append(text_2)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['return', 'num_enter'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *textFeedback* updates
        if t >= 0.0 and textFeedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            textFeedback.tStart = t  # underestimates by a little under one frame
            textFeedback.frameNStart = frameN  # exact frame index
            textFeedback.setAutoDraw(True)
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
    # store data for trials (TrialHandler)
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('stim_pos_rev.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_correct = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_correct.status = NOT_STARTED
    key_resp_faulse = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_faulse.status = NOT_STARTED
    circle1.setPos([stim1_posx, stim1_posy])
    circle2.setPos([stim2_posx, stim2_posy])
    
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_6.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(cross1)
    trialComponents.append(closs2)
    trialComponents.append(key_resp_correct)
    trialComponents.append(key_resp_faulse)
    trialComponents.append(squre_right)
    trialComponents.append(squre_left)
    trialComponents.append(squre_top)
    trialComponents.append(squre_bottom)
    trialComponents.append(circle1)
    trialComponents.append(circle2)
    trialComponents.append(key_resp_3)
    trialComponents.append(key_resp_6)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross1* updates
        if t >= 0.0 and cross1.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross1.tStart = t  # underestimates by a little under one frame
            cross1.frameNStart = frameN  # exact frame index
            cross1.setAutoDraw(True)
        if cross1.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            cross1.setAutoDraw(False)
        
        # *closs2* updates
        if t >= 0.0 and closs2.status == NOT_STARTED:
            # keep track of start time/frame for later
            closs2.tStart = t  # underestimates by a little under one frame
            closs2.frameNStart = frameN  # exact frame index
            closs2.setAutoDraw(True)
        if closs2.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            closs2.setAutoDraw(False)
        
        # *key_resp_correct* updates
        if t >= 3 and key_resp_correct.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_correct.tStart = t  # underestimates by a little under one frame
            key_resp_correct.frameNStart = frameN  # exact frame index
            key_resp_correct.status = STARTED
            # AllowedKeys looks like a variable named `correctAns`
            if not 'correctAns' in locals():
                logging.error('AllowedKeys variable `correctAns` is not defined.')
                core.quit()
            if not type(correctAns) in [list, tuple, np.ndarray]:
                if not isinstance(correctAns, basestring):
                    logging.error('AllowedKeys variable `correctAns` is not string- or list-like.')
                    core.quit()
                elif not ',' in correctAns: correctAns = (correctAns,)
                else:  correctAns = eval(correctAns)
            # keyboard checking is just starting
            key_resp_correct.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_correct.status == STARTED:
            theseKeys = event.getKeys(keyList=list(correctAns))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_correct.keys = theseKeys[-1]  # just the last key pressed
                key_resp_correct.rt = key_resp_correct.clock.getTime()
                # was this 'correct'?
                if (key_resp_correct.keys == str(correctAns)) or (key_resp_correct.keys == correctAns):
                    key_resp_correct.corr = 1
                else:
                    key_resp_correct.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *key_resp_faulse* updates
        if t >= 3 and key_resp_faulse.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_faulse.tStart = t  # underestimates by a little under one frame
            key_resp_faulse.frameNStart = frameN  # exact frame index
            key_resp_faulse.status = STARTED
            # AllowedKeys looks like a variable named `faulseAns`
            if not 'faulseAns' in locals():
                logging.error('AllowedKeys variable `faulseAns` is not defined.')
                core.quit()
            if not type(faulseAns) in [list, tuple, np.ndarray]:
                if not isinstance(faulseAns, basestring):
                    logging.error('AllowedKeys variable `faulseAns` is not string- or list-like.')
                    core.quit()
                elif not ',' in faulseAns: faulseAns = (faulseAns,)
                else:  faulseAns = eval(faulseAns)
            # keyboard checking is just starting
            key_resp_faulse.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_faulse.status == STARTED:
            theseKeys = event.getKeys(keyList=list(faulseAns))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_faulse.keys = theseKeys[-1]  # just the last key pressed
                key_resp_faulse.rt = key_resp_faulse.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *squre_right* updates
        if t >= 3 and squre_right.status == NOT_STARTED:
            # keep track of start time/frame for later
            squre_right.tStart = t  # underestimates by a little under one frame
            squre_right.frameNStart = frameN  # exact frame index
            squre_right.setAutoDraw(True)
        
        # *squre_left* updates
        if t >= 3 and squre_left.status == NOT_STARTED:
            # keep track of start time/frame for later
            squre_left.tStart = t  # underestimates by a little under one frame
            squre_left.frameNStart = frameN  # exact frame index
            squre_left.setAutoDraw(True)
        
        # *squre_top* updates
        if t >= 3 and squre_top.status == NOT_STARTED:
            # keep track of start time/frame for later
            squre_top.tStart = t  # underestimates by a little under one frame
            squre_top.frameNStart = frameN  # exact frame index
            squre_top.setAutoDraw(True)
        
        # *squre_bottom* updates
        if t >= 3 and squre_bottom.status == NOT_STARTED:
            # keep track of start time/frame for later
            squre_bottom.tStart = t  # underestimates by a little under one frame
            squre_bottom.frameNStart = frameN  # exact frame index
            squre_bottom.setAutoDraw(True)
        
        # *circle1* updates
        if t >= 3 and circle1.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle1.tStart = t  # underestimates by a little under one frame
            circle1.frameNStart = frameN  # exact frame index
            circle1.setAutoDraw(True)
        
        # *circle2* updates
        if t >= 3 and circle2.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle2.tStart = t  # underestimates by a little under one frame
            circle2.frameNStart = frameN  # exact frame index
            circle2.setAutoDraw(True)
        
        
        # *key_resp_3* updates
        if t >= 3 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            key_resp_3.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', '4', '6', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
                # was this 'correct'?
                if (key_resp_3.keys == str(num_correnctAns)) or (key_resp_3.keys == num_correnctAns):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *key_resp_6* updates
        if t >= 3 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t  # underestimates by a little under one frame
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            key_resp_6.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', '4', '6', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6.keys = theseKeys[-1]  # just the last key pressed
                key_resp_6.rt = key_resp_6.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_correct.keys in ['', [], None]:  # No response was made
       key_resp_correct.keys=None
       # was no response the correct answer?!
       if str(correctAns).lower() == 'none': key_resp_correct.corr = 1  # correct non-response
       else: key_resp_correct.corr = 0  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_correct.keys',key_resp_correct.keys)
    trials_2.addData('key_resp_correct.corr', key_resp_correct.corr)
    if key_resp_correct.keys != None:  # we had a response
        trials_2.addData('key_resp_correct.rt', key_resp_correct.rt)
    # check responses
    if key_resp_faulse.keys in ['', [], None]:  # No response was made
       key_resp_faulse.keys=None
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_faulse.keys',key_resp_faulse.keys)
    if key_resp_faulse.keys != None:  # we had a response
        trials_2.addData('key_resp_faulse.rt', key_resp_faulse.rt)
    if  key_resp_correct.keys:
        feedbackMsg = u'true'
    else:
        feedbackMsg = u'false'
    
    
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
       key_resp_3.keys=None
       # was no response the correct answer?!
       if str(num_correnctAns).lower() == 'none': key_resp_3.corr = 1  # correct non-response
       else: key_resp_3.corr = 0  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_3.keys',key_resp_3.keys)
    trials_2.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        trials_2.addData('key_resp_3.rt', key_resp_3.rt)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
       key_resp_6.keys=None
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        trials_2.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    textFeedback.setText(feedbackMsg)
    # keep track of which components have finished
    feedbackComponents = []
    feedbackComponents.append(key_resp_2)
    feedbackComponents.append(textFeedback)
    feedbackComponents.append(text_2)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['return', 'num_enter'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *textFeedback* updates
        if t >= 0.0 and textFeedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            textFeedback.tStart = t  # underestimates by a little under one frame
            textFeedback.frameNStart = frameN  # exact frame index
            textFeedback.setAutoDraw(True)
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_2.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


#------Prepare to start Routine "Thanks"-------
t = 0
ThanksClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
ThanksComponents = []
ThanksComponents.append(text)
ThanksComponents.append(key_resp_4)
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Thanks"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = ThanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['return', 'num_enter'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
   key_resp_4.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "Thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



win.close()
core.quit()
