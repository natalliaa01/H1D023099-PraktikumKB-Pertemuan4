#!/usr/bin/env python3
# knowledge_base.py - Knowledge base module for Outfit Recommendation System

import os
import sys
import subprocess
from datetime import datetime

class KnowledgeBase:
    """Class to handle the knowledge base for outfit recommendations"""
    
    def __init__(self, use_prolog=False):
        """Initialize knowledge base
        
        Args:
            use_prolog (bool): If True, will try to use the Prolog knowledge base
                              If False, will use the Python dictionary knowledge base
        """
        self.use_prolog = use_prolog
        
        # Initialize the Python version of the knowledge base
        self._init_python_kb()
        
        # Try to initialize Prolog if requested
        if self.use_prolog:
            self._init_prolog_kb()
    
    def _init_python_kb(self):
        """Initialize the Python version of the knowledge base"""
        self.knowledge_base = {
            "tops": {
                "formal": {
                    "hot": ["Kemeja katun lengan pendek", "Kemeja linen tipis", "Blus sutra"],
                    "warm": ["Kemeja formal lengan panjang", "Blus semi-formal", "Kemeja katun lengan 3/4"],
                    "cold": ["Kemeja tebal", "Sweater kasmir", "Turtle neck"],
                    "rainy": ["Kemeja lengan panjang", "Blus dengan lapisan dalam"]
                },
                "casual": {
                    "hot": ["Kaos katun", "Tank top", "Crop top", "T-shirt vintage"],
                    "warm": ["Kaos lengan panjang", "Henley shirt", "Polo shirt"],
                    "cold": ["Sweater rajut", "Hoodie", "Sweatshirt"],
                    "rainy": ["Kaos lengan panjang", "Sweater tipis"]
                },
                "sports": {
                    "hot": ["Singlet olahraga", "Sport bra", "Kaos dry-fit"],
                    "warm": ["Kaos olahraga lengan panjang", "Jersey ringan"],
                    "cold": ["Jaket olahraga", "Sweater training", "Base layer thermal"],
                    "rainy": ["Kaos olahraga waterproof", "Jaket lari ringan"]
                }
            },
            
            "bottoms": {
                "formal": {
                    "hot": ["Celana bahan tipis", "Rok A-line", "Celana kulot"],
                    "warm": ["Celana bahan", "Rok pensil", "Celana ankle-length"],
                    "cold": ["Celana wool", "Rok panjang", "Celana bahan tebal"],
                    "rainy": ["Celana bahan anti air", "Rok panjang"]
                },
                "casual": {
                    "hot": ["Celana pendek", "Rok mini", "Jeans pendek", "Rok flare"],
                    "warm": ["Jeans", "Celana chino", "Rok midi"],
                    "cold": ["Jeans tebal", "Celana cargo", "Legging"],
                    "rainy": ["Jeans", "Celana panjang waterproof"]
                },
                "sports": {
                    "hot": ["Celana pendek olahraga", "Legging pendek", "Rok tennis"],
                    "warm": ["Celana training", "Legging 3/4", "Jogger pants"],
                    "cold": ["Celana training tebal", "Legging thermal", "Sweatpants"],
                    "rainy": ["Celana training waterproof", "Legging tahan air"]
                }
            },
            
            "outerwear": {
                "formal": {
                    "hot": ["Tidak diperlukan", "Blazer ultra tipis (opsional)"],
                    "warm": ["Blazer ringan", "Cardigan formal", "Jas tipis"],
                    "cold": ["Blazer wol", "Coat formal", "Trench coat"],
                    "rainy": ["Blazer waterproof", "Trench coat", "Jas hujan formal"]
                },
                "casual": {
                    "hot": ["Tidak diperlukan"],
                    "warm": ["Cardigan tipis", "Jaket denim", "Kemeja flannel"],
                    "cold": ["Jaket tebal", "Parka", "Coat casual", "Puffer jacket"],
                    "rainy": ["Jaket hujan", "Windbreaker", "Parka tahan air"]
                },
                "sports": {
                    "hot": ["Tidak diperlukan"],
                    "warm": ["Jaket olahraga ringan", "Windbreaker tipis"],
                    "cold": ["Jaket olahraga tebal", "Windbreaker berlapis", "Down jacket"],
                    "rainy": ["Jaket hujan olahraga", "Anorak", "Poncho olahraga"]
                }
            },
            
            "shoes": {
                "formal": {
                    "hot": ["Loafer", "Flat shoes", "Sepatu pantofel"],
                    "warm": ["Oxford shoes", "Sepatu kulit", "Heels"],
                    "cold": ["Boots formal", "Chelsea boots", "Sepatu kulit berlapis"],
                    "rainy": ["Boots tahan air", "Sepatu kulit waterproof"]
                },
                "casual": {
                    "hot": ["Sandal", "Slip-on", "Sneakers ringan", "Espadrilles"],
                    "warm": ["Sneakers", "Sepatu kanvas", "Moccasin"],
                    "cold": ["Boots casual", "Sneakers tebal", "High-top sneakers"],
                    "rainy": ["Boots hujan", "Sneakers waterproof"]
                },
                "sports": {
                    "hot": ["Sepatu lari ringan", "Training shoes", "Sandal olahraga"],
                    "warm": ["Sepatu olahraga", "Cross-trainer", "Athletic shoes"],
                    "cold": ["Sepatu trail", "Sneakers olahraga tebal", "Hiking shoes"],
                    "rainy": ["Trail shoes waterproof", "Sepatu olahraga tahan air"]
                }
            },
            
            "accessories": {
                "formal": {
                    "hot": ["Kacamata hitam", "Tas kerja", "Jam tangan", "Scarf tipis"],
                    "warm": ["Jam tangan", "Dasi", "Tas kerja", "Belt kulit"],
                    "cold": ["Syal wol", "Sarung tangan kulit", "Tas kerja", "Topi formal"],
                    "rainy": ["Payung", "Tas waterproof", "Syal anti air"]
                },
                "casual": {
                    "hot": ["Topi bucket", "Kacamata hitam", "Tas selempang", "Gelang"],
                    "warm": ["Topi baseball", "Sling bag", "Jam tangan casual"],
                    "cold": ["Beanie", "Syal rajut", "Sarung tangan", "Backpack"],
                    "rainy": ["Payung pocket", "Tas anti air", "Topi hujan"]
                },
                "sports": {
                    "hot": ["Sport cap", "Wristband", "Tas olahraga", "Headband"],
                    "warm": ["Beanie sport", "Gym bag", "Smart watch", "Bottle holder"],
                    "cold": ["Ear warmer", "Sarung tangan olahraga", "Syal microfiber"],
                    "rainy": ["Tas waterproof", "Penutup sepatu", "Payung mini"]
                }
            }
        }
    
    def _init_prolog_kb(self):
        """Initialize the Prolog knowledge base connection if available"""
        try:
            # Check if the prolog file exists
            if not os.path.exists("outfit_kb.pl"):
                print("Warning: outfit_kb.pl not found, reverting to Python knowledge base")
                self.use_prolog = False
                return
                
            # Try to import pyswip if it's available
            try:
                from pyswip import Prolog
                self.prolog = Prolog()
                self.prolog.consult("outfit_kb.pl")
                print("Successfully loaded Prolog knowledge base")
            except ImportError:
                print("Warning: pyswip not installed, reverting to Python knowledge base")
                self.use_prolog = False
        except Exception as e:
            print(f"Error initializing Prolog knowledge base: {e}")
            self.use_prolog = False
    
    def get_item_options(self, category, occasion, weather):
        """Get item options based on category, occasion and weather
        
        Args:
            category (str): Item category (tops, bottoms, etc.)
            occasion (str): Occasion type (formal, casual, sports)
            weather (str): Weather condition (hot, warm, cold, rainy)
            
        Returns:
            list: List of items matching the criteria
        """
        if self.use_prolog:
            return self._get_from_prolog(category, occasion, weather)
        else:
            return self._get_from_python(category, occasion, weather)
    
    def _get_from_python(self, category, occasion, weather):
        """Get items from the Python knowledge base
        
        Args:
            category (str): Item category (tops, bottoms, etc.)
            occasion (str): Occasion type (formal, casual, sports)
            weather (str): Weather condition (hot, warm, cold, rainy)
            
        Returns:
            list: List of items matching the criteria
        """
        try:
            return self.knowledge_base[category][occasion][weather]
        except KeyError:
            print(f"Warning: No items found for {category}/{occasion}/{weather}")
            return []
    
    def _get_from_prolog(self, category, occasion, weather):
        """Get items from the Prolog knowledge base
        
        Args:
            category (str): Item category (tops, bottoms, etc.)
            occasion (str): Occasion type (formal, casual, sports)
            weather (str): Weather condition (hot, warm, cold, rainy)
            
        Returns:
            list: List of items matching the criteria
        """
        try:
            query = f"item_options({category}, {occasion}, {weather}, Items)"
            result = list(self.prolog.query(query))
            if result:
                # Extract items from the first result
                return result[0]["Items"]
            else:
                print(f"Warning: No Prolog results for {query}")
                # Fall back to Python knowledge base
                return self._get_from_python(category, occasion, weather)
        except Exception as e:
            print(f"Error querying Prolog: {e}")
            # Fall back to Python knowledge base
            return self._get_from_python(category, occasion, weather)
    
    def get_season_from_month(self, month):
        """Determine season based on month number
        
        Args:
            month (int): Month number (1-12)
            
        Returns:
            str: Season name (spring, summer, fall, winter)
        """
        if 3 <= month <= 5:
            return "spring"
        elif 6 <= month <= 8:
            return "summer"
        elif 9 <= month <= 11:
            return "fall"
        else:
            return "winter"
    
    def get_color_recommendation(self, season):
        """Get color recommendation based on season
        
        Args:
            season (str): Season name
            
        Returns:
            str: Color recommendation text
        """
        recommendations = {
            "spring": "Warna-warna pastel seperti mint, peach, atau baby blue cocok untuk musim semi.",
            "summer": "Warna-warna cerah seperti kuning, biru laut, atau coral ideal untuk musim panas.",
            "fall": "Warna-warna hangat seperti maroon, olive, atau mustard cocok untuk musim gugur.",
            "winter": "Warna-warna gelap seperti navy, burgundy, atau forest green ideal untuk musim dingin."
        }
        return recommendations.get(season, "Pilih warna yang sesuai dengan preferensi Anda.")
    
    def get_weather_tip(self, weather):
        """Get tip based on weather condition
        
        Args:
            weather (str): Weather condition
            
        Returns:
            str: Weather-specific tip
        """
        tips = {
            "hot": "☀️ Tip: Pilih bahan yang breathable dan menyerap keringat. Jangan lupa sunscreen!",
            "rainy": "🌧️ Tip: Bawa payung atau jas hujan dan hindari sepatu berbahan suede atau kulit yang mudah rusak terkena air.",
            "cold": "❄️ Tip: Gunakan teknik layering untuk menjaga tubuh tetap hangat. Inner thermal bisa jadi pilihan tepat.",
            "warm": "🌤️ Tip: Pilih lapisan yang bisa ditambah atau dikurangi sesuai dengan perubahan suhu sepanjang hari."
        }
        return tips.get(weather, "")
    
    def get_occasion_tip(self, occasion):
        """Get tip based on occasion
        
        Args:
            occasion (str): Occasion type
            
        Returns:
            str: Occasion-specific tip
        """
        tips = {
            "formal": "💼 Tip: Pilih aksesoris minimalis namun elegan untuk tampilan profesional.",
            "casual": "🛍️ Tip: Prioritaskan kenyamanan namun tetap stylish dengan memadukan item basic dan statement piece.",
            "sports": "🏃 Tip: Utamakan kenyamanan dan mobilitas. Bawa botol air dan handuk kecil."
        }
        return tips.get(occasion, "")