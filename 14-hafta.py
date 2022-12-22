# Kullanıcıdan 1 ile 7 arasında pozitif bir tamsayı isteyen
# (Kullanıcının 1'den 7'ye kadar herhangi bir sayı girebileceğini varsayalım)
# ve bu sayıya karşılık gelen haftanın gününü tamamı büyük harflerle yazdıran
# bir program yazınız. Haftanın gününün PAZARTESİ'den başladığını varsayalım.
# Örneğin: kullanıcı şunu girerse:  2
# programınız SALI yazdırsın...

# 1st way
days = ['MONDAY', "TUESDAY", "WEDNESDAY",
        "THURSDAY", "FRIDAY", "SATURDAY", 'SUNDAY']
inputDay = int(input("Enter an integer between 1 and 7 "))
print(days[inputDay-1])


# 2nd way
day = int(input("Enter an integer between 1 and 7 "))
if (day == 1):
    {print("MONDAY")}
elif (day == 2):
    {print("TUESDAY")}
elif (day == 3):
    {print("WEDNESDAY")}
elif (day == 4):
    {print("THURSDAY")}
elif (day == 5):
    {print("FRIDAY")}
elif (day == 6):
    {print("SATURDAY")}
else:
    {print("SUNDAY")}