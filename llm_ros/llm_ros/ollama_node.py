import ollama

import rclpy
from rclpy.node import Node

from llm_msgs.srv import Prompt, Prompt_Request, Prompt_Response


class LlmOllama(Node):
    def __init__(self):
        super().__init__("llm_ollama_interface")
        self.declare_parameter("ip_address", "127.0.0.1")
        ip_address = self.get_parameter("ip_address").get_parameter_value().string_value
        self.get_logger().info(
            f"Connecting to the ollama server at {ip_address}:11343 ..."
        )
        self._prompt_service = self.create_service(
            Prompt,
            "llm/prompt",
            self.service_handler,
        )
        self.client = ollama.Client(ip_address)
        # This call ensures we have a connection
        model_list = self.client.list()
        self.get_logger().info("... Connected.\nNetworks:")
        for model in model_list["models"]:
            self.get_logger().info(
                f"Model: {model['name']} Size: {model['details']['parameter_size']} Quantization level: {model['details']['quantization_level']}"
            )

    def service_handler(
        self, request: Prompt_Request, response: Prompt_Response
    ) -> Prompt_Response:
        ollama_resp = self.client.generate(request.network, request.prompt)
        print(ollama_resp)
        response.result = ollama_resp["response"]
        return response


def main(args=None):
    rclpy.init(args=args)
    ollama_service = LlmOllama()
    rclpy.spin(ollama_service)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
