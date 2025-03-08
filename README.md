# Instrucciones de configuración del Repositorio

Este repositorio contiene Notebooks en Jupyter para analizar, limpiar y visualizar datos de candidatos a partir del archivo `Candidates.csv`. Sigue los pasos descritos a continuación para configurar correctamente el entorno de trabajo.

## 1. Clonar el repositorio

Abre una terminal y ejecuta el siguiente comando:

```bash
gh repo clone NicolasCuaran/NicolasCuaran-Work_Shop-1
```

Reemplaza `<url-del-repositorio>` con la dirección URL proporcionada del repositorio en GitHub.

## 2. Preparar archivos esenciales

### Archivo de datos

Debes contar con el archivo `Candidates.csv` ubicado en la carpeta raíz del proyecto.

### Archivo `.env`

Crea un archivo llamado `.env` en la raíz del proyecto con el siguiente formato:

```env
PG_USER=usuario
PG_PASSWORD=contraseña
PG_HOST=host
PG_PORT=puerto
PG_DATABASE=nombre_base_de_datos
```

Reemplaza los valores con las credenciales específicas de tu base de datos PostgreSQL.

## 3. Configuración del entorno Python

Asegúrate de tener instalado Python en tu sistema. Luego, configura un entorno virtual ejecutando:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Esto instalará las dependencias necesarias especificadas en `requirements.txt`.

## 4. Ejecución de los Notebooks

Abre Jupyter Notebook ejecutando:

```bash
jupyter notebook
```

Luego sigue el orden detallado a continuación:

1. **000_TraslateScript.ipynb**: Ejecuta este notebook paso a paso como está descrito en el archivo. Este script es esencial para preparar los datos para los análisis posteriores.

2. **001_EDA_Candidates.ipynb**: Realiza el análisis exploratorio de datos para entender mejor las características y estructura de la información.

3. **002_HiredCandidates.ipynb**: Finalmente, ejecuta este notebook para limpiar los datos y crear la tabla `HiredCandidates` en la base de datos con la información procesada y lista para visualizaciones.

## 5. Visualización de resultados

Una vez generada la tabla en tu base de datos, puedes usar herramientas de visualización como **Power BI** para crear dashboards interactivos y obtener insights claros de los datos procesados.

