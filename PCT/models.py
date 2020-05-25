from django.db import models
import uuid 

# Create your models here.


class Volunteer(models.Model):
	v_id = models.UUIDField( 
      	 unique = True,
      	 null = False,
         default = uuid.uuid4, 
         editable = True) 
	v_name = models.CharField(max_length=50,unique=False,null=False)
	v_address = models.CharField(max_length=400,unique=False,null=False)
	v_mob = models.CharField(max_length=10,unique=True,null=False)
	join_date = models.DateField(auto_now_add=True)
	v_image = models.ImageField(default="default.jpg")

	def __str__(self):
		return(f'{self.v_id}')

class Lab1(models.Model):
	v_id = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
	lastvisit_date = models.DateField(auto_now_add=True)
	visit_no = models.IntegerField(default=0)

	@property
	def v_name(self):
		return self.v_id.v_name

	def __str__(self):
		return(f'{self.v_id}')


class Lab2(models.Model):
	v_id = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
	lastvisit_date = models.DateField(auto_now_add=True)
	visit_no = models.IntegerField(default=0)

	@property
	def v_name(self):
		return self.v_id.v_name

	def __str__(self):
		return(f'{self.v_id}')


class Lab3(models.Model):
	v_id = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
	lastvisit_date = models.DateField(auto_now_add=True)
	visit_no = models.IntegerField(default=0)

	@property
	def v_name(self):
		return self.v_id.v_name

	def __str__(self):
		return(f'{self.v_id}')



class Lab4(models.Model):
	v_id = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
	lastvisit_date = models.DateField(auto_now_add=True)
	visit_no = models.IntegerField(default=0)

	@property
	def v_name(self):
		return self.v_id.v_name

	def __str__(self):
		return(f'{self.v_id}')

class Visited_data(models.Model):
	v_id = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
	visit_date = models.DateField(auto_now_add=True)
	entry_time = models.TimeField(auto_now_add=True)
	going_time = models.TimeField()
	lab_no =models.IntegerField()
	reason = models.CharField(max_length=200)
	last_visit  = models.BooleanField(default=False)
	lab_tech_id = models.CharField(max_length=100,unique=False,default="")

	@property
	def v_name(self):
		return self.v_id.v_name

	def __str__(self):
		return(f'{self.v_id}')



