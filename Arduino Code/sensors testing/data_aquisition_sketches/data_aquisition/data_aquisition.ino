#include <ArduinoJson.h>
#include <SoftwareSerial.h>


SoftwareSerial MyBlue(2, 3); // RX | TX
  //SoftwareSerial MyBlue(2, 4); // RX | TX

int counter = 0;
String msg;

void setup()
{
  Serial.begin(9600);
  MyBlue.begin(9600);  // normal mode
  //MyBlue.begin(38400);  //Baud Rate for AT-command Mode.
  //Serial.println("***AT commands mode***");
  Serial.println("Ready to connect\nDefualt password is 1234 or 0000\n\n");
}
void loop()
{

  counter++;
  StaticJsonDocument<128> doc;

  doc["sensor"] = "gps";
  doc["heart-rate"] = 12;
  doc["acceleration_x"] = 0.5;
  doc["acceleration_y"] = 0.5;
  doc["acceleration_z"] = 0.5;

  JsonObject acceleration = doc.createNestedObject("acceleration");
  acceleration["x"] = 4;
  acceleration["y"] = 5;
  acceleration["z"] = 9;
  doc["distance"] = 0.5;
  doc["time"] = 1351824120;

  String output = "";
  serializeJson(doc, output);
  //Serial.println(output);


    readSerialPort();
    //from bluetooth to Terminal.
    if (MyBlue.available() > 0) {
    Serial.write(MyBlue.read());
    }


    //from termial to bluetooth
    if (msg!=""){
      MyBlue.println(msg);
    }

//    if(counter > 240){
//     counter = 0;
//    }
//
//    MyBlue.write(counter);

    MyBlue.print(output);
    delay(1500);
}


void readSerialPort() {
  msg = "";
  while (Serial.available()) {
    delay(10);
    if (Serial.available() > 0) {
      char c = Serial.read();  //gets one byte from serial buffer
      msg += c; //makes the string readString
    }
  }
}
