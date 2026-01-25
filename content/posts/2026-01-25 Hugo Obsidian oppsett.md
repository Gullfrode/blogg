# Oppsett for Automatisert Publisering av Blogg fra Obsidian til GitHub Pages

Dette dokumentet beskriver hvordan bloggen på [blogg.grimsen.com](https://blogg.grimsen.com) blir automatisk oppdatert fra et Obsidian-vault ved hjelp av et-par skript.

## Forutsetninger

For at denne prosessen skal fungere, må følgende verktøy være installert på maskinen:

*   `git`: For versjonskontroll og publisering til GitHub.
*   `rsync`: For å synkronisere filer fra Obsidian-vaultet til Hugo-nettstedets innholdsmappe.
*   `python3`: For å kjøre et egendefinert skript som håndterer bilder.
*   `hugo`: For å bygge det statiske nettstedet.

## Katalogstruktur

Prosessen involverer flere nøkkelkataloger:

*   **Obsidian Vault:** `/Users/frodesolem/Library/Mobile Documents/iCloud~md~obsidian/Documents/Mi Casa`
    *   **Innlegg:** `Posts` - Her ligger alle blogginnleggene som markdown-filer.
    *   **Vedlegg:** `Filer` - Her ligger alle vedlegg, som bilder, som brukes i innleggene.
*   **Hugo Repo:** `/Users/frodesolem/Library/Mobile Documents/com~apple~CloudDocs/Privat/Blogg/blogg`
    *   Dette er et git-repository som inneholder Hugo-nettstedet.

## Skriptene

### `oppdatergrimsen`

Dette er hovedskriptet som orkestrerer hele prosessen. Det utfører følgende steg:

1.  **Navigerer** til Hugo-repositoryet.
2.  **Sikrer** at `main`-grenen er aktiv.
3.  **Synkroniserer** innholdet fra `Posts`-mappen i Obsidian til `content/posts` i Hugo-repoet ved hjelp av `rsync`. `--delete`-flagget sørger for at innlegg som slettes fra Obsidian også fjernes fra bloggen.
4.  **Kjører `images.py`** for å håndtere bilder (mer om dette under).
5.  **Bygger nettstedet** med `hugo`. Resultatet legges i `public`-mappen.
6.  **Oppretter en `CNAME`-fil** i `public`-mappen slik at GitHub Pages bruker det egendefinerte domenet `blogg.grimsen.com`.
7.  **Commiter og pusher** alle endringene i Hugo-repoet (kildekoden for nettstedet) til `main`-grenen på GitHub.
8.  **Splitter ut `public`-mappen** til en midlertidig git-gren (`gh-pages-tmp`) ved hjelp av `git subtree split`.
9.  **Tvinger push** av denne midlertidige grenen til `gh-pages`-grenen på GitHub. Dette er grenen som GitHub Pages bruker for å publisere nettstedet.
10. **Sletter** den midlertidige grenen.

### `images.py`

Dette Python-skriptet blir kalt fra `oppdatergrimsen` og har ansvaret for å fikse bildelinker og kopiere bildefiler.

1.  **Leser alle markdown-filer** i `content/posts`.
2.  **Finner alle Obsidian-style bildelinker**, som ser slik ut: `!![Image](/images/bilde.png)`.
3.  **Konverterer** disse linkene til standard markdown-format: `![Image](/images/bilde.png)`.
4.  **Søker etter bildefilen** i `Filer`-mappen i Obsidian-vaultet.
5.  **Kopierer bildefilen** over til `static/images`-mappen i Hugo-repoet.

Denne prosessen sørger for at bildene som er innebygd i Obsidian-notatene blir korrekt vist på den publiserte bloggen.
