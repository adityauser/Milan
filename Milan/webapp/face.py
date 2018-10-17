from django.contrib import messages
from django.core.mail import send_mail


from webapp.models import Lost,Found


def return_id(img_url,list_num):

	try:
		import cognitive_face as CF
		KEY = 'd56e4adcb31944e6a9e6cd824048f1c5'  # Replace with a valid Subscription Key here.
		CF.Key.set(KEY)

		BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
		CF.BaseUrl.set(BASE_URL)

		id = CF.face_list.add_face(img_url,list_num)['persistedFaceId']
		return id

	except Exception as e:
		print("error")
		return("None")

def find_similar(list_num,img_url = 'http://www.uniquefbcovers.com/download/cute_stylish_child_girl-wallpaper-1440x900.jpg'):
	if(list_num==1):
		face_list_id = str(2)
	else:
		face_list_id = str(1)

	try:
		import cognitive_face as CF
		KEY = 'd56e4adcb31944e6a9e6cd824048f1c5'  # Replace with a valid Subscription Key here.
		CF.Key.set(KEY)

		BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
		CF.BaseUrl.set(BASE_URL)

		face = CF.face.detect(img_url)
		result = CF.face.find_similars(face[0]['faceId'],face_list_id)

		if(len(result)>0):
			return True
		else:
			return False

	except Exception as e:
		print("error")





