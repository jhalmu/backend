import os
from pathlib import Path

import duckdb


def init_db():
    """Initialize DuckDB connection with proper configuration"""
    db_path = os.getenv("DUCKDB_PATH", "data/portfolio.db")

    # Ensure data directory exists
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    # Configure DuckDB connection
    conn = duckdb.connect(db_path)

    # Set cache size (default 1GB if not specified)
    cache_size = os.getenv("DUCKDB_CACHE_SIZE", "1GB")
    conn.execute(f"PRAGMA cache_size='{cache_size}'")

    # Enable memory mapping for better performance
    conn.execute("PRAGMA memory_map=true")

    # Set temp directory for better performance
    conn.execute(f"PRAGMA temp_directory='{Path(db_path).parent}/temp'")

    # Enable parallel processing
    conn.execute("PRAGMA threads=4")

    return conn


def get_db():
    """Get DuckDB connection with proper configuration"""
    return init_db()
