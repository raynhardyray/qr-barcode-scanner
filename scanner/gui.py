from tkinter import *
from scanner.utils import openFile, scanFile, imageConvertToTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
IMAGE_WIDTH = 400
IMAGE_HEIGHT = 260
DEFAULT_FONT = ("Arial", 10, "bold")
RESULT_FONT = ("Arial", 16, "bold")

class ApplicationGUI:
    def __init__(self, root):
        root.title("Barcode/QR Code Scanner")
        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        root.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=BOTH, expand=True)

        self.filePathVar = StringVar()
        self.resultVar = StringVar()
        self.imgTk = None
        self.current_file_path = None

        self._create_widgets(main_frame)
        self._layout_widgets()
        
    def _create_widgets(self, parent_frame):
        self.file_frame = ttk.Frame(parent_frame)
        self.file_name_label = ttk.Label(self.file_frame, text="Image File", font=DEFAULT_FONT)
        self.file_path_label = ttk.Label(self.file_frame, textvariable=self.filePathVar, width=55, relief="sunken", anchor=W)
        self.browse_button = ttk.Button(self.file_frame, text="Browse...", command=self.browseFile, bootstyle="outline")
        
        self.image_placeholder = Canvas(parent_frame, relief="sunken", width=IMAGE_WIDTH, height=IMAGE_HEIGHT)
        self.scan_button = ttk.Button(parent_frame, text="Scan Image", command=self.scanSelectedFile, bootstyle="success-outline")
        
        self.result_label = ttk.Label(parent_frame, textvariable=self.resultVar, relief="sunken", anchor=CENTER, font=RESULT_FONT)
        
    def _layout_widgets(self):
        self.file_frame.grid(column=0, row=0, sticky=(E, W), padx=5, pady=5)
        self.file_name_label.grid(column=0, row=0, sticky=W)
        self.file_path_label.grid(column=1, row=0, sticky=(E, W), padx=5)
        self.browse_button.grid(column=2, row=0, sticky=E)
        
        self.image_placeholder.grid(column=0, row=1, pady=5)
        self.scan_button.grid(column=0, row=2)
        self.result_label.grid(column=0, row=3, sticky=(E, W), pady=10)
        
        self.file_frame.columnconfigure(1, weight=1)
        self.file_frame.master.columnconfigure(0, weight=1)
        
    def browseFile(self):
        path = openFile()
        if not path:
            return
            
        self.current_file_path = path
        self.filePathVar.set(path)
        self.resultVar.set("")
        self.displayImage(path)
        
    def displayImage(self, path):
        try:
            self.imgTk = imageConvertToTk(path, (IMAGE_WIDTH, IMAGE_HEIGHT))
            self.image_placeholder.create_image(0, 0, anchor=NW, image=self.imgTk)
        except Exception as e:
            self.resultVar.set(f"Error loading image: {e}")
            self.image_placeholder.delete("all")
            
    def scanSelectedFile(self):
        if not self.current_file_path:
            self.resultVar.set("Please browse for a file first!")
            return
            
        results = scanFile(self.current_file_path)
        
        if not results:
            self.resultVar.set("No barcode/QR code found.")
            return
            
        all_data = [result.data.decode('utf-8') for result in results]
        self.resultVar.set("\n".join(all_data))