# Central configuration file for HydroBot

# =====================
# Motor Configuration
# =====================
BASE_SPEED = 50          # Nominal motor speed
MAX_SPEED = 80           # Maximum motor speed
STEERING_GAIN = 0.6      # Steering sensitivity factor

# =====================
# Vision Configuration
# =====================
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
CONFIDENCE_THRESHOLD = 0.5

# =====================
# Ultrasonic Sensor
# =====================
OBSTACLE_DISTANCE_CM = 40

# =====================
# Power Management
# =====================
LOW_BATTERY_THRESHOLD = 11.2  # volts
CRITICAL_BATTERY_THRESHOLD = 10.5

# =====================
# IoT Configuration
# =====================
IOT_ENDPOINT = "http://example-iot-endpoint"
DEVICE_ID = "HYDROBOT_01"
