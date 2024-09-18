from django.shortcuts import render, get_object_or_404
from main.models import Client, Plate
from main.forms import ClientForm, RegistrationForm
from django.db import IntegrityError
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request, "home.html")

def client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            registration = form.cleaned_data["registration"]
            client, created = Client.objects.get_or_create(email=email)

            if registration:
                # attempt to create a valid Plate object
                try:
                    plate = Plate.objects.create(client=client, registration=registration)
                except IntegrityError:
                    error_message = "Client already has the license plate " + registration + " registered."
                    return render(request, "clients.html", {"form": form, "message": {"error": error_message}})
                except:
                    error_message = "There was an error registering the license plate."
                    return render(request, "clients.html", {"form": form, "message": {"error": error_message}})

                # new client and plate
                if created:
                    success_message = "plate " + plate.registration + " added to new client: " + client.email
                    return render(request, "clients.html", {"form": form, "message": {"success": success_message}})

                # added a new plate to an existing client
                success_message = "plate " + plate.registration + " added to client: " + client.email
                return render(request, "clients.html", {"form": form, "message": {"success": success_message}})

            # new client only
            if created:
                success_message = "Added new client: " + client.email
                return render(request, "clients.html", {"form": form, "message": {"success": success_message}})

            # error creating a new client because it already exists
            error_message = "There is already a client registed with the email " + client.email
            return render(request, "clients.html", {"form": form, "message": {"error": error_message}})

    else:
        form = ClientForm()

    return render(request, "clients.html", {"form": form})

def client_detail(request, client_id):
    client_object = get_object_or_404(Client, pk=client_id)
    registrations = Plate.objects.filter(client=client_id)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.cleaned_data["registration"]
            try:
                Plate.objects.create(client=client_object, registration=registration)
            except IntegrityError: # checks if there is an attempt to create duplicate of a Plate
                error_message = "Client already has the license plate " + registration + " registered."
                return render(request, "client.html", {"form": form,
                                                       "client": client_object,
                                                       "registrations": registrations,
                                                       "message": {"error": error_message}
                                                       })
            form = RegistrationForm()
    else:
        form = RegistrationForm()

    registrations = Plate.objects.filter(client=client_id)

    return render(request, "client.html", {"form": form, "client": client_object, "registrations": registrations})


def registration(request):
    registrations = Plate.objects.all()
    return render(request, "registrations.html", {"registrations": registrations})

class PlateDeleteView(DeleteView):
    model = Plate
    template_name = "delete.html"

    def form_valid(self, form):
        self.client_id = Plate.objects.get(id=self.kwargs['pk']).client.id # get client id for reverse
        return super().form_valid(form)

    def get_success_url(self):
         return reverse("client_detail", kwargs={'client_id': self.client_id})

class PlateUpdateView(UpdateView):
    model = Plate
    fields = ["registration"]
    template_name = "update.html"

    def form_valid(self, form):
        self.client_id = Plate.objects.get(id=self.kwargs['pk']).client.id # get client id for reverse
        return super().form_valid(form)

    def get_success_url(self):
         return reverse("client_detail", kwargs={'client_id': self.client_id})