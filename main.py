import PyPDF2

pdf_files=["sample1.pdf", "sample2.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdf_files:
    pdffile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdffile)
    merger.append(pdfReader)

pdffile.close()
merger.write('merged.pdf')    