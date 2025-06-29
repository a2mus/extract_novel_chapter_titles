import tkinter as tk
from tkinter import filedialog, Text
import threading
from scraper import extract_chapter_titles
from file_saver import save_chapters_to_markdown

class ChapterExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Novel Chapter Extractor")

        # URL Input
        self.url_label = tk.Label(root, text="Novel URL:")
        self.url_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

        # Destination Folder
        self.folder_label = tk.Label(root, text="Destination Folder:")
        self.folder_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.folder_path_entry = tk.Entry(root, width=50)
        self.folder_path_entry.grid(row=1, column=1, padx=10, pady=5)
        self.browse_button = tk.Button(root, text="Browse...", command=self.browse_folder)
        self.browse_button.grid(row=1, column=2, padx=10, pady=5)

        # Filename Input
        self.filename_label = tk.Label(root, text="Output Filename:")
        self.filename_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.filename_entry = tk.Entry(root, width=50)
        self.filename_entry.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

        # Extract Button
        self.extract_button = tk.Button(root, text="Extract Chapters", command=self.extract_chapters)
        self.extract_button.grid(row=3, column=1, padx=10, pady=10)

        # Preview Area
        self.preview_label = tk.Label(root, text="Preview:")
        self.preview_label.grid(row=4, column=0, padx=10, pady=5, sticky='nw')
        self.preview_text = Text(root, height=15, width=80, state='disabled')
        self.preview_text.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

        # Status Bar
        self.status_label = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.grid(row=6, column=0, columnspan=3, sticky='ew')

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path_entry.delete(0, tk.END)
            self.folder_path_entry.insert(0, folder_selected)

    def extract_chapters(self):
        self.status_label.config(text="Extracting...")
        self.extract_button.config(state='disabled')
        thread = threading.Thread(target=self.run_extraction_in_thread)
        thread.start()

    def run_extraction_in_thread(self):
        url = self.url_entry.get()
        dest_folder = self.folder_path_entry.get()
        filename = self.filename_entry.get()

        if not url or not dest_folder or not filename:
            self.status_label.config(text="Error: All fields are required.")
            self.extract_button.config(state='normal')
            return

        try:
            chapters = extract_chapter_titles(url)
            if chapters:
                self.preview_text.config(state='normal')
                self.preview_text.delete(1.0, tk.END)
                for chapter in chapters:
                    self.preview_text.insert(tk.END, f"- {chapter}\n")
                self.preview_text.config(state='disabled')

                save_chapters_to_markdown(chapters, dest_folder, filename)
                self.status_label.config(text="Extraction complete. File saved.")
            else:
                self.status_label.config(text="Error: Could not extract chapters.")
        except Exception as e:
            self.status_label.config(text=f"Error: {e}")
        finally:
            self.extract_button.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    app = ChapterExtractorApp(root)
    root.mainloop()