import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

def convert_single_file(args):
    """Convert a single SVG file to PNG using Inkscape."""
    svg_file, input_directory, output_directory = args
    input_path = os.path.join(input_directory, svg_file)
    output_path = os.path.join(output_directory, os.path.splitext(svg_file)[0] + '.png')
    subprocess.run(["C:\\Program Files\\Inkscape\\bin\\inkscape.exe", input_path, "--export-type=png", "--export-filename=" + output_path])

def convert_svg_to_png_with_inkscape(input_directory, output_directory, progress_label):
    svg_files = [f for f in os.listdir(input_directory) if f.endswith('.svg')]
    if not svg_files:
        messagebox.showerror("Error", "No SVG files found in the selected directory.")
        return

    total_files = len(svg_files)

    # Use multiprocessing to speed up the conversion
    with Pool(processes=cpu_count()) as pool, \
            tqdm(total=total_files, desc="Converting SVG to PNG") as pbar:
        results = pool.imap_unordered(convert_single_file, [(svg, input_directory, output_directory) for svg in svg_files])

        for _ in results:
            pbar.update(1)

    messagebox.showinfo("Info", "Conversion complete!")

def main_gui():
    root = tk.Tk()
    root.title("Batch SVG to PNG Converter")

    style = ttk.Style()
    style.theme_use("clam")  # Apply the 'clam' theme for a nicer look

    frame = ttk.LabelFrame(root, text="SVG to PNG Conversion")
    frame.pack(padx=20, pady=20)

    input_label = ttk.Label(frame, text="Input Directory:")
    input_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

    input_dir_var = tk.StringVar()
    input_entry = ttk.Entry(frame, textvariable=input_dir_var, width=50)
    input_entry.grid(row=0, column=1, padx=5, pady=5)

    def browse_input_dir():
        input_dir = filedialog.askdirectory()
        input_dir_var.set(input_dir)

    input_browse_button = ttk.Button(frame, text="Browse", command=browse_input_dir)
    input_browse_button.grid(row=0, column=2, padx=5, pady=5)

    output_label = ttk.Label(frame, text="Output Directory:")
    output_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

    output_dir_var = tk.StringVar()
    output_entry = ttk.Entry(frame, textvariable=output_dir_var, width=50)
    output_entry.grid(row=1, column=1, padx=5, pady=5)

    def browse_output_dir():
        output_dir = filedialog.askdirectory()
        output_dir_var.set(output_dir)

    output_browse_button = ttk.Button(frame, text="Browse", command=browse_output_dir)
    output_browse_button.grid(row=1, column=2, padx=5, pady=5)

    progress_frame = ttk.Frame(frame)
    progress_frame.grid(row=2, columnspan=3, padx=5, pady=10)
    
    progress_label = ttk.Label(progress_frame, text="")
    progress_label.pack()
    
    progress_bar = ttk.Progressbar(progress_frame, orient=tk.HORIZONTAL, length=300, mode="determinate")
    progress_bar.pack(pady=5)

    def start_conversion():
        input_directory = input_dir_var.get()
        output_directory = output_dir_var.get()
        if not input_directory:
            messagebox.showerror("Error", "Please select an input directory.")
            return
        if not output_directory:
            messagebox.showerror("Error", "Please select an output directory.")
            return
            
        convert_svg_to_png_with_inkscape(input_directory, output_directory, progress_label)

    convert_button = ttk.Button(frame, text="Start Conversion", command=start_conversion)
    convert_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_gui()
