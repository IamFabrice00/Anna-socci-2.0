import os
import json

TARGETS = ["foto_346", "foto_243", "foto_244", "foto_245", "foto_246", "foto_247", "foto_248", "foto_249", "foto_250", "foto_251", "foto_252", "foto_253", "foto_255", "foto_257", "foto_258", "foto_259", "foto_260", "foto_261", "foto_262", "foto_263", "foto_264", "foto_265", "foto_266", "foto_267", "foto_268", "foto_269", "foto_270", "foto_271", "foto_272", "foto_273", "foto_274", "foto_275", "foto_276", "foto_277", "foto_278", "foto_279", "foto_280", "foto_281", "foto_282", "foto_283", "foto_284", "foto_285", "foto_286", "foto_287", "foto_288", "foto_289", "foto_290", "foto_291", "foto_292", "foto_293", "foto_294", "foto_295", "foto_296", "foto_297", "foto_298", "foto_299", "foto_300", "foto_301", "foto_302", "foto_303", "foto_304", "foto_305", "foto_306", "foto_307", "foto_308", "foto_309", "foto_310", "foto_311", "foto_312", "foto_313", "foto_314", "foto_315", "foto_316", "foto_317", "foto_318", "foto_319", "foto_320", "foto_322", "foto_323", "foto_324", "foto_325", "foto_326", "foto_327", "foto_328", "foto_329", "foto_330", "foto_331", "foto_332", "foto_333", "foto_334", "foto_335", "foto_336", "foto_337", "foto_338", "foto_339", "foto_340", "foto_341", "foto_342", "foto_343", "foto_344", "foto_345"]

OUTPUT_DIR = r"C:\Users\Logon Fabrice\Desktop\ANTIGRAVITY\Anna Socci"
DATA_DIR = os.path.join(OUTPUT_DIR, "data")
PORTFOLIO_JSON_PATH = os.path.join(DATA_DIR, "portfolio.json")

ORIGINALS_DIR = os.path.join(OUTPUT_DIR, "photos", "originals")
THUMBS_DIR = os.path.join(OUTPUT_DIR, "photos", "thumbs")

with open(PORTFOLIO_JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

new_photos = []
deleted_count = 0

for p in data.get("photos", []):
    filename = p.get("filename", "")
    
    # check if filename starts with any target
    should_delete = any(filename.startswith(target) for target in TARGETS)
    
    if should_delete:
        # Delete from originals
        orig_path = os.path.join(ORIGINALS_DIR, filename)
        if os.path.exists(orig_path):
            os.remove(orig_path)
            
        # Delete from thumbs
        thumb_path = os.path.join(THUMBS_DIR, filename)
        if os.path.exists(thumb_path):
            os.remove(thumb_path)
            
        deleted_count += 1
    else:
        new_photos.append(p)

data["photos"] = new_photos

with open(PORTFOLIO_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"Deleted {deleted_count} photos.")
