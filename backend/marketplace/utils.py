import os
from supabase import create_client

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_API_KEY")
bucket = os.environ.get("SUPABASE_BUCKET")


supabase = create_client(supabase_url, supabase_key)


def upload_image_to_supabase(file_obj, filename):
    path = f"{filename}"
    result = supabase.storage().from_(bucket).upload(path, file_obj, {"content-type": "image/jpeg"})
    if result.get('error'):
        print("Upload error:", result['error'])
        return None
    return f"{supabase_url}/storage/v1/object/public/{bucket}/{filename}"