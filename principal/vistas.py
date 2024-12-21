from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .modelos import Inscrito
from .formularios import FormularioInscrito, FormularioInstitucion
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializadores import InscritoSerializer, InstitucionSerializer
from .modelos import Institucion 

def pagina_inicio(request):
    return render(request, 'inicio.html')

def lista_inscritos(request):
    inscritos = Inscrito.objects.select_related('institucion_asociada').all()
    return render(request, 'inscritos/lista_inscritos.html', {'inscritos': inscritos})

def crear_inscrito(request):
    if request.method == 'POST':
        form = FormularioInscrito(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_inscritos')  
    else:
        form = FormularioInscrito()
    return render(request, 'inscritos/formulario_inscrito.html', {'form': form})

def editar_inscrito(request, pk):
    inscrito = get_object_or_404(Inscrito, pk=pk)
    if request.method == 'POST':
        form = FormularioInscrito(request.POST, instance=inscrito)
        if form.is_valid():
            form.save()
            return redirect('lista_inscritos')
    else:
        form = FormularioInscrito(instance=inscrito)
    return render(request, 'inscritos/formulario_inscrito.html', {'form': form})

def eliminar_inscrito(request, pk):
    inscrito = get_object_or_404(Inscrito, pk=pk)
    if request.method == 'POST':
        inscrito.delete()
        return redirect('lista_inscritos')
    return render(request, 'inscritos/confirmar_eliminacion_inscrito.html', {'inscrito': inscrito})

def api_vista_inscritos(request):
    return render(request, 'api_inscritos.html')

def api_vista_instituciones(request):
    return render(request, 'api_instituciones.html')

class InscritoAPIListadoCrear(APIView):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InscritoAPIDetalle(APIView):
    def get(self, request, pk):
        inscrito = get_object_or_404(Inscrito, pk=pk)
        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data)

    def put(self, request, pk):
        inscrito = get_object_or_404(Inscrito, pk=pk)
        serializer = InscritoSerializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inscrito = get_object_or_404(Inscrito, pk=pk)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InstitucionAPIListadoCrear(APIView):
    def get(self, request):
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InstitucionAPIDetalle(APIView):
    def get(self, request, pk):
        institucion = get_object_or_404(Institucion, pk=pk)
        serializer = InstitucionSerializer(institucion)
        return Response(serializer.data)

    def put(self, request, pk):
        institucion = get_object_or_404(Institucion, pk=pk)
        serializer = InstitucionSerializer(institucion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        institucion = get_object_or_404(Institucion, pk=pk)
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def lista_instituciones(request):
    instituciones = Institucion.objects.all()
    return render(request, 'instituciones/lista_instituciones.html', {'instituciones': instituciones})

def crear_institucion(request):
    if request.method == 'POST':
        form = FormularioInstitucion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_instituciones')
    else:
        form = FormularioInstitucion()
    return render(request, 'instituciones/formulario_institucion.html', {'form': form})

def editar_institucion(request, pk):
    institucion = get_object_or_404(Institucion, pk=pk)
    if request.method == 'POST':
        form = FormularioInstitucion(request.POST, instance=institucion)
        if form.is_valid():
            form.save()
            return redirect('lista_instituciones')
    else:
        form = FormularioInstitucion(instance=institucion)
    return render(request, 'instituciones/formulario_institucion.html', {'form': form})

def eliminar_institucion(request, pk):
    institucion = get_object_or_404(Institucion, pk=pk)
    if request.method == 'POST':
        institucion.delete()
        return redirect('lista_instituciones')
    return render(request, 'instituciones/confirmar_eliminacion_institucion.html', {'institucion': institucion})


