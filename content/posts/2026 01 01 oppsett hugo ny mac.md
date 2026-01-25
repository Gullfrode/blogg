---
title: Oppsett Hugo (ny Mac)
draft: false
date: 2026-01-01T00:00:00
tags:
  - innlegg
---

Dette er **fasit for å sette opp bloggen på ny Mac**  
(Obsidian → Hugo → Congo → GitHub Pages).

TL;DR:
- Kjør `oppdatergrimsen`
- Kjør `hugo server -D`

## Forutsetninger

- Slå av «Optimaliser Mac-lagring» for iCloud Drive
- Vent til Obsidian-vault og Hugo-repo er fullstendig lastet lokalt

## Installer verktøy

### Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

### Hugo (extended!)
```
brew install hugo  
hugo version  
(Må vise `extended`)
```

## GitHub + SSH
```
cd ~/.ssh  
ssh-keygen -t rsa -b 4096 -C "gullfrode@gmail.com"  
cat id_rsa.pub  
```

Lim inn nøkkelen i GitHub → Settings → SSH keys

## oppdatergrimsen-script
```
cd /Users/frodesolem/Library/Mobile\ Documents/com\~apple\~CloudDocs/scripts
nano oppdatergrimsen  
```

Script:
```
export PATH="$HOME/bin:$PATH"  
source ~/.bash_profile  

#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/Users/grimsen/Library/Mobile Documents/com~apple~CloudDocs/Privat/Blog/blog"
VAULT_DIR="/Users/grimsen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Mi Casa"
POSTS_DIR="$VAULT_DIR/Posts"
ATTACH_DIR="$VAULT_DIR/_filer"

REMOTE_URL="git@github.com:Gullfrode/blogg.git"
DEPLOY_BRANCH="gh-pages"
TMP_BRANCH="gh-pages-tmp"

for cmd in git rsync python3 hugo; do
  command -v "$cmd" >/dev/null 2>&1 || exit 1
done

cd "$REPO_DIR"
git checkout main || git checkout -b main

rsync -av --delete "$POSTS_DIR/" content/posts/
python3 images.py --posts content/posts --attachments "$ATTACH_DIR" --static-images static/images
hugo
echo "blogg.grimsen.com" > public/CNAME

git add .
git commit -m "Auto update" || true
git push

git subtree split --prefix public -b "$TMP_BRANCH"
git push origin "$TMP_BRANCH":"$DEPLOY_BRANCH" --force
git branch -D "$TMP_BRANCH"
```
Gjør kjørbar
```
chmod +x /Users/frodesolem/Library/Mobile\ Documents/com\~apple\~CloudDocs/scripts/oppdatergrimsen
```

## Test

oppdatergrimsen  
hugo server -D  
