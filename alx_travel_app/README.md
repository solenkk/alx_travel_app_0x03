ALX Travel App 0x03 – Background Task Management with Celery and Email Notifications
This project demonstrates how to use Celery with RabbitMQ to handle background tasks in Django.
The feature implemented here is sending a booking confirmation email asynchronously.

🚀 Setup Instructions
1. Install Dependencies
pip install celery
sudo apt-get install rabbitmq-server

# **Chapa Payment Integration — ALX Travel App**

## **Overview**

This project integrates **[Chapa API](https://developer.chapa.co/)** for secure payment processing in the Django travel booking system.
Users can initiate payments for their bookings, complete transactions via Chapa, and have the payment status verified automatically.

---

## **Setup Instructions**

### 1️⃣ **Clone the Project**

```bash
git clone https://github.com/<your-username>/alx_travel_app_0x02.git
cd alx_travel_app_0x02
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Environment Variables
Create a .env file in the project root:

SECRET_KEY=your_django_secret_key
DEBUG=True
CHAPA_SECRET_KEY=your_chapa_secret_key
4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate
Payment Workflow
1. Initiate Payment
Endpoint:

POST /payments/initiate/
Request Body:

{
    "booking_reference": "BK001",
    "amount": "100.00",
    "email": "customer@example.com"
}
Response Example:

{
    "checkout_url": "https://checkout.chapa.co/..."
}
Redirect the user to checkout_url to complete payment.

2. Verify Payment
Endpoint:

GET /payments/verify/<transaction_id>/
Response Example:

{
    "status": "Completed"
}
Testing with Chapa Sandbox
Sign up for a Chapa account and enable sandbox mode.
Use the sandbox API keys in .env.
Make a payment with test card details from Chapa docs.
Verify the transaction status via the /verify/ endpoint.
Model Reference
Payment model stores:

booking_reference
transaction_id
amount
status (Pending, Completed, Failed)
created_at
updated_at
Additional Features
Email notification on successful payment (via Celery).
Error handling for failed payments.
Secure environment-based API key storage.
