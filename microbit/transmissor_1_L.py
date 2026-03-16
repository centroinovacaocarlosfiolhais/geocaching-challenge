# ============================================================
#  TRANSMISSOR — Geocaching Digital: O Legado do Lidador
#  ESTACAO 1 · Canal 1 · Letra L · ᛚ Laguz
# ============================================================
#  Este micro:bit esta escondido e emite continuamente.
#  Nao necessita de interacao — ligar e esconder.
#  power=7 → alcance maximo (obriga participantes a chegar perto)
# ============================================================

from microbit import *
import radio

# -- Configuracao desta estacao -----------------------------
CANAL  = 1        # grupo de radio (unico por estacao)
LETRA  = "L"      # letra que esta estacao revela
RUNA   = Image("09000:09000:99900:09090:09000")

# -- Inicializar radio -------------------------------------
radio.config(group=CANAL, power=3)   # power=7 = alcance maximo
radio.on()

# -- Mostrar simbolo continuamente ------------------------
display.show(RUNA)

# -- Loop: emitir letra a cada segundo --------------------
while True:
    radio.send(LETRA)
    sleep(1000)
