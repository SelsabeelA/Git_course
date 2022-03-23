import tkinter as tk
HEIGHT = 700
WIDTH = 800
root = tk.Tk()

from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter


def pdf_merge(entry,entry2, entry3):
    pdf_input1 = entry.get() + ".pdf"
    pdf_input2 = entry2.get() + ".pdf"
    merger = PdfFileMerger()
    pdfs = [pdf_input1, pdf_input2]
    name = entry3.get() + ".pdf"
    [merger.append(pdf) for pdf in pdfs]
    with open(name, "wb") as new_file:
        merger.write(new_file)


def extract(entry , entry2):
    name = entry.get() + ".pdf"
    with open(name, 'rb') as infile:
        reader = PdfFileReader(infile)
        writer = PdfFileWriter()
        writer.addPage(reader.getPage(int(entry2.get())-1))
        name = str(entry.get()) + "-" + str(entry2.get()) + ".pdf"
        with open(name, 'wb') as outfile:
            writer.write(outfile)


def split(entry):
    with open(entry.get() + ".pdf", 'rb') as infile:
        reader = PdfFileReader(infile)
        writer = PdfFileWriter()
        pdfnums = reader.numPages
        for num in range(1,pdfnums):
            name = entry.get() + "[" + str(num) + "]" + ".pdf"
            writer.addPage(reader.getPage(num))
            with open(name, 'wb') as outfile:
                writer.write(outfile)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


frame = tk.Frame(root, bg='#F3F2E1')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


label = tk.Label(frame, text="Please enter into the gray-colored entries, then click on the button you want.", bg='#C49494', fg='white', font='overstrike')
label.place(relx=0.1, rely=0.03, relheight=0.1,relwidth=0.8)

label1 = tk.Label(frame, text="If you'd like to merge, please enter the two file names in entry (1,2), then the new merged pdf name in entry(3).", bg='#72B6B6', fg='white')
label1.place(relx=0.05, rely=0.2, relheight=0.05,relwidth=0.9)

label2 = tk.Label(frame, text="If you'd like to extract a pdf, please enter the pdf's name in entry(1), page number in entry(2).", bg='#72B6B6', fg='white')
label2.place(relx=0.1, rely=0.3, relheight=0.05,relwidth=0.8)

label3 = tk.Label(frame, text="If you'd like to split a pdf, please enter the file name in the first entry.", bg='#72B6B6', fg='white')
label3.place(relx=0.2, rely=0.4, relheight=0.05,relwidth=0.6)


entry = tk.Entry(frame, bg='#DFDFDF')
entry.place(relx=0.1,rely=0.5, relwidth=0.8,relheight=0.05)

entry2 = tk.Entry(frame, bg='#DFDFDF')
entry2.place(relx=0.1, rely=0.6,relwidth=0.8,relheight=0.05)

entry3 = tk.Entry(frame, bg='#DFDFDF')
entry3.place(relx=0.1, rely=0.7,relwidth=0.8,relheight=0.05)

#merge button
button1 = tk.Button(frame, text="Merge", bg='#F4D084', fg='white', command=lambda: pdf_merge(entry,entry2,entry3))
#this passes in the button into root or frame, which acts as a container for everything
button1.place(relx=0.1, rely=0.8, relwidth=0.2, relheight = 0.1 )

#extract button
button2 = tk.Button(frame, text="Extract", bg='#F69292', fg='white', command=lambda: extract(entry, entry2))
button2.place(relx=0.4, rely=0.8, relwidth=0.2, relheight = 0.1)

#split button
button3 = tk.Button(frame, text="Split", bg='#F6F092', fg='white' , command=lambda: split(entry))
button3.place(relx=0.7, rely=0.8, relwidth=0.2, relheight = 0.1)


root.mainloop()