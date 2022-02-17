/*   
HC05 - Bluetooth AT-Command mode  
modified on 10 Feb 2019 
by Saeed Hosseini 
https://electropeak.com/learn/ 
*/ 
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
 Serial.println("Ready to connect\nDefualt password is 1234 or 000"); 
} 
void loop() 
{ 
 
   counter++;
   readSerialPort();

   
   //from bluetooth to Terminal. 
   if (MyBlue.available() > 0) {
     Serial.write(MyBlue.read());
   } 

   
   //from termial to bluetooth 
   if (msg!=""){ 
     MyBlue.println(msg);
   }

   if(counter > 240){
      counter = 0;
    }
    
   MyBlue.write(counter);

   delay(150);
}  


void readSerialPort(){
  msg="";
 while (Serial.available()) {
   delay(10);  
   if (Serial.available() >0) {
     char c = Serial.read();  //gets one byte from serial buffer
     msg += c; //makes the string readString
   }
 }
}
