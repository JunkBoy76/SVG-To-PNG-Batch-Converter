SVG to PNG Batch Converter
Easily convert multiple SVG files to PNG format using a user-friendly Python script with an intuitive graphical interface.

Features
Batch Conversion: Convert multiple SVG files simultaneously.

Graphical Interface: No need for command-line expertise; just select your files and convert.

Multiprocessing: Speed up conversions by processing multiple files in parallel.


Prerequisites:
Python 3.x: Ensure you have Python 3.x installed on your machine.

Inkscape: This tool uses Inkscape for the SVG to PNG conversion process. 
Make sure it's installed and accessible at the following path:
C:\Program Files\Inkscape\bin\inkscape.exe


Setup and Installation:
Clone the Repository:
git clone https://github.com/JunkBoy76/SVG-To-PNG-Batch-Converter.git


Navigate to the Project Directory:
cd SVG-To-PNG-Batch-Converter

Install Required Dependencies:
pip install -r requirements.txt

How to Use:
Run the Script:
python batch_svg2png.py


Select Directories:

Click "Browse" next to "Input Directory" to choose the directory containing your SVG files.
Click "Browse" next to "Output Directory" to specify where you'd like the PNG files to be saved.
Start Conversion:
Click the "Start Conversion" button. The tool will begin converting all SVG files from the input directory to PNG format, saving them in the specified output directory.

Monitor Progress: The progress of the conversion will be displayed in the interface. Once complete, a notification will inform you of the completion.
