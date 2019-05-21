import time
import smtplib
from pirc522 import RFID
import signal
import RPi.GPIO as GPIO

ledpin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin, GPIO.OUT)
rdr = RFID()
util = rdr.util()
util.debug = True


i = 0



try:
   if kart_uid == "xxxxxxxxxxxxxxxx":
       Masa=1
             if   i == 3:
                    time.sleep(86000)
                    print("Ceza aldınız.")
                    i == 0
        
        
    
         if GPIO.input(sensor_pin) and i == 0:
        
   
            kullanici = "kutuphanesesuygulama@gmail.com"
            kullanici_sifresi = 'kutuphane123'
            alici = 'sinan.usta.1905@gmail.com'  # alıcının mail adresi
            konu = 'UYARI1'
            msj = 'Lütfen kütüphane içinde sessiz olalım!!!' 
           
            email_text1 = """"
            From: {}
            To: {}
            Subject: {}
            {}
            """.format(kullanici, alici, konu, msj)

            server = smtplib.SMTP('smtp.gmail.com:587')  # servere bağlanmak için gerekli host ve portu belirttik
            server.starttls()  # serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
            server.login(kullanici, kullanici_sifresi)  # Gmail SMTP server'ına giriş yaptık
            server.sendmail(kullanici, alici, email_text1)  # Mail'imizi gönderdik
            server.close()  # SMTP serverimizi kapattık
            print('email-1 gönderildi')
            sleep(10)
            i = i + 1
         if GPIO.input(sensor_pin) and i == 1:
        
   
            kullanici = "kutuphanesesuygulama@gmail.com"
            kullanici_sifresi = 'kutuphane123'
            alici = 'sinan.usta.1905@gmail.com'  # alıcının mail adresi
            konu = 'UYARI2'
            msj = 'Sayın SİNAN USTA bu size son uyarımızdır kütüphane içinde sessiz olmalısınız aksi taktirde ceza alacaksınız!!!' 
           
            email_text1 = """"
            From: {}
            To: {}
            Subject: {}
            {}
            """.format(kullanici, alici, konu, msj)

            server = smtplib.SMTP('smtp.gmail.com:587')  # servere bağlanmak için gerekli host ve portu belirttik
            server.starttls()  # serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
            server.login(kullanici, kullanici_sifresi)  # Gmail SMTP server'ına giriş yaptık
            server.sendmail(kullanici, alici, email_text1)  # Mail'imizi gönderdik
            server.close()  # SMTP serverimizi kapattık
            print('email-2 gönderildi')
            sleep(10)
            i = i + 1

         if GPIO.input(sensor_pin) and i == 2:
            kullanici = "kutuphanesesuygulama@gmail.com"
            kullanici_sifresi = 'kutuphane123'
            alici = 'sinan.usta.1905@gmail.com'  # alıcının mail adresi
            alici2 = 'muharremozturk1998@gmail.com'
            konu = 'UYARI3'
            msj = 'Sayın SİNAN USTA  kütüphane içinde yüksek sesle konustuğunuz için 1gün boyunca ceza aldınız.Güvenlik görevlisi birazdan sizi kütüphaneden cıkaracaktır.!!!' 
            msj2 = 'Sayın güvenlik görevlisi 1 numaralı masamızda oturan öğrencimiz SİNAN USTA uyarılara rağmen yüksek sesle konumaya devam ederek diğer öğrencilerimizi rahatsız etmiştir.Lütfen kütüphaneden uzaklaştırılmasını sağlayalım.Teşekkürler.'
            # bilgileri bir metinde derledik

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

            server = smtplib.SMTP('smtp.gmail.com:587')  # servere bağlanmak için gerekli host ve portu belirttik
            server.starttls()  # serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
            server.login(kullanici, kullanici_sifresi)  # Gmail SMTP server'ına giriş yaptık
            server.sendmail(kullanici, alici, email_text)  # Mail'imizi gönderdik
            server.close()  # SMTP serverimizi kapattık
            print('email-3 gönderildi')


            server = smtplib.SMTP('smtp.gmail.com:587')  # servere bağlanmak için gerekli host ve portu belirttik
            server.starttls()  # serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
            server.login(kullanici, kullanici_sifresi)  # Gmail SMTP server'ına giriş yaptık
            server.sendmail(kullanici, alici2, email_text2)  # Mail'imizi gönderdik
            server.close()  # SMTP serverimizi kapattık
            print('email-3 gönderildi')
            i += 1
            GPIO.output(buzzer_pin, True)
	    time.sleep(2)
	    GPIO.output(buzzer_pin, False)
	    time.sleep(1)
            GPIO.output(led, True)
            time.sleep(2)
            GPIO.output(led, False)
            time.sleep(1)
   if kart_uid == "yyyyyyyyyyyyyyyyyy":
         Masa=2
             if   i == 3:
                    time.sleep(86000)
                    print("Ceza aldınız.")
                    i == 0
        
        
    
         if GPIO.input(sensor_pin) and i == 0:
        
   
            kullanici = "kutuphanesesuygulama@gmail.com"
            kullanici_sifresi = 'kutuphane123'
            alici = 'batuyerinde@gmail.com'  # alıcının mail adresi
            konu = 'UYARI1'
            msj = 'Lütfen kütüphane içinde sessiz olalım!!!' 
           
            email_text1 = """"
            From: {}
            To: {}
            Subject: {}
            {}
            """.format(kullanici, alici, konu, msj)

            server = smtplib.SMTP('smtp.gmail.com:587')  # servere bağlanmak için gerekli host ve portu belirttik
            server.starttls()  # serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
            server.login(kullanici, kullanici_sifresi)  # Gmail SMTP server'ına giriş yaptık
            server.sendmail(kullanici, alici, email_text1)  # Mail'imizi gönderdik
            server.close()  # SMTP serverimizi kapattık
            print('email-1 gönderildi')
            sleep(10)
            i = i + 1
         if GPIO.input(sensor_pin) and i == 1:
        
   
            kullanici = "kutuphanesesuygulama@gmail.com"
            kullanici_sifresi = 'kutuphane123'
            alici = 'batuyerinde@gmail.com'  # alıcının mail adresi
            konu = 'UYARI2'
            msj = 'Sayın BATUHAN YERİNDE kütüphane içinde sessiz olalım bu size son uyarımızıdır aksi taktirde cezalandırılacaksınız.!!!' 
           
            email_text1 = """"
            From: {}
            To: {}
            Subject: {}
            {}
            """.format(kullanici, alici, konu, msj)

            server = smtplib.SMTP('smtp.gmail.com:587')  # servere bağlanmak için gerekli host ve portu belirttik
            server.starttls()  # serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
            server.login(kullanici, kullanici_sifresi)  # Gmail SMTP server'ına giriş yaptık
            server.sendmail(kullanici, alici, email_text1)  # Mail'imizi gönderdik
            server.close()  # SMTP serverimizi kapattık
            print('email-2 gönderildi')
            sleep(10)
            i = i + 1

         if GPIO.input(sensor_pin) and i == 2:
            kullanici = "kutuphanesesuygulama@gmail.com"
            kullanici_sifresi = 'kutuphane123'
            alici = 'batuyerinde@gmail.com'  # alıcının mail adresi
            alici2 = 'muharremozturk1998@gmail.com'
            konu = 'UYARI3'
            msj = 'Sayın BATUHAN YERİNDE  kütüphane içinde yüksek sesle konustuğunuz için 1gün boyunca ceza aldınız.Güvenlik görevlisi birazdan sizi kütüphaneden cıkaracaktır. !' 
            msj2 = 'Sayın güvenlik görevlisi 2 numaralı masamızda oturan öğrencimiz SİNAN USTA uyarılara rağmen yüksek sesle konumaya devam ederek diğer öğrencilerimizi rahatsız etmiştir.Lütfen kütüphaneden uzaklaştırılmasını sağlayalım.Teşekkürler.'
            # bilgileri bir metinde derledik

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

            server = smtplib.SMTP('smtp.gmail.com:587')  # servere bağlanmak için gerekli host ve portu belirttik
            server.starttls()  # serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
            server.login(kullanici, kullanici_sifresi)  # Gmail SMTP server'ına giriş yaptık
            server.sendmail(kullanici, alici, email_text)  # Mail'imizi gönderdik
            server.close()  # SMTP serverimizi kapattık
            print('email-3 gönderildi')


            server = smtplib.SMTP('smtp.gmail.com:587')  # servere bağlanmak için gerekli host ve portu belirttik
            server.starttls()  # serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
            server.login(kullanici, kullanici_sifresi)  # Gmail SMTP server'ına giriş yaptık
            server.sendmail(kullanici, alici2, email_text2)  # Mail'imizi gönderdik
            server.close()  # SMTP serverimizi kapattık
            print('email-3 gönderildi')
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
        print("bir hata oluştu")
        sleep(0.1)
