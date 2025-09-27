---
title: 2025-09-26
draft: "false"
date: 2025-09-27
tags:
  - innlegg
---
###### Innstaller Hugo
brew install hugo
###### Sync
rsync -av --delete fra til

###### Lag side på github, og legg inn nøkkel fra maskina
generer ssh-key
cd ~/.ssh
 ssh-keygen -t rsa -b 4096 -C "gullfrode@gmail.com"
cat id_rsa.pub
Lim inn innholdet i github

<details>
  <summary>📁 Lag Script</summary>
```
mkdir -p ~/bin
nano ~/bin/oppdatergrimsen
```

```
export PATH="$HOME/bin:$PATH"
```

```
source ~/.bash_profile
```

```
#!/usr/bin/env bash

set -euo pipefail

  

### === KONFIG ===

REPO_DIR="/Users/grimsen/Library/Mobile Documents/com~apple~CloudDocs/Privat/Blog/blog"

  

# Obsidian-vault

VAULT_DIR="/Users/grimsen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Mi Casa"

POSTS_DIR="$VAULT_DIR/Posts"

ATTACH_DIR="$VAULT_DIR/_filer"

  

REMOTE_URL="git@github.com:Gullfrode/blogg.git"

DEPLOY_BRANCH="gh-pages"

TMP_BRANCH="gh-pages-tmp"

  

### === SJEKKER ===

for cmd in git rsync python3 hugo; do

command -v "$cmd" >/dev/null 2>&1 || { echo "Mangler $cmd i PATH"; exit 1; }

done

  

[ -d "$REPO_DIR" ] || { echo "Finner ikke REPO_DIR: $REPO_DIR"; exit 1; }

[ -d "$POSTS_DIR" ] || { echo "Finner ikke POSTS_DIR: $POSTS_DIR"; exit 1; }

[ -d "$ATTACH_DIR" ] || { echo "Finner ikke ATTACH_DIR: $ATTACH_DIR"; exit 1; }

  

### === KJØR I REPO ===

cd "$REPO_DIR"

  

# Git + riktig origin

[ -d .git ] || git init

if git remote | grep -q '^origin$'; then

git remote set-url origin "$REMOTE_URL"

else

git remote add origin "$REMOTE_URL"

fi

  

# Sørg for main

if git rev-parse --verify main >/dev/null 2>&1; then

git checkout main

else

git checkout -b main

fi

  

### === SYNC OBSIDIAN → HUGO ===

CONTENT_DIR="$REPO_DIR/content/posts"

STATIC_IMAGES_DIR="$REPO_DIR/static/images"

mkdir -p "$CONTENT_DIR" "$STATIC_IMAGES_DIR"

  

echo "Rsync fra Obsidian/Posts → Hugo/content ..."

rsync -av --delete "$POSTS_DIR/" "$CONTENT_DIR/"

  

### === BILDER/LENKER ===

[ -f "$REPO_DIR/images.py" ] || { echo "images.py mangler i $REPO_DIR"; exit 1; }

python3 "$REPO_DIR/images.py" \

--posts "$CONTENT_DIR" \

--attachments "$ATTACH_DIR" \

--static-images "$STATIC_IMAGES_DIR"

  

### === HUGO BYGG ===

echo "Bygger Hugo ..."

hugo

[ -d public ] || { echo "public/ mangler (build feilet)"; exit 1; }

  

### === legg til CNAME ===

  

echo "blogg.grimsen.com" > public/CNAME

  

### === COMMIT & PUSH main ===

if ! git diff --quiet || ! git diff --cached --quiet; then git add .; fi

if ! git diff --cached --quiet; then

git commit -m "Auto: oppdateringer $(date +'%Y-%m-%d %H:%M:%S')"

fi

  

if git rev-parse --abbrev-ref --symbolic-full-name @{u} >/dev/null 2>&1; then

git push

else

git branch -M main

git push -u origin main

fi

  

### === DEPLOY TIL gh-pages ===

echo "Deploy til $DEPLOY_BRANCH ..."

git branch -D "$TMP_BRANCH" >/dev/null 2>&1 || true

git subtree split --prefix public -b "$TMP_BRANCH"

git push origin "$TMP_BRANCH":"$DEPLOY_BRANCH" --force

git branch -D "$TMP_BRANCH"

  

echo "Ferdig ✔"
´´´
