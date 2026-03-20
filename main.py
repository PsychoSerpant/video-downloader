import os
import subprocess
import sys
import uuid
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/download")
async def download_video(url: str = Form(...)):
    if not url.strip():
        return JSONResponse({"error": "No URL provided."}, status_code=400)

    job_id = str(uuid.uuid4())[:8]
    output_template = os.path.join(DOWNLOAD_DIR, f"{job_id}_%(title)s.%(ext)s")

    command = [
        sys.executable, "-m", "yt_dlp",
        "-f", "best",
        "-o", output_template,
        "--no-playlist",
        url.strip()
    ]

    try:
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            timeout=120
        )

        # Find the downloaded file
        files = [
            f for f in os.listdir(DOWNLOAD_DIR)
            if f.startswith(job_id)
        ]
        if not files:
            return JSONResponse({"error": "Download completed but file not found."}, status_code=500)

        filename = files[0]
        clean_name = filename[len(job_id) + 1:]  # strip job_id prefix
        return JSONResponse({
            "success": True,
            "filename": filename,
            "display_name": clean_name,
            "download_url": f"/file/{filename}"
        })

    except subprocess.TimeoutExpired:
        return JSONResponse({"error": "Download timed out. Try a shorter video."}, status_code=408)
    except subprocess.CalledProcessError as e:
        return JSONResponse({"error": f"yt-dlp failed: {e.stderr[-300:] if e.stderr else 'Unknown error'}"}, status_code=500)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


@app.get("/file/{filename}")
async def serve_file(filename: str):
    filepath = os.path.join(DOWNLOAD_DIR, filename)
    if not os.path.exists(filepath):
        return JSONResponse({"error": "File not found."}, status_code=404)
    return FileResponse(
        filepath,
        filename=filename[9:],  # strip job_id prefix for clean download name
        media_type="application/octet-stream"
    )
