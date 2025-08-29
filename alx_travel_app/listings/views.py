from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from .tasks import send_booking_confirmation_email  # Import the task

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save the booking
        booking = serializer.save()
        
        # Trigger email task asynchronously
        send_booking_confirmation_email.delay(
            booking_id=booking.id,
            user_email=booking.user.email,  # Adjust based on your model
            user_name=f"{booking.user.first_name} {booking.user.last_name}",  # Adjust based on your model
            listing_title=booking.listing.title,  # Adjust based on your model
            booking_date=booking.created_at.strftime('%Y-%m-%d %H:%M:%S')
        )
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)