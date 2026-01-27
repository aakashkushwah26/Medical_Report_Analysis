# 🩺 MediScanAI – Medical Report Analysis & X‑Ray Diagnosis Platform

MediScanAI is a **full‑stack AI-powered medical diagnostics web application** that enables automated **medical report analysis** using OCR and **X‑ray disease detection** using deep learning. The platform is designed to assist healthcare professionals and researchers by providing fast, accurate, and visually clear diagnostic insights.

---

## 🚀 Key Features

### 🏠 Home Page

* Modern, responsive UI with a professional medical theme
* Highlights platform features, statistics, and call‑to‑action
* Clean layout with medical icons and smooth navigation

### 📄 Medical Report Analysis

* Upload medical reports in **PDF, PNG, JPG, JPEG** formats
* OCR-based text extraction using **Tesseract OCR**
* AI-driven report interpretation using **Google Gemini**
* Displays categorized and structured medical results
* Clean, readable medical-style formatting

### 🩻 X‑Ray Disease Detection (NEW)

* Integrated **YOLOv8 (Ultralytics)** deep learning model
* Supports **chest X‑ray image uploads**
* Classifies **17 different X‑ray-related diseases**
* Displays:

  * Disease name
  * Confidence percentage
  * Medical-grade visualization output

#### 🦴 Example Diagnoses

* Pneumonia
* Cardiomegaly
* Edema
* Hernia
* Infiltration
* Pleural Effusion
* Fibrosis
* Atelectasis
* Emphysema
* Nodule
* Mass
* Consolidation
* Pneumothorax
* Pleural Thickening
* Calcification
* Effusion
* No Finding

### 👥 About Page

* Project mission and vision
* Team information
* Development timeline and milestones

### 📞 Contact Page

* Validated contact form
* Business hours
* Email and location details

### 🔐 Authentication System

* Secure **Login / Signup**
* Form validation with error alerts
* Social login options (optional integration)

---

## 🛠 Technology Stack

| Component            | Technology             |
| -------------------- | ---------------------- |
| Backend              | Django 3.2             |
| Frontend             | HTML, CSS, JavaScript  |
| OCR Engine           | Tesseract OCR          |
| PDF Processing       | pdfplumber             |
| AI (Report Analysis) | Google Gemini API      |
| X‑Ray Model          | YOLOv8 (Ultralytics)   |
| Styling              | Custom CSS             |
| Icons                | Font Awesome           |
| Fonts                | Google Fonts (Poppins) |

---

## 📌 Installation & Setup

### 🔧 Prerequisites

* Python **3.7+**
* Django **3.2**
* Tesseract OCR installed
* Google Gemini API Key
* YOLOv8 dependencies (**ultralytics**)

---

### 📥 Installation Steps

```bash
git clone https://github.com/your-username/MediScanAI.git
cd MediScanAI
```

```bash
pip install -r requirements.txt
```

### 🧠 Configure Environment Variables

Create a `.env` file and add:

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

### 🩻 Install YOLOv8

```bash
pip install ultralytics
```

### 🔠 Install Tesseract OCR

* **Windows:** Download from [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
* **Linux:**

```bash
sudo apt install tesseract-ocr
```

---

### ▶️ Run the Project

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open browser and visit:

```
http://127.0.0.1:8000/
```

---

## 📂 Project Structure (Simplified)

```
MediScanAI/
│── manage.py
│── requirements.txt
│── .env
│
├── accounts/        # Authentication module
├── reports/         # OCR & report analysis
├── xray/            # YOLOv8 X‑ray classification
├── templates/       # HTML templates
├── static/          # CSS, JS, images
└── media/           # Uploaded reports & X‑rays
```

---

## ⚠️ Disclaimer

MediScanAI is intended **for educational and research purposes only**. It is **not a replacement for professional medical diagnosis**. Always consult certified medical professionals for clinical decisions.

---

## 🤝 Contribution

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit changes
4. Open a Pull Request

---

## 📧 Contact

**Developer:** Aakash Kushwah
📩 Email: [aakashkushwah2603@gmail.com](mailto:aakashkushwah2603@gmail.com)
💼 Domain: AI • Medical Imaging • Deep Learning

---

⭐ If you like this project, don’t forget to **star the repository**!
