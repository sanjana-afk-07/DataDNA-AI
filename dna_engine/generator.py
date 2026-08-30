from .fingerprint import generate_fingerprint
from .statistics import calculate_statistics
from .quality import analyze_quality
from .anomalies import detect_anomalies
from .patterns import discover_patterns


def generate_datadna(file_path):
    """Generate a complete DataDNA report."""

    dna = {
        "fingerprint": generate_fingerprint(file_path),
        "statistics": calculate_statistics(file_path),
        "quality": analyze_quality(file_path),
        "anomalies": detect_anomalies(file_path),
        "patterns": discover_patterns(file_path)
    }

    return dna
