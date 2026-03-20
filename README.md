# VDROP — Universal Video Downloader

A FastAPI web app wrapping `yt-dlp` to download videos from YouTube, Twitter/X, Instagram, TikTok, Vimeo, and 1000+ more sites.

## Local Development

```bash
pip install -r requirements.txt
uvicorn main:app --reload
# Open http://localhost:8000
```

## Deploy to Render (Recommended — Free Tier)

1. Push this folder to a GitHub repo
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Render auto-detects `render.yaml` — click **Deploy**
5. Your app will be live at `https://your-app.onrender.com`

## Deploy to Railway

1. Push to GitHub
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Railway detects the `Procfile` and deploys automatically

## Deploy to Fly.io (Docker)

```bash
fly launch
fly deploy
```

## Project Structure

```
.
├── main.py            # FastAPI app
├── templates/
│   └── index.html     # Frontend UI
├── requirements.txt
├── render.yaml        # Render config
├── Procfile           # Railway/Heroku
├── Dockerfile         # Docker / Fly.io
└── downloads/         # Downloaded files (auto-created, gitignored)
```

## Notes

- Downloaded files are stored temporarily in `downloads/`
- On Render free tier, the disk resets on each deploy — files are ephemeral
- For production, consider linking cloud storage (S3, R2) for persistence
