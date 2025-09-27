#!/usr/bin/env python3
import os, re, shutil, argparse
from pathlib import Path
from urllib.parse import quote

def main():
    p = argparse.ArgumentParser(description="Oppdater Obsidian-bildelinker for Hugo og kopier bilder.")
    p.add_argument("--posts", required=True, help="Hugo content/-mappe")
    p.add_argument("--attachments", required=True, help="Obsidian _filer/-mappe")
    p.add_argument("--static-images", required=True, help="Hugo static/images/-mappe")
    args = p.parse_args()

    posts_dir = Path(args.posts)
    attachments_dir = Path(args.attachments)
    static_images_dir = Path(args.static_images)
    if not posts_dir.is_dir():       raise SystemExit(f"Posts finnes ikke: {posts_dir}")
    if not attachments_dir.is_dir(): raise SystemExit(f"Attachments finnes ikke: {attachments_dir}")
    static_images_dir.mkdir(parents=True, exist_ok=True)

    # Matche [[fil.png]] og ![[fil.jpg]] (ev. undermapper)
    pat = re.compile(r"!?\[\[([^\]]+\.(?:png|jpg|jpeg))\]\]", re.IGNORECASE)

    for md_path in posts_dir.glob("**/*.md"):
        text = md_path.read_text(encoding="utf-8")
        matches = pat.findall(text)
        if not matches:
            continue

        for rel in matches:
            rel_clean = rel.strip().lstrip("/")
            # primært søk i _filer med samme relative bane
            src = attachments_dir / rel_clean
            if not src.exists():
                # fallback: kun filnavn (flatt)
                src = attachments_dir / Path(rel_clean).name

            # Erstatt til standard markdown-bildesyntaks og legg i /images/
            url_part = quote(Path(rel_clean).name)
            replacement = f"![Image](/images/{url_part})"
            # erstatt både [[x]] og ![[x]]
            text = text.replace(f"[[{rel}]]", replacement).replace(f"![[{rel}]]", replacement)

            if src.exists() and src.is_file():
                dst = static_images_dir / Path(rel_clean).name
                if not dst.exists() or os.path.getmtime(src) > os.path.getmtime(dst):
                    shutil.copy2(src, dst)

        md_path.write_text(text, encoding="utf-8")

    print("Markdown oppdatert og bilder kopiert ✔")

if __name__ == "__main__":
    main()