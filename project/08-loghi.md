# Loghi

Il logo di Sosia ha due parti, create in Claude Design: il **simbolo** (una persona vista da dietro con accanto l'agente) e il **logo-scritta** «Sosia». Nella scritta la «o» diventa la testa dell'agente, con gli occhi salvia. I file sono in `assets/Logos/`, 21 in tutto.

## Logo-scritta

Il nome «Sosia» in Space Grotesk 700, con le lettere già convertite in tracciati. Non serve avere il font installato, e l'SVG si vede giusto anche dentro un `<img>`.

- **sosia-scritta**: per fondo chiaro. «S» e «s» in inchiostro, «o» (testa dell'agente) e «ia» in petrolio.
- **sosia-scritta-fondo-scuro**: per fondo `ink` o foto scure. «S» e «s» in carta, «ia» in petrolio chiaro.
- **sosia-scritta-fondo-petrolio**: per fondo `brand`. «S» e «s» in carta, «ia» in inchiostro.

Ogni versione c'è in SVG e in PNG trasparente, a 1200 e 2400 px di larghezza. Il rapporto tra larghezza e altezza è circa 3,15 a 1.

## Simbolo

Una persona vista da dietro, in inchiostro o in carta, con accanto l'agente in petrolio e occhi salvia.

- **sosia-marchio**: il simbolo, sfondo trasparente. PNG a 512, 1024 e 2048 px, più SVG.
- **sosia-marchio-fondo-scuro**: per fondi scuri. PNG a 512, 1024 e 2048 px, più SVG.
- **sosia-marchio-fondo-petrolio**: per fondo petrolio. Solo PNG, 512 e 1024 px.
- **sosia-icona-carta** e **sosia-icona-inchiostro**: il simbolo su un quadrato pieno, 1024 px. Per avatar social e icone app.

## Quale usare

| Uso | File |
|---|---|
| Intestazioni, slide, post, firma dei video | logo-scritta, versione secondo il fondo |
| Avatar social, icone app, spazi quadrati piccoli | icona-carta o icona-inchiostro |
| Simbolo da solo su un fondo | marchio, versione secondo il fondo |

## Su quale fondo

| Fondo | Logo-scritta | Simbolo |
|---|---|---|
| Chiaro (`surface`, `surface-raised`) | `sosia-scritta` | `sosia-marchio` |
| Inchiostro (`ink`) o foto scure | `sosia-scritta-fondo-scuro` | `sosia-marchio-fondo-scuro` |
| Petrolio (`brand`, `#497A84`) | `sosia-scritta-fondo-petrolio` | `sosia-marchio-fondo-petrolio` (solo PNG) |

## Dove è usato nel design system

Le anteprime Cover, LandingHero, SlideCard, SocialPost e VerticalVideo usano il logo-scritta. La versione cambia con il fondo e con il tema chiaro o scuro.

## Regole

- Non ricolorare, non ridisegnare e non allungare il logo.
- Usa la versione `-fondo-scuro` su inchiostro o su foto scure, e `-fondo-petrolio` su petrolio.
- Altezza minima consigliata del logo-scritta: non verificata. Controlla che «ia» e gli occhi restino leggibili.

## Da fare

- Verificare dominio, marchio e profili social del nome Sosia. Non è ancora stato fatto.
- Verificare i contrasti del logo-scritta su petrolio: «S» e «s» in carta su `#497A84` non sono stati misurati.

Fonte: file SVG e PNG consegnati dall'utente il 12 ottobre 2026 (colori letti nei file). Il simbolo viene dall'esportazione zip di Claude Design.
