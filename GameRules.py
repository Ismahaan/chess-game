#Game rules

#schaak stukken(6+1-13)
 #loper
 #toren
 #pion
 #koningin
 #paar
 #koning

 #staten(beschikbaarheid)
 #schaak x2
 #schaakmat x2

 #De prositie van de stukken wordt geplaatst naar aanleiding van de vlak posities
 #Er wordt gebruik gemaakt van 64 bits vanwege de rekenkracht

#  schaak stukken moeten hun stappen kunnen doen
#  De schaalstukken moeten elkaar kunnen slaan
#  De schaakstukken moeten binnen het bord blijven
#  Als een schaakstuk is geslagen moet die van het bord verdwijnen
#  Op de lege plek komt weer een 0 te staan
#  De bijzondere zetten moeten de schaakstukken kunnen
#  De schaakstukken moeten het verschil tussen schaak en schaakmat kennen

# toren

# Moet zich horizontaal en verticaal bewegen
# method beweging toren
# kijkt in zijn eigen rij en kolom of die kan bewegen
# kijkt of er een schaakstuk voor de toren staat
# Kijkt of dat schaakstuk van zijn eigen team is of van een andere
# zoja blijf staan of ga een andere kant op als dat mogelijk
# Of kan de tegenstander slaan
