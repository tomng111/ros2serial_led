import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import serial

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        arduinoCmd = serial.Serial('/dev/ttyACM0',9600)
        self.subscription = self.create_subscription(
            String,
            'led_cmd',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        # Welcome
        self.get_logger().info("Welcome to the serial node command!")
        # Command
        while True:
            myCmd = input('Enter the command (e-ON: a-OFF): ')
            myCmd = myCmd + '\r'
            arduinoCmd.write(myCmd.encode())

    def listener_callback(self, msg):
        self.get_logger().info(' ')

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
