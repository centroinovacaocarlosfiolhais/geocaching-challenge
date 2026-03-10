# ============================================================
#  TRANSMISSOR — Geocaching Digital: O Legado do Lidador
#  ESTACAO 5 · Canal 5 · Letra O · ᛟ Othala
#  Local: Cantina
# ============================================================
#  Este micro:bit esta escondido e emite continuamente.
#  Nao necessita de interacao — ligar e esconder.
#  power=0 → alcance ~1-2m (obriga participantes a chegar perto)
# ============================================================

from microbit import *
import radio

# -- Configuracao desta estacao -----------------------------
CANAL  = 5        # grupo de radio (unico por estacao)
LETRA  = "O"      # letra que esta estacao revela
RUNA   = Image("00900:09090:90009:09090:90009")

# -- Inicializar radio -------------------------------------
radio.config(group=CANAL, power=0)   # power=0 = alcance minimo
radio.on()

# -- Mostrar simbolo continuamente ------------------------
display.show(RUNA)

# -- Loop: emitir letra a cada segundo --------------------
while True:
    radio.send(LETRA)
    sleep(1000)
