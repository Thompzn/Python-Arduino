const int pinoTrigger = 5;
const int pinoEcho = 7;
const int pinoBuzzer = 2;

int cm = 0;
bool buzzerLigado = false;
String distancias = "";

unsigned long tempoInicio = 0;
unsigned long tempoFim = 0;

void setup() {
  Serial.begin(9600);
  pinMode(pinoTrigger, OUTPUT);
  pinMode(pinoEcho, INPUT);
  pinMode(pinoBuzzer, OUTPUT);
}

void loop() {
  
  digitalWrite(pinoTrigger, LOW);
  delayMicroseconds(2);
  digitalWrite(pinoTrigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinoTrigger, LOW);

  
  long duracao = pulseIn(pinoEcho, HIGH);
  cm = duracao * 0.01723;

 
  if (cm > 0 && cm <= 50) {
    if (!buzzerLigado) {
      buzzerLigado = true;
      tempoInicio = millis();
      distancias = "";
      tone(pinoBuzzer, 4000);
    }
    distancias += String(cm) + "cm, ";
  }

  if (cm > 50 && buzzerLigado) {
    buzzerLigado = false;
    tempoFim = millis();
    noTone(pinoBuzzer);

    // para o python
    Serial.println("INICIO");
    Serial.println(tempoInicio);
    Serial.println(tempoFim);
    Serial.println(distancias);
    Serial.println("FIM");
  }

  delay(1000);
}