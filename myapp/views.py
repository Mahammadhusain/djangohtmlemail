from django.shortcuts import render,redirect
from django.contrib import messages
from django.template import loader
from django.core.mail import EmailMultiAlternatives
# Create your views here.


def HomeView(request):
    context = {
      'h': 'Hello world with django'
    }
    return render(request, 'email.html', context)


# Function to send data to email (gmail)
def send_mail(request):
  # name = request. POST.get('name') 
  # email = request. POST.get('email') 
  # courses = request. POST.get('courses')
  template= loader.get_template('email.html') 

  context = {
    'name' :'Demo name', 
    'email' :'kadiwala.530@email.com', 
    'courses': 'Python',  
  }

  message = template.render(context)

  email = EmailMultiAlternatives(
  "Mastery Courses", message, 
  "Congratulation" + "- A gift to you", 
  ['kadiwala.530@gmail.com'])

  # Convert the html and css Inside the email.content_subtype = 'html'
  email.content_subtype = 'html'
  email.send() 
  messages.success(request, 'We sent a Ling to your email !') 
  return redirect('/')
