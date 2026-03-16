# ============================================================
#  TRANSMISSOR — Geocaching Digital: O Legado do Lidador
#  ESTACAO 4 · Canal 4 · Letra A · ᚨ Ansuz
#  Local: Ginasio
# ============================================================
#  Este micro:bit esta escondido e emite continuamente.
#  Nao necessita de interacao — ligar e esconder.
#  power=7 → alcance maximo (obriga participantes a chegar perto)
# ============================================================

from microbit import *
import radio

# -- Configuracao desta estacao -----------------------------
CANAL  = 4        # grupo de radio (unico por estacao)
LETRA  = "A"      # letra que esta estacao revela
RUNA   = Image("00900:00900:09990:90900:00900")

# -- Inicializar radio -------------------------------------
radio.config(group=CANAL, power=3)   # power=7 = alcance maximo
radio.on()

# -- Mostrar simbolo continuamente ------------------------
display.show(RUNA)

# -- Loop: emitir letra a cada segundo --------------------
while True:
    radio.send(LETRA)
    sleep(1000)
