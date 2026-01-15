import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'VCU2AI', 10)
        self.subscription = self.create_subscription(String,'AI2VCU',self.listener_callback,10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = self.a = 0
        self.subscription #prevent unused variable error

    def timer_callback(self):
        msg = String()
        msg.data = '%d' % self.i
        self.publisher_.publish(msg)
        if(self.a<5):
            self.get_logger().info('Checking... "%s"' % msg.data)
        else:
            self.get_logger().info('FAILSAFE, Autonomous software is dead!! "%s"' %msg.data)
        self.i += 1
        self.a += 1
    
    def listener_callback(self, msg):
        self.a = 0
        self.get_logger().info('Autonomous software is alive: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()