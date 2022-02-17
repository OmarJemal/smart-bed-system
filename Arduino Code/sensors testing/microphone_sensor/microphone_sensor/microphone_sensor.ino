
#define Digital_input 2 // attach pin D2 Arduino to pin Digital of M5stack Mic
#define Analog_input A1 //attach pin D3 Arduino to pin Trig of HC-SR04


int analog_reading = 0;
void setup() {
  //pinMode(Digital_input, INPUT); // Sets the trigPin as an OUTPUT


  
  Serial.begin(115200); // // Serial Communication is starting with 9600 of baudrate speed
  Serial.println("Starting Microphone"); 
}

void loop() {
 
  int analog_reading = analogRead(Analog_input);
  //Serial.print("Analog reading: ");
  Serial.print(analog_reading);
  Serial.print("\n");

  //int buttonState = digitalRead(Digital_input);
  
  //Serial.print("Digital reading: ");
  //Serial.print(buttonState);
  //Serial.print("\n");


  delay(2);


}
