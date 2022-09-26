#define A 12
#define B 13
#define C 7
#define D 8
#define E 9
#define F 11
#define G 10
#define ledRojo 4
#define ledAmarillo 3
#define ledAzul 2
#define SENSOR_TEMPERATURA A0
#define SWITCH A4

int lecturaTemperatura=0;
int open = 0;

void setup()
{
  pinMode(C, OUTPUT);
  pinMode(D, OUTPUT);
  pinMode(E, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(F, OUTPUT);
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(ledRojo, OUTPUT);
  pinMode(ledAmarillo, OUTPUT);
  pinMode(ledAzul, OUTPUT);
  pinMode(SWITCH, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop()
{
  
  int temperatura = 0;  
  //se toma el valor del pin A0
  lecturaTemperatura = analogRead(A0);
  open = digitalRead(SWITCH);
  
  if(open == 1){
  	Serial.print("\nValor sensor:\n");
  	Serial.print(lecturaTemperatura);
  	delay(1000);
  
  	//se mapea temperatura
  	temperatura = map(lecturaTemperatura,20,358,-40,125); 
  	if(temperatura > 24)
  	{
    	printDigit('c');
    	switchStateLeds('c');
  	} 
  	else if(temperatura < 0)
  	{
    	printDigit('f');
    	switchStateLeds('f');
  	}
  	else
  	{
    	printDigit('d');
    	switchStateLeds('d');
  	}
  
  	Serial.print("\nTemperatura:\n");
  	Serial.print(temperatura);
  	delay(1000);
  }
  else{
    printDigit('o');
    switchStateLeds('o');
  }
  
}

void printDigit(char valor)
{
  digitalWrite(A, LOW);
  digitalWrite(B, LOW);
  digitalWrite(C, LOW);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, LOW);
  digitalWrite(G, LOW);  
  switch (valor)
  {
  	case 'c':
  	{
        digitalWrite(A, HIGH);
 	    digitalWrite(D, HIGH);
        digitalWrite(E, HIGH);
        digitalWrite(F, HIGH);
      	break;
  	}
    case 'f':
  	{
        digitalWrite(A, HIGH);
        digitalWrite(E, HIGH);
        digitalWrite(F, HIGH);
        digitalWrite(G, HIGH);
      	break;
  	}
    case 'd':
      digitalWrite(G, HIGH);
      break;
    case 'o':
  	{
        digitalWrite(A, LOW);
  		digitalWrite(B, LOW);
  		digitalWrite(C, LOW);
  		digitalWrite(D, LOW);
  		digitalWrite(E, LOW);
  		digitalWrite(F, LOW);
  		digitalWrite(G, LOW);
      	break;
  	}
  }
}

void switchStateLeds(char valor){  
  switch (valor)
  {
  	case 'c':
  	{
        digitalWrite(ledRojo, HIGH);
 	    digitalWrite(ledAmarillo, LOW);
        digitalWrite(ledAzul, LOW);
      	break;
  	}
    case 'f':
  	{
        digitalWrite(ledAzul, HIGH);
        digitalWrite(ledAmarillo, LOW);
        digitalWrite(ledRojo, LOW);
      	break;
  	}
    case 'd':
        digitalWrite(ledAmarillo, HIGH);
        digitalWrite(ledAzul, LOW);
        digitalWrite(ledRojo, LOW);
        break;
    case 'o':
  	{
        digitalWrite(ledAmarillo, LOW);
  		digitalWrite(ledAzul, LOW);
  		digitalWrite(ledRojo, LOW);
      	break;
  	}
  }
}
