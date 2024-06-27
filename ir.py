import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BCM)
    
    IR_IN1 = 5  # Pin connected to the OUT pin of the first HW-201 sensor
    IR_IN2 = 6  # Pin connected to the OUT pin of the second HW-201 sensor
    GPIO.setup(IR_IN1, GPIO.IN)
    GPIO.setup(IR_IN2, GPIO.IN)
    
    try:
        while True:
            sensor1_state = GPIO.input(IR_IN1)
            sensor2_state = GPIO.input(IR_IN2)
            
            if not sensor1_state:
                print("Sensor 1: Obstacle detected")
            else:
                print("Sensor 1: No obstacle")
                
            if not sensor2_state:
                print("Sensor 2: Obstacle detected")
            else:
                print("Sensor 2: No obstacle")
                
            time.sleep(1)  # Short delay to make the loop responsive
    except KeyboardInterrupt:
        print("Program terminated")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
