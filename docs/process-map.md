# HydroBot Process Map

1. System powers on
2. Camera captures live video feed
3. YOLOv8 model performs inference
4. If no waste is detected → Patrol mode
5. If waste is detected:
   - Calculate target direction
   - Navigate toward waste
6. Intake mechanism activates when waste reaches pickup zone
7. Waste count is incremented
8. Sensor and status data is uploaded to IoT dashboard
9. Loop repeats until battery reaches safe threshold
