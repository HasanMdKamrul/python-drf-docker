import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, mixins
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer

# Create your views here.

now = datetime.datetime.now()
time = now.strftime("%H:%M:%S")

print("Current Time =", time)

# class Postview(APIView):
#     permission_classes = (AllowAny,)
    
#     def get_object(self,pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return Response({"message":"Data not found"})
    
#     def get(self, request,format=None,*args, **kwargs):
        
#       posts = Post.objects.all()
#       serializer = PostSerializer(posts, many=True)
#       return Response(serializer.data)
            
        
#         # if pk
#         #     post = Post.objects.get(pk=pk)
#         #     serializer = PostSerializer(post)
#         #     return Response(serializer.data)
        
        
    
#     # def get(self, request, pk,*args, **kwargs):
#     #     post = Post.objects.get(pk=pk)
#     #     serializer = PostSerializer(post)
#     #     return Response(serializer.data)
        
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
            
#         return Response(serializer.errors)
        
#     def put(self,request,pk,*args,**kwargs):
#         data = request.data
#         post_modified = Post.objects.get(pk=pk)
#         serializer = PostSerializer(post_modified,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,)
            
#         return Response(serializer._errors)
    
#     def delete(self,request,pk,*args,**kwargs):
#         post_deleted = Post.objects.get(pk=pk)
#         post_deleted.delete()
#         return Response({"message" : "Post deleted"})
        
   
   


# class PostListMixinView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [AllowAny]
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
   
#     # ** write a mixin which will retrive only one data
    

class Get_all_posts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
class Create_post(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
class Retrive_post(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
class Destroy_post(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    
    
            


# @csrf_exempt

# def get_all_posts(request):
    
#     if request.method == "GET":
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many = True)
        
#         return JsonResponse(serializer.data, safe=False)
        
        
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe=False, status = 200)
#         return JsonResponse(serializer.errors, status = 404)
            
        
    


# @csrf_exempt

# def get_post_detail(request,pk):
    
#     try:
#         post = Post.objects.get(pk=pk)
#     except post.DoesNotExist :
#         return HttpResponse(status=404)
    
    
#     if request.method == "GET":
#         serializer = PostSerializer(post)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == "DELETE" :
#         post.delete()
#         return HttpResponse(404)
#     elif request.method == "PUT" :
#         data = JSONParser().parse(request)
#         serializer = PostSerializer(post,data=data) 
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe=False)
#         return JsonResponse(serializer.errors, status=400)
            
        
    

   

   
  


# @csrf_exempt
# def post_list(request):
#     """
#     List all code posts, or create a new post.
#     """
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    

# @csrf_exempt
# def post_detail(request, pk):
#     """
#     Retrieve, update or delete a code post.
#     """
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = PostSerializer(post, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         post.delete()
#         return HttpResponse(status=204)