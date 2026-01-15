import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class ai(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(String,'VCU2AI',self.listener_callback,10)
        self.publisher = self.create_publisher(String,'AI2VCU',10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.publisher.publish(msg)
        self.get_logger().info('Responding: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = ai()

    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()