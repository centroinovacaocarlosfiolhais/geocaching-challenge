# ============================================================
#  RECETOR — Geocaching Digital: O Legado do Lidador
#  Escola Secundária da Maia · 20 março 2026
# ============================================================
#  Botão A  → desce canal (1 → 2 → 3 → 4 → 5 → 6)
#  Botão B  → sobe canal  (6 → 5 → 4 → 3 → 2 → 1)
#  Quando recebe sinal:
#    1. Beep
#    2. Mostra símbolo rúnico 3 segundos
#    3. Volta a mostrar número do canal
# ============================================================

from microbit import *
import radio
import music

# ── Padrões rúnicos (5×5) ──────────────────────────────────
# Cada string: 5 linhas × 5 dígitos (9=aceso, 0=apagado)
# separadas por ':'

RUNAS = {
    "L": Image("09000:09000:99900:09090:09000"),  # ᛚ Laguz
    "I": Image("09090:00900:99999:00900:09090"),  # ✳ Asterisco
    "D": Image("90009:09090:00900:09090:90009"),  # ᛞ Dagaz
    "A": Image("00900:00900:09990:90900:00900"),  # ᚨ Ansuz
    "O": Image("00900:09090:90009:09090:90009"),  # ᛟ Othala
    "R": Image("09090:99999:09090:99999:09090"),  # # Hash
}

# Mapeamento canal → letra
CANAL_LETRA = {1: "L", 2: "I", 3: "D", 4: "A", 5: "O", 6: "R"}

# Canal inicial
canal = 1
radio.config(group=canal, power=0)
radio.on()

def mostrar_canal():
    display.show(str(canal))

def subir_canal():
    global canal
    if canal < 6:
        canal += 1
        radio.config(group=canal)
        mostrar_canal()

def descer_canal():
    global canal
    if canal > 1:
        canal -= 1
        radio.config(group=canal)
        mostrar_canal()

# Mostrar canal inicial
mostrar_canal()

# ── Loop principal ──────────────────────────────────────────
while True:

    # Botão A → desce canal
    if button_a.was_pressed():
        descer_canal()

    # Botão B → sobe canal
    if button_b.was_pressed():
        subir_canal()

    # Verificar se há sinal de uma estação
    msg = radio.receive()
    if msg and msg in RUNAS:
        # Beep de confirmação
        music.pitch(880, duration=200, wait=False)
        sleep(100)
        music.pitch(1100, duration=300, wait=True)

        # Mostrar símbolo rúnico
        display.show(RUNAS[msg])
        sleep(3000)

        # Voltar a mostrar número do canal
        mostrar_canal()

    sleep(50)
