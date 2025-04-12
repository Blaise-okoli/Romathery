import os
import uuid
from supabase import create_client

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_API_KEY")
bucket = os.environ.get("SUPABASE_BUCKET")


supabase = create_client(supabase_url, supabase_key)


def upload_image_to_supabase(file_obj, filename):
    # Generate a unique filename using UUID and original extension
    ext = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4()}.{ext}"
    path = unique_filename

    # Read file contents as bytes
    file_obj.seek(0)  # ensure we read from the beginning
    file_bytes = file_obj.read()

    result = supabase.storage.from_(bucket).upload(
        path, 
        file_bytes, 
        {"content-type": "image/jpeg"}
    )

    if result.error:
        print("Upload error:", result.error)
        return None
    
    return f"{supabase_url}/storage/v1/object/public/{bucket}/{path}"
