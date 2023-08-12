A Python script that converts multiple SVG files to PNG format with a user-friendly graphical interface.

Prerequisites:

Python 3.x installed on your machine.

Make sure you have Inkscape installed and accessible at the following path: 
"C:\Program Files\Inkscape\bin\inkscape.exe"

Clone this repository to your local machine by running the following command in your terminal:

git clone https://github.com/JunkBoy76/SVG-To-PNG-Batch-Converter.git
Navigate to the project directory:

cd SVG-To-PNG-Batch-Converter
(Optional) It is recommended to set up a virtual environment before installing any dependencies:

python3 -m venv venv
Activate the virtual environment:

On macOS/Linux:

source venv/bin/activate

On Windows:

venv\Scripts\activate
Install the required dependencies:
pip install -r requirements.txt
Usage
Ensure that you have Inkscape installed and it is located at the following path: "C:\Program Files\Inkscape\bin\inkscape.exe".

From the project directory, run the script by executing the following command:

python converter.py
The graphical interface will appear, allowing you to browse and select the SVG files you want to convert.

Choose the output directory where the converted PNG files will be saved.

Customize any desired settings and options.

Click the "Convert" button to start the conversion process.

The converted PNG files will be saved in the designated output directory.
