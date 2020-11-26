from src.audio import parbaudam_darbibu, atskano_datni, beep
from src.audio_mix import atskano, mikse_skanas, saglaba_skanu

# 1. solis
# Pārbaudām vai bibliotēka strādā
#parbaudam_darbibu()

# 2.solis
# Atrodam un saglabājam audio datni wav formātā
# Audio datnes var atrast, piemēram, šeit - http://soundbible.com/
atskano_datni("poker-chips-daniel_simon.wav")

# 3.solis
# Veidojam skaņas tīri matemātiski
#beep(327.03, 1)    # MI
#beep(348.83, 1)    # FA
#beep(392.44, 1)    # SOL
#beep(436.04, 1)    # LA
#beep(490.55, 1)    # SI
#beep(523.25, 1)    # DO
#beep()             # Noklusētā frekvence un ilgums

# 4.solis
# Miksējam skaņas, mainām skaļumu
#atskano("Birds In Forest-SoundBible.com-472460759.wav")

# 5.solis
# saglabajam skaņu datnē
# skana = mikse_skanas("dati/clock-chimes-daniel_simon.wav")
# saglaba_skanu(skana, "dati/zvani.wav")
