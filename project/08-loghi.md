# Loghi

Il logo è stato creato in Claude Design e importato qui dall'esportazione zip del progetto. Le versioni del logotipo erano due, 5a e 5b. **La versione scelta è la 5b** (fonte: scelta dell'utente del 12 ottobre 2026). I file della 5a restano in `assets/Logos/` come archivio, non si usano. I file sono in `assets/Logos/`.

## Il simbolo

Una persona vista da dietro, in inchiostro o in carta, con accanto l'agente in petrolio e occhi salvia. Nella scritta, «Alter» è in inchiostro e «ego» in petrolio; la «o» diventa la testa dell'agente.

## Varianti

- **marchio**: solo il simbolo, sfondo trasparente. PNG a 512, 1024 e 2048 px, più SVG.
- **icona-carta** e **icona-inchiostro**: il simbolo su un quadrato pieno, 1024 px. Per avatar social e icone app.
- **scritta**: solo il nome.
- **orizzontale**: simbolo a sinistra e scritta. È l'uso principale: intestazioni e firma dei video.
- **verticale**: simbolo sopra e scritta. Per copertine e formati quadrati.
- **5b** (scelta): la A ad arco, attraversata dalla barra salvia, e una linea salvia sotto il nome.
- **5a** (non scelta, archivio): la A classica.

## Su quale fondo

| Fondo | File da usare |
|---|---|
| Chiaro (`surface`, `surface-raised`) | file senza suffisso |
| Inchiostro (`ink`) o foto scure | suffisso `-fondo-scuro` |
| Petrolio (`brand`, `#497A84`) | suffisso `-fondo-petrolio` (solo PNG) |

## Dove è usato nel design system

Nelle anteprime Cover, LandingHero, SlideCard, SocialPost e VerticalVideo il nome scritto è stato sostituito dal logo orizzontale 5b. La versione cambia con il fondo e con il tema chiaro o scuro.

## Regole

- Non ricolorare e non ridisegnare il logo.
- Usa la versione `-fondo-scuro` su inchiostro o su foto scure.
- **Gli SVG di scritta, orizzontale e verticale (5a e 5b) contengono il nome come testo, non convertito in tracciati.** Si vedono giusti solo dove Space Grotesk 700 è installato. Dentro un `<img>` il browser usa un altro font e si apre un buco prima della «o». Per ora usa i **PNG** per queste varianti. Gli SVG del marchio sono solo forme e vanno bene.
- Le versioni `-fondo-petrolio` sono solo PNG. Sono state ricavate dalle versioni `-fondo-scuro`, perché su petrolio «ego» e l'agente sparivano (circa 1,5:1 secondo il progetto Claude Design).

## Da fare

- Chiedere gli SVG con il testo convertito in tracciati, e gli SVG `-fondo-petrolio`.
- **Rifare la scritta con il nome Sosia.** I file attuali dicono «Alterego». Il simbolo (persona e agente) resta. La scritta va rigenerata in Claude Design, finché non è pronta le anteprime mostrano ancora il logo con il nome precedente.
- Verificare dominio, marchio e profili social del nome Sosia. Non è ancora stato fatto.

Fonte: file `README.md` dell'esportazione zip di Claude Design (sezione LOGHI). I contrasti citati sono quelli indicati lì, non ricalcolati.
