graph TD
    classDef largeFont font-size:20px;
    classDef largeTitle font-size:20px;

    %% Aumentar tamaño de los títulos de los subgráficos
    subgraph dataIngestionLayer["Data Ingestion Layer"]
        A1["Annual Tax Returns - XML API"]:::largeFont
        A2["Credit Card Transaction History - JSON API and PostgreSQL"]:::largeFont
        A3["Bank Statements - XML API and S3 Bucket"]:::largeFont
    end
    class dataIngestionLayer largeTitle;

    subgraph dataStorageLayer["Data Storage Layer"]
        B1["S3 Bucket"]:::largeFont
        B2["Redshift"]:::largeFont
    end
    class dataStorageLayer largeTitle;

    subgraph dataProcessingLayer["Data Processing Layer"]
        C1["ETL/ELT Pipelines - Python"]:::largeFont
        C2["Batch Processing"]:::largeFont
        C3["Data Cleaning and Transformation"]:::largeFont
    end
    class dataProcessingLayer largeTitle;

    subgraph dataAccessLayer["Data Access Layer"]
        D1["Power BI"]:::largeFont
        D2["Tableau"]:::largeFont
    end
    class dataAccessLayer largeTitle;

    subgraph dataAnalysisLayer["Data Analysis Layer"]
        E1["Python (Pandas, NumPy, Matplotlib, Seaborn)"]:::largeFont
        E2["SQL Queries"]:::largeFont
        E3["Machine Learning Models"]:::largeFont
    end
    class dataAnalysisLayer largeTitle;

    A1 --> B1
    A2 --> B2
    A3 --> B1
    B1 --> C1
    B2 --> C2
    C1 --> D1
    C2 --> D2
    D1 --> E1
    D2 --> E2
    E1 --> E3
    E2 --> E3