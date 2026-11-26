class Vehiculo:
    def __init__(self, matricula: str, modelo: str, nivel_bateria: float = 100.0, kilometros_totales: float = 0.0):
        self.matricula = matricula
        self.modelo = modelo
        # 1. Atributos protegidos con guion bajo
        self._nivel_bateria = 100.0
        self._kilometros_totales = 0.0
        
        # Usamos los setters para aplicar las validaciones iniciales
        self.nivel_bateria = nivel_bateria
        self.kilometros_totales = kilometros_totales

    # --- Getter y Setter para nivel_bateria ---
    @property
    def nivel_bateria(self) -> float:
        """Getter: Devuelve el porcentaje de batería actual."""
        return self._nivel_bateria

    @nivel_bateria.setter
    def nivel_bateria(self, nuevo_nivel: float) -> None:
        """Setter: Valida que el nivel se encuentre siempre en el rango [0.0, 100.0]."""
        if nuevo_nivel < 0.0 or nuevo_nivel > 100.0:
            raise ValueError(f"Nivel de batería inválido: {nuevo_nivel}%. Debe estar entre 0 y 100.")
        self._nivel_bateria = nuevo_nivel

    # --- Reto Autónomo: Getter y Setter para kilometros_totales ---
    @property
    def kilometros_totales(self) -> float:
        """Getter: Devuelve los kilómetros acumulados del vehículo."""
        return self._kilometros_totales

    @kilometros_totales.setter
    def kilometros_totales(self, nuevos_km: float) -> None:
        """Setter: Valida que los kilómetros no disminuyan (fraude de odómetro)."""
        if nuevos_km < self._kilometros_totales:
            raise ValueError("Los kilómetros no pueden disminuir (fraude de odómetro).")
        self._kilometros_totales = nuevos_km

    # --- Método actualizar para usar atributos protegidos/propiedades ---
    def conducir(self, km: float) -> None:
        """Simula la conducción consumiendo batería y sumando kilómetros."""
        if km <= 0:
            raise ValueError("Los kilómetros a recorrer deben ser positivos.")
        
        # Ejemplo simple de consumo (1% de batería por cada 5 km, por ejemplo)
        consumo = km * 0.2 
        nuevo_nivel = self._nivel_bateria - consumo
        
        # Actualizamos usando las propiedades para mantener las validaciones
        self.nivel_bateria = max(0.0, nuevo_nivel)
        self.kilometros_totales = self._kilometros_totales + km