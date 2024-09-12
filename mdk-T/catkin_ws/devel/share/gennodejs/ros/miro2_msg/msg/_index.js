
"use strict";

let voice_state = require('./voice_state.js');
let objects = require('./objects.js');
let object_tag = require('./object_tag.js');
let priority_peak = require('./priority_peak.js');
let BatteryState = require('./BatteryState.js');
let affect = require('./affect.js');
let sleep = require('./sleep.js');
let object_face = require('./object_face.js');
let affect_adjust = require('./affect_adjust.js');
let animal_state = require('./animal_state.js');
let funnel_web = require('./funnel_web.js');
let object_ball = require('./object_ball.js');
let adjust = require('./adjust.js');
let sensors_package = require('./sensors_package.js');
let animal_adjust = require('./animal_adjust.js');
let sleep_adjust = require('./sleep_adjust.js');
let img_annotation = require('./img_annotation.js');
let push = require('./push.js');

module.exports = {
  voice_state: voice_state,
  objects: objects,
  object_tag: object_tag,
  priority_peak: priority_peak,
  BatteryState: BatteryState,
  affect: affect,
  sleep: sleep,
  object_face: object_face,
  affect_adjust: affect_adjust,
  animal_state: animal_state,
  funnel_web: funnel_web,
  object_ball: object_ball,
  adjust: adjust,
  sensors_package: sensors_package,
  animal_adjust: animal_adjust,
  sleep_adjust: sleep_adjust,
  img_annotation: img_annotation,
  push: push,
};
