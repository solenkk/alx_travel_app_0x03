## Celery Background Tasks with RabbitMQ

### Setup Instructions

1. **Install RabbitMQ**:

   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install rabbitmq-server
   sudo systemctl enable rabbitmq-server
   sudo systemctl start rabbitmq-server

   # macOS
   brew install rabbitmq
   brew services start rabbitmq
   ```
