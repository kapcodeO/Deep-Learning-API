# Deep Learning Translation API

This is a simple Deep Learning-based API that translates text from **English** to **Hindi** using FastAPI.

## 🚀 Features

- Built using FastAPI
- Environment-friendly setup for macOS, Windows, and Linux
- Docker support for easy deployment
- Interactive API documentation at `/docs`

---

## 📁 Project Setup

```bash
# Create project folder and virtual environment
mkdir Deep-Learning-API
cd Deep-Learning-API
python3 -m venv venv

# Activate virtual environment
# macOS / Linux
source venv/bin/activate
# Windows (Command Prompt)
venv\Scripts\activate.bat
# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload
```

---

## 🧪 API Testing

Once the server is running, go to:

```
http://127.0.0.1:8000/docs
```

Use the interactive Swagger UI to test the `/translate` endpoint by sending an English sentence and receiving the Hindi translation.

---

## 🐳 Docker Commands

### Build Docker Image

```bash
docker build -t dl-api .
```

### Run Docker Container

```bash
# macOS / Linux
docker run -d --name dl-api -p 8000:8000 dl-api
```

### Stop Docker Container

```bash
docker stop dl-api
```

### Remove Docker Container

```bash
docker rm dl-api
```

---

## 🧼 Notes

- Ensure `main.py` exists and contains the FastAPI app as `app`
- Ensure `requirements.txt` includes all required dependencies (e.g., `fastapi`, `uvicorn`, `transformers`, etc.)

---

## 🛠 Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Docker (optional for containerization)

---

Happy Translating! 🌐✨