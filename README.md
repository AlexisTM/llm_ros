LLM ROS 2 interface
==================

This package is providing an interface to simplify access to LLMs for ROS 2. The initial implementation is to use a local Ollama instance. See [this page](https://ollama.com/) to install your own Ollama instance.

Quick start
--------------

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh
# Add a network
ollama pull llama3.2

# Build this package
mkdir -p ws && cd ws
git clone https://github.com/AlexisTM/llm_ros
colcon build

# Run the node
ros2 run llm_ros ollama_node
ros2 service call /llm/prompt llm_msgs/srv/Prompt '{network: "llama3.2", prompt: "Are LLMs useful in robotics?"}'
```

Remote server
-------------

If you use a remote instance, you will need to enable the server
to listen to the network. Add the following to the `.bashrc` and restart Ollama:

```bash
export OLLAMA_HOST=0.0.0.0:11434`
```

And run the node with:

```bash
ros2 run llm_ros ollama_node --ros-args -p ip_address:=ollama_ip
```
