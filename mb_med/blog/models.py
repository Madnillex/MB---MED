from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=160, verbose_name='Kurs nomi')
    image = models.ImageField(verbose_name='Kurs rasmi', upload_to=f'courses/')

    def get_photo(self):
        return self.image.url

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'


class Teachers(models.Model):
    name = models.CharField(max_length=150, verbose_name='Ism')
    lastname = models.CharField(max_length=150, verbose_name='Familiya')
    year = models.IntegerField(default=3, verbose_name='Mutaxasisilik yili')
    phone = models.CharField(max_length=15, verbose_name='Telefon raqami')
    gmail = models.EmailField(blank=True, null=True, verbose_name='Email')
    instagram = models.URLField(blank=True, null=True, verbose_name='Instagram')
    facebook = models.URLField(blank=True, null=True, verbose_name='Facebook')
    telegram = models.URLField(blank=True, null=True, verbose_name='Telegram')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='teachers/', null=True, blank=True)

    def get_photo(self):
        if self.image:
            return self.image.url
        else:
            return 'https://www.qptech.ie/wp-content/uploads/tn_Profile-Picture.png'

    def __str__(self):
        return f"{self.name} {self.lastname}"

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"
