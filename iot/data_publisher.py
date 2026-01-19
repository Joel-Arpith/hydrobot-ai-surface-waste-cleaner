"""
IoT data publishing module
"""

import time
from config import DEVICE_ID

def publish_data(detection):
    payload = {
        "device_id": DEVICE_ID,
        "waste_type": detection.get("label", "unknown"),
        "confidence": detection.get("confidence", 0),
        "timestamp": time.time()
    }

    print(f"[IoT] Publishing data: {payload}")
