from django.db import models


# Create your models here.
class Theatre(models.Model):
    city_choice=(
        ('DELHI', 'Delhi'),
        ('KOLKATA', 'Kolkata'),
        ('MUMBAI', 'Mumbai'),
        ('CHENNAI', 'Chennai'),
        ('BANGALORE', 'Bangalore'),
        ('HYDERABAD', 'Hyderabad'),
    )
    name = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=9, choices=city_choice, null=False)
    address = models.CharField(max_length=30)
    no_of_screen = models.IntegerField()

    def __str__(self):
        return self.name+"-"+self.address+"-"+self.city


class Screen(models.Model) :
    name = models.CharField(max_length=20)
    theatre = models.ForeignKey(Theatre, related_name="screen",
                                on_delete=models.CASCADE)

    def __str__(self) :
        return "{x} {y}".format(x=self.name, y=self.theatre.name)


class Show(models.Model) :
    date = models.DateField()
    time = models.TimeField()
    screen = models.ForeignKey(Screen, related_name="show_screen",
                               on_delete=models.CASCADE)
    theatre = models.ForeignKey(Screen, related_name="show_theatre",
                                on_delete=models.CASCADE)
    movie = models.ForeignKey(Screen, related_name="show_movie",
                              on_delete=models.CASCADE)

    def __str__(self) :
        return "Date : {}".format(self.date)


class Seat(models.Model):
    seat_choice = (
        ('', 'Select'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
    )
    no = models.CharField(max_length=3, null=True, blank=False)
    seat_type = models.CharField(max_length=8, choices=seat_choice, blank=False)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return self.no + str(self.show)
