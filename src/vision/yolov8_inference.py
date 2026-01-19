"""
YOLOv8 inference wrapper (reference implementation)
"""

import random
from config import CONFIDENCE_THRESHOLD

def detect_waste():
    """
    Simulated YOLOv8 detection result.
    Replace this logic with real model inference.
    """

    detected = random.choice([True, False])

    if detected:
        return {
            "found": True,
            "confidence": round(random.uniform(0.6, 0.9), 2),
            "offset": random.uniform(-1.0, 1.0),  # -1 left, +1 right
            "label": "plastic"
        }

    return {"found": False}
