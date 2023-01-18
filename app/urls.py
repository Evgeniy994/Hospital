from django.urls import path

from app.views import index, DoctorsContactsListView, DepartmentsListView, DoctorsListView, DoctorDetailView, \
    DepartmentDetailView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView, DepartmentCreateView, \
    DepartmentUpdateView, DepartmentDeleteView, contact_us

urlpatterns = [
    path("", index, name="index"),
    path("contact_us/", contact_us, name="contact_us"),
    path("doctors/", DoctorsListView.as_view(), name="doctors_list"),
    path("dotors/<int:pk>/", DoctorDetailView.as_view(), name="doctor_detail"),
    path("doctors/create", DoctorCreateView.as_view(), name="doctors_create"),
    path("doctors/<int:pk>/update", DoctorUpdateView.as_view(), name="doctors_update"),
    path("doctors/<int:pk>/delete", DoctorDeleteView.as_view(), name="doctors_delete"),
    path("doctors_contact/", DoctorsContactsListView.as_view(), name="doctors_contact_list"),
    path("doctors_contact/<int:pk>/", DoctorDetailView.as_view(), name="doctor_contact_detail"),
    path("departments/", DepartmentsListView.as_view(), name="departments_list"),
    path("departments/<int:pk>/", DepartmentDetailView.as_view(), name="departments_detail"),
    path("departments/create", DepartmentCreateView.as_view(), name="departments_create"),
    path("departments/<int:pk>/update", DepartmentUpdateView.as_view(), name="departments_update"),
    path("departments/<int:pk>/delete", DepartmentDeleteView.as_view(), name="departments_delete"),
]

app_name = "app"
