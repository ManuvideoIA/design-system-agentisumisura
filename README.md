# Alterego — Design System

Design system di Alterego (nome di lavoro, provvisorio). Il servizio crea agenti IA e automazioni su misura per piccole attività. Il nome del repository è ancora quello precedente, `design-system-agentisumisura`.

## Contenuto

- `project/tokens.json`: colori (chiaro e scuro), font, spaziature, raggi, ombre.
- `project/README.md`: regole di marchio e di scrittura.
- `project/01-…06-*.md`: nome e voce, luce, immagini IA, video IA, contenuti social, pagine e slide.
- `project/components/*/`: un `README.md` e un `preview.html` per ogni componente.
- `project/components/Lp01…Lp09*/`: nove template wireframe per la landing page, da personalizzare. Vedi `project/07-template-landing-page.md`.
- `project/design-system.json`: indice del design system.

## Scelte attuali

- Colore principale: petrolio `#497A84`. Accento: salvia `#8CC5AE`.
- Font: Baskervville (titoli grandi), Space Grotesk (altri titoli), Figtree (testo), monospazio di sistema (dati). Sono gli stessi di Shegöne.
- Stile di scrittura: frasi brevi, punto finale, italiano, "tu".
- Offerta in una frase: due versioni, entrambe tenute (vedi `project/01-nome-e-voce.md`).
- Riga sulla sicurezza dei dati: in salvia (`accent-text`), piccola, centrata, sotto la frase, solo su fondo chiaro.
- Logo: non c'è ancora. Il concetto è una persona vista da dietro che appoggia la mano sulla testa a monitor di un bambino, per rappresentare l'agente IA.

## Da verificare

- Disponibilità di dominio, marchio e profili social del nome. Esiste già un'azienda IA con lo stesso nome (interfaccia neurale, San Francisco).
- Disponibilità dei font su Google Fonts con questi nomi.
- Anteprime mai visualizzate in un browser.
- Contrasti calcolati a mano.

## Pagina web (GitHub Pages)

La cartella `docs/` contiene la pagina che mostra il design system: colori, nomi dei font con prove di testo, spaziature, componenti con anteprima e sezioni di testo. Si genera da `project/`.

- Per rigenerarla: `python3 tools/build.py`
- Per attivarla: Settings → Pages → ramo `main`, cartella `/docs`. Serve un repository pubblico.

## Come aggiornare

1. Modifica i file in `project/`.
2. Mantieni `design-system.json` coerente (campo `lastChange`).
3. Rigenera la pagina con `python3 tools/build.py`.
4. Ripubblica la cartella `project/` sul design system su Claude.
5. Fai commit con un messaggio che dice cosa cambia.
