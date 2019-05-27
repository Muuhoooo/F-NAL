import time
import smtplib
from pirc522 import RFID
import signal
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
buzzer_pin = 17
sensor_pin = 16
ledpin = 7
GPIO.setup(ledpin, GPIO.OUT)
rdr = RFID()
util = rdr.util()
util.debug = True


i = 0



try:
    
    if kart_uid == "75 153 52 13 235":
        
        
        Masa=1
        if i == 3:
            
        
            time.sleep(86000)
            print("Ceza aldiniz.")
            i == 0
        
        
    
        if GPIO.input(sensor_pin) and i == 0:
             
             
        
   
            kullanici = "kutuphanesesuygulama@gmail.com"
            kullanici_sifresi = 'kutuphane123'
            alici = 'melihturkaslan98@gmail.com'  
            konu = 'UYARI1'
            msj = 'Lutfen kutuphane icinde sessiz olalim!!!' 
           
            email_text1 = """"
            From: {}
            To: {}
            Subject: {}
            {}
            """.format(kullanici, alici, konu, msj)

            server = smtplib.SMTP('smtp.gmail.com:587')  
            server.starttls()  
            server.login(kullanici, kullanici_sifresi)  
            server.sendmail(kullanici, alici, email_text1)  
            server.close()  
            print('email-1 gonderildi')
            sleep(10)
            i = i + 1
        if GPIO.input(sensor_pin) and i == 1:
             
        
   
            kullanici = "kutuphanesesuygulama@gmail.com"
            kullanici_sifresi = 'kutuphane123'
            alici = 'melihturkaslan98@gmail.com'  
            konu = 'UYARI2'
            msj = 'Sayin SINAN USTA bu size son uyarimizdir kutuphane icinde sessiz olmalisiniz aksi taktirde ceza alacaksiniz!!!' 
           
            email_text1 = """"
            From: {}
            To: {}
            Subject: {}
            {}
            """.format(kullanici, alici, konu, msj)

            server = smtplib.SMTP('smtp.gmail.com:587') 
            server.starttls() 
            server.login(kullanici, kullanici_sifresi) 
            server.sendmail(kullanici, alici, email_text1)  
            server.close()  
            print('email-2 gonderildi')
            sleep(10)
            i = i + 1

        if GPIO.input(sensor_pin) and i == 2:
            kullanici = "kutuphanesesuygulama@gmail.com"
            kullanici_sifresi = 'kutuphane123'
            alici = 'melihturkaslan98@gmail.com'  
            alici2 = 'muharremozturk1998@gmail.com'
            konu = 'UYARI3'
            msj = 'Sayin SINAN USTA  kutuphane icinde yuksek sesle konustugunuz icin 1gun boyunca ceza aldiniz.Guvenlik gorevlisi birazdan sizi kutuphaneden cikaracaktir.!!!' 
            msj2 = 'Sayin guvenlik gorevlisi 1 numarali masamizda oturan ogrencimiz SINAN USTA uyarilara ragmen yuksek sesle konusmaya devam ederek diger ogrencilerimizi rahatsiz etmistir.Lutfen kutuphaneden uzaklastirilmasini saglayalim.Tesekkurler.'
            

            email_text = """
            From: {}
            To: {}
            Subject: {}
            {}
            """.format(kullanici, alici, konu, msj)

            email_text2 = """"
            From: {}
            To: {}
            Subject: {}
            {}
            """.format(kullanici, alici2, konu, msj2)

            server = smtplib.SMTP('smtp.gmail.com:587')  
            server.starttls()
            server.login(kullanici, kullanici_sifresi)  
            server.sendmail(kullanici, alici, email_text)  
            server.close()  
            print('email-3 gonderildi')


            server = smtplib.SMTP('smtp.gmail.com:587')  
            server.starttls()  
            server.login(kullanici, kullanici_sifresi)  
            server.sendmail(kullanici, alici2, email_text2) 
            server.close()  
            print('email-3 gonderildi')
            i += 1
            GPIO.output(buzzer_pin, True)
            time.sleep(2)
            GPIO.output(buzzer_pin, False)
            time.sleep(1)
            GPIO.output(led, True)
            time.sleep(2)
            GPIO.output(led, False)
            time.sleep(1)
    if kart_uid == "73 143 130 99 39":
        Masa=2
        if   i == 3:
            time.sleep(86000)
            print("Ceza aldiniz.")
            i == 0
        
        
    
        if GPIO.input(sensor_pin) and i == 0:
        
   
            kullanici = "kutuphanesesuygulama@gmail.com"
            kullanici_sifresi = 'kutuphane123'
            alici = 'batuyerinde@gmail.com'  
            konu = 'UYARI1'
            msj = 'Lutfen kutuphane icinde sessiz olalim!!!' 
           
            email_text1 = """"
            From: {}
            To: {}
            Subject: {}
            {}
            """.format(kullanici, alici, konu, msj)

            server = smtplib.SMTP('smtp.gmail.com:587')  
            server.starttls()  
            server.login(kullanici, kullanici_sifresi)  
            server.sendmail(kullanici, alici, email_text1)  
            server.close() 
            print('email-1 gonderildi')
            sleep(10)
            i = i + 1
        if GPIO.input(sensor_pin) and i == 1:
        
   
            kullanici = "kutuphanesesuygulama@gmail.com"
            kullanici_sifresi = 'kutuphane123'
            alici = 'batuyerinde@gmail.com'  
            konu = 'UYARI2'
            msj = 'Sayin BATUHAN YERINDE kutuphane icinde sessiz olalim bu size son uyarimizidir aksi taktirde cezalandirilacaksiniz.!!!' 
           
            email_text1 = """"
            From: {}
            To: {}
            Subject: {}
            {}
            """.format(kullanici, alici, konu, msj)

            server = smtplib.SMTP('smtp.gmail.com:587') 
            server.starttls()  
            server.login(kullanici, kullanici_sifresi)  
            server.sendmail(kullanici, alici, email_text1)  
            server.close()  
            print('email-2 gonderildi')
            sleep(10)
            i = i + 1

        if GPIO.input(sensor_pin) and i == 2:
            kullanici = "kutuphanesesuygulama@gmail.com"
            kullanici_sifresi = 'kutuphane123'
            alici = 'batuyerinde@gmail.com'  
            alici2 = 'muharremozturk1998@gmail.com'
            konu = 'UYARI3'
            msj = 'Sayin BATUHAN YERINDE  kutuphane icinde yuksek sesle konustugunuz icin 1gun boyunca ceza aldiniz.Guvenlik gorevlisi birazdan sizi kutuphaneden cikaracaktir. !' 
            msj2 = 'Sayin guvenlik gorevlisi 2 numarali masamizda oturan ogrencimiz BATUHAN YERINDE uyarilara ragmen yuksek sesle konusmaya devam ederek diger ogrencilerimizi rahatsiz etmistir.Lutfen kutuphaneden uzaklastirilmasini saglayalim.Tesekkurler.'
            

            email_text = """
            From: {}
            To: {}
            Subject: {}
            {}
            """.format(kullanici, alici, konu, msj)

            email_text2 = """"
            From: {}
            To: {}
            Subject: {}
            {}
            """.format(kullanici, alici2, konu, msj2)

            server = smtplib.SMTP('smtp.gmail.com:587')  
            server.starttls()  
            server.login(kullanici, kullanici_sifresi)  
            server.sendmail(kullanici, alici, email_text)  
            server.close()  
            print('email-3 gonderildi')


            server = smtplib.SMTP('smtp.gmail.com:587')  
            server.starttls()  
            server.login(kullanici, kullanici_sifresi)  
            server.sendmail(kullanici, alici2, email_text2) 
            server.close()  
            print('email-3 gonderildi')
            i += 1
            GPIO.output(buzzer_pin, True)
            time.sleep(2)
            GPIO.output(buzzer_pin, False)
            time.sleep(1)
            GPIO.output(led, True)
            time.sleep(2)
            GPIO.output(led, False)
            time.sleep(1)    


except:
        print("bir hata olustu")
        time.sleep(0.1)
