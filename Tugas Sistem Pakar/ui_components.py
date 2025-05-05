#!/usr/bin/env python3
# ui_components.py - UI components for Outfit Recommendation System

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime

class OutfitRecommendationUI:
    """The UI class for the Outfit Recommendation System"""
    
    def __init__(self, root, recommendation_engine):
        """Initialize the UI
        
        Args:
            root: The tkinter root window
            recommendation_engine: The recommendation engine object
        """
        self.root = root
        self.engine = recommendation_engine
        
        # Configure the main window
        self.root.title("Sistem Pakar Rekomendasi Outfit Harian")
        self.root.geometry("900x650")
        self.root.configure(bg="#f5f5f5")
        
        # Weather and occasion mapping dictionaries
        self.weather_options = ["Panas (>30°C)", "Hangat (20-30°C)", "Dingin (<20°C)", "Hujan"]
        self.weather_values = ["hot", "warm", "cold", "rainy"]
        self.weather_mapping = dict(zip(self.weather_options, self.weather_values))
        
        self.occasion_options = ["Formal (Kerja/Meeting)", "Casual (Santai/Jalan-jalan)", "Olahraga/Aktivitas Fisik"]
        self.occasion_values = ["formal", "casual", "sports"]
        self.occasion_mapping = dict(zip(self.occasion_options, self.occasion_values))
        
        # Create the UI components
        self.create_widgets()
    
    def create_widgets(self):
        """Create and layout all UI widgets"""
        # Header
        self.create_header()
        
        # Main container
        main_container = tk.Frame(self.root, bg="#f5f5f5", padx=20, pady=20)
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Input frame
        self.create_input_frame(main_container)
        
        # Button to generate recommendation
        self.create_button_frame(main_container)
        
        # Result frame
        self.create_result_frame(main_container)
        
        # Footer
        self.create_footer()
    
    def create_header(self):
        """Create the application header"""
        header_frame = tk.Frame(self.root, bg="#5c6bc0", padx=10, pady=10)
        header_frame.pack(fill=tk.X)
        
        header_label = tk.Label(
            header_frame, 
            text="Sistem Pakar Rekomendasi Outfit Harian", 
            font=("Helvetica", 16, "bold"),
            fg="white",
            bg="#5c6bc0"
        )
        header_label.pack()
        
        subtitle_label = tk.Label(
            header_frame, 
            text="Berdasarkan Cuaca dan Agenda", 
            font=("Helvetica", 12),
            fg="white",
            bg="#5c6bc0"
        )
        subtitle_label.pack()
    
    def create_input_frame(self, parent):
        """Create the input form frame
        
        Args:
            parent: The parent widget
        """
        input_frame = tk.LabelFrame(
            parent, 
            text="Input Data", 
            font=("Helvetica", 12, "bold"), 
            bg="#f5f5f5", 
            padx=15, 
            pady=15
        )
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Grid for inputs
        input_grid = tk.Frame(input_frame, bg="#f5f5f5")
        input_grid.pack(fill=tk.X)
        
        # Weather selection
        weather_label = tk.Label(input_grid, text="Cuaca:", font=("Helvetica", 11), bg="#f5f5f5")
        weather_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        
        self.weather_var = tk.StringVar()
        
        self.weather_combobox = ttk.Combobox(
            input_grid, 
            textvariable=self.weather_var,
            values=self.weather_options,
            width=20,
            state="readonly"
        )
        self.weather_combobox.grid(row=0, column=1, sticky="w", padx=10, pady=10)
        self.weather_combobox.current(1)  # Default to warm
        
        # Occasion selection
        occasion_label = tk.Label(input_grid, text="Agenda:", font=("Helvetica", 11), bg="#f5f5f5")
        occasion_label.grid(row=0, column=2, sticky="w", padx=10, pady=10)
        
        self.occasion_var = tk.StringVar()
        
        self.occasion_combobox = ttk.Combobox(
            input_grid, 
            textvariable=self.occasion_var,
            values=self.occasion_options,
            width=25,
            state="readonly"
        )
        self.occasion_combobox.grid(row=0, column=3, sticky="w", padx=10, pady=10)
        self.occasion_combobox.current(0)  # Default to formal
        
        # Gender preference
        gender_label = tk.Label(input_grid, text="Preferensi Style:", font=("Helvetica", 11), bg="#f5f5f5")
        gender_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        
        self.gender_var = tk.StringVar(value="neutral")
        
        gender_frame = tk.Frame(input_grid, bg="#f5f5f5")
        gender_frame.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        
        tk.Radiobutton(
            gender_frame, 
            text="Maskulin", 
            variable=self.gender_var, 
            value="masculine",
            bg="#f5f5f5",
            font=("Helvetica", 10)
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Radiobutton(
            gender_frame, 
            text="Feminin", 
            variable=self.gender_var, 
            value="feminine",
            bg="#f5f5f5",
            font=("Helvetica", 10)
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Radiobutton(
            gender_frame, 
            text="Netral", 
            variable=self.gender_var, 
            value="neutral",
            bg="#f5f5f5",
            font=("Helvetica", 10)
        ).pack(side=tk.LEFT, padx=5)
        
        # Special considerations
        special_label = tk.Label(input_grid, text="Pertimbangan Khusus:", font=("Helvetica", 11), bg="#f5f5f5")
        special_label.grid(row=1, column=2, sticky="w", padx=10, pady=10)
        
        self.special_var = tk.StringVar(value="none")
        
        special_frame = tk.Frame(input_grid, bg="#f5f5f5")
        special_frame.grid(row=1, column=3, sticky="w", padx=10, pady=10)
        
        tk.Radiobutton(
            special_frame, 
            text="Modest/Tertutup", 
            variable=self.special_var, 
            value="modest",
            bg="#f5f5f5",
            font=("Helvetica", 10)
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Radiobutton(
            special_frame, 
            text="Tidak Ada", 
            variable=self.special_var, 
            value="none",
            bg="#f5f5f5",
            font=("Helvetica", 10)
        ).pack(side=tk.LEFT, padx=5)
        
        # Date input for seasonal consideration
        date_label = tk.Label(input_grid, text="Tanggal:", font=("Helvetica", 11), bg="#f5f5f5")
        date_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        
        date_frame = tk.Frame(input_grid, bg="#f5f5f5")
        date_frame.grid(row=2, column=1, columnspan=3, sticky="w", padx=10, pady=10)
        
        self.day_var = tk.StringVar()
        self.month_var = tk.StringVar()
        self.year_var = tk.StringVar()
        
        # Set default date to today
        today = datetime.now()
        self.day_var.set(today.day)
        self.month_var.set(today.month)
        self.year_var.set(today.year)
        
        ttk.Combobox(
            date_frame, 
            textvariable=self.day_var,
            values=[str(i).zfill(2) for i in range(1, 32)],
            width=5,
            state="readonly"
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Label(date_frame, text="/", bg="#f5f5f5").pack(side=tk.LEFT)
        
        ttk.Combobox(
            date_frame, 
            textvariable=self.month_var,
            values=[str(i).zfill(2) for i in range(1, 13)],
            width=5,
            state="readonly"
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Label(date_frame, text="/", bg="#f5f5f5").pack(side=tk.LEFT)
        
        ttk.Combobox(
            date_frame, 
            textvariable=self.year_var,
            values=[str(i) for i in range(2020, 2031)],
            width=7,
            state="readonly"
        ).pack(side=tk.LEFT, padx=2)
    
    def create_button_frame(self, parent):
        """Create the button frame
        
        Args:
            parent: The parent widget
        """
        button_frame = tk.Frame(parent, bg="#f5f5f5", padx=10, pady=10)
        button_frame.pack(fill=tk.X)
        
        generate_button = tk.Button(
            button_frame,
            text="Buat Rekomendasi",
            command=self.generate_recommendation,
            bg="#7986cb",
            fg="white",
            font=("Helvetica", 12, "bold"),
            padx=20,
            pady=10,
            relief=tk.RAISED,
            bd=2
        )
        generate_button.pack(pady=10)
    
    def create_result_frame(self, parent):
        """Create the result display frame
        
        Args:
            parent: The parent widget
        """
        result_frame = tk.LabelFrame(
            parent, 
            text="Rekomendasi Outfit", 
            font=("Helvetica", 12, "bold"), 
            bg="#f5f5f5", 
            padx=15, 
            pady=15
        )
        result_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.result_text = scrolledtext.ScrolledText(
            result_frame, 
            wrap=tk.WORD, 
            font=("Helvetica", 11), 
            height=12
        )
        self.result_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.result_text.config(state=tk.DISABLED)
    
    def create_footer(self):
        """Create the application footer"""
        footer_frame = tk.Frame(self.root, bg="#5c6bc0", padx=10, pady=5)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        footer_label = tk.Label(
            footer_frame, 
            text="© 2025 Sistem Pakar Rekomendasi Outfit | Dibuat dengan Python & Tkinter", 
            font=("Helvetica", 8),
            fg="white",
            bg="#5c6bc0"
        )
        footer_label.pack()
    
    def generate_recommendation(self):
        """Handle the recommendation generation button click"""
        try:
            # Get selected values
            weather_display = self.weather_combobox.get()
            weather = self.weather_mapping[weather_display]
            
            occasion_display = self.occasion_combobox.get()
            occasion = self.occasion_mapping[occasion_display]
            
            gender = self.gender_var.get()
            special = self.special_var.get()
            
            # Get date values
            day = self.day_var.get()
            month = self.month_var.get()
            year = self.year_var.get()
            
            # Generate the recommendation
            recommendation = self.engine.generate_recommendation(
                weather, 
                occasion, 
                gender, 
                special, 
                (day, month, year)
            )
            
            # Format the recommendation text
            result_text = self.engine.format_recommendation_text(recommendation)
            
            # Update the result text widget
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_text)
            self.result_text.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Helper class for styling the UI components
class AppStyles:
    """Helper class to manage application styles"""
    
    @staticmethod
    def apply_styles(root):
        """Apply custom styles to the application
        
        Args:
            root: The root Tk instance
        """
        style = ttk.Style()
        
        # Configure TCombobox style
        style.configure(
            "TCombobox",
            fieldbackground="#ffffff",
            background="#ffffff",
            foreground="#333333",
            arrowcolor="#5c6bc0"
        )
        
        # Configure TButton style
        style.configure(
            "TButton",
            foreground="#ffffff",
            background="#7986cb",
            font=("Helvetica", 11),
            padding=10
        )
        
        # Apply custom theme if available
        try:
            root.tk.call("source", "azure.tcl")
            root.tk.call("set_theme", "light")
        except tk.TclError:
            # Azure theme not available, use default styling
            pass