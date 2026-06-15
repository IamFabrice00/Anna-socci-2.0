import os
import json
import hashlib

OUTPUT_DIR = r"C:\Users\Logon Fabrice\Desktop\ANTIGRAVITY\Anna Socci"
DATA_DIR = os.path.join(OUTPUT_DIR, "data")
PORTFOLIO_JSON_PATH = os.path.join(DATA_DIR, "portfolio.json")

ORIGINALS_DIR = os.path.join(OUTPUT_DIR, "photos", "originals")
THUMBS_DIR = os.path.join(OUTPUT_DIR, "photos", "thumbs")

def get_hash(filepath):
    h = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        print(f"Error hashing {filepath}: {e}")
        return None

def main():
    print("Starting deduplication process...")
    with open(PORTFOLIO_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    seen_hashes = set()
    new_photos = []
    deleted_count = 0
    first_deleted = False

    for i, p in enumerate(data.get("photos", [])):
        filename = p.get("filename", "")
        category = p.get("category", "")
        
        orig_path = os.path.join(ORIGINALS_DIR, filename)
        
        should_delete = False
        reason = ""
        
        # 1. Delete the first photo
        if not first_deleted:
            should_delete = True
            first_deleted = True
            reason = "First uploaded photo"
            
        # 2. Check for duplicates (exclude Wedding)
        elif category != "Wedding":
            file_hash = get_hash(orig_path)
            if file_hash:
                if file_hash in seen_hashes:
                    should_delete = True
                    reason = "Duplicate content"
                else:
                    seen_hashes.add(file_hash)
                    
        if should_delete:
            print(f"Deleting {filename} - Reason: {reason}")
            if os.path.exists(orig_path):
                os.remove(orig_path)
            thumb_path = os.path.join(THUMBS_DIR, filename)
            if os.path.exists(thumb_path):
                os.remove(thumb_path)
            deleted_count += 1
        else:
            new_photos.append(p)

    data["photos"] = new_photos

    with open(PORTFOLIO_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Total photos deleted: {deleted_count}")

if __name__ == "__main__":
    main()
