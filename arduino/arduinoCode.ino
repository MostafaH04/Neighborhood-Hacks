const int buttonIn = 2;

const int trig = 5;
const int echo = 6;

const int led1 = 10;
const int led2 = 11;

const int buzz = 12;

bool left = true;

void setup()
{
  pinMode(buttonIn, INPUT);
  
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  
  pinMode(buzz, OUTPUT);
  
  Serial.begin(9600);
}

float distance;
bool inRange;
bool buzzed = false;
char input;
bool clicked = false;

void loop()
{
  while (Serial.available() > 0){
    input = Serial.read();
    
    if (input == 'r'){
      for (int i = 0; i < 10; i++){
        digitalWrite(led2, HIGH);
        digitalWrite(buzz, HIGH);
        delay(100);
        digitalWrite(led2,LOW);
        digitalWrite(buzz, LOW);
        delay(100);
      }
    }
    else if(input == 'b'){
      digitalWrite(led1, HIGH);
      digitalWrite(buzz, HIGH);
      delay(100);
      digitalWrite(buzz,LOW);
      delay(500);
      digitalWrite(led1, LOW);
    }
    
  }
  
  distance = dist();
  
  if (distance < 100){
    inRange = true;
  }else{
    inRange = false;
    if (left == false){
      Serial.println("leftRange");
      left = true;
    }
    buzzed = false;
  }
  
  if (inRange == true){
    if (buzzed == false){
      buzzed = true;
    }
    if (left == true){
      Serial.println("inRange");
      left = false;
    }
    delay(100);
    digitalWrite(buzz,LOW);
    
  }
  if (digitalRead(buttonIn) == 1){
    if (clicked == false){
      Serial.println("click");
      clicked = true;
    }
  }else{
    clicked = false;
  }

  
}

float calc_distance;
float duration;

double dist()
{
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, HIGH);
  calc_distance = duration * 0.034 / 2;
  return calc_distance;
}
