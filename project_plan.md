# Projektplan – Svenska klubbars ekonomi

Detta dokument beskriver steg och delmål för projektet.

---

## 🎯 Mål
- Samla och lagra ekonomisk data för svenska fotbollsklubbar i Allsvenskan och Superettan.
- Hålla koll på serietillhörighet över tid (uppflyttning/nedflyttning).
- Möjliggöra analys och visualisering av data med Python/SQL.

---

## 🗂️ Projektstruktur
- data/ – lagring av rådata och bearbetad data
- 
otebooks/ – Jupyter Notebooks för analys
- src/ – ETL-kod (Extract, Transform, Load)
- docs/ – dokumentation och planer

---

## ✅ Steg 1: Setup (Nuvarande fas)
- [x] Skapa GitHub-repo med grundstruktur
- [x] Lägga till .gitignore (exkludera env)
- [x] README och projektplan

---

## 🔄 Steg 2: Datainsamling
- [ ] Identifiera årsredovisningar (PDF) för klubbar i Allsvenskan/Superettan
- [ ] Ladda ned och spara i data/raw/
- [ ] Strukturera metadata (år, klubb, serie)

---

## 🧹 Steg 3: Datatransformering
- [ ] Extrahera siffror från PDF (t.ex. omsättning, resultat, eget kapital)
- [ ] Rensa och standardisera tabeller
- [ ] Spara i data/processed/

---

## 💾 Steg 4: Databas
- [ ] Definiera databasstruktur (SQLite eller PostgreSQL)
- [ ] Skapa tabeller för:
  - Klubbar
  - Säsonger
  - Ekonomiska nyckeltal
- [ ] Ladda in data via Python

---

## 📊 Steg 5: Analys och visualisering
- [ ] Skapa Jupyter Notebooks för enklare analyser
- [ ] Visualisera nyckeltal (t.ex. omsättning per klubb/år)
- [ ] Följ serietillhörighet över tid

---

## 🚀 Steg 6: Vidare utveckling
- [ ] Automatisera nedladdning av PDF:er (web scraping om möjligt)
- [ ] AI-baserad tolkning av tabeller i PDF
- [ ] Dashboard för interaktiv analys
