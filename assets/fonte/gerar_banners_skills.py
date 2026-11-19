"""Gera os banners das páginas das skills /pandora:sync (PT e EN).

Uso: python3 gerar_banners_skills.py
Cria assets/fonte/skills/<skill>-<idioma>.html a partir de banner-sync.html.
Para gerar as imagens, capture cada HTML em 1280x440, escala 2x, e salve em
assets/banners/<skill>-<idioma>.webp (ver LEIA-ME.md).
"""
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = open(os.path.join(AQUI, "banner-sync.html"), encoding="utf-8").read()
L = "#C9A6E8"

ART = {
    # anel: a conversa em volta de uma ideia
    "sync-me": f'''<circle cx="1010" cy="215" r="112" fill="none" stroke="{L}" stroke-opacity=".75"/>
<circle cx="1010" cy="215" r="64" fill="rgba(112,36,174,.22)" stroke="{L}" stroke-opacity=".45" stroke-dasharray="2 6"/>
<circle cx="1089" cy="136" r="3" fill="{L}"/><circle cx="931" cy="294" r="3" fill="{L}"/>
<circle cx="1010" cy="215" r="3" fill="#FFFFFF"/>''',
    # páginas: o registro de glossário e decisões
    "sync-docs": f'''<rect x="955" y="95" width="170" height="230" rx="6" fill="rgba(112,36,174,.08)" stroke="{L}" stroke-opacity=".4"/>
<rect x="930" y="110" width="170" height="230" rx="6" fill="rgba(112,36,174,.22)" stroke="{L}" stroke-opacity=".8"/>
<g stroke="{L}" stroke-opacity=".55">
<line x1="972" y1="150" x2="1072" y2="150"/><line x1="972" y1="180" x2="1060" y2="180"/>
<line x1="972" y1="210" x2="1072" y2="210"/><line x1="972" y1="240" x2="1048" y2="240"/>
<line x1="972" y1="270" x2="1066" y2="270"/><line x1="972" y1="300" x2="1040" y2="300"/></g>
<g fill="{L}"><circle cx="956" cy="150" r="2.5"/><circle cx="956" cy="180" r="2.5"/><circle cx="956" cy="210" r="2.5"/>
<circle cx="956" cy="240" r="2.5"/><circle cx="956" cy="270" r="2.5"/></g>
<circle cx="956" cy="300" r="3" fill="#FFFFFF"/>''',
    # cubo em fio com a planta: a estrutura do sistema
    "sync-spec": f'''<g fill="none" stroke="{L}" stroke-linejoin="round">
<polygon points="1010,105 1105,160 1010,215 915,160" fill="rgba(112,36,174,.28)" stroke-opacity=".9"/>
<polygon points="915,160 1010,215 1010,325 915,270" fill="rgba(112,36,174,.16)" stroke-opacity=".7"/>
<polygon points="1010,215 1105,160 1105,270 1010,325" fill="rgba(112,36,174,.08)" stroke-opacity=".7"/></g>
<g stroke="{L}" stroke-opacity=".35" stroke-dasharray="2 5">
<line x1="962" y1="132" x2="1057" y2="187"/><line x1="1057" y1="132" x2="962" y2="187"/>
<line x1="962" y1="187" x2="962" y2="297"/><line x1="1057" y1="187" x2="1057" y2="297"/></g>
<circle cx="1010" cy="160" r="3" fill="#FFFFFF"/>''',
    # arco: as versões do experimento até a evidência
    "sync-mva": f'''<path d="M890 300 A120 120 0 0 1 1130 300" fill="none" stroke="{L}" stroke-opacity=".75"/>
<line x1="870" y1="300" x2="1150" y2="300" stroke="{L}" stroke-opacity=".3"/>
<g fill="{L}"><circle cx="890" cy="300" r="3"/><circle cx="925" cy="215" r="3" opacity=".6"/>
<circle cx="1010" cy="180" r="3" opacity=".8"/><circle cx="1095" cy="215" r="3"/></g>
<circle cx="1130" cy="300" r="3.5" fill="#FFFFFF"/>
<text x="890" y="330" text-anchor="middle" font-family="Inter" font-size="12.5" fill="rgba(255,255,255,.48)">v1</text>
<text x="1130" y="330" text-anchor="middle" font-family="Inter" font-size="12.5" fill="rgba(255,255,255,.48)">evidência</text>''',
    # marcas de +: a grade de dados sintéticos
    "syncdb": "\n".join(
        f'<path d="M{x-6} {y}h12M{x} {y-6}v12" stroke="{L}" stroke-opacity="{op}"/>'
        for i, x in enumerate(range(905, 1120, 34))
        for j, y in enumerate(range(115, 320, 34))
        for op in [(".9" if (i + 2 * j) % 5 == 0 else ".35")]
    ) + '\n<rect x="932" y="166" width="102" height="34" fill="rgba(112,36,174,.28)" stroke="#C9A6E8" stroke-opacity=".6"/>\n<circle cx="1041" cy="217" r="3" fill="#FFFFFF"/>',
}

