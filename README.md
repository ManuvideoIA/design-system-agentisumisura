# Sosia — Design System

Design system di Sosia (nome di lavoro, provvisorio). Il servizio crea agenti IA e automazioni su misura per piccole attività. Il nome del repository è ancora quello precedente, `design-system-agentisumisura`.

## Contenuto

- `project/tokens.json`: colori (chiaro e scuro), font, spaziature, raggi, ombre.
- `project/README.md`: regole di marchio e di scrittura.
- `project/01-…08-*.md`: nome e voce, luce, immagini IA, video IA, contenuti social, pagine e slide, template landing, loghi.
- `project/components/*/`: un `README.md` e un `preview.html` per ogni componente.
- `project/components/Lp01…Lp09*/`: nove template wireframe per la landing page, da personalizzare. Vedi `project/07-template-landing-page.md`.
- `project/assets/Logos/`: i loghi (SVG e PNG): versione scelta 5b, la 5a resta in archivio, vedi `project/08-loghi.md`.
- `project/fonts/`: i font in locale (nove file `.ttf`), dichiarati in `tokens.json`.
- `project/design-system.json`: indice del design system.

## Scelte attuali

- Colore principale: petrolio `#497A84`. Accento: salvia `#8CC5AE`.
- Font: Baskervville (titoli grandi), Space Grotesk (altri titoli), Figtree (testo), Space Mono (dati, pesi 400 e 700). I primi tre sono gli stessi di Shegöne. Tutti sono file locali in `project/fonts/`.
- Stile di scrittura: frasi brevi, punto finale, italiano, "tu".
- Offerta in una frase: due versioni, entrambe tenute (vedi `project/01-nome-e-voce.md`).
- Riga sulla sicurezza dei dati: in salvia (`accent-text`), piccola, centrata, sotto la frase, solo su fondo chiaro.
- Logo: creato in Claude Design, versione del logotipo scelta: 5b (la 5a resta in archivio). Concetto: una persona vista da dietro con accanto l'agente. Per scritta, orizzontale e verticale usa i PNG (negli SVG il nome è testo).

## Da verificare

- Disponibilità di dominio, marchio e profili social di Sosia. Nella ricerca web non ho trovato aziende di IA con questo nome, ma su sosia.com c'è un sito attivo che non ho potuto leggere. Alterego è stato scartato (esiste già un'agenzia con servizi di IA).
- La scritta del logo dice ancora «Alterego»: va rifatta con il nome Sosia. Il simbolo resta.
- Licenze dei file dei font: non verificate. Controlla che la licenza permetta l'uso commerciale e la ridistribuzione.
- Mancano gli SVG dei loghi con il testo convertito in tracciati e gli SVG su fondo petrolio.
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
