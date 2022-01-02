#include <Servo.h> //memanggil library servo karena kita akan menggunakan module servo
 
Servo servol; //menentukan pin 2 s/d 7 sebagai mode INPUT 
 
void setup(){ 
  for(pin=2;pin<=7;pin+=1){  //menentukan pin 2 s/d 7 sebagai mode INPUT 
    pinMode(pin,INPUT);
    
  }
 
  pinMode(13,OUTPUT);  //menentukan pin 13 sebagai OUTPUT yang nantinya digunakan saat fungsi else blinking
  servol.attach(9);  //menentukan servo pada pin 9
}
 
void loop(){
  if (digitalRead(2)==HIGH && digitalRead(3)==HIGH && digitalRead(4)==LOW && digitalRead(5)==LOW && digitalRead(6)==LOW && digitalRead(7)==LOW){
    servol.write(0); //tabel kebenaran 110000, servo ke 0'
  }
  else if (digitalRead(2)==HIGH && digitalRead(3)==LOW && digitalRead(4)==HIGH && digitalRead(5)==LOW && digitalRead(6)==LOW && digitalRead(7)==LOW){
    servol.write(180);  //tabel kebenaran 101000, servo ke 180'
  }
  else if (digitalRead(2)==HIGH && digitalRead(3)==LOW && digitalRead(4)==LOW && digitalRead(5)==HIGH && digitalRead(6)==LOW digitalRead(7)==LOW){
    servol.write(135);  //tabel kebenaran 100100, servo ke 135'
  }
  else if (digitalRead(2)==HIGH && digitalRead(3)==LOW && digitalRead(4)==LOW && digitalRead(5)==LOW && digitalRead(6)==HIGH digitalRead(7)==LOW){ 
   servol.write(90);  //tabel kebenaran 100010, servo ke 90'
     
  }
  else if (digitalRead(2)==HIGH && digitalRead(3)==LOW && digitalRead(4)==LOW && digitalRead(5)==LOW && digitalRead(6)==LOW digitalRead(7)==HIGH){ 
    servol.write(45);  //tabel kebenaran 100001, servo ke 45'
  }
   else if (digitalRead(2)==LOW && digitalRead(3)==HIGH && digitalRead(4)==HIGH && digitalRead(5)==LOW && digitalRead(6)==LOW digitalRead(7)==LOW){ 
    servol.write(160);  //tabel kebenaran 011000, servo ke 160'
   }
   else if (digitalRead(2)==LOW && digitalRead(3)==HIGH && digitalRead(4)==LOW && digitalRead(5)==HIGH && digitalRead(6)==LOW digitalRead(7)==LOW){
     servol.write(115);  //tabel kebenaran 010100, servo ke 115'
   }
    else if (digitalRead(2)==LOW && digitalRead(3)==HIGH && digitalRead(4)==LOW && digitalRead(5)==LOW && digitalRead(6)==HIGH digitalRead(7)==LOW){
      servol.write(70);  //tabel kebenaran 010010, servo ke 70'
    }
    else if (digitalRead(2)==LOW && digitalRead(3)==HIGH && digitalRead(4)==LOW && digitalRead(5)==LOW && digitalRead(6)==LOW digitalRead(7)==HIGH){
      servol.write(70);  //tabel kebenaran 010001, servo ke 25'
    }
    else{
      digitalWrite(13,HIGH); //jika tidak ada yang sesuai dengan tabel kebenaran
      delay(20);             //servo akan ke 0 derajat dan led pin 13 blinking
      digitalWrite(13,LOW);
      delay(20);
      servol.write(0);
    }
  
    
  
  
}
 
