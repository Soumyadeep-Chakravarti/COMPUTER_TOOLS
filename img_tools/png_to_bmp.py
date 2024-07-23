#!/usr/bin/env python3

import os
import argparse
import glob
from PIL import Image

def convert_png_to_bmp(input_files, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for input_pattern in input_files:
        # Expand the wildcard pattern
        for input_file in glob.glob(input_pattern):
            try:
                # Check if the file is a PNG
                if input_file.lower().endswith('.png'):
                    # Open the PNG image
                    with Image.open(input_file) as img:
                        # Generate output file name
                        file_name = os.path.basename(input_file)
                        file_name_without_ext = os.path.splitext(file_name)[0]
                        output_file = os.path.join(output_folder, f"{file_name_without_ext}.bmp")
                        
                        # Convert and save as BMP
                        img.save(output_file, 'BMP')
                        print(f"Converted {input_file} to {output_file}")
                else:
                    print(f"Skipped {input_file}: Not a PNG file")
            except Exception as e:
                print(f"Error converting {input_file}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Convert PNG images to BMP format.")
    parser.add_argument("input_files", nargs='+', help="Input PNG file(s) or patterns")
    parser.add_argument("-o", "--output", default="output", help="Output folder for BMP files")
    
    args = parser.parse_args()
    
    convert_png_to_bmp(args.input_files, args.output)

if __name__ == "__main__":
    main()