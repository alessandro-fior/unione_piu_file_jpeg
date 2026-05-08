# JPG to PDF Converter

A simple Python utility that merges multiple JPEG images into a single PDF file.

## Description

This project provides a straightforward script to combine all JPG and JPEG images from a folder into a single PDF document. Images are automatically sorted and combined in order.

## Features

- Combines multiple JPEG images into a single PDF
- Automatic file sorting for consistent ordering
- Simple and easy to use
- Handles both `.jpg` and `.jpeg` file extensions

## Requirements

- Python 3.6+
- `img2pdf` library

## Installation

1. Clone or download this repository
2. Install the required dependency:

```bash
pip install img2pdf
```

## Usage

1. **Edit the script** to specify your source folder:
   - Open `unione_jpg_to_pdf.py`
   - Modify the `cartella` variable to point to your folder containing JPEG images:
   
   ```python
   cartella = Path(r"C:\path\to\your\folder")
   ```

2. **Run the script**:
   ```bash
   python unione_jpg_to_pdf.py
   ```

3. **Check the output**:
   - The script will display all found JPEG files
   - A `output.pdf` file will be created in the same folder as your source images

## Example

If your folder structure looks like:
```
my_images/
  ├── image1.jpg
  ├── image2.jpg
  ├── image3.jpeg
  └── image4.jpg
```

Running the script will create:
```
my_images/
  ├── image1.jpg
  ├── image2.jpg
  ├── image3.jpeg
  ├── image4.jpg
  └── output.pdf  ← newly created
```

## Error Handling

If no JPEG files are found in the specified folder, the script will raise an exception with the message: `"Nessun file JPG/JPEG trovato"` (No JPG/JPEG files found).

## Notes

- Images are sorted alphabetically before combining
- The output PDF maintains the quality of the original JPEG images
- All images are combined in sorted order, so naming conventions matter for desired page order

## License

Feel free to use and modify this script for your needs.
