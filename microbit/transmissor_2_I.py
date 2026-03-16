# ============================================================
#  TRANSMISSOR — Geocaching Digital: O Legado do Lidador
#  ESTACAO 2 · Canal 2 · Letra I · ✳ Asterisco
#  Local: Corredor principal
# ============================================================
#  Este micro:bit esta escondido e emite continuamente.
#  Nao necessita de interacao — ligar e esconder.
#  power=7 → alcance maximo (obriga participantes a chegar perto)
# ============================================================

from microbit import *
import radio

# -- Configuracao desta estacao -----------------------------
CANAL  = 2        # grupo de radio (unico por estacao)
LETRA  = "I"      # letra que esta estacao revela
RUNA   = Image("09090:00900:99999:00900:09090")

# -- Inicializar radio -------------------------------------
radio.config(group=CANAL, power=3)   # power=7 = alcance maximo
radio.on()

# -- Mostrar simbolo continuamente ------------------------
display.show(RUNA)

# -- Loop: emitir letra a cada segundo --------------------
while True:
    radio.send(LETRA)
    sleep(1000)
