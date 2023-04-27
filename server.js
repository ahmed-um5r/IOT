var SerialPort = require('serialport');
var xbee_api = require('xbee-api');
var C = xbee_api.constants;
var mqtt = require('mqtt');
var express= require('express')
var app = express()
var path = require('path')
require('dotenv').config();

const SERIAL_PORT = process.env.SERIAL_PORT;
const client = mqtt.connect('mqtt://test.mosquitto.org:1883')
const MQTT_TOPIC = process.env.MQTT_TOPIC;

var xbeeAPI = new xbee_api.XBeeAPI({
  api_mode: 2
});

let serialport = new SerialPort(SERIAL_PORT, {
  baudRate: 9600,
}, function (err) {
  if (err) {
    return console.log('Error: ', err.message)
  }
});

serialport.pipe(xbeeAPI.parser);
xbeeAPI.builder.pipe(serialport);

client.on('connect', function () {
  console.log('MQTT connected')
});

function sendRemoteCommandRequest(command, commandParameter) {
  var frame_obj = { 
    type: C.FRAME_TYPE.REMOTE_AT_COMMAND_REQUEST,
    destination64: "FFFFFFFFFFFFFFFF",
    command: command,
    commandParameter: [commandParameter],
  };
  xbeeAPI.builder.write(frame_obj);
 
}


serialport.on("open", function () {
  frame_obj = { // AT Request to be sent
    type: C.FRAME_TYPE.REMOTE_AT_COMMAND_REQUEST,
    destination64: "FFFFFFFFFFFFFFFF",
    command: "D0",
    commandParameter: [],
  };
  xbeeAPI.builder.write(frame_obj);

  var frame_obj = { // AT Request to be sent
    type: C.FRAME_TYPE.AT_COMMAND,
    command: "NI",
    commandParameter: [],
  };

  xbeeAPI.builder.write(frame_obj);

});


app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'public')))

xbeeAPI.parser.on("data", function (frame) {
  if (C.FRAME_TYPE.ZIGBEE_RECEIVE_PACKET === frame.type) {
    let dataReceived = String.fromCharCode.apply(null, frame.data);
    console.log(dataReceived)
    app.get('/',(request, response) =>{
      response.render("index", {temperature : dataReceived})
    })

    // Publish data to MQTT broker
    client.publish("temperature", dataReceived);
  }dataReceived

  if (C.FRAME_TYPE.NODE_IDENTIFICATION === frame.type) {
    app.get('/',(request, response) =>{
      response.render("index", {temperature : dataReceived})
    })
  } else if (C.FRAME_TYPE.ZIGBEE_IO_DATA_SAMPLE_RX === frame.type) {
    console.log("ZIGBEE_IO_DATA_SAMPLE_RX")
    app.get('/',(request, response) =>{
      response.render("index", {temperature : dataReceived})
    })
  } else if (C.FRAME_TYPE.REMOTE_COMMAND_RESPONSE === frame.type) {
    console.log("REMOTE_COMMAND_RESPONSE")
  } else {
    console.debug(frame);
    let dataReceived = String.fromCharCode.apply(null, frame.commandData)
    app.get('/',(request, response) =>{
      response.render("index", {temperature : dataReceived})
    })
  }
});





app.get('/aroser', (req, res) => {

  sendRemoteCommandRequest("D0", [05]);
  res.sendStatus(200);
});

app.get('/stop', (req, res) => {
  
  sendRemoteCommandRequest("D0", 0x04);
  res.sendStatus(200);
});


 app.listen(8001)