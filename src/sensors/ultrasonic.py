"""
Ultrasonic obstacle detection (mock)
"""

import random
from config import OBSTACLE_DISTANCE_CM

def obstacle_detected():
    """
    Simulate ultrasonic distance reading
    """
    distance = random.randint(20, 100)
    return distance < OBSTACLE_DISTANCE_CM
