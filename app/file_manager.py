import os
import re
import json
from urllib.parse import urlparse
from config import FILE_OUTPUT_DIR # Treat this as your base data directory

def save_data_to_file(url, text_data, topic_name="general", base_dir=FILE_OUTPUT_DIR):
     # 1. Sanitize topic_name
    safe_topic = re.sub(r'[^a-zA-Z0-9]', '_', topic_name.lower().strip())
    safe_topic = re.sub(r'_+', '_', safe_topic).strip('_')
    if not safe_topic:
        safe_topic = "general"

    # 2. Define the new folder paths (cleaned and metadata)
    cleaned_dir = os.path.join(base_dir, 'cleaned', safe_topic)
    metadata_dir = os.path.join(base_dir, 'metadata')

    os.makedirs(cleaned_dir, exist_ok=True)
    os.makedirs(metadata_dir, exist_ok=True)

    # 3. Create a safe filename for the .txt file
    parsed_url = urlparse(url)
    raw_name = f"{parsed_url.netloc}_{parsed_url.path}"
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', raw_name)
    safe_name = re.sub(r'_+', '_', safe_name).strip('_')
    txt_filename = f"{safe_name}.txt"
    txt_filepath = os.path.join(cleaned_dir, txt_filename)

    # 4. Save the pure text data to the .txt file
    try:
        with open(txt_filepath, 'w', encoding='utf-8') as f:
            f.write(text_data)
        print(f"📄 Saved text to: {txt_filepath}")
    except Exception as e:
        print(f"❌ Error saving text file {txt_filename}: {e}")
        return None

    # 5. Define the metadata JSON file path (e.g., metadata/cataract_metadata.json)
    metadata_filepath = os.path.join(metadata_dir, f"{safe_topic}_metadata.json")
    
    # Simple extraction for 'source' (e.g., converting www.aao.org to AAO)
    domain = parsed_url.netloc.replace('www.', '').split('.')[0].upper()

    # Create the metadata payload per the image structure
    new_metadata = {
        "file": txt_filename,
        "source": domain,
        "url": url,
        "topic": safe_topic
    }

    # 6. Load existing metadata array if it exists
    records = []
    if os.path.exists(metadata_filepath):
        try:
            with open(metadata_filepath, 'r', encoding='utf-8') as f:
                records = json.load(f)
        except Exception as e:
            print(f"⚠️ Warning: Could not read {metadata_filepath}, starting fresh: {e}")

    # 7. Update existing record if the file was scraped before, otherwise append
    records = [r for r in records if r.get("file") != txt_filename]
    records.append(new_metadata)

    # 8. Save updated array back to JSON
    try:
        with open(metadata_filepath, 'w', encoding='utf-8') as f:
            json.dump(records, f, indent=4, ensure_ascii=False)
        print(f"🔗 Updated metadata in: {metadata_filepath}")
    except Exception as e:
        print(f"❌ Error saving metadata to {metadata_filepath}: {e}")
        return None

    return txt_filepath