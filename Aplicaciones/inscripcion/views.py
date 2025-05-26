from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Docente, Taller, Alumno, Inscripcion


def inicio(request):
    return render(request, 'inicio.html')

# DOCENTE
def listarDocentes(request):
    docentes = Docente.objects.all()
    return render(request, "listarDocentes.html", {'docentes': docentes})

def nuevoDocente(request):
    return render(request, "agregarDocente.html")

def guardarDocente(request):
    nombre = request.POST["nombre"]
    especialidad = request.POST["especialidad"]
    correo = request.POST["correo"]
    Docente.objects.create(nombre=nombre, especialidad=especialidad, correo=correo)
    messages.success(request, "Docente guardado exitosamente")
    return redirect('listarDocentes')

def eliminarDocente(request, id):
    docente = Docente.objects.get(id=id)
    docente.delete()
    messages.success(request, "Docente eliminado exitosamente")
    return redirect('listarDocentes')

def editarDocente(request, id):
    docente = Docente.objects.get(id=id)
    return render(request, "editarDocente.html", {'docenteEditar': docente})

def procesarEdicionDocente(request):
    id = request.POST["id"]
    docente = Docente.objects.get(id=id)
    docente.nombre = request.POST["nombre"]
    docente.especialidad = request.POST["especialidad"]
    docente.correo = request.POST["correo"]
    docente.save()
    messages.success(request, "Docente actualizado exitosamente")
    return redirect('listarDocentes')

# TALLER
def listarTalleres(request):
    talleres = Taller.objects.all()
    return render(request, "listarTalleres.html", {'talleres': talleres})

def nuevoTaller(request):
    docentes = Docente.objects.all()
    return render(request, "agregarTaller.html", {'docentes': docentes})

def guardarTaller(request):
    nombre = request.POST["nombre"]
    cupo = request.POST["cupo"]
    duracion = request.POST["duracion"]
    id_docente = request.POST["id_docente"]
    docente = Docente.objects.get(id=id_docente)
    Taller.objects.create(nombre=nombre, cupo=cupo, duracion=duracion, id_docente=docente)
    messages.success(request, "Taller guardado exitosamente")
    return redirect('listarTalleres')

def eliminarTaller(request, id):
    taller = Taller.objects.get(id=id)
    taller.delete()
    messages.success(request, "Taller eliminado exitosamente")
    return redirect('listarTalleres')

def editarTaller(request, id):
    taller = Taller.objects.get(id=id)
    docentes = Docente.objects.all()
    return render(request, "editarTaller.html", {'tallerEditar': taller, 'docentes': docentes})

def procesarEdicionTaller(request):
    id = request.POST["id"]
    taller = Taller.objects.get(id=id)
    taller.nombre = request.POST["nombre"]
    taller.cupo = request.POST["cupo"]
    taller.duracion = request.POST["duracion"]
    id_docente = request.POST["id_docente"]
    docente = Docente.objects.get(id=id_docente)
    taller.id_docente = docente
    taller.save()
    messages.success(request, "Taller actualizado exitosamente")
    return redirect('listarTalleres')

# ALUMNO
def listarAlumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, "listarAlumnos.html", {'alumnos': alumnos})

def nuevoAlumno(request):
    return render(request, "agregarAlumno.html")

def guardarAlumno(request):
    nombre = request.POST["nombre"]
    edad = request.POST["edad"]
    correo = request.POST["correo"]
    Alumno.objects.create(nombre=nombre, edad=edad, correo=correo)
    messages.success(request, "Alumno guardado exitosamente")
    return redirect('listarAlumnos')

def eliminarAlumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    messages.success(request, "Alumno eliminado exitosamente")
    return redirect('listarAlumnos')

def editarAlumno(request, id):
    alumno = Alumno.objects.get(id=id)
    return render(request, "editarAlumno.html", {'alumnoEditar': alumno})

def procesarEdicionAlumno(request):
    id = request.POST["id"]
    alumno = Alumno.objects.get(id=id)
    alumno.nombre = request.POST["nombre"]
    alumno.edad = request.POST["edad"]
    alumno.correo = request.POST["correo"]
    alumno.save()
    messages.success(request, "Alumno actualizado exitosamente")
    return redirect('listarAlumnos')

# INSCRIPCION
def listarInscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, "listarInscripciones.html", {'inscripciones': inscripciones})

def nuevaInscripcion(request):
    alumnos = Alumno.objects.all()
    talleres = Taller.objects.all()
    return render(request, "agregarInscripcion.html", {'alumnos': alumnos, 'talleres': talleres})

def guardarInscripcion(request):
    id_alumno = request.POST["id_alumno"]
    id_taller = request.POST["id_taller"]
    fecha_de_inscripcion = request.POST["fecha_de_inscripcion"]
    alumno = Alumno.objects.get(id=id_alumno)
    taller = Taller.objects.get(id=id_taller)
    Inscripcion.objects.create(id_alumno=alumno, id_taller=taller, fecha_de_inscripcion=fecha_de_inscripcion)
    messages.success(request, "Inscripción guardada exitosamente")
    return redirect('listarInscripciones')

def eliminarInscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id=id)
    inscripcion.delete()
    messages.success(request, "Inscripción eliminada exitosamente")
    return redirect('listarInscripciones')

def editarInscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id=id)
    alumnos = Alumno.objects.all()
    talleres = Taller.objects.all()
    return render(request, "editarInscripcion.html", {'inscripcionEditar': inscripcion, 'alumnos': alumnos, 'talleres': talleres})

def procesarEdicionInscripcion(request):
    id = request.POST["id"]
    inscripcion = Inscripcion.objects.get(id=id)
    id_alumno = request.POST["id_alumno"]
    id_taller = request.POST["id_taller"]
    fecha_de_inscripcion = request.POST["fecha_de_inscripcion"]
    alumno = Alumno.objects.get(id=id_alumno)
    taller = Taller.objects.get(id=id_taller)
    inscripcion.id_alumno = alumno
    inscripcion.id_taller = taller
    inscripcion.fecha_de_inscripcion = fecha_de_inscripcion
    inscripcion.save()
    messages.success(request, "Inscripción actualizada exitosamente")
    return redirect('listarInscripciones')
