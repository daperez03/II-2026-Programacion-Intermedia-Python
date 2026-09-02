import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Clase Estudiante
# Representa a un estudiante y almacena sus datos.
# ============================================================
class Estudiante:
    def __init__(
        self,
        nombre: str,
        edad: int,
        estatura: float,
        horas_estudio: int,
        calificacion: float
    ):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.horas_estudio = horas_estudio
        self.calificacion = calificacion

    def mostrar_datos(self):
        """Muestra en pantalla los datos del estudiante."""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Estatura: {self.estatura}")
        print(f"Horas de estudio: {self.horas_estudio}")
        print(f"Calificación: {self.calificacion}")


# ============================================================
# Crear una lista para almacenar los estudiantes
# ============================================================
estudiantes = []


# ============================================================
# Solicitar los datos de 5 estudiantes
# ============================================================
for i in range(5):
    print(f"\n--- Estudiante {i + 1} ---")

    estudiante = Estudiante(
        input("Nombre: "),
        int(input("Edad: ")),
        float(input("Estatura: ")),
        int(input("Horas de estudio: ")),
        float(input("Calificación: "))
    )

    estudiantes.append(estudiante)


# ============================================================
# Convertir los objetos Estudiante en un DataFrame
# ============================================================

# __dict__ permite obtener los atributos del objeto
# como un diccionario.
datos = []

for estudiante in estudiantes:
    datos.append(estudiante.__dict__)

df = pd.DataFrame(datos)


# ============================================================
# Mostrar los datos registrados
# ============================================================
print("\n========== DATOS DE LOS ESTUDIANTES ==========")
print(df)


# ============================================================
# Calcular el promedio de las variables numéricas
# ============================================================
print("\n========== PROMEDIOS ==========")
print(df.mean(numeric_only=True))


# ============================================================
# Encontrar el estudiante con la calificación más alta
# ============================================================
indice = df["calificacion"].idxmax()

print("\n========== MEJOR CALIFICACIÓN ==========")
print(f"Calificación máxima: {df['calificacion'].max()}")
print("Datos del estudiante:")
print(df.loc[indice])


# ============================================================
# Encontrar el estudiante con la calificación más baja
# ============================================================
indice = df["calificacion"].idxmin()

print("\n========== MENOR CALIFICACIÓN ==========")
print(f"Calificación mínima: {df['calificacion'].min()}")
print("Datos del estudiante:")
print(df.loc[indice])


# ============================================================
# Analizar la correlación entre las variables numéricas
# ============================================================
print("\n========== MATRIZ DE CORRELACIÓN ==========")
print(df.corr(numeric_only=True))


# ============================================================
# Crear un gráfico de dispersión
# Relaciona las horas de estudio con la calificación.
# ============================================================
df.plot(
    kind="scatter",
    x="horas_estudio",
    y="calificacion"
)
plt.show()