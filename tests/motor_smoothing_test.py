"""
Test smooth motor response across offsets
"""

from navigation.motor_control import navigate

def test_motor_smoothing():
    print("[Test] Motor smoothing test")
    for offset in [-1.0, -0.5, 0, 0.5, 1.0]:
        navigate(offset)

if __name__ == "__main__":
    test_motor_smoothing()
