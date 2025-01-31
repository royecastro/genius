# Genius Data Pipeline

## 📌 Project Overview
This project extracts song lyrics, song details, artist information, and album details from the **Genius API** and stores the data in **Google Cloud Storage (GCS)**. The final goal is to process the data and load it into **BigQuery** for further analysis.

## 🏗️ Project Structure
📂 genius-data-pipeline/  
│── 📄 README.md        # Project documentation (this file)  
│── 📄 .gitignore       # Ignore unnecessary files (e.g., venv, credentials)  
│── 📄 requirements.txt  # Required dependencies  
│── 📄 config.py        # Stores API credentials (DO NOT UPLOAD TO GITHUB)  
│── 📄 genius_fetch.py  # Fetches data from Genius API  
│── 📄 genius_store.py  # Uploads raw data to Google Cloud Storage  
│── 📄 genius_transform.py  # Cleans and processes data  
│── 📄 genius_load.py  # Loads data into BigQuery  
│── 📂 data/            # Local storage for testing (optional)  


## 🔧 Setup Instructions

### 1️⃣ Prerequisites
- Python 3.x installed
- Genius API access token ([Get it here](https://genius.com/api-clients))
- Google Cloud SDK configured for authentication

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/genius-data-pipeline.git
cd genius-data-pipeline

pip install -r requirements.txt

GENIUS_ACCESS_TOKEN = "your_genius_access_token"

python genius_store.py
