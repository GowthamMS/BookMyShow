from django.db import models
from Users.models import Users
from Theaters.models import Seat


# Create your models here.
class Booking(models.Model):
    payment_choice = (
        ('Credit Card', 'Credit Card'),
    )
    id = models.CharField(primary_key=True, max_length=200)
    timestamp = models.DateTimeField('%Y-%m-%d %H:%M:%S', null=True,
                                     blank=True)
    payment_type = models.CharField(max_length=11, choices=payment_choice,
                                    default='Credit Card')
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2,
                                      null=True, blank=True)
    paid_by = models.ForeignKey(Users, on_delete=models.DO_NOTHING,
                                null=True, blank=True)

    def __str__(self):
        return str(self.id)


class BookedSeat(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('seat', 'booking')

    def __str__(self):
        return str(self.seat) + '|' + str(self.booking)
