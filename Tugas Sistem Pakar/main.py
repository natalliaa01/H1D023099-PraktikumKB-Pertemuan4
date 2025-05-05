#!/usr/bin/env python3
# main.py - Main application file for Outfit Recommendation System

import tkinter as tk
from ui_components import OutfitRecommendationUI
from recommendation_engine import OutfitRecommendationEngine
from knowledge_base import KnowledgeBase

def main():
    """Main entry point for the application"""
    root = tk.Tk()
    # Initialize knowledge base
    kb = KnowledgeBase()
    # Initialize recommendation engine with knowledge base
    engine = OutfitRecommendationEngine(kb)
    # Initialize UI with recommendation engine
    app = OutfitRecommendationUI(root, engine)
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()