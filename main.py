from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import uuid
import uvicorn

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



UPLOAD_DIR = "videos_aprobados"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)



@app.get("/")
async def root():
    return {"mensaje": "Servidor VideitosApp en la Nube (Render) funcionando"}

@app.post("/subir-video/")
async def subir_video(file: UploadFile = File(...)):
    import os
    
    if not os.path.exists("videos_recibidos"):
        os.makedirs("videos_recibidos")
    
    file_path = f"videos_recibidos/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    return {"video_id": file.filename, "mensaje": "Guardado con éxito"}
async def upload_video(file: UploadFile = File(...)):
    try:
    
        nombre_original = file.filename
        extension = nombre_original.split(".")[-1] if "." in nombre_original else "mp4"
        
        
        nombre_unico = f"{uuid.uuid4()}.{extension}"
        ruta_final = os.path.join(UPLOAD_DIR, nombre_unico)

        
        with open(ruta_final, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        print(f"✅ Video guardado en la nube: {nombre_unico}")

        return {
            "mensaje": "Aprobado",
            "video_id": nombre_unico,
            "url": f"/ver/{nombre_unico}"
        }
    except Exception as e:
        print(f"❌ Error en Render: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/ver/{video_id}")
async def get_video(video_id: str):
    ruta_video = os.path.join(UPLOAD_DIR, video_id)
    if not os.path.exists(ruta_video):
        raise HTTPException(status_code=404, detail="Video no encontrado")
    return FileResponse(ruta_video)

@app.get("/feed")
async def get_feed():
    archivos = os.listdir(UPLOAD_DIR)
    return {"videos": archivos}
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(app, host="0.0.0.0", port=port)
    @app.get("/videos") 
async def listar_videos():
import os
    if not os.path.exists("videos_recibidos"):
        os.makedirs("videos_recibidos")
    videos = os.listdir("videos_recibidos")
    links = [f"https://videitos-backend.onrender.com/descargar/{v}" for v in videos]
    return {"videos": links}

@app.post("/subir-video")
async def subir_video(file: UploadFile = File(...)):
    import os
    if not os.path.exists("videos_recibidos"):
        os.makedirs("videos_recibidos")
    file_path = f"videos_recibidos/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    return {"video_id": file.filename, "mensaje": "Éxito"}

    
    videos = os.listdir("videos_recibidos")

    links = [f"https://videitos-backend.onrender.com/descargar/{v}" for v in videos]
    return {"videos": links}
    
    videos = os.listdir("videos_recibidos")
    
    links = [f"https://videitos-backend.onrender.com/descargar/{v}" for v in videos]
    return {"videos": links}

@app.get("/descargar/{nombre_video}")
async def descargar_video(nombre_video: str):
    from fastapi.responses import FileResponse
    path = f"videos_recibidos/{nombre_video}"
    return FileResponse(path)





