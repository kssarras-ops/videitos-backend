from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Permisos para que la App de Flutter entre sin problemas
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carpeta donde se guardan los videos
UPLOAD_DIR = "videos_recibidos"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@app.get("/")
async def inicio():
    return {"mensaje": "Servidor funcionando correctamente"}

@app.get("/videos")
async def listar_videos():
    videos = os.listdir(UPLOAD_DIR)
    links = [f"https://videitos-backend.onrender.com/descargar/{v}" for v in videos]
    return {"videos": links}

@app.post("/subir-video")
async def subir_video(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    return {"video_id": file.filename, "mensaje": "Éxito"}

@app.get("/descargar/{nombre_video}")
async def descargar_video(nombre_video: str):
    path = os.path.join(UPLOAD_DIR, nombre_video)
    return FileResponse(path)

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)




