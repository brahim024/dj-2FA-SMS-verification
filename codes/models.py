from django.db import models
from users.models import CustomUser 
# Create your models here.
class Code(models.Model):
	number= models.CharField(max_length=5)
	user =models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.number)

	def save(self.*args,**kwargs):
		number_list=[x for x in range(10)]
		code_item=[]

		for i in range(5):
			num=random.choice(number_list)
			code_item.append(num)

		code_str="".join(srt(item)for item in code_item)
		self.number=code_str
		super().save(*args,**kwargs)
