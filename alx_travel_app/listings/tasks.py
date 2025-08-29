from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@shared_task
def send_booking_confirmation_email(booking_id, user_email, user_name, listing_title, booking_date):
    """
    Send booking confirmation email asynchronously
    """
    try:
        subject = 'Booking Confirmation - ALX Travel App'
        
        # HTML email content
        html_message = render_to_string('email/booking_confirmation.html', {
            'user_name': user_name,
            'listing_title': listing_title,
            'booking_date': booking_date,
            'booking_id': booking_id,
        })
        
        # Plain text version
        plain_message = strip_tags(html_message)
        
        # Send email
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user_email],
            html_message=html_message,
            fail_silently=False,
        )
        
        return f"Email sent successfully to {user_email}"
        
    except Exception as e:
        return f"Failed to send email: {str(e)}"