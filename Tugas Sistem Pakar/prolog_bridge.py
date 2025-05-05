#!/usr/bin/env python3
# prolog_bridge.py - Bridge module for Python to Prolog interaction

"""
This module provides a bridge between Python and Prolog for the Outfit Recommendation System.
It uses the pyswip library if available, otherwise it provides fallback mechanisms.
"""

import os
import sys
import subprocess
import tempfile

class PrologBridge:
    """Bridge class for Python to Prolog interaction"""
    
    def __init__(self, prolog_file="outfit_kb.pl"):
        """Initialize the Prolog bridge
        
        Args:
            prolog_file (str): Path to the Prolog knowledge base file
        """
        self.prolog_file = prolog_file
        self.pyswip_available = False
        
        # Check if pyswip is available
        try:
            from pyswip import Prolog
            self.prolog = Prolog()
            self.pyswip_available = True
            self._consult_prolog_file()
            print("Successfully initialized pyswip Prolog bridge")
        except ImportError:
            print("pyswip not available, will use alternative methods")
            # Check if SWI-Prolog is installed
            self._check_swipl_installed()
    
    def _consult_prolog_file(self):
        """Consult the Prolog knowledge base file"""
        if not self.pyswip_available:
            return
        
        try:
            if os.path.exists(self.prolog_file):
                self.prolog.consult(self.prolog_file)
                print(f"Successfully consulted {self.prolog_file}")
            else:
                print(f"Warning: Prolog file {self.prolog_file} not found")
        except Exception as e:
            print(f"Error consulting Prolog file: {e}")
    
    def _check_swipl_installed(self):
        """Check if SWI-Prolog is installed on the system"""
        try:
            result = subprocess.run(
                ["swipl", "--version"], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True
            )
            if result.returncode == 0:
                print("SWI-Prolog found on system")
                self.swipl_available = True
            else:
                print("SWI-Prolog not found on system")
                self.swipl_available = False
        except Exception:
            print("Could not check for SWI-Prolog, assuming not available")
            self.swipl_available = False
    
    def query(self, query_string):
        """Execute a Prolog query
        
        Args:
            query_string (str): The Prolog query string
            
        Returns:
            list: List of results (dictionaries of variable bindings)
        """
        if self.pyswip_available:
            return self._query_pyswip(query_string)
        elif hasattr(self, 'swipl_available') and self.swipl_available:
            return self._query_subprocess(query_string)
        else:
            print("No Prolog interface available, cannot execute query")
            return []
    
    def _query_pyswip(self, query_string):
        """Execute a query using pyswip
        
        Args:
            query_string (str): The Prolog query string
            
        Returns:
            list: List of results (dictionaries of variable bindings)
        """
        try:
            results = list(self.prolog.query(query_string))
            return results
        except Exception as e:
            print(f"Error executing pyswip query: {e}")
            return []
    
    def _query_subprocess(self, query_string):
        """Execute a query using subprocess to call swipl
        
        Args:
            query_string (str): The Prolog query string
            
        Returns:
            list: List of results (dictionaries of variable bindings)
        """
        try:
            # Create a temporary Prolog script file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.pl', delete=False) as temp_file:
                temp_file_name = temp_file.name
                # Write the query to the temporary file
                temp_file.write(f":- consult('{self.prolog_file}').\n")
                temp_file.write(f":- {query_string}, write(user_output, true), halt.\n")
                temp_file.write(":- write(user_output, false), halt.\n")
            
            # Execute the temporary Prolog script
            result = subprocess.run(
                ["swipl", "-q", "-f", temp_file_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Clean up the temporary file
            os.unlink(temp_file_name)
            
            # Process the result
            if "true" in result.stdout:
                # Very simplified result, just indicating success
                return [{'success': True}]
            else:
                return []
        except Exception as e:
            print(f"Error executing subprocess query: {e}")
            return []

    def recommend_outfit(self, occasion, weather, gender, modesty, month):
        """Get a complete outfit recommendation
        
        Args:
            occasion (str): Occasion type (formal, casual, sports)
            weather (str): Weather condition (hot, warm, cold, rainy)
            gender (str): Gender preference (masculine, feminine, neutral)
            modesty (str): Modesty preference (modest, none)
            month (int): Month number for seasonal considerations
            
        Returns:
            dict: Dictionary containing recommendation details
        """
        query = f"recommend_outfit({occasion}, {weather}, {gender}, {modesty}, {month}, Recommendation)"
        results = self.query(query)
        
        if results:
            # Extract recommendation text from the first result
            recommendation_text = results[0].get('Recommendation', '')
            return {"success": True, "recommendation": recommendation_text}
        else:
            return {"success": False, "error": "No recommendation found"}