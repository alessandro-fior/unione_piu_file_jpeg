import img2pdf
from pathlib import Path

cartella = Path(r"C:\Users\Alessandro Fior\Documents\Scanned Documents\contratto moongy")

files = sorted(list(cartella.glob("*.jpg")) + list(cartella.glob("*.jpeg")))

print("File trovati:")
for f in files:
    print(f.name)

if not files:
    raise Exception("Nessun file JPG/JPEG trovato")

output = cartella / "output.pdf"

with open(output, "wb") as f:
    f.write(img2pdf.convert([str(x) for x in files]))

print(f"\nPDF creato: {output}")