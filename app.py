import pyttsx3
from PyPDF2 import PdfFileWriter, PdfFileReader

# Takes the page number to extract 
# Text from the pdf using PyPDF2
def parsePDF(page):
    inputPDF = PdfFileReader(open("sample.pdf", "rb"))
    getPageObj = inputPDF.getPage(int(page))
    pageContent = getPageObj.extractText()
    if pageContent is not None:
        print("Text parsed successfully!")
        pdfToTTS(str(pageContent))
    else:
        print("Parsing error occured!")


# Extracted text sent to pyttsx3
# and take parameters like voice &
# speech rate as input 
def pdfToTTS(pageContent):
    engine = pyttsx3.init()
    print("TTS engine initialized \n*Enter speech rate*")
    speechRate = int(input())
    engine.setProperty('rate', speechRate)
    print("Speech rate set to %d \nEnter 0 for Female voice or 1 for Male voice" %speechRate)
    voiceChoice = int(input())
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voiceChoice].id)
    engine.say(pageContent)
    print("Save file to mp3 ? [1] to confirm else [0]")
    opt = int(input())
    if opt == 1:
        engine.save_to_file(pageContent , 'sample.mp3')
    engine.runAndWait()
    engine.stop()
     

if __name__ == "__main__":
    print("\Welcome to PyAudiobook\ \n*Enter Page Number to read out*")
    page = int(input())
    parsePDF(page)


