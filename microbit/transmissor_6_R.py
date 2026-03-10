# ============================================================
#  TRANSMISSOR — Geocaching Digital: O Legado do Lidador
#  ESTACAO 6 · Canal 6 · Letra R · # Hash
#  Local: Entrada principal
# ============================================================
#  Este micro:bit esta escondido e emite continuamente.
#  Nao necessita de interacao — ligar e esconder.
#  power=0 → alcance ~1-2m (obriga participantes a chegar perto)
# ============================================================

from microbit import *
import radio

# -- Configuracao desta estacao -----------------------------
CANAL  = 6        # grupo de radio (unico por estacao)
LETRA  = "R"      # letra que esta estacao revela
RUNA   = Image("09090:99999:09090:99999:09090")

# -- Inicializar radio -------------------------------------
radio.config(group=CANAL, power=0)   # power=0 = alcance minimo
radio.on()

# -- Mostrar simbolo continuamente ------------------------
display.show(RUNA)

# -- Loop: emitir letra a cada segundo --------------------
while True:
    radio.send(LETRA)
    sleep(1000)
