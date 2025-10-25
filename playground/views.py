from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Construire le message à envoyer
        full_message = f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject=f"Nouveau message de {name}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["bekkiche23ikram@gmail.com"],  # <-- Mets ton email ici
                fail_silently=False,
            )
            messages.success(request, "Votre message a été envoyé avec succès ✅")
        except Exception as e:
            print(e)
            messages.error(request, "Une erreur est survenue lors de l’envoi ❌")

        return redirect('home')

    return render(request, 'contact.html')
