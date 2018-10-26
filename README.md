# Milan
WebApp for Code.fun.do++ by Team Sunami

## Team Members

- <a href="https://github.com/RituRajSingh878">Ritu Raj Singh</a>
- <a href="https://github.com/adityauser">Aditya Singh</a>
- <a href="https://github.com/BAJUKA">Sharvan Nayak</a>

## Problem
When a calamity strikes people get separated from their families,several people get injured and unfortunately lot of lives are lost.The whereabouts of many of these people especially the kids, injured and the dead are not known and a lot of manpower and resources goes into uniting these people with their families.There is also a growing concern on the side of the family of these people as they do not have a clear idea as to where and how to look for their loved ones. Uniting these people with their families is a very important task of disaster management.

## Our Solution
We aim to build a webapp that would completely automate the process of uniting people. On one side we would maintain a database which would comprise of photos of people who are missing which would be uploaded by their loved ones along with their basic details. On the other side we would maintain another database which would comprise photos of people who are found either by rescue operations or in relief camps who are unable to communicate especially the dead,injured and the children. Then we would search both the databases and find matching faces and the information of these people are sent to their loved ones. We propose to use one shot learning by implementing a siamese network to speed and automate up this process of searching. Our webapp would provide:
* An interface to upload images of missing and the found people.
* These images would be then sent to the backend server where search would be done using one shot learning.
* The information about the found is sent to their loved ones in the form of email or message. Same will be done to the relief ops/NGOs whoerver uploaded the photo of the found. 
## Dataset and Technology 
* We would use public data set like MS Celeb to train our network.
* We would use one shot learning using siamese network to compare the images in both the databases.<br>
![alt WORKFLOW](https://github.com/adityauser/Milan/blob/master/Images/Architecture.jpeg)
## Advantages
* There would be better cordination between the rescue ops and the families which would save a lot of time,resources and manpower which could be used elsewhere during the time of the calamity.
* This approach would provide a general platform for storing the data of missing and found and would help the NGO's and the government agencies to plan the necessary actions in an efficient way.<br>

## Edit
We have used microsoft's state of the art cognitive servies **(face api)** instead of implementing our own model but the underlying ideas are the same.<br>
**The url of the site is:  <a href="http://139.59.85.220/">Milan</a>**


