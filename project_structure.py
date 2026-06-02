from pathlib import Path

# Root project folder
root = Path("bluestock_mf_capstone")

# List of directories to create
directories = [
    root / "data" / "raw",
    root / "data" / "processed",
    root / "data" / "db",

    root / "notebooks",

    root / "scripts",

    root / "sql",

    root / "dashboard",

    root / "reports",
]

# Create directories
for directory in directories:
    directory.mkdir(parents=True, exist_ok=True)

# Create empty files
files = [
    root / "README.md",

    root / "notebooks" / "01_data_ingestion.ipynb",
    root / "notebooks" / "02_data_cleaning.ipynb",
    root / "notebooks" / "03_eda_analysis.ipynb",
    root / "notebooks" / "04_performance_analytics.ipynb",
    root / "notebooks" / "05_advanced_analytics.ipynb",

    root / "scripts" / "etl_pipeline.py",
    root / "scripts" / "live_nav_fetch.py",
    root / "scripts" / "compute_metrics.py",
    root / "scripts" / "recommender.py",

    root / "sql" / "schema.sql",
    root / "sql" / "queries.sql",

    root / "dashboard" / "bluestock_mf.pbix",

    root / "reports" / "Final_Report.pdf",
    root / "reports" / "Presentation.pptx",
]

for file in files:
    file.touch(exist_ok=True)

print(f"\nProject structure created successfully at: {root.resolve()}")