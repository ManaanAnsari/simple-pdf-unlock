#!/usr/bin/env python3
"""
PDF Unlocker - Remove password protection from PDF files
Author: PDF Processing Tool
Description: This script unlocks password-protected PDF files and creates
             new PDF files without password protection.
"""

import sys
import os
import argparse
from pikepdf import Pdf, PasswordError


def unlock_pdf(input_path, password, output_path):
    """
    Unlock a password-protected PDF and save it without protection.

    Args:
        input_path (str): Path to the input PDF file
        password (str): Password to unlock the PDF
        output_path (str): Path where the unlocked PDF will be saved

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Open the password-protected PDF
        with Pdf.open(input_path, password=password) as pdf:
            # Save the PDF without password protection
            pdf.save(output_path)
            return True

    except PasswordError:
        print(f"Error: Incorrect password for {input_path}")
        return False
    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def main():
    """Main function to handle command line arguments and PDF unlocking."""
    parser = argparse.ArgumentParser(
        description="Unlock password-protected PDF files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python pdf_unlock.py -i protected.pdf -p mypassword -o unlocked.pdf
  python pdf_unlock.py --input protected.pdf --password mypassword --output unlocked.pdf

Note:
  The output file will be created without any password protection.
        """
    )

    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Path to the password-protected input PDF file'
    )

    parser.add_argument(
        '-p', '--password',
        required=True,
        help='Password to unlock the PDF'
    )

    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Path for the output unlocked PDF file'
    )

    args = parser.parse_args()

    # Validate input file exists
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' does not exist")
        sys.exit(1)

    # Unlock the PDF
    print(f"Unlocking PDF: {args.input}")
    print(f"Output will be saved to: {args.output}")

    success = unlock_pdf(args.input, args.password, args.output)

    if success:
        print("✅ PDF successfully unlocked!")
        print(f"📄 Unlocked PDF saved as: {args.output}")

        # Show file size comparison
        if os.path.exists(args.output):
            input_size = os.path.getsize(args.input) / 1024  # KB
            output_size = os.path.getsize(args.output) / 1024  # KB
            print(f"📊 File size: {input_size:.1f} KB → {output_size:.1f} KB")
    else:
        print("❌ Failed to unlock PDF")
        sys.exit(1)


if __name__ == "__main__":
    main()