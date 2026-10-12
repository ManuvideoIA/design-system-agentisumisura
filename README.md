# Agenti su Misura — Design System

Design system di Agenti su Misura (nome di lavoro, provvisorio). Il servizio crea agenti IA e automazioni per piccole attività.

## Contenuto

- `project/tokens.json`: colori (chiaro e scuro), font, spaziature, raggi, ombre.
- `project/README.md`: regole di marchio e di scrittura.
- `project/01-…06-*.md`: nome e voce, luce, immagini IA, video IA, contenuti social, pagine e slide.
- `project/components/*/`: un `README.md` e un `preview.html` per ogni componente.
- `project/design-system.json`: indice del design system.

## Scelte attuali

- Colore principale: petrolio `#497A84`. Accento: salvia `#8CC5AE`.
- Font: Baskervville (titoli grandi), Space Grotesk (altri titoli), Figtree (testo), monospazio di sistema (dati). Sono gli stessi di Shegöne.
- Stile di scrittura: frasi brevi, punto finale, italiano, "tu".

## Da verificare

- Disponibilità di dominio, marchio e profili social del nome.
- Disponibilità dei font su Google Fonts con questi nomi.
- Anteprime mai visualizzate in un browser.
- Contrasti calcolati a mano.

## Come aggiornare

1. Modifica i file in `project/`.
2. Mantieni `design-system.json` coerente (campo `lastChange`).
3. Ripubblica la cartella `project/` sul design system su Claude.
4. Fai commit con un messaggio che dice cosa cambia.
