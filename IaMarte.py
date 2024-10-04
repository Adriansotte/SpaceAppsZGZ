import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo CSV con los datos escalados
data_file = './output/detection_catalog_scaled_mars.csv'  # Cambia esta ruta según sea necesario
data = pd.read_csv(data_file)

# Eliminar la columna 'time_abs(%Y-%m-%dT%H:%M:%S.%f)' ya que es un valor de fecha y no se puede usar directamente
X = data.drop(columns=['is_sismo_start', 'time_abs(%Y-%m-%dT%H:%M:%S.%f)'])

# La etiqueta objetivo es 'is_sismo_start'
y = data['is_sismo_start']

# Dividir los datos en conjuntos de entrenamiento y prueba (70% entrenamiento, 30% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inicializar el modelo RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Mostrar un reporte de clasificación
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()
