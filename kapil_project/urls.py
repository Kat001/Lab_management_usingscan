
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('PCT.urls'))

]


'''
if k == 5:
					a = "170303105052"
					a = a.encode("utf-8")
					flag = False
					print("Attendence marked succwssfully")
					cap.release()
					cv2.destroyAllWindows()
					s.close()
				else:
					cap.release()
					cv2.destroyAllWindows()
					s.close()
			cv2.imshow("frame", frame)
			if cv2.waitKey(1) & 0xFF == ord("q"):
				break
		cap.release()
		cv2.destroyAllWindows()
'''