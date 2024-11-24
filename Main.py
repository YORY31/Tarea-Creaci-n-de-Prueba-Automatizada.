import os
import pytest

def run_tests():

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    if not os.path.exists("reports"):
        os.makedirs("reports")

    
    pytest.main([
        "test",  
        "--html=reports/report.html",  
        "--self-contained-html"
    ])

if __name__ == "__main__":
    print("Iniciando pruebas automatizadas...")
    run_tests()
    print("Pruebas completadas. Revisa el reporte en 'reports/report.html'.")
