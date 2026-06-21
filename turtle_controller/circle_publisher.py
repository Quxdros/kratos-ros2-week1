import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CirclePublisher(Node):

    def __init__(self):
        super().__init__('circle_publisher')

        self.publisher_ = self.create_publisher(
    Twist,
    '/turtle1/cmd_vel',
    10)

        self.timer = self.create_timer(
            0.1,
            self.timer_callback)

    def timer_callback(self):

        msg = Twist()

        msg.linear.x = 0.2
        msg.angular.z = 0.5

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Publishing: linear={msg.linear.x}, angular={msg.angular.z}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = CirclePublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
