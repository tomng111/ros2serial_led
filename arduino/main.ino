int led = 13; // LED pin
void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    char myCmd = Serial.read();
    if(myCmd == 'e') digitalWrite(led, HIGH); // Turn ON the LED 
    else if(myCmd == 'a')  digitalWrite(led, LOW); // Turn OFF the LED
  }
}
