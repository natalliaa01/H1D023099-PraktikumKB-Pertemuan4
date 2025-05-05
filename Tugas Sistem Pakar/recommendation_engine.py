#!/usr/bin/env python3
# recommendation_engine.py - Recommendation engine for Outfit Recommendation System

import random
from datetime import datetime

class OutfitRecommendationEngine:
    """The main recommendation engine for outfit suggestions"""
    
    def __init__(self, knowledge_base):
        """Initialize the recommendation engine
        
        Args:
            knowledge_base: The knowledge base object to use for recommendations
        """
        self.kb = knowledge_base
    
    def generate_recommendation(self, weather, occasion, gender, special, date=None):
        """Generate an outfit recommendation based on input parameters
        
        Args:
            weather (str): Weather value (hot, warm, cold, rainy)
            occasion (str): Occasion value (formal, casual, sports)
            gender (str): Gender preference (masculine, feminine, neutral)
            special (str): Special considerations (modest, none)
            date (tuple): Optional tuple of (day, month, year) for seasonal considerations
            
        Returns:
            dict: A dictionary containing the recommendation details
        """
        try:
            # Get the current date if none provided
            if date is None:
                now = datetime.now()
                month = now.month
                day = now.day
                year = now.year
            else:
                day, month, year = date
                # Ensure month is an integer
                month = int(month)
            
            # Get season based on date
            season = self.kb.get_season_from_month(month)
            
            # Get items from knowledge base
            tops = self.kb.get_item_options("tops", occasion, weather)
            bottoms = self.kb.get_item_options("bottoms", occasion, weather)
            outerwear = self.kb.get_item_options("outerwear", occasion, weather)
            shoes = self.kb.get_item_options("shoes", occasion, weather)
            accessories = self.kb.get_item_options("accessories", occasion, weather)
            
            # Apply gender filtering
            if gender == "masculine":
                # Filter out feminine items
                feminine_items = ["Blus", "Rok", "Dress", "Crop top"]
                tops = [item for item in tops if not any(f_item in item for f_item in feminine_items)]
                bottoms = [item for item in bottoms if not any(f_item in item for f_item in feminine_items)]
            
            if gender == "feminine":
                # Add some feminine options if available for the occasion
                if occasion == "formal" and random.random() > 0.5:
                    tops.extend(["Blus formal", "Kemeja feminine"])
                    bottoms.extend(["Rok pensil", "Dress formal"])
                elif occasion == "casual" and random.random() > 0.5:
                    tops.extend(["Blus casual", "Crop top stylish"])
                    bottoms.extend(["Rok casual", "Dress santai"])
                elif occasion == "sports":
                    tops.extend(["Sport bra", "Tank top feminine"])
            
            # Apply modesty filtering
            if special == "modest":
                # Remove items that aren't modest
                immodest_items = ["Crop top", "Tank top", "Singlet", "Rok mini", "Celana pendek"]
                tops = [item for item in tops if not any(im_item in item for im_item in immodest_items)]
                bottoms = [item for item in bottoms if not any(im_item in item for im_item in immodest_items)]
                
                # Add modest alternatives if needed
                if not tops:
                    tops = ["Kemeja lengan panjang", "Blus tertutup", "Kaos lengan panjang"]
                if not bottoms:
                    bottoms = ["Celana panjang", "Rok panjang", "Celana kulot"]
            
            # Get color recommendation based on season
            color_recommendation = self.kb.get_color_recommendation(season)
            
            # Get weather tip
            weather_tip = self.kb.get_weather_tip(weather)
            
            # Get occasion tip
            occasion_tip = self.kb.get_occasion_tip(occasion)
            
            # Select random items from each category
            selected_top = random.choice(tops) if tops else "Outfit tidak tersedia"
            selected_bottom = random.choice(bottoms) if bottoms else "Outfit tidak tersedia"
            selected_outerwear = random.choice(outerwear) if outerwear else "Tidak diperlukan"
            selected_shoes = random.choice(shoes) if shoes else "Outfit tidak tersedia"
            
            # Select 2-3 random accessories
            selected_accessories = random.sample(accessories, min(len(accessories), random.randint(2, 3))) if accessories else ["Aksesoris minimal"]
            
            # Current datetime for the recommendation
            now = datetime.now()
            date_str = now.strftime("%d %B %Y")
            time_str = now.strftime("%H:%M")
            
            # Build the recommendation result
            result = {
                "date": date_str,
                "time": time_str,
                "top": selected_top,
                "bottom": selected_bottom,
                "outerwear": selected_outerwear if "Tidak diperlukan" not in selected_outerwear else None,
                "shoes": selected_shoes,
                "accessories": selected_accessories,
                "color_recommendation": color_recommendation,
                "weather_tip": weather_tip,
                "occasion_tip": occasion_tip
            }
            
            return result
            
        except Exception as e:
            # Return error information if something goes wrong
            return {
                "error": str(e),
                "date": datetime.now().strftime("%d %B %Y"),
                "time": datetime.now().strftime("%H:%M")
            }
    
    def format_recommendation_text(self, recommendation):
        """Format a recommendation dictionary as displayable text
        
        Args:
            recommendation (dict): The recommendation dictionary
            
        Returns:
            str: Formatted recommendation text
        """
        if "error" in recommendation:
            return f"Error: {recommendation['error']}"
        
        # Build the text output
        text = []
        text.append(f"=== REKOMENDASI OUTFIT {recommendation['date']} ===\n")
        text.append(f"👕 Atasan: {recommendation['top']}\n")
        text.append(f"👖 Bawahan: {recommendation['bottom']}\n")
        
        if recommendation['outerwear']:
            text.append(f"🧥 Outer: {recommendation['outerwear']}\n")
        
        text.append(f"👟 Alas Kaki: {recommendation['shoes']}\n")
        text.append(f"👜 Aksesoris: {', '.join(recommendation['accessories'])}\n")
        text.append(f"🎨 {recommendation['color_recommendation']}\n")
        
        if recommendation['weather_tip']:
            text.append(f"\n{recommendation['weather_tip']}")
        
        if recommendation['occasion_tip']:
            text.append(f"\n{recommendation['occasion_tip']}")
        
        text.append(f"\nDibuat pada: {recommendation['time']}")
        
        return "\n".join(text)