from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app.models import Doctor, Department


def index(request):
    num_doctors = Doctor.objects.count()

    context = {
        "num_doctors": num_doctors
    }
    return render(request, "app/index.html", context=context)


def contact_us(request):
    return render(request, "app/contact_us.html")


class DoctorsListView(generic.ListView):
    model = Doctor
    template_name = "app/doctors_list.html"
    context_object_name = "doctors_list"
    paginate_by = 4


class DoctorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Doctor
    fields = ("first_name", "last_name", "experience", "description", "contacts", "avatar", "department")
    success_url = reverse_lazy("app:doctors_list")


class DoctorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Doctor
    fields = ("first_name", "last_name", "experience", "description", "contacts", "avatar", "department")
    success_url = reverse_lazy("app:doctors_list")


class DoctorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Doctor
    template_name = "app/doctor_delete_confirm.html"
    success_url = reverse_lazy("app:doctors_list")


class DoctorDetailView(generic.DetailView):
    model = Doctor


class DepartmentsListView(generic.ListView):
    model = Department
    template_name = "app/departments_list.html"
    context_object_name = "departments_list"


class DepartmentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Department
    fields = "__all__"
    success_url = reverse_lazy("app:departments_list")


class DepartmentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Department
    fields = "__all__"
    success_url = reverse_lazy("app:departments_list")


class DepartmentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Department
    template_name = "app/department_delete_confirm.html"
    success_url = reverse_lazy("app:departments_list")


class DepartmentDetailView(generic.DetailView):
    model = Department


class DoctorsContactsListView(generic.ListView):
    model = Doctor
    template_name = "app/doctors_contacts_list.html"
    context_object_name = "doctors_contacts_list"
    paginate_by = 8
