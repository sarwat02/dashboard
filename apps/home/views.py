# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmailForm
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText


# def send_email(request):
#     send_email_to_client()
#     return redirect('/')

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def send_email(request):
    if request.method == 'POST':
        to_email = request.POST['to']
        subject = request.POST['subject']
        message = request.POST['message']

        # SMTP configuration
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'kamalafridi000@gmail.com'
        smtp_password = 'wkzp goot yzgg lqdy'

        # Create a MIMEText object for the message
        mime_message = MIMEText(message)

        # Connect to the SMTP server and start TLS
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()

            # Log in to the SMTP server
            server.login(smtp_username, smtp_password)

            # Send the email
            server.sendmail(smtp_username, to_email, mime_message.as_string())

        return render(request, '../templates/home/email_sent.html')