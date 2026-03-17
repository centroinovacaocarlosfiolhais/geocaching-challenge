# Geocaching Digital — O Legado do Lidador

> Atividade de escape room com micro:bits, cifra rúnica e geocache real.  
> Escola Secundária da Maia · 20 de março de 2026 · 19h00–23h00

---

## Conceito

Os participantes recebem um **micro:bit** e uma **folha cifrada** com a palavra **LIDADOR** codificada em símbolos rúnicos. Exploram o espaço escolar à noite, varrem frequências de rádio, descobrem 6 micro:bits escondidos — cada um a emitir uma letra — e decifram a mensagem.

No final, escrevem `LIDADOR` num **terminal CRT dos anos 80** que revela as coordenadas GPS de uma **geocache real** escondida na escola.

A narrativa é baseada em **Soeiro Mendes da Maia** (séc. XI–XII), cavaleiro medieval que deu nome à cidade — "O Lidador" significa "o guerreiro".

```
Participantes: até 10 pessoas · 2–3 grupos de 3–4
Duração:       4 horas (19h–23h)
Hardware:      micro:bit V2 (6 transmissores + 1 recetor por grupo)
Tecnologia:    MicroPython · rádio interno · HTML/CSS/JS
```

---

## Ficheiros

```
geocaching-lidador/
│
├── guiao_dinamizador.html   — guião completo para o dinamizador
│                              (sidebar navegável, checklist interativa,
│                               padrões LED, fases colapsáveis)
│
├── codigo_microbit.html     — documentação técnica do código
│                              (tabs: visão geral, recetor, transmissores,
│                               como carregar, testar & debug)
│
├── terminal_crt.html        — terminal CRT dos anos 80
│                              (configurável via JSON embutido,
│                               botão power skeuomórfico IBM PS/2)
│
└── microbit/
    ├── recetor.py           — código do micro:bit dos participantes
    ├── transmissor_1_L.py   — estação 1 · canal 1 · letra L · Biblioteca
    ├── transmissor_2_I.py   — estação 2 · canal 2 · letra I · Corredor
    ├── transmissor_3_D.py   — estação 3 · canal 3 · letra D · Lab Ciências
    ├── transmissor_4_A.py   — estação 4 · canal 4 · letra A · Ginásio
    ├── transmissor_5_O.py   — estação 5 · canal 5 · letra O · Cantina
    └── transmissor_6_R.py   — estação 6 · canal 6 · letra R · Entrada
```

---

## Como funciona

### 1. Rádio micro:bit

O micro:bit V2 tem rádio interno que comunica por **grupos (0–255)**. Cada transmissor fica fixo num grupo. O recetor muda de grupo com os botões A/B.

| Canal | Letra | Símbolo | Local sugerido |
|-------|-------|---------|----------------|
| 1 | L | ᛚ Laguz | Biblioteca |
| 2 | I | ✳ Asterisco | Corredor principal |
| 3 | D | ᛞ Dagaz *(2× em LIDADOR)* | Lab de Ciências |
| 4 | A | ᚨ Ansuz | Ginásio |
| 5 | O | ᛟ Othala | Cantina |
| 6 | R | # Hash | Entrada principal |

`power=0` nos transmissores limita o alcance a ~1–2m — os participantes têm de chegar mesmo perto da estação para receber o sinal.

### 2. Cifra rúnica

Cada estação emite uma letra. O participante tem uma **folha impressa** com:
- A mensagem cifrada `L · I · D · A · D · O · R` em símbolos rúnicos
- Uma tabela em branco para mapear símbolo → letra

O símbolo **ᛞ Dagaz (D)** aparece duas vezes na cifra — ao encontrar o canal 3, os participantes preenchem dois espaços de uma só vez.

### 3. Terminal CRT

Quando a palavra LIDADOR está completa, os participantes vão ao terminal e escrevem o código. O terminal mostra uma sequência de boot e, após autenticação, revela a mensagem do Lidador e as coordenadas GPS da geocache.

---

## Carregar código nos micro:bits

1. Abrir **[python.microbit.org](https://python.microbit.org)** no browser
2. Copiar o conteúdo do ficheiro `.py` pretendido e colar no editor
3. Ligar o micro:bit por USB → clicar **Connect** → clicar **Flash**
4. O micro:bit reinicia e começa a emitir automaticamente

> **Atenção:** carregar o ficheiro certo em cada micro:bit. Etiquetar com fita adesiva após programar (ex: `C3 · D`).

---

## Configurar o terminal para outras atividades

O ficheiro `terminal_crt.html` é reutilizável. Editar o bloco JSON no topo do ficheiro:

```json
{
  "sistema":      "NOME DO SISTEMA",
  "versao":       "v1.0 — 1987",
  "passwords":    ["PALAVRA-CHAVE", "palavra-chave"],
  "resposta": [
    "Linha 1 da resposta após autenticação.",
    "Linha 2...",
    "",
    "COORDENADAS: N xx° xx.xxx  W xxx° xx.xxx"
  ],
  "erro_msgs":    ["ACESSO NEGADO.", "CÓDIGO INVÁLIDO. TENTE NOVAMENTE."],
  "boot_msgs":    ["Mensagem de arranque 1", "Mensagem 2", ""],
  "prompt_label": "CÓDIGO DE ACESSO"
}
```

O terminal funciona completamente **offline** — não precisa de servidor nem de ligação à internet.

---

## Material necessário

- 6× micro:bit V2 com suporte de pilhas (transmissores)
- 2–3× micro:bit V2 com suporte de pilhas (recetores — 1 por grupo)
- Pilhas AAA (novas no dia — autonomia ~5h com `power=0`)
- Caixas ou suportes para esconder os transmissores
- PC com browser para o terminal CRT
- Folhas dos participantes impressas (1 por grupo)
- Canetas/lápis
- Logbook + caneta para a geocache

---

## Créditos e contexto

Atividade desenvolvida para o **Centro de Competências Digitais da Maia** no âmbito de uma noite de atividades STEAM para jovens.

A narrativa centra-se em **Soeiro Mendes da Maia** (? – c. 1120), cavaleiro e senhor do território da Maia durante o período da Reconquista, cujo cognome "O Lidador" ("o que combate") ficou associado à identidade da cidade.

Os símbolos rúnicos são inspirados no alfabeto **Elder Futhark** (séc. II–VIII), adaptados para a matriz 5×5 de LEDs do micro:bit.

---

## Licença

MIT — livre para adaptar e reutilizar com atribuição.
