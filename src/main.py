"""
Main control loop for HydroBot
"""

from vision.yolov8_inference import detect_waste
from navigation.motor_control import navigate
from collection.intake_control import collect_waste
from sensors.ultrasonic import obstacle_detected
from iot.data_publisher import publish_data

def main():
    print("[HydroBot] System booting...")

    while True:
        if obstacle_detected():
            print("[HydroBot] Obstacle detected. Stopping.")
            navigate(0)
            continue

        detection = detect_waste()

        if detection["found"]:
            print("[HydroBot] Waste detected. Navigating.")
            navigate(detection["offset"])
            collect_waste()
            publish_data(detection)
        else:
            print("[HydroBot] Patrol mode.")
            navigate(0)

if __name__ == "__main__":
    main()
