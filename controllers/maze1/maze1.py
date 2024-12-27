from controller import Robot

def run_robot(robot):

    # Time step for the control loop......................................................
    time_step = int(robot.getBasicTimeStep())
    max_speed = 6.28

    # Get the motors for the wheels.......................................................
    left_motor = robot.getDevice('left wheel motor')  
    right_motor = robot.getDevice('right wheel motor')  

    left_motor.setPosition(float('inf'))  
    left_motor.setVelocity(0.0)
  
    right_motor.setPosition(float('inf')) 
    right_motor.setVelocity(0.0)

    # Get the proximity sensors............................................................
    proximity_sensors = []
    for ind in range(8):
        sensor_name = 'ps' + str(ind)
        proximity_sensors.append(robot.getDevice(sensor_name))
        proximity_sensors[ind].enable(time_step)  

    # Main control loop....................................................................
    while robot.step(time_step) != -1:
       
        for ind in range(8):
            print("ind: {}, val: {}".format(ind, proximity_sensors[ind].getValue()))
    
    #sensor reading values of 5,6,7 sensors................................................
        left_wall = proximity_sensors[5].getValue() > 80
        left_cornner=proximity_sensors[6].getValue() > 80
        front_wall = proximity_sensors[7].getValue() > 80
        
        # Default motor speeds.............................................................
        left_speed = max_speed
        right_speed = max_speed
        
        if front_wall:
            print("Turn right in place")
            left_speed = max_speed
            right_speed = -max_speed
        elif left_wall:
            print("Drive forward")
            left_speed = max_speed
            right_speed = max_speed
        else:
            print("Turn left")
            left_speed = max_speed / 8 
            right_speed = max_speed
        if left_cornner:
            print("come to close drive right")
            left_speed = max_speed
            right_speed = max_speed / 8
            
        # Set the speeds...................................................................
        left_motor.setVelocity(left_speed)        
        right_motor.setVelocity(right_speed) 

# Main execution...........................................................................
if __name__ == "__main__": 
    my_robot = Robot()
    run_robot(my_robot)
