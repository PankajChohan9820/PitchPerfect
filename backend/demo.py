import PyPDF2

# Replace 'your_resume.pdf' with the path to your PDF file
pdf_file = r'resumes\Software Engineer.pdf'


# Open the PDF file in read-binary mode
with open(pdf_file, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)

    resume_data = ""

    # Loop through all the pages in the PDF
    for page in pdf_reader.pages:
        resume_data += page.extract_text()

# Now, 'resume_data' contains the text extracted from the PDF
print(resume_data)