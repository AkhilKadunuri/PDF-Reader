import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Select PDF file
book = askopenfilename()

# Open the PDF file
with open(book, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    total_pages = len(reader.pages)

    print(f"Total pages in PDF: {total_pages}")
    
    # Ask user how many pages to read
    num_to_read = int(input(f"How many pages do you want to read (1 to {total_pages}): "))
    num_to_read = min(num_to_read, total_pages)  # ensure it doesn't go out of range

    # Initialize text-to-speech engine
    speak = pyttsx3.init()

    for num in range(num_to_read):
        page = reader.pages[num]
        text = page.extract_text()

        if text:
            speak.say(text)
            speak.runAndWait()
print("Reading complete")