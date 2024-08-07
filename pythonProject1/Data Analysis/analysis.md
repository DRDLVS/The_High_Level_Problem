## Análisis de Datos

### Información Básica del DataFrame

El DataFrame ha sido cargado correctamente y contiene las siguientes columnas:

- `row`, `_id`, `_uuid`, `_position`, `_address`
- `Year`, `resident_type`, `place_of_residence`, `country`, `state`, `county`
- `Total Returns`, `Total AGI (Thousands)`, `Total Tax Liability (Thousands)`
- `Taxable Returns`, `Taxable AGI (Thousands)`, `Taxable Tax Liability (Thousands)`
- `Non-Taxable Returns`, `Non-Taxable AGI (Thousands)`
- `Average AGI (All Returns)`, `Average Tax (All Returns)`
- `Average AGI (Taxable Returns)`, `Average Tax (Taxable Returns)`
- `Average AGI (Non-Taxable Returns)`, `county_sort_order`

Los tipos de datos en el DataFrame son principalmente enteros (`int64`) y objetos (`object`) para las columnas categóricas.

### Estadísticas Descriptivas

Las estadísticas descriptivas para las columnas numéricas son las siguientes:

| Column                                | Count | Mean       | Std Dev   | Min       | 25th %    | Median    | 75th %    | Max        |
|---------------------------------------|-------|------------|-----------|-----------|-----------|-----------|-----------|------------|
| `Total AGI (Thousands)`               | 1830  | 1,955.17   | 546,514.1 | -188,756  | 8,056.25  | 9,866.00  | 153,650.8 | 9,855,074  |
| `Taxable AGI (Thousands)`             | 1830  | 1,955.17   | 546,514.1 | -188,756  | 8,056.25  | 9,866.00  | 153,650.8 | 9,855,074  |
| `Non-Taxable AGI (Thousands)`         | 1830  | 1,955.17   | 546,514.1 | -188,756  | 8,056.25  | 9,866.00  | 153,650.8 | 9,855,074  |

### Datos Faltantes

No se encontraron datos faltantes en el DataFrame, lo que indica que el conjunto de datos está completo.

### Distribución de los Años Fiscales

El histograma de los años fiscales muestra que la frecuencia de registros aumenta con los años. Esto sugiere que hay más entradas de datos en los años fiscales más recientes. Podría ser indicativo de un mayor número de registros o una expansión en la cobertura de datos en los últimos años.

### Matriz de Correlación

La matriz de correlación revela las siguientes observaciones clave:

- **Alta Correlación (0.88)**: `Taxable AGI (Thousands)` y `Non-Taxable AGI (Thousands)` tienen una alta correlación de **0.88**, lo que indica una fuerte relación positiva. Esto sugiere que a medida que el AGI imponible aumenta, también tiende a aumentar el AGI no imponible, lo que podría reflejar un patrón general en los datos fiscales.

- **Baja Correlación (0.02)**: Correlaciones cercanas a **0** indican relaciones débiles o nulas. Por ejemplo, una correlación de **0.02** sugiere que no hay una relación lineal significativa entre esas variables.


