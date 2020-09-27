import pyttsx3
from PyPDF2 import PdfFileWriter, PdfFileReader


def parsePDF(page):
    inputPDF = PdfFileReader(open("sample.pdf", "rb"))
    getPageObj = inputPDF.getPage(int(page))
    pageContent = getPageObj.extractText()
    if pageContent is not None:
        pdfToTTS(str(pageContent))
    else:
        print("Parsing error occured!")

def pdfToTTS(pageContent):
    engine = pyttsx3.init()
    print("TTS engine initialized \n*Enter speech rate*")
    speechRate = int(input())
    engine.setProperty('rate', speechRate)
    print("Speech rate set to %d" %speechRate) 

if __name__ == "__main__":
    print("\Welcome to PyAudiobook\ \n*Enter Page Number to read out*")
    page = int(input())
    parsePDF(page)


