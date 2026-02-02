import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from PIL import Image
import pdfplumber
import pytesseract

# Google Gemini
from google.generativeai import configure, GenerativeModel

# Configure Gemini API
configure(api_key="")
model = GenerativeModel('gemini-1.5-flash')

# Tesseract for Windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def upload_file(request):
    extracted_text = ""
    summary = ""

    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        fs = FileSystemStorage()
        file_path = fs.save(uploaded_file.name, uploaded_file)
        full_path = fs.path(file_path)

        # Extract from PDF
        if uploaded_file.name.lower().endswith(".pdf"):
            with pdfplumber.open(full_path) as pdf:
                for page in pdf.pages:
                    extracted_text += page.extract_text() + "\n"

        # Extract from Image
        else:
            img = Image.open(full_path)
            extracted_text = pytesseract.image_to_string(img)

        os.remove(full_path)  # cleanup uploaded file

        # Send to Gemini for medical analysis
        if extracted_text.strip():
            prompt = f"""
            You are a medical report analysis assistant. 
            Analyze the following extracted text from a patient's medical report 
            and provide a concise summary: possible diseases, infections, or abnormalities.

            Report Text:
            {extracted_text}
            """
            try:
                response = model.generate_content(prompt)
                summary = response.text
            except Exception as e:
                summary = f"Error while contacting Gemini API: {e}"

    return render(request, "upload.html", {
        "extracted_text": extracted_text,
        "summary": summary
    })

