/*************************************** 
 * Vr_Memory_Test_Day2_Screenshot Test *
 ***************************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'VR_Memory_Test_Day2_Screenshot';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
var px_pos;
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(introRoutineBegin());
flowScheduler.add(introRoutineEachFrame());
flowScheduler.add(introRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
const trials_4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_4LoopBegin(trials_4LoopScheduler));
flowScheduler.add(trials_4LoopScheduler);
flowScheduler.add(trials_4LoopEnd);
flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'materials/9_roadtrack.png', 'path': 'materials/9_roadtrack.png'},
    {'name': 'materials/14_barbershop.png', 'path': 'materials/14_barbershop.png'},
    {'name': 'materials/3_dis_sofa.PNG', 'path': 'materials/3_dis_sofa.PNG'},
    {'name': 'materials/7_dis_tree.png', 'path': 'materials/7_dis_tree.png'},
    {'name': 'Avatar/Case_8.png', 'path': 'Avatar/Case_8.png'},
    {'name': 'material2/1_flower.PNG', 'path': 'material2/1_flower.PNG'},
    {'name': 'materials/13_dis_cafe.png', 'path': 'materials/13_dis_cafe.png'},
    {'name': 'Avatar/Case_7.png', 'path': 'Avatar/Case_7.png'},
    {'name': 'orderexcel/pair_drag_2.xlsx', 'path': 'orderexcel/pair_drag_2.xlsx'},
    {'name': 'materials/15_dis_police.png', 'path': 'materials/15_dis_police.png'},
    {'name': 'Avatar/Case_1.png', 'path': 'Avatar/Case_1.png'},
    {'name': 'orderexcel/pair_drag_3.xlsx', 'path': 'orderexcel/pair_drag_3.xlsx'},
    {'name': 'materials/12_dis_bank.png', 'path': 'materials/12_dis_bank.png'},
    {'name': 'Avatar/Case_4.png', 'path': 'Avatar/Case_4.png'},
    {'name': 'materials/6_wash.PNG', 'path': 'materials/6_wash.PNG'},
    {'name': 'orderexcel/pair_drag_1.xlsx', 'path': 'orderexcel/pair_drag_1.xlsx'},
    {'name': 'TestM3.PNG', 'path': 'TestM3.PNG'},
    {'name': 'Avatar/Male_21.png', 'path': 'Avatar/Male_21.png'},
    {'name': 'materials/11_dis_building.png', 'path': 'materials/11_dis_building.png'},
    {'name': 'Avatar/Female_31.png', 'path': 'Avatar/Female_31.png'},
    {'name': 'material2/6_wash.PNG', 'path': 'material2/6_wash.PNG'},
    {'name': 'materials/12_gym.png', 'path': 'materials/12_gym.png'},
    {'name': 'materials/1_dis_cola.png', 'path': 'materials/1_dis_cola.png'},
    {'name': 'material2/2_bin.PNG', 'path': 'material2/2_bin.PNG'},
    {'name': 'materials/10_trash.png', 'path': 'materials/10_trash.png'},
    {'name': 'material2/4_plant.PNG', 'path': 'material2/4_plant.PNG'},
    {'name': 'Avatar/Case_6.png', 'path': 'Avatar/Case_6.png'},
    {'name': 'materials/13_hospital.png', 'path': 'materials/13_hospital.png'},
    {'name': 'Avatar/Female_23.png', 'path': 'Avatar/Female_23.png'},
    {'name': 'materials/4_dis_lemontree.PNG', 'path': 'materials/4_dis_lemontree.PNG'},
    {'name': 'materials/16_dis_castle.PNG', 'path': 'materials/16_dis_castle.PNG'},
    {'name': 'materials/2_bin.PNG', 'path': 'materials/2_bin.PNG'},
    {'name': 'materials/9_dis_mailbox.png', 'path': 'materials/9_dis_mailbox.png'},
    {'name': 'materials/5_dis_chair.png', 'path': 'materials/5_dis_chair.png'},
    {'name': 'materials/14_dis_hotel.png', 'path': 'materials/14_dis_hotel.png'},
    {'name': 'p.png', 'path': 'p.png'},
    {'name': 'Avatar/Male_33.png', 'path': 'Avatar/Male_33.png'},
    {'name': 'materials/2_dis_Traflight.png', 'path': 'materials/2_dis_Traflight.png'},
    {'name': 'materials/6_dis_booth.PNG', 'path': 'materials/6_dis_booth.PNG'},
    {'name': 'materials/8_dis_wash.png', 'path': 'materials/8_dis_wash.png'},
    {'name': 'material2/3_sofa.PNG', 'path': 'material2/3_sofa.PNG'},
    {'name': 'materials/10_dis_car.png', 'path': 'materials/10_dis_car.png'},
    {'name': 'Avatar/Female_29.png', 'path': 'Avatar/Female_29.png'},
    {'name': 'materials/3_sofa.PNG', 'path': 'materials/3_sofa.PNG'},
    {'name': 'materials/17_bank.png', 'path': 'materials/17_bank.png'},
    {'name': 'materials/16_burger.png', 'path': 'materials/16_burger.png'},
    {'name': 'material2/5_mail.PNG', 'path': 'material2/5_mail.PNG'},
    {'name': 'materials/8_palmtree.png', 'path': 'materials/8_palmtree.png'},
    {'name': 'materials/17_dis_shop.png', 'path': 'materials/17_dis_shop.png'},
    {'name': 'Avatar/Male_25.png', 'path': 'Avatar/Male_25.png'},
    {'name': 'pairloop.xlsx', 'path': 'pairloop.xlsx'},
    {'name': 'ratepic.xlsx', 'path': 'ratepic.xlsx'},
    {'name': 'materials/1_flower.PNG', 'path': 'materials/1_flower.PNG'},
    {'name': 'materials/5_mail.PNG', 'path': 'materials/5_mail.PNG'},
    {'name': 'Arrange.xlsx', 'path': 'Arrange.xlsx'},
    {'name': 'materials/11_coffeeshop.png', 'path': 'materials/11_coffeeshop.png'},
    {'name': 'materials/15_police.png', 'path': 'materials/15_police.png'},
    {'name': 'materials/4_plant.PNG', 'path': 'materials/4_plant.PNG'},
    {'name': 'TestD21.png', 'path': 'TestD21.png'},
    {'name': 'TestD22.png', 'path': 'TestD22.png'},
    {'name': 'Avatar/Female_39.png', 'path': 'Avatar/Female_39.png'},
    {'name': 'Avatar/Male_35.png', 'path': 'Avatar/Male_35.png'},
    {'name': 'arrang2.png', 'path': 'arrang2.png'},
    {'name': 'Avatar/Case_3.png', 'path': 'Avatar/Case_3.png'},
    {'name': 'Avatar/Case_2.png', 'path': 'Avatar/Case_2.png'},
    {'name': 'Avatar/Case_5.png', 'path': 'Avatar/Case_5.png'},
    {'name': 'materials/7_chair.png', 'path': 'materials/7_chair.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `d2data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var introClock;
var image_4;
var key_resp_4;
var trial1Clock;
var landmark;
var slider;
var status_mouse;
var vtxt;
var text_2;
var fixationClock;
var iti;
var intro2Clock;
var key_resp;
var image_2;
var tr2Clock;
var tmouse;
var count;
var polygon;
var landmark_1;
var landmark_2;
var btn;
var intro3Clock;
var key_resp_2;
var image_n;
var tr3Clock;
var image_3;
var mouse;
var scene;
var label1;
var label2;
var label3;
var label4;
var label5;
var label6;
var label7;
var label8;
var label9;
var label10;
var label11;
var label12;
var label13;
var label14;
var button;
var thanksClock;
var key_resp_3;
var thankstext;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "intro"
  introClock = new util.Clock();
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : undefined, 
    image : 'TestD21.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.76, 0.99],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial1"
  trial1Clock = new util.Clock();
  landmark = new visual.ImageStim({
    win : psychoJS.window,
    name : 'landmark', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.1], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    startValue: undefined,
    size: [0.8, 0.08], pos: [0, (- 0.3)], ori: 0.0, units: 'height',
    labels: [1, 2, 3, 4, 5, 6, 7], fontSize: 0.05, ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  status_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  status_mouse.mouseClock = new util.Clock();
  vtxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'vtxt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.45)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), 1.0, (- 1.0)]),  opacity: undefined,
    depth: -4.0 
  });
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '一点也不喜欢                                                       非常喜欢',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.01), (- 0.23)], height: 0.04,  wrapWidth: 2.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  iti = new visual.ShapeStim ({
    win: psychoJS.window, name: 'iti', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "intro2"
  intro2Clock = new util.Clock();
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : 'TestD22.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.76, 0.99],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "tr2"
  tr2Clock = new util.Clock();
  tmouse = new core.Mouse({
    win: psychoJS.window,
  });
  tmouse.mouseClock = new util.Clock();
  // Run 'Begin Experiment' code from drg
  count = 1;
  
  polygon = new visual.Polygon({
    win: psychoJS.window, name: 'polygon', 
    edges: 100, size:[0.75, 0.75],
    ori: 0.0, pos: [0.04, 0],
    lineWidth: 5.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1.0, depth: -2, interpolate: true,
  });
  
  landmark_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'landmark_1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.04, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  landmark_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'landmark_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.4), 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  btn = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'btn',
    text: 'Finish',
    fillColor: [0.0353, 1.0, 0.4588],
    borderColor: null,
    color: [(- 1.0), (- 1.0), (- 1.0)],
    colorSpace: 'rgb',
    pos: [0.75, (- 0.37)],
    letterHeight: 0.05,
    size: [0.2, 0.07]
  });
  btn.clock = new util.Clock();
  
  // Initialize components for Routine "intro3"
  intro3Clock = new util.Clock();
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image_n = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_n', units : undefined, 
    image : 'TestM3.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.76, 0.99],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "tr3"
  tr3Clock = new util.Clock();
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : undefined, 
    image : 'arrang2.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.76, 0.99],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Run 'Begin Experiment' code from drag
  var new_scenes, new_scene_value;
  scene = new visual.ImageStim({
    win : psychoJS.window,
    name : 'scene', units : undefined, 
    image : 'p.png', mask : undefined,
    ori : 0.0, pos : [0.1, 0], size : [0.96, 1.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  label1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'label1', units : undefined, 
    image : 'material2/1_flower.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.12, 0.12],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  label2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'label2', units : undefined, 
    image : 'material2/2_bin.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.08, 0.1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  label3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'label3', units : undefined, 
    image : 'material2/3_sofa.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.12, 0.12],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  label4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'label4', units : undefined, 
    image : 'material2/4_plant.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.12, 0.12],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  label5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'label5', units : undefined, 
    image : 'material2/5_mail.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.12, 0.12],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  label6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'label6', units : undefined, 
    image : 'material2/6_wash.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.12, 0.12],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -9.0 
  });
  label7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'label7', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.13, 0.13],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -10.0 
  });
  label8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'label8', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.13, 0.13],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -11.0 
  });
  label9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'label9', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.13, 0.13],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -12.0 
  });
  label10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'label10', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.13, 0.13],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -13.0 
  });
  label11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'label11', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -14.0 
  });
  label12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'label12', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -15.0 
  });
  label13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'label13', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.11, 0.11],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -16.0 
  });
  label14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'label14', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.11, 0.11],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -17.0 
  });
  button = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'button',
    text: 'Finish',
    fillColor: [0.0353, 1.0, 0.4588],
    borderColor: null,
    color: [(- 1.0), (- 1.0), (- 1.0)],
    colorSpace: 'rgb',
    pos: [0.75, (- 0.37)],
    letterHeight: 0.05,
    size: [0.2, 0.07]
  });
  button.clock = new util.Clock();
  
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  thankstext = new visual.TextStim({
    win: psychoJS.window,
    name: 'thankstext',
    text: '您现在已经完成了上机部分的实验。\n\n请按任意键结束本部分的实验。\n\n请您休息一会儿，谢谢您的参与~！',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_4_allKeys;
var introComponents;
function introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'intro' ---
    t = 0;
    introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    introComponents = [];
    introComponents.push(image_4);
    introComponents.push(key_resp_4);
    
    for (const thisComponent of introComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function introRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'intro' ---
    // get current time
    t = introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_4* updates
    if (t >= 0.0 && image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_4.tStart = t;  // (not accounting for frame time here)
      image_4.frameNStart = frameN;  // exact frame index
      
      image_4.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: [], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of introComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function introRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'intro' ---
    for (const thisComponent of introComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 0, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'ratepic.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trial1RoutineBegin(snapshot));
      trialsLoopScheduler.add(trial1RoutineEachFrame());
      trialsLoopScheduler.add(trial1RoutineEnd(snapshot));
      trialsLoopScheduler.add(fixationRoutineBegin(snapshot));
      trialsLoopScheduler.add(fixationRoutineEachFrame());
      trialsLoopScheduler.add(fixationRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 0, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'pairloop.xlsx',
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_3 of trials_3) {
      snapshot = trials_3.getSnapshot();
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(intro2RoutineBegin(snapshot));
      trials_3LoopScheduler.add(intro2RoutineEachFrame());
      trials_3LoopScheduler.add(intro2RoutineEnd(snapshot));
      const trials_2LoopScheduler = new Scheduler(psychoJS);
      trials_3LoopScheduler.add(trials_2LoopBegin(trials_2LoopScheduler, snapshot));
      trials_3LoopScheduler.add(trials_2LoopScheduler);
      trials_3LoopScheduler.add(trials_2LoopEnd);
      trials_3LoopScheduler.add(trials_3LoopEndIteration(trials_3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: group_file,
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_2 of trials_2) {
      snapshot = trials_2.getSnapshot();
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(tr2RoutineBegin(snapshot));
      trials_2LoopScheduler.add(tr2RoutineEachFrame());
      trials_2LoopScheduler.add(tr2RoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trials_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_4;
function trials_4LoopBegin(trials_4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Arrange.xlsx',
      seed: undefined, name: 'trials_4'
    });
    psychoJS.experiment.addLoop(trials_4); // add the loop to the experiment
    currentLoop = trials_4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_4 of trials_4) {
      snapshot = trials_4.getSnapshot();
      trials_4LoopScheduler.add(importConditions(snapshot));
      trials_4LoopScheduler.add(intro3RoutineBegin(snapshot));
      trials_4LoopScheduler.add(intro3RoutineEachFrame());
      trials_4LoopScheduler.add(intro3RoutineEnd(snapshot));
      trials_4LoopScheduler.add(tr3RoutineBegin(snapshot));
      trials_4LoopScheduler.add(tr3RoutineEachFrame());
      trials_4LoopScheduler.add(tr3RoutineEnd(snapshot));
      trials_4LoopScheduler.add(trials_4LoopEndIteration(trials_4LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var is_pressed;
var gotValidClick;
var trial1Components;
function trial1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial1' ---
    t = 0;
    trial1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    landmark.setImage(image);
    slider.reset()
    // Run 'Begin Routine' code from code
    is_pressed = false;
    
    // setup some python lists for storing info about the status_mouse
    // current position of the mouse:
    status_mouse.x = [];
    status_mouse.y = [];
    status_mouse.leftButton = [];
    status_mouse.midButton = [];
    status_mouse.rightButton = [];
    status_mouse.time = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    trial1Components = [];
    trial1Components.push(landmark);
    trial1Components.push(slider);
    trial1Components.push(status_mouse);
    trial1Components.push(vtxt);
    trial1Components.push(text_2);
    
    for (const thisComponent of trial1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var vall;
var timer;
var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function trial1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial1' ---
    // get current time
    t = trial1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *landmark* updates
    if (t >= 0.0 && landmark.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      landmark.tStart = t;  // (not accounting for frame time here)
      landmark.frameNStart = frameN;  // exact frame index
      
      landmark.setAutoDraw(true);
    }

    
    // *slider* updates
    if (t >= 0.0 && slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider.tStart = t;  // (not accounting for frame time here)
      slider.frameNStart = frameN;  // exact frame index
      
      slider.setAutoDraw(true);
    }

    // Run 'Each Frame' code from code
    vall = slider.markerPos;
    if ((vall !== null)) {
        vtxt.text = ("\u5f53\u524d\u60a8\u7684\u8bc4\u5206\uff1a " + Math.round(vall, 3).toString());
    }
    if (((! is_pressed) && status_mouse.getPressed()[0])) {
        is_pressed = true;
        slider.fillColor = "blue";
        timer = new util.CountdownTimer(0.3);
        
    }
    if (is_pressed) {
        if ((timer.getTime() <= 0)) {
            continueRoutine = false;
        }
    } else {
        slider.fillColor = "red";
        
        px_pos = util.to_px(status_mouse.getPos(), "height", psychoJS.window);
        slider.markerPos = slider._posToRating(px_pos);
        
    //    slider.markerPos = slider._posToRating(slider.mouse.getPos());
        slider.recordRating(slider.markerPos);
    }
    
    // *status_mouse* updates
    if (t >= 0.0 && status_mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      status_mouse.tStart = t;  // (not accounting for frame time here)
      status_mouse.frameNStart = frameN;  // exact frame index
      
      status_mouse.status = PsychoJS.Status.STARTED;
      prevButtonState = status_mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (status_mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = status_mouse.getPressed();
      _mouseXYs = status_mouse.getPos();
      status_mouse.x.push(_mouseXYs[0]);
      status_mouse.y.push(_mouseXYs[1]);
      status_mouse.leftButton.push(_mouseButtons[0]);
      status_mouse.midButton.push(_mouseButtons[1]);
      status_mouse.rightButton.push(_mouseButtons[2]);
      status_mouse.time.push(globalClock.getTime());
    }
    
    // *vtxt* updates
    if (t >= 0.0 && vtxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      vtxt.tStart = t;  // (not accounting for frame time here)
      vtxt.frameNStart = frameN;  // exact frame index
      
      vtxt.setAutoDraw(true);
    }

    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trial1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial1' ---
    for (const thisComponent of trial1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('slider.response', slider.getRating());
    psychoJS.experiment.addData('slider.rt', slider.getRT());
    // Run 'End Routine' code from code
    is_pressed = false;
    psychoJS.experiment.addData("stage", "rate");
    
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('status_mouse.x', status_mouse.x);
    psychoJS.experiment.addData('status_mouse.y', status_mouse.y);
    psychoJS.experiment.addData('status_mouse.leftButton', status_mouse.leftButton);
    psychoJS.experiment.addData('status_mouse.midButton', status_mouse.midButton);
    psychoJS.experiment.addData('status_mouse.rightButton', status_mouse.rightButton);
    psychoJS.experiment.addData('status_mouse.time', status_mouse.time);
    
    // the Routine "trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation' ---
    t = 0;
    fixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.200000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(iti);
    
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation' ---
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *iti* updates
    if (t >= 0.0 && iti.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      iti.tStart = t;  // (not accounting for frame time here)
      iti.frameNStart = frameN;  // exact frame index
      
      iti.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (iti.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      iti.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation' ---
    for (const thisComponent of fixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var intro2Components;
function intro2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'intro2' ---
    t = 0;
    intro2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    intro2Components = [];
    intro2Components.push(key_resp);
    intro2Components.push(image_2);
    
    for (const thisComponent of intro2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function intro2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'intro2' ---
    // get current time
    t = intro2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: [], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of intro2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function intro2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'intro2' ---
    for (const thisComponent of intro2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "intro2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var drg_in_process;
var clicked_stim;
var tr2Components;
function tr2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'tr2' ---
    t = 0;
    tr2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the tmouse
    // current position of the mouse:
    tmouse.x = [];
    tmouse.y = [];
    tmouse.leftButton = [];
    tmouse.midButton = [];
    tmouse.rightButton = [];
    tmouse.time = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from drg
    psychoJS.experiment.addData("stage", "Pair_Rate");
    drg_in_process = false;
    clicked_stim = null;
    psychoJS.experiment.nextEntry();
    
    landmark_1.setSize([sizex, sizey]);
    landmark_1.setImage(fixed);
    landmark_2.setSize([sizex, sizey]);
    landmark_2.setImage(moved);
    // keep track of which components have finished
    tr2Components = [];
    tr2Components.push(tmouse);
    tr2Components.push(polygon);
    tr2Components.push(landmark_1);
    tr2Components.push(landmark_2);
    tr2Components.push(btn);
    
    for (const thisComponent of tr2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function tr2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'tr2' ---
    // get current time
    t = tr2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *tmouse* updates
    if (t >= 0.0 && tmouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tmouse.tStart = t;  // (not accounting for frame time here)
      tmouse.frameNStart = frameN;  // exact frame index
      
      tmouse.status = PsychoJS.Status.STARTED;
      tmouse.mouseClock.reset();
      prevButtonState = [0, 0, 0];  // if now button is down we will treat as 'new' click
      }
    if (tmouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = tmouse.getPressed();
      _mouseXYs = tmouse.getPos();
      tmouse.x.push(_mouseXYs[0]);
      tmouse.y.push(_mouseXYs[1]);
      tmouse.leftButton.push(_mouseButtons[0]);
      tmouse.midButton.push(_mouseButtons[1]);
      tmouse.rightButton.push(_mouseButtons[2]);
      tmouse.time.push(tmouse.mouseClock.getTime());
    }
    // Run 'Each Frame' code from drg
    if ((! drg_in_process)) {
        if (tmouse.isPressedIn(landmark_2)) {
            drg_in_process = true;
            clicked_stim = landmark_2;
            tmouse.x = [];
            tmouse.y = [];
            tmouse.time = [];
        }
    }
    if ((tmouse.getPressed()[0] === 1)) {
        if (drg_in_process) {
            clicked_stim.pos = tmouse.getPos();
        }
    } else {
        if (drg_in_process) {
            psychoJS.experiment.addData("item.x", tmouse.x);
            psychoJS.experiment.addData("item.y", tmouse.y);
            psychoJS.experiment.addData("item.time", tmouse.time);
        }
        drg_in_process = false;
    }
    
    
    // *polygon* updates
    if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }

    
    // *landmark_1* updates
    if (t >= 0.0 && landmark_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      landmark_1.tStart = t;  // (not accounting for frame time here)
      landmark_1.frameNStart = frameN;  // exact frame index
      
      landmark_1.setAutoDraw(true);
    }

    
    // *landmark_2* updates
    if (t >= 0.0 && landmark_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      landmark_2.tStart = t;  // (not accounting for frame time here)
      landmark_2.frameNStart = frameN;  // exact frame index
      
      landmark_2.setAutoDraw(true);
    }

    
    // *btn* updates
    if (t >= 0 && btn.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      btn.tStart = t;  // (not accounting for frame time here)
      btn.frameNStart = frameN;  // exact frame index
      
      btn.setAutoDraw(true);
    }

    if (btn.status === PsychoJS.Status.STARTED) {
      // check whether btn has been pressed
      if (btn.isClicked) {
        if (!btn.wasClicked) {
          // store time of first click
          btn.timesOn.push(btn.clock.getTime());
          btn.numClicks += 1;
          // store time clicked until
          btn.timesOff.push(btn.clock.getTime());
        } else {
          // update time clicked until;
          btn.timesOff[btn.timesOff.length - 1] = btn.clock.getTime();
        }
        if (!btn.wasClicked) {
          // end routine when btn is clicked
          continueRoutine = false;
          continueRoutine = false;
        }
        // if btn is still clicked next frame, it is not a new click
        btn.wasClicked = true;
      } else {
        // if btn is clicked next frame, it is a new click
        btn.wasClicked = false;
      }
    } else {
      // keep clock at 0 if btn hasn't started / has finished
      btn.clock.reset();
      // if btn is clicked next frame, it is a new click
      btn.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of tr2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function tr2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'tr2' ---
    for (const thisComponent of tr2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('tmouse.x', tmouse.x);
    psychoJS.experiment.addData('tmouse.y', tmouse.y);
    psychoJS.experiment.addData('tmouse.leftButton', tmouse.leftButton);
    psychoJS.experiment.addData('tmouse.midButton', tmouse.midButton);
    psychoJS.experiment.addData('tmouse.rightButton', tmouse.rightButton);
    psychoJS.experiment.addData('tmouse.time', tmouse.time);
    
    // Run 'End Routine' code from drg
    //var screenshot = psychoJS.window.getSnapshot();
    //screenshot.save((((("d2data/" + expInfo["participant"]) + "_count_") + count.toString()) + "_markmove.png"));
    //count += 1;
    //psychoJS.window.clearBuffer();
    landmark_2.setPos([(- 0.4), 0]);
    psychoJS.experiment.nextEntry();
    
    psychoJS.experiment.addData('btn.numClicks', btn.numClicks);
    psychoJS.experiment.addData('btn.timesOn', btn.timesOn);
    psychoJS.experiment.addData('btn.timesOff', btn.timesOff);
    // the Routine "tr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_2_allKeys;
var intro3Components;
function intro3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'intro3' ---
    t = 0;
    intro3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    intro3Components = [];
    intro3Components.push(key_resp_2);
    intro3Components.push(image_n);
    
    for (const thisComponent of intro3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function intro3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'intro3' ---
    // get current time
    t = intro3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: [], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image_n* updates
    if (t >= 0.0 && image_n.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_n.tStart = t;  // (not accounting for frame time here)
      image_n.frameNStart = frameN;  // exact frame index
      
      image_n.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of intro3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function intro3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'intro3' ---
    for (const thisComponent of intro3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "intro3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var scenes;
var scene_value;
var new_scenes;
var new_scene_value;
var drag_in_process;
var tr3Components;
function tr3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'tr3' ---
    t = 0;
    tr3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from drag
    psychoJS.experiment.addData("stage", "Arrangement");
    function shuffle_twolist(list1, list2) {
        // Create shuffled index based on length of list1
        const shuffled_indices = [...Array(list1.length).keys()].sort(() => Math.random() - 0.5);
      
        // Create shuffled lists using the generated indices
        const shuffled_list1 = shuffled_indices.map((i) => list1[i]);
        const shuffled_list2 = shuffled_indices.map((i) => list2[i]);
      
        return [shuffled_list1, shuffled_list2];
      }
    
    scenes = [label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14];
    scene_value = ["flower", "bin", "sofa", "plant", "mailbox", "wash", "CaseAvatar1", "CaseAvatar2", "CaseAvatar3", "CaseAvatar4", "CaseAvatar5", "CaseAvatar6", "CaseAvatar7", "CaseAvatar8"];
    //[new_scenes, new_scene_value] = shuffle_twolist(scenes, scene_value);
    new_scenes = shuffle_twolist(scenes, scene_value)[0];
    new_scene_value = shuffle_twolist(scenes, scene_value)[1];
    
    psychoJS.experiment.addData("scenes", new_scene_value);
    for (var pointer, _pj_c = 0, _pj_a = util.range(new_scenes.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        pointer = _pj_a[_pj_c];
        var x = ((- 0.8) + (Math.floor(pointer / 6) * 0.1));
        var y = ((0.15 * (pointer % 6)) - 0.37);
        new_scenes[pointer].setPos([x, y]);
    //    [wid, hei] = new_scenes[pointer].size;
        var wid = new_scenes[pointer].size[0];
        var hei = new_scenes[pointer].size;[1];
        console.log("wid: ", wid);
        if (((wid > 0.125) || (wid < 0.115))) {
            new_scenes[pointer].setSize([new_size, new_size]);
        }
        console.log(new_scene_value[pointer], "(", x, ",", y, ")");
    }
    drag_in_process = false;
    clicked_stim = null;
    psychoJS.experiment.nextEntry();
    
    label7.setImage(t1);
    label8.setImage(t2);
    label9.setImage(t3);
    label10.setImage(t4);
    label11.setImage(t5);
    label12.setImage(t6);
    label13.setImage(t7);
    label14.setImage(t8);
    // keep track of which components have finished
    tr3Components = [];
    tr3Components.push(image_3);
    tr3Components.push(mouse);
    tr3Components.push(scene);
    tr3Components.push(label1);
    tr3Components.push(label2);
    tr3Components.push(label3);
    tr3Components.push(label4);
    tr3Components.push(label5);
    tr3Components.push(label6);
    tr3Components.push(label7);
    tr3Components.push(label8);
    tr3Components.push(label9);
    tr3Components.push(label10);
    tr3Components.push(label11);
    tr3Components.push(label12);
    tr3Components.push(label13);
    tr3Components.push(label14);
    tr3Components.push(button);
    
    for (const thisComponent of tr3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function tr3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'tr3' ---
    // get current time
    t = tr3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_3* updates
    if (t >= 0.0 && image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_3.tStart = t;  // (not accounting for frame time here)
      image_3.frameNStart = frameN;  // exact frame index
      
      image_3.setAutoDraw(true);
    }

    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = [0, 0, 0];  // if now button is down we will treat as 'new' click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      _mouseXYs = mouse.getPos();
      mouse.x.push(_mouseXYs[0]);
      mouse.y.push(_mouseXYs[1]);
      mouse.leftButton.push(_mouseButtons[0]);
      mouse.midButton.push(_mouseButtons[1]);
      mouse.rightButton.push(_mouseButtons[2]);
      mouse.time.push(mouse.mouseClock.getTime());
    }
    // Run 'Each Frame' code from drag
    if ((! drag_in_process)) {
        for (var i, _pj_c = 0, _pj_a = util.range(new_scenes.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            i = _pj_a[_pj_c];
            if (mouse.isPressedIn(new_scenes[i])) {
                drag_in_process = true;
                clicked_stim = new_scenes[i];
                psychoJS.experiment.addData("scene", new_scene_value[i]);
                mouse.x = [];
                mouse.y = [];
                mouse.time = [];
                break;
            }
        }
    }
    if ((mouse.getPressed()[0] === 1)) {
        if (drag_in_process) {
            clicked_stim.pos = mouse.getPos();
        }
    } else {
        if (drag_in_process) {
            psychoJS.experiment.addData("item.x", mouse.x);
            psychoJS.experiment.addData("item.y", mouse.y);
            psychoJS.experiment.addData("item.time", mouse.time);
            psychoJS.experiment.nextEntry();
        }
        drag_in_process = false;
    }
    
    
    // *scene* updates
    if (t >= 0.0 && scene.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      scene.tStart = t;  // (not accounting for frame time here)
      scene.frameNStart = frameN;  // exact frame index
      
      scene.setAutoDraw(true);
    }

    
    // *label1* updates
    if (t >= 0.0 && label1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      label1.tStart = t;  // (not accounting for frame time here)
      label1.frameNStart = frameN;  // exact frame index
      
      label1.setAutoDraw(true);
    }

    
    // *label2* updates
    if (t >= 0.0 && label2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      label2.tStart = t;  // (not accounting for frame time here)
      label2.frameNStart = frameN;  // exact frame index
      
      label2.setAutoDraw(true);
    }

    
    // *label3* updates
    if (t >= 0.0 && label3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      label3.tStart = t;  // (not accounting for frame time here)
      label3.frameNStart = frameN;  // exact frame index
      
      label3.setAutoDraw(true);
    }

    
    // *label4* updates
    if (t >= 0.0 && label4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      label4.tStart = t;  // (not accounting for frame time here)
      label4.frameNStart = frameN;  // exact frame index
      
      label4.setAutoDraw(true);
    }

    
    // *label5* updates
    if (t >= 0.0 && label5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      label5.tStart = t;  // (not accounting for frame time here)
      label5.frameNStart = frameN;  // exact frame index
      
      label5.setAutoDraw(true);
    }

    
    // *label6* updates
    if (t >= 0.0 && label6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      label6.tStart = t;  // (not accounting for frame time here)
      label6.frameNStart = frameN;  // exact frame index
      
      label6.setAutoDraw(true);
    }

    
    // *label7* updates
    if (t >= 0.0 && label7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      label7.tStart = t;  // (not accounting for frame time here)
      label7.frameNStart = frameN;  // exact frame index
      
      label7.setAutoDraw(true);
    }

    
    // *label8* updates
    if (t >= 0.0 && label8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      label8.tStart = t;  // (not accounting for frame time here)
      label8.frameNStart = frameN;  // exact frame index
      
      label8.setAutoDraw(true);
    }

    
    // *label9* updates
    if (t >= 0.0 && label9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      label9.tStart = t;  // (not accounting for frame time here)
      label9.frameNStart = frameN;  // exact frame index
      
      label9.setAutoDraw(true);
    }

    
    // *label10* updates
    if (t >= 0.0 && label10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      label10.tStart = t;  // (not accounting for frame time here)
      label10.frameNStart = frameN;  // exact frame index
      
      label10.setAutoDraw(true);
    }

    
    // *label11* updates
    if (t >= 0.0 && label11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      label11.tStart = t;  // (not accounting for frame time here)
      label11.frameNStart = frameN;  // exact frame index
      
      label11.setAutoDraw(true);
    }

    
    // *label12* updates
    if (t >= 0.0 && label12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      label12.tStart = t;  // (not accounting for frame time here)
      label12.frameNStart = frameN;  // exact frame index
      
      label12.setAutoDraw(true);
    }

    
    // *label13* updates
    if (t >= 0.0 && label13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      label13.tStart = t;  // (not accounting for frame time here)
      label13.frameNStart = frameN;  // exact frame index
      
      label13.setAutoDraw(true);
    }

    
    // *label14* updates
    if (t >= 0.0 && label14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      label14.tStart = t;  // (not accounting for frame time here)
      label14.frameNStart = frameN;  // exact frame index
      
      label14.setAutoDraw(true);
    }

    
    // *button* updates
    if (t >= 0 && button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button.tStart = t;  // (not accounting for frame time here)
      button.frameNStart = frameN;  // exact frame index
      
      button.setAutoDraw(true);
    }

    if (button.status === PsychoJS.Status.STARTED) {
      // check whether button has been pressed
      if (button.isClicked) {
        if (!button.wasClicked) {
          // store time of first click
          button.timesOn.push(button.clock.getTime());
          button.numClicks += 1;
          // store time clicked until
          button.timesOff.push(button.clock.getTime());
        } else {
          // update time clicked until;
          button.timesOff[button.timesOff.length - 1] = button.clock.getTime();
        }
        if (!button.wasClicked) {
          // end routine when button is clicked
          continueRoutine = false;
          continueRoutine = false;
        }
        // if button is still clicked next frame, it is not a new click
        button.wasClicked = true;
      } else {
        // if button is clicked next frame, it is a new click
        button.wasClicked = false;
      }
    } else {
      // keep clock at 0 if button hasn't started / has finished
      button.clock.reset();
      // if button is clicked next frame, it is a new click
      button.wasClicked = false;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of tr3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var screenshot;
function tr3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'tr3' ---
    for (const thisComponent of tr3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse.x', mouse.x);
    psychoJS.experiment.addData('mouse.y', mouse.y);
    psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
    psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
    psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
    psychoJS.experiment.addData('mouse.time', mouse.time);
    
    // Run 'End Routine' code from drag
    function nscreenshot() {
      let gl = document.querySelector("canvas");
      return new Promise((resolve) => {
        requestAnimationFrame(() => {
          resolve(gl.toDataURL("image/png"));
        });
      });
    }   //psychoJS.window.clearBuffer();
    let s = await nscreenshot();
    psychoJS.experiment.addData('base64pic',s)
    //
    psychoJS.experiment.addData('button.numClicks', button.numClicks);
    psychoJS.experiment.addData('button.timesOn', button.timesOn);
    psychoJS.experiment.addData('button.timesOff', button.timesOff);
    // the Routine "tr3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_3_allKeys;
var thanksComponents;
function thanksRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'thanks' ---
    t = 0;
    thanksClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    thanksComponents = [];
    thanksComponents.push(key_resp_3);
    thanksComponents.push(thankstext);
    
    for (const thisComponent of thanksComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function thanksRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'thanks' ---
    // get current time
    t = thanksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_3.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: [], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *thankstext* updates
    if (t >= 0.0 && thankstext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thankstext.tStart = t;  // (not accounting for frame time here)
      thankstext.frameNStart = frameN;  // exact frame index
      
      thankstext.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (thankstext.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      thankstext.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of thanksComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function thanksRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'thanks' ---
    for (const thisComponent of thanksComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
