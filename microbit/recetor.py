# ==================================================================
#  RECETOR — Geocaching Digital: O Legado do Lidador
#  Centro de Inovação Carlos Fiolhais · David Marques · Março 2026
# ==================================================================
#  Botão A  → desce canal (1 → 2 → 3 → 4 → 5 → 6)
#  Botão B  → sobe canal  (6 → 5 → 4 → 3 → 2 → 1)
#  Quando recebe sinal:
#    1. Beep duplo
#    2. Mostra símbolo rúnico 2.5 segundos
#    3. Mostra a letra correspondente 2.5 segundos
#    4. Volta a mostrar número do canal
# ============================================================

from microbit import *
import radio
import music

# ── Padrões rúnicos (5×5) ──────────────────────────────────
# 9 = LED aceso · 0 = LED apagado · ':' = separador de linha

RUNAS = {
    "L": Image("09000:09000:99900:09090:09000"),  # ᛚ Laguz
    "I": Image("09090:00900:99999:00900:09090"),  # ✳ Asterisco
    "D": Image("90009:09090:00900:09090:90009"),  # ᛞ Dagaz
    "A": Image("00900:00900:09990:90900:00900"),  # ᚨ Ansuz
    "O": Image("00900:09090:90009:09090:90009"),  # ᛟ Othala
    "R": Image("09090:99999:09090:99999:09090"),  # # Hash
}

# ── Alcance do rádio ───────────────────────────────────────
# power: 0=mínimo (~1m), 1=~10m, 2=~20m, ... 7=máximo
# Ajustar conforme o espaço — 2 é um bom compromisso

POWER = 5

# Canal inicial
canal = 1
radio.config(group=canal, power=POWER)
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

# Volume máximo no altifalante integrado
set_volume(255)

# Mostrar canal inicial ao ligar
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

        # 1. Beep duplo de confirmação
        music.pitch(880,  duration=150, wait=True)
        sleep(60)
        music.pitch(1320, duration=250, wait=True)

        # 2. Símbolo rúnico — 2.5 segundos
        display.show(RUNAS[msg])
        sleep(2500)

        # 3. Voltar ao número do canal
        mostrar_canal()

    sleep(50)
