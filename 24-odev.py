"""
Ödev 1:
Kullanıcıdan, kullanıcının bir hafta içinde çalıştığı toplam saat olan 'n' tamsayısını
girmesini isteyen ve kullanıcının o hafta boyunca kazandığı toplam parayı hesaplayıp
yazdıran bir program yazın. Kullanıcı 0'dan küçük veya 168'den büyük herhangi bir sayı
girerse (n < 0 veya n > 168), programınız INVALID yazdırmalıdır.
İlk 40 saat için saatlik ücretin saat başına 8 ABD doları olduğunu varsayalım.
41 ile 50 (41 <= n <= 50 ) arasındaki fazladan saatler için saatlik ücret, saat başına 9 ABD dolarıdır.
50'den fazla ekstra saat için saatlik ücret, saat başına 10 ABD dolarıdır.
İşte birkaç örnek:
kullanıcı -5 girerse, programınız şunu yazdırmalıdır
INVALID
kullanıcı 34 girerse, programınız şunu yazdırmalıdır
YOU MADE 272 DOLLARS THIS WEEK
kullanıcı 45 girerse programınız şunu yazdırmalıdır
YOU MADE 365 DOLLARS THIS WEEK
kullanıcı 67 girerse programınız şunu yazdırmalıdır
YOU MADE 580 DOLLARS THIS WEEK
Kullanıcı tarafından kazanılan para miktarının bir tamsayı (kayan değil) olması gerektiğini ve
çıktınızın tam olarak yukarıda belirtilen biçimle (boşluklar ve büyük harf kullanımı dahil) eşleşmesi gerektiğini unutmayın."""

weekHours = int(input("Enter your week hours between 0-168 : "))

if weekHours < 0:
    print("INVALID")
elif weekHours <= 40:
    print(f"YOU MADE {weekHours*8} DOLLARS THIS WEEK")
elif weekHours <= 50:
    print(f"YOU MADE {320+(weekHours-40)*9} DOLLARS THIS WEEK")
elif weekHours <= 168:
    print(F"YOU MADE {410+(weekHours-50)*10} DOLLARS THIS WEEK")
else:
    print("INVALID")