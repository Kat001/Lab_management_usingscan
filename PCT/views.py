from django.shortcuts import render,redirect
import cv2
from pyzbar import pyzbar
from .models import *
# Create your views here.

def index(request):
	print("hiii")
	return render(request,'PCT_templates/index.html')


def scan(request):
	flag = True
	try:
		cap = cv2.VideoCapture(0)
		while flag:
			koi, frame = cap.read()

			obj_data = pyzbar.decode(frame)
			for obj in obj_data:
				pct_id = obj.data
				pct_id = pct_id.decode('utf')

				flag = False
			cv2.imshow("frame", frame)
			if cv2.waitKey(1) & 0xFF == ord("q"):
				break
		cap.release()
		cv2.destroyAllWindows()
	except Exception as e:
		print("Gadabad....")

	

	try:
		v_obj = Volunteer.objects.get(v_id=pct_id)
		
		d = {
		'obj': v_obj,
		'v_id' : pct_id,
	}
	except Exception as e:
		print("data nit matched")
		return redirect('index')
		
	
	
	return render(request,'PCT_templates/scan.html',d)

def add_record(request,v_iid):
	tech_name = request.user.username
	lab_id  = 4
	obj = Volunteer.objects.get(v_id=v_iid)
	d = {
		'tech_name' : tech_name,
		'lab_id' : lab_id,
		'obj' : obj,
	}
	return render(request,'PCT_templates/add_record.html',d)



def update(request):
	lab_id  = request.POST.get('lab_id')
	v_id  = request.POST.get('pcd_id')
	reason = request.POST.get('reason')
	lab_tech_id = request.POST.get('id1')
	time = request.POST.get('time')

	v_id = Volunteer.objects.get(v_id=v_id)
	obj = Visited_data(v_id=v_id,lab_no = lab_id,reason=reason,
		 going_time="15:25",lab_tech_id=lab_tech_id)

	obj.save()
	return render(request,'PCT_templates/update.html')



def cheak_record(request,v_iid):
	v_id = Volunteer.objects.get(v_id=v_iid)
	obj = Visited_data.objects.filter(v_id=v_id)
	
	l1_obj = obj.filter(lab_no=1)
	l2_obj = obj.filter(lab_no=2)
	l3_obj = obj.filter(lab_no=3)
	l4_obj = obj.filter(lab_no=4) 
	
	d = {
		'idd' : v_iid,
		'l1_obj' : l1_obj,
		'l2_obj' : l2_obj,
		'l3_obj' : l3_obj,
		'l4_obj' : l4_obj,
	}

	return render(request,'PCT_templates/cheak_record.html',d)


	


