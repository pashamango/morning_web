import unittest
from gram import generate_content  # Assuming generate_content is in gram.py

class TestGenerateContent(unittest.TestCase):

    def test_generate_content(self):
        header = "Quantum Entanglement"
        result = generate_content(header)
        
        # Check if the result is not empty
        self.assertTrue(len(result) > 0)
        
        # Check if the result contains the word 'quantum'
        self.assertTrue('quantum' in result.lower())
        
        # Add more checks based on what you expect the function to return

if __name__ == '__main__':
    unittest.main()
