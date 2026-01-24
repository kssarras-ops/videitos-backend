import cloudinary
import cloudinary.uploader
from fastapi import FastAPI, File, UploadF

cloudinary.config( 
  cloud_name = "TU_CLOUD_NAME", 
  api_key = "TU_API_KEY", 
  api_secret = "TU_API_SECRET" 
)

@app.post("/subir-video")
async def subir_video(file: UploadFile = File(...)):
    # Subida directa a Cloudinary
    upload_result = cloudinary.uploader.upload(
        file.file, 
        resource_type = "video",
        folder = "videitos_tiktok"
    )
    
    video_url = upload_result['secure_url']
    
    return {"mensaje": "exito", "url": video_url}
   




