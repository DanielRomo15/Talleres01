from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),

    # DOCENTE
    path('docentes/', views.listarDocentes, name='listarDocentes'),
    path('nuevoDocente', views.nuevoDocente, name='nuevoDocente'),
    path('guardarDocente', views.guardarDocente, name='guardarDocente'),
    path('eliminarDocente/<int:id>', views.eliminarDocente, name='eliminarDocente'),
    path('editarDocente/<int:id>', views.editarDocente, name='editarDocente'),
    path('procesarEdicionDocente', views.procesarEdicionDocente, name='procesarEdicionDocente'),

    # TALLER
    path('talleres/', views.listarTalleres, name='listarTalleres'),
    path('nuevoTaller', views.nuevoTaller, name='nuevoTaller'),
    path('guardarTaller', views.guardarTaller, name='guardarTaller'),
    path('eliminarTaller/<int:id>', views.eliminarTaller, name='eliminarTaller'),
    path('editarTaller/<int:id>', views.editarTaller, name='editarTaller'),
    path('procesarEdicionTaller', views.procesarEdicionTaller, name='procesarEdicionTaller'),

    # ALUMNO
    path('alumnos/', views.listarAlumnos, name='listarAlumnos'),
    path('nuevoAlumno', views.nuevoAlumno, name='nuevoAlumno'),
    path('guardarAlumno', views.guardarAlumno, name='guardarAlumno'),
    path('eliminarAlumno/<int:id>', views.eliminarAlumno, name='eliminarAlumno'),
    path('editarAlumno/<int:id>', views.editarAlumno, name='editarAlumno'),
    path('procesarEdicionAlumno', views.procesarEdicionAlumno, name='procesarEdicionAlumno'),

    # INSCRIPCION
    path('inscripciones/', views.listarInscripciones, name='listarInscripciones'),
    path('nuevaInscripcion', views.nuevaInscripcion, name='nuevaInscripcion'),
    path('guardarInscripcion', views.guardarInscripcion, name='guardarInscripcion'),
    path('eliminarInscripcion/<int:id>', views.eliminarInscripcion, name='eliminarInscripcion'),
    path('editarInscripcion/<int:id>', views.editarInscripcion, name='editarInscripcion'),
    path('procesarEdicionInscripcion', views.procesarEdicionInscripcion, name='procesarEdicionInscripcion'),
]
