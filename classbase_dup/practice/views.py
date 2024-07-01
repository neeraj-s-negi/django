from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import Student,CustomUser
from .serializers import StudentSerializer, MyTokenObtainPairSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework.viewsets import ModelViewSet
from .pagination import MyLimitOffsetPagination

########################### TOKEN AUTHENTICATION #############################
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

########################### JWT AUTHENTICATION #############################

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.decorators import api_view        # function base drf

from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer

###############################################################################################

                                         #CLASS BASE VIEW


class StudentClassBaseView(APIView):

    # authentication_classes = [TokenAuthentication]

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    # pagination_class =MyLimitOffsetPagination
    
    def get(self, request, id=None, format=None):
        id =id
        try:
            if id is not None:
                data=Student.objects.get(pk=id)
                serializer=StudentSerializer(data)
                return Response(serializer.data)
        except Student.DoesNotExist:
            data = Student.objects.all()      
                                       #.order_by('-id') - for serial order who create latest
            serializer = StudentSerializer(data, many=True)
            print(serializer.data)
            return Response(serializer.data)  


    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request, id=None, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None, format=None):
        id = id
        if id is not None:
            data = Student.objects.get(id=id)
            data.delete()
            return Response('successfully deleted')
        

    def put(self, request, id=None, format=None):
        stu_data = Student.objects.get(id=id)
        serializer = StudentSerializer(stu_data ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'update successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id=None, format=None):
        stu_data = Student.objects.get(id=id)
        serializer = StudentSerializer(stu_data ,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial update successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def get_object(self, request,id=None, format=None):

        # try:
        #     book = Student.objects.get(id=id)
        # except Student.DoesNotExist:
        #     return Response({'error': 'student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # serializer = StudentSerializer(book)
        # return Response(serializer.data)


        # id = id
        # if id is not None:
        #     data = Student.objects.get(id=id)
        #     serialize = StudentSerializer(data)
        #     return Response(serialize.data)
        
        # return Response({'msg': 'not valid id'})



###############################################################################################

                             # MIXIN BASE VIEW

class StudentMixinBaseView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,mixins.UpdateModelMixin, generics.GenericAPIView):

    queryset = Student.objects.all()            #model
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)    


###############################################################################################

                             # GENERIC BASE VIEW

class StudentGenericBaseView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView,generics.RetrieveAPIView):
    queryset = Student.objects.all()

    serializer_class = StudentSerializer
    pagination_class =MyLimitOffsetPagination


class RegisterView(generics.ListCreateAPIView):
    """Handles creating and listing Users."""
    queryset = CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            all_data = serializer.validated_data['user']
            login(request, all_data)
            user_serializer = RegisterSerializer(all_data)
            # return Response({'detail': 'Successfully logged in.'}, status=status.HTTP_200_OK)
            return Response({'detail': 'Successfully logged in.', 'data': user_serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        logout(request)
        return Response({'msg': 'Success Logout'})



    
###############################################################################################

                             # MODEL VIEW SET

class StudentViewSet(ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer                 



##################################################################################################################################################

                             # FUNCTION BASE DRF

@api_view(['GET'])
def show_list(request):
    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)
    
    return Response(serializer.errors, status= status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        serializer_data = StudentSerializer(data = request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data)
        return Response(serializer_data.errors, status= status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def get_id_data(request, id):
    # if request.method == 'GET':
    try:
        if id is not None:
            obj = Student.objects.get(id=id)
            serializer_data = StudentSerializer(obj)
            return Response(serializer_data.data)
    except Student.DoesNotExist:
        return Response({'msg': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)              #it is not work

@api_view(['DELETE'])
def remove_id(request, id):
    try:
        if id is not None:
            obj = Student.objects.get(id=id)
            obj.delete()
            return Response({'message':'successful delete'})
    except Student.DoesNotExist:
        return Response({'message':'id is not here'})                   #it is not work

@api_view(['PUT'])
def update(request, id):
    if id is not None:
        obj = Student.objects.get(id=id)
        serializer_data = StudentSerializer(obj, data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data)
        else:
            return Response(serializer_data.errors, status= status.HTTP_204_NO_CONTENT)
    
    return Response({'message':'id is not here'})

@api_view(['PATCH'])
def partial_update(request, id):
    if id is not None:
        obj = Student.objects.get(id=id)
        serializer_data = StudentSerializer(obj, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data)
    
    return Response(serializer_data.errors, status= status.HTTP_204_NO_CONTENT)