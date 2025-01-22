import unittest
import os
from unittest.mock import patch, mock_open
from io import StringIO
from logging import getLogger, FileHandler

# Les fonctions à tester (copiées ou importées)
def log_error(message):
    import logging
    logging.basicConfig(
        filename="error.log",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.error(message)

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        error_message = f"Erreur : le fichier '{filename}' n'a pas été trouvé."
        log_error(error_message)
        raise
    finally:
        print("Bloc finally exécuté, que l'erreur se produise ou non.")

class TestFileOperations(unittest.TestCase):

    def setUp(self):
        """Préparation avant chaque test."""
    import logging
    logging.shutdown()  # Libère les ressources utilisées par logging
    if os.path.exists("error.log"):
        os.remove("error.log")



    def test_read_file_file_not_found(self):
        """Test que FileNotFoundError est levé et journalisé lorsque le fichier est introuvable."""
        filename = "fichier_inexistant.txt"
        with self.assertRaises(FileNotFoundError):
            read_file(filename)
        
        # Vérifie que le message est journalisé dans error.log
        self.assertTrue(os.path.exists("error.log"))
        with open("error.log", "r") as log_file:
            log_content = log_file.read()
            self.assertIn(f"Erreur : le fichier '{filename}' n'a pas été trouvé.", log_content)

    @patch("builtins.open", new_callable=mock_open, read_data="contenu de test")
    def test_read_file_success(self, mock_file):
        """Test que le fichier est lu correctement lorsque le fichier existe."""
        filename = "fichier_existant.txt"
        content = read_file(filename)
        self.assertEqual(content, "contenu de test")
        mock_file.assert_called_once_with(filename, "r")

    def tearDown(self):
        """Nettoyage après chaque test."""
    import logging
    logging.shutdown()  # Libère les ressources utilisées par logging
    if os.path.exists("error.log"):
        os.remove("error.log")

# Point d'entrée pour exécuter les tests
if __name__ == "__main__":
    import sys
    unittest.main(argv=['first-arg-is-ignored'], exit=False)