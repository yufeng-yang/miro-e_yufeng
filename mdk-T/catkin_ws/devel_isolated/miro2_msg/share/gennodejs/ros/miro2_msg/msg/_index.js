
"use strict";

let sensors_package = require('./sensors_package.js');
let object_face = require('./object_face.js');
let push = require('./push.js');
let animal_state = require('./animal_state.js');
let funnel_web = require('./funnel_web.js');
let affect = require('./affect.js');
let priority_peak = require('./priority_peak.js');
let object_tag = require('./object_tag.js');
let img_annotation = require('./img_annotation.js');
let sleep = require('./sleep.js');
let object_ball = require('./object_ball.js');
let adjust = require('./adjust.js');
let objects = require('./objects.js');
let BatteryState = require('./BatteryState.js');
let sleep_adjust = require('./sleep_adjust.js');
let animal_adjust = require('./animal_adjust.js');
let voice_state = require('./voice_state.js');
let affect_adjust = require('./affect_adjust.js');

module.exports = {
  sensors_package: sensors_package,
  object_face: object_face,
  push: push,
  animal_state: animal_state,
  funnel_web: funnel_web,
  affect: affect,
  priority_peak: priority_peak,
  object_tag: object_tag,
  img_annotation: img_annotation,
  sleep: sleep,
  object_ball: object_ball,
  adjust: adjust,
  objects: objects,
  BatteryState: BatteryState,
  sleep_adjust: sleep_adjust,
  animal_adjust: animal_adjust,
  voice_state: voice_state,
  affect_adjust: affect_adjust,
};
