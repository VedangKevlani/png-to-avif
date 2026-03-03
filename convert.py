import os
import subprocess

# Folder containing PNG files
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_avif"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(".png"):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_filename = os.path.splitext(filename)[0] + ".avif"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        command = [
            "ffmpeg",
            "-y",                    # overwrite if exists
            "-i", input_path,
            "-c:v", "libaom-av1",
            "-lossless", "1",        # TRUE lossless mode
            "-cpu-used", "4",        # Faster encoding (0-8, where 0 is slowest but best compression)
            "-pix_fmt", "yuv444p",   # preserve full chroma
            "-still-picture", "1",
            output_path
        ]

        print(f"Converting {filename} → {output_filename}")
        subprocess.run(command, check=True)

print("✅ All PNG files have been converted to AVIF (lossless).")