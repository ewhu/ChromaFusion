# test_chromafusion.py
"""
Tests for ChromaFusion module.
"""

import unittest
from chromafusion import ChromaFusion

class TestChromaFusion(unittest.TestCase):
    """Test cases for ChromaFusion class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChromaFusion()
        self.assertIsInstance(instance, ChromaFusion)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChromaFusion()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
