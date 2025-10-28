from utils.printer import print_message
def saludo(name: str):
    """Genera un saludo simple."""
    message = f"BUenos dias, {name}. Espero que tengas un excelente dia."
    print_message(message)
    
def greeting(name: str):
    """Genera un salido simple en ingles."""
    message = f"Hello, {name}!"
    print_message(message)