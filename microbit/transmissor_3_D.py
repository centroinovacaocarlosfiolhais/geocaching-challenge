# ============================================================
#  TRANSMISSOR — Geocaching Digital: O Legado do Lidador
#  ESTACAO 3 · Canal 3 · Letra D · ᛞ Dagaz
#  Local: Lab de Ciencias
# ============================================================
#  Este micro:bit esta escondido e emite continuamente.
#  Nao necessita de interacao — ligar e esconder.
#  power=0 → alcance ~1-2m (obriga participantes a chegar perto)
# ============================================================

from microbit import *
import radio

# -- Configuracao desta estacao -----------------------------
CANAL  = 3        # grupo de radio (unico por estacao)
LETRA  = "D"      # letra que esta estacao revela
RUNA   = Image("90009:09090:00900:09090:90009")

# -- Inicializar radio -------------------------------------
radio.config(group=CANAL, power=0)   # power=0 = alcance minimo
radio.on()

# -- Mostrar simbolo continuamente ------------------------
display.show(RUNA)

# -- Loop: emitir letra a cada segundo --------------------
while True:
    radio.send(LETRA)
    sleep(1000)
