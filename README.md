# Video Downloader

A FastAPI web app wrapping `yt-dlp` to download videos from YouTube, Twitter/X, Instagram, TikTok, Vimeo, and 1000+ more sites.

## Deploy to Render

1. Push this folder to a GitHub repo
2. Go to [render.com](https://render.com) → **New → Web Service**
3. Connect your GitHub repo
4. Render auto-detects `render.yaml` → click **Deploy**
5. Your app will be live at `https://your-app.onrender.com`

> **Note:** The free plan on Render spins down after inactivity — first request after sleep may take ~30s.

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
# Open http://localhost:8000
```

## Project Structure

```
.
├── main.py              # FastAPI app (download + file-serve endpoints)
├── templates/
│   └── index.html       # Frontend UI
├── requirements.txt     # Python dependencies
├── render.yaml          # Render deployment config
└── downloads/           # Downloaded files (auto-created, gitignored)
```

## Notes

- `yt-dlp` is unpinned in requirements so it always installs the latest version (important — older versions break frequently as sites update)
- Downloaded files live in `downloads/` which is mounted as a 1GB persistent disk on Render
- Files are served directly from the FastAPI `/file/{filename}` endpoint
