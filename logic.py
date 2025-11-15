class CalculatorLogic:
    def __init__(self):
        self.expression = "" # La ecuación actual (ej: "5 + 5")
        self.result = ""     # El resultado final

    def press_key(self, key):
        """Maneja la lógica de qué pasa cuando se presiona una tecla"""
        
        if key == "=":
            try:
                # Evalúa la expresión matemática de forma segura
                # Reemplazamos 'x' por '*' para que Python entienda la multiplicación
                safe_expression = self.expression.replace('x', '*').replace('÷', '/')
                self.result = str(eval(safe_expression))
                self.expression = self.result # El resultado se vuelve la nueva base
            except Exception:
                self.result = "Error"
                self.expression = ""
        
        elif key == "C":
            # Limpiar todo
            self.expression = ""
            self.result = ""
            
        elif key == "←":
            # Borrar el último caracter
            self.expression = self.expression[:-1]
            
        else:
            # Añadir número u operador
            self.expression += str(key)

    def get_display_text(self):
        """Devuelve lo que se debe mostrar en pantalla"""
        if self.expression == "":
            return "0"
        return self.expression