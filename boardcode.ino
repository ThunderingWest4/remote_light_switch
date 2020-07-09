//This is something like C i think
//Using a Particle Photon board to run this code

bool state = false;
//true means motor goes left, false means turn right
int m1 = D0;
int m2 = D2;
//one end of the switch is connected to power, other is connected to resistor going to ground
int toggle = D5;
bool remoteFlip = false;
bool justFlipped = false;
int prevstate;
int tps;
//to make sure that it doesnt keep flipping after bootup
bool justBooted = true;

void setup() {
    Particle.function("flip", flipSwitch);
    Particle.variable("Switch state", tps);
    Particle.variable("State bool", state);
    Particle.variable("Remote flip", remoteFlip);
    Particle.variable("Manual flip", justFlipped);
    pinMode(m1, OUTPUT);
    pinMode(m2, OUTPUT);
    pinMode(toggle, INPUT_PULLUP);
    
}

void loop() {
    //unnecessary maybe but just making sure that we avoid errors with the whole state vs tps thing
    //should be always aligned now
    if(digitalRead(toggle) == HIGH) {
        tps=1;
        state=true;
    } else { tps=0; state=false; }
    //checking that switch wasn't just:
    //flipped by pi (remoteFlip)
    //flipped manually (justflipped)
    //and that it was actually flipped (read!=prev)
    if(tps != prevstate && (!remoteFlip && !justFlipped) && !justBooted) {
        //moveMotor();
        //means that person flipped it manually and we don't move the motor
        remoteFlip = false;
        justFlipped = true;
        changeState("");
        //make it recognize that we now turning other way
    } else {
        justBooted = false;
        remoteFlip=false;
        justFlipped=false;
    }
    prevstate = tps;
    
}

void changeState(String s) {
    state = !state;
}

int flipSwitch(String s) {
    //changeState("");
    moveMotor();
    remoteFlip = true;
    return tps;
}

void moveMotor() {
    
    //while the switch is not flipped
    while(tps == digitalRead(toggle)) {
        if(state==true) {
            digitalWrite(m1, HIGH);
            digitalWrite(m2, LOW);
        } else {
            //means that state=false
            digitalWrite(m1, LOW);
            digitalWrite(m2, HIGH);
        }
    }
    digitalWrite(m1, LOW);
    digitalWrite(m2, LOW);
    //turn off motor
    
}

