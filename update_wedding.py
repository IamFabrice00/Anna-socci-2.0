import os
import json
from PIL import Image
import shutil
import uuid

OUTPUT_DIR = r"C:\Users\Logon Fabrice\Desktop\ANTIGRAVITY\Anna Socci"
DATA_DIR = os.path.join(OUTPUT_DIR, "data")
PORTFOLIO_JSON_PATH = os.path.join(DATA_DIR, "portfolio.json")

WEDDING_IMG_DIR = os.path.join(OUTPUT_DIR, "assets", "img", "wedding")
ORIGINALS_DIR = os.path.join(OUTPUT_DIR, "photos", "originals")
THUMBS_DIR = os.path.join(OUTPUT_DIR, "photos", "thumbs")

def update_wedding():
    print("Starting wedding photos update...")
    
    with open(PORTFOLIO_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Rimuovi le vecchie foto Wedding
    initial_count = len(data.get("photos", []))
    data["photos"] = [p for p in data.get("photos", []) if p.get("category") != "Wedding"]
    print(f"Removed {initial_count - len(data['photos'])} old wedding photos.")

    # Processa le nuove
    added_count = 0
    for filename in os.listdir(WEDDING_IMG_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            src_path = os.path.join(WEDDING_IMG_DIR, filename)
            
            # Genera nome sicuro
            safe_filename = f"wedding_{uuid.uuid4().hex[:8]}.jpg"
            orig_dest = os.path.join(ORIGINALS_DIR, safe_filename)
            thumb_dest = os.path.join(THUMBS_DIR, safe_filename)
            
            # Copia originale
            shutil.copy2(src_path, orig_dest)
            
            # Crea miniatura
            try:
                with Image.open(src_path) as img:
                    # Fix EXIF orientation before resizing
                    from PIL import ImageOps
                    img = ImageOps.exif_transpose(img)
                    
                    img.thumbnail((600, 800))
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    img.save(thumb_dest, format="JPEG", quality=85)
            except Exception as e:
                print(f"Error generating thumbnail for {filename}: {e}")
                continue
                
            # Aggiungi a JSON
            data["photos"].append({
                "id": f"photo_{uuid.uuid4().hex[:6]}",
                "filename": safe_filename,
                "category": "Wedding",
                "confidence": 100,
                "secondary_category": "",
                "tags": ["wedding"],
                "needs_review": False,
                "notes": "Added from custom wedding folder"
            })
            added_count += 1

    with open(PORTFOLIO_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Added {added_count} new wedding photos.")
    print("portfolio.json updated successfully!")

if __name__ == "__main__":
    update_wedding()
