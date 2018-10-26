from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import time


from webapp.models import Lost,Found,idlost,idfound



def mail(subject,message,from_email,to_list,fail_silently=False):
	send_mail(subject,message,from_email,to_list,fail_silently=False)



'''def return_id(img_url,list_num,p_k):
	img_url = 'http://139.59.85.220:8000'+img_url
	
	
	try:
		import cognitive_face as CF
		KEY = '86e4d8b85f274327b3919a7e6a026ad5'  # Replace with a valid Subscription Key here.
		CF.Key.set(KEY)

		BASE_URL = 'https://southcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
		CF.BaseUrl.set(BASE_URL)

		id_p = CF.face_list.add_face(img_url,list_num)['persistedFaceId']
		o.person_id = idp
		
		return id_p

		

	except Exception as e:
		print("error1")'''
		
def find_similar(list_num,img_url,obj):
	img_url = 'http://139.59.85.220'+img_url	
	#img_url = 'https://media.allure.com/photos/5a26c1d8753d0c2eea9df033/1:1/w_767/mostbeautiful.jpg'
	if(list_num==1):
		face_list_id = str(2)
	else:
		face_list_id = str(1)

	try:
		import cognitive_face as CF
		KEY = '86e4d8b85f274327b3919a7e6a026ad5'  # Replace with a valid Subscription Key here.
		CF.Key.set(KEY)

		BASE_URL = 'https://southcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
		CF.BaseUrl.set(BASE_URL)

		id_p = CF.face_list.add_face(img_url,list_num)['persistedFaceId']
		time.sleep(1)
		if list_num == 1:
			p = idlost(link = obj,person_id = id_p)
			p.save()
		elif list_num == 2:
			p = idfound(link = obj,person_id = id_p)
			p.save()

		result = CF.face.detect(img_url)
		result = CF.face.find_similars(result[0]['faceId'],face_list_id)

		#Logic for storing and using facelist id




		
		print(len(result))

		if(len(result)>0):
			if face_list_id == str(1):
				print("came in")
				#o = Lost.objects.get(pk=p_k)
				o = idlost.objects.get(person_id = result[0]["persistedFaceId"])
				print("cameout")
				o = o.link
				email = o.provider_email
				location = obj.location
				contact = obj.provider_number
				name = obj.provider_name
				condition = obj.condition

				subject = "Found"
				message = "your loved one has been found by {}. The location is {}. His/her condition is{}. The contact of the person is {}. ".format(name,location,condition,contact)
				from_email = settings.EMAIL_HOST_USER
				to_list = [email]
				#print("sending mail")
				send_mail(subject,message,from_email,to_list,fail_silently=False)
				#print("mail sent")

				email = obj.provider_email
				l_name = o.provider_name
				l_contact = o.provider_number
				subject = "Found"
				message = "The family of the person has been found. The name is {}.The contact is {}.".format(l_name,l_contact)
				from_email = settings.EMAIL_HOST_USER
				to_list = [email]

				send_mail(subject,message,from_email,to_list,fail_silently=False)


			if face_list_id == str(2):
				print("came in")
				#o = Found.objects.get(pk = p_k)
				o = idfound.objects.get(person_id = result[0]["persistedFaceId"])
				print("cameout")
				o = o.link
				email = o.provider_email
				location = o.location
				contact = o.provider_number
				name = o.provider_name
				condition = o.condition

				l_name = obj.provider_name
				l_contact = obj.provider_number

				subject = "Found"
				message = "The family of the person has been found. The name is {}.The contact is {}.".format(l_name,l_contact)
				from_email = settings.EMAIL_HOST_USER
				to_list = [email]

				#print("sending mail")
				send_mail(subject,message,from_email,to_list,fail_silently=False)
				#print("mail sent")

				email = obj.provider_email
				subject = "Found"
				message = "your loved one has been found by {}. The location is {}. His/her condition is{}. The contact of the person is {}. ".format(name,location,condition,contact)
				from_email = settings.EMAIL_HOST_USER
				to_list = [email]
				#time.sleep(20)

				#print("sending mail")
				send_mail(subject,message,from_email,to_list,fail_silently=False)
				#print("mail sent")


	except Exception as e:
		print(str(e))
			


	