TXT = {
    "sync-me": {
        "pt": ("Pense a ideia antes de decidir.", "Uma entrevista que começa pela sua visão e pergunta só o que sustenta essa visão. Sem arquivos, só clareza."),
        "en": ("Think the idea through first.", "An interview that starts from your vision and only asks what holds it up. No files, just clarity."),
    },
    "sync-docs": {
        "pt": ("Entenda e registre o projeto.", "Glossário e decisões gravados durante a conversa, prontos para virar spec ou MVA."),
        "en": ("Understand and record the project.", "Glossary and decisions saved during the conversation, ready to become a spec or an MVA."),
    },
    "sync-spec": {
        "pt": ("A spec para a IA de código.", "Propósito, acesso, segurança, telas, arquitetura e plano de etapas, para construir com segurança."),
        "en": ("The spec for a coding AI.", "Purpose, access, security, screens, architecture and a step plan, to build safely."),
    },
    "sync-mva": {
        "pt": ("Teste o valor antes de construir.", "Prompt com autoteste, documentos de referência e manual para montar o agente no Cowork."),
        "en": ("Test the value before you build.", "A prompt with self-test, reference documents and a manual to set up the agent in Cowork."),
    },
    "syncdb": {
        "pt": ("Dados de teste sem expor ninguém.", "Bases sintéticas em CSV ou Markdown, com a mesma estrutura dos dados reais."),
        "en": ("Test data without exposing anyone.", "Synthetic datasets in CSV or Markdown, with the same structure as the real data."),
    },
}

SELO = {"pt": "/pandora:sync · Pandora Box", "en": "/pandora:sync · Pandora Box"}

os.makedirs(os.path.join(AQUI, "skills"), exist_ok=True)
for skill, arte in ART.items():
    for lang in ("pt", "en"):
        titulo, texto = TXT[skill][lang]
        s = BASE
        s = re.sub(r'<span class="seal"><i></i>.*?</span>', f'<span class="seal"><i></i>{SELO[lang]}</span>', s)
        s = re.sub(r"<h1>.*?</h1>", f'<h1><span class="cmd">/pandora:{skill}</span><br><em>{titulo}</em></h1>', s, flags=re.S)
        s = re.sub(r"<p>.*?</p>", f"<p>{texto}</p>", s, flags=re.S)
        s = re.sub(r'(<svg class="art"[^>]*>).*?(</svg>)', lambda m: m.group(1) + "\n" + arte + "\n" + m.group(2), s, flags=re.S)
        s = s.replace("<span>pandora-box/skills/sync</span>", f"<span>pandora-box/skills/sync/{skill}</span>")
        open(os.path.join(AQUI, "skills", f"{skill}-{lang}.html"), "w", encoding="utf-8").write(s)
print("ok")
