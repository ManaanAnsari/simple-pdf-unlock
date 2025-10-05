# PDF Unlocker

A simple Python script to remove password protection from PDF files.

## Features

- 🔓 Unlock password-protected PDF files
- 🛡️ Remove password protection completely
- 📊 Show file size comparison
- ⚡ Fast and efficient processing
- 🐍 Pure Python implementation

## Requirements

- Python 3.6 or higher
- pikepdf library

## Installation

1. Install the required dependency:
```bash
pip install pikepdf
```

Or install from requirements.txt:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

```bash
python pdf_unlock.py -i input.pdf -p password -o output.pdf
```

### Arguments

- `-i, --input`: Path to the password-protected input PDF file (required)
- `-p, --password`: Password to unlock the PDF (required)
- `-o, --output`: Path for the output unlocked PDF file (required)

### Examples

```bash
# Basic usage
python pdf_unlock.py -i protected.pdf -p mypassword -o unlocked.pdf

# Using long form arguments
python pdf_unlock.py --input protected.pdf --password mypassword --output unlocked.pdf

# With full paths
python pdf_unlock.py --input "/path/to/protected.pdf" --password "secret123" --output "/path/to/unlocked.pdf"
```

## How It Works

1. The script opens the password-protected PDF using the provided password
2. It creates a new PDF file without any password protection
3. The original file remains unchanged
4. File size comparison is shown after successful unlocking

## Security Note

⚠️ **Important**: This tool removes password protection from PDFs. Make sure you have the legal right to remove protection from any PDF you process.

## Error Handling

The script handles common errors:
- Incorrect password
- File not found
- Invalid PDF format
- Permission errors

## Output

After successful unlocking, you'll see:
- ✅ Confirmation message
- 📄 Output file path
- 📊 File size comparison (input → output)

## License

This project is provided as-is for educational purposes.