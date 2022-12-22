"""
Ödev 2:
Kullanıcıdan n pozitif tamsayısını girmesini isteyen bir program yazınız.
 Bu tamsayının saniye cinsinden olduğunu varsayarsak, programınız
saniye sayısını gün(day), saat(hours), dakika(minutes) ve saniyeye(seconds) çevirerek tam olarak aşağıda belirtilen
formatta yazdırmalıdır. İşte programınızın ne yapması gerektiğine dair birkaç örnek çalıştırma:
kullanıcı girdiğinde
369121517
programınız şunu yazdırmalıdır:
4272 days 5 hours 45 minutes 17 seconds
kullanıcı girdiğinde
24680
programınız şunu yazdırmalıdır:
0 days 6 hours 51 minutes 20 seconds
kullanıcı girdiğinde
129600
programınız şunu yazdırmalıdır:
1 days 12 hours 0 minutes 0 seconds
Yukarıdaki çıktıdaki sayıların ve kelimelerin yalnızca bir boşlukla ayrıldığına dikkat edin.
Tüm kelimeler küçük harflerle yazılmıştır. Çıktınız yukarıda gösterilen formatla tam olarak eşleşmelidir.
"""

seconds = int(input("Enter the time in seconds: "))
days = seconds//(60*60*24)  # or int(seconds/86400) or seconds//86400
hours = (seconds % 86400)//3600  # or int((seconds % 86400)//3600)
# or minutes = int(((seconds % 86400) % 3600)/60)
minutes = ((seconds % 86400) % 3600)//60
seconds = int(((seconds % 86400) % 3600) % 60)

print(f"{days} days {hours} hours {minutes} minutes {seconds} seconds")

# 2nd way
totalSec = int(input("Please Enter Total Sec :"))
day = totalSec//86400
min = (totalSec//60) % 60
sec = totalSec % 60
hour = ((totalSec//60)//60) % 24


print(f"{day} days {hour} hours {min} minutes {sec} seconds")
