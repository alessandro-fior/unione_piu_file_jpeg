import argparse
import img2pdf
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert all JPG/JPEG images in a folder into a single PDF."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=".",
        help="Cartella contenente i file JPG/JPEG (default: cartella corrente).",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    cartella = Path(args.folder)

    if not cartella.exists() or not cartella.is_dir():
        raise Exception(f"La cartella specificata non esiste: {cartella}")

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