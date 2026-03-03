# png-to-avif
An image conversion script that takes a collection of input images in png format and converts them to avif using ffmpeg lossless conversion. See README.md for further instructions on how to use.

# PNG → AVIF Batch Converter (Lossless)

## Overview

This Python script converts a collection of PNG images into **AVIF format** using lossless encoding.

The conversion is powered by :contentReference[oaicite:0]{index=0}, which must be installed and accessible via system PATH.

The script is designed for:

- Batch image processing
- Maximum image quality preservation
- Efficient storage compression using AVIF
- Simple folder-based workflow

---

## Features

✅ Batch converts all `.png` files in a folder  
✅ Uses **lossless AVIF encoding**  
✅ Preserves full color information  
✅ Overwrites safe output directory  
✅ Easy to modify and extend  

---

## Requirements

### Software

- Python 3.x  
- FFmpeg with AVIF codec support  

Verify installation:

```bash
python --version
ffmpeg -version
```

## Installation
1. Install FFmpeg

Download FFmpeg from the official website:
```
👉 https://ffmpeg.org/download.html
```
After installation, add FFmpeg to your system PATH.

## Test:
```
ffmpeg -encoders | findstr av1
```
You should see AV1 encoder support.

2. Clone This Repository
```   
git clone https://github.com/yourusername/png-avif-converter.git
cd png-avif-converter
```
4. Install Python (If Needed)

Windows users can use:
```
py --version
```
Folder Structure
project/
│
├── convert.py
├── input_images/
│     ├── image1.png
│     ├── image2.png
│
└── output_avif/

## Usage
Step 1 — Place PNG Files

Put all PNG images inside:

input_images/
Step 2 — Run Script

Windows:

py convert.py

Linux / macOS:

python3 convert.py

## Output

Converted AVIF images will be saved in:

output_avif/

with the same filenames.

Example:

image1.png → image1.avif
Encoding Quality

The script uses:

Lossless AVIF mode

Full chroma preservation (yuv444p)

Still-picture optimization

Command internally used:

ffmpeg -i input.png -c:v libaom-av1 -lossless 1 -pix_fmt yuv444p output.avif

## Troubleshooting
Python Not Found

Enable Python execution alias or add Python to PATH.

Windows setting:

Settings → Apps → Advanced App Settings → App Execution Aliases

Disable Python aliases if necessary.

FFmpeg Not Found

Run:

where ffmpeg

If empty, add FFmpeg bin folder to PATH.

## Performance Notes

⚠ Lossless AVIF encoding is computationally expensive.

Conversion speed depends on:

CPU performance

Image resolution

Number of images

## License

You can add your preferred license.

## Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss modifications.

## Author

Created for batch image optimization workflows.

Star ⭐ the Repository

If you find this useful, consider starring the repository.
