from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken




@api_view(['GET'])
def getit(request):
    student_obj=Student.objects.all()
    serializer=StudentSerializer(student_obj,many=True)
    return Response({"status":200,'payload':serializer.data})

@api_view(['POST'])
def postit(request):
    data=request.data
    serializer=StudentSerializer(data=data)

    if not serializer.is_valid():
        return Response({
            'status':404,
            'error':serializer.errors,
            'message':'Something went wrong while posting'
        })
    serializer.save()
    return Response({
            'status':200,
            'message':'Data Posted successfully'
        })

@api_view(['PUT'])
def putit(request,id):
    try:
        student_obj=Student.objects.get(id=id)
        serializer=StudentSerializer(student_obj,data=request.data)

        if not serializer.is_valid():
            return Response({
                'status':404,
                'error':serializer.errors,
                'message':'Something went wrong while posting'
            })
        serializer.save()
        return Response({
                'status':200,
                'message':'Data Posted successfully'
            })
    except Exception as e:
          return Response({
                'status':404,
                'error':serializer.errors,
                'message':'Invalid ID'
            })

# for making it patch make partial=True in fileds you want

@api_view(['DELETE'])
def deleteit(request,id):
    try:
        student_obj=Student.objects.get(id=id)
        student_obj.delete()
        return Response({
                'status':200,
                'message':'Data successfully deleted'
        })

    except Exception as e:
          return Response({
                'status':404,
                'message':'Invalid ID'
            })


# APIView
class StudentAPI(APIView):
    # For token authentication
    # authentication_classes = [TokenAuthentication]
    # For JWT authentication
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
       student_obj=Student.objects.all()
       serializer=StudentSerializer(student_obj,many=True)
       print(request.user)
       return Response({"status":200,'payload':serializer.data})
    
    def post(self,request):
        data=request.data
        serializer=StudentSerializer(data=request.data)

        if not serializer.is_valid():
         return Response({
            'status':404,
            'error':serializer.errors,
            'message':'Something went wrong while posting'
        })
        serializer.save()
        return Response({
            'status':200,
            'message':'Data Posted successfully'
        })
    
    def put(self,request):
        try:
            student_obj=Student.objects.get(id=request.data['id'])
            serializer=StudentSerializer(student_obj,data=request.data)

            if not serializer.is_valid():
             return Response({
                'status':404,
                'error':serializer.errors,
                'message':'Something went wrong while posting'
            })
            serializer.save()
            return Response({
                'status':200,
                'message':'Data Posted successfully'
            })
        except Exception as e:
          return Response({
                'status':404,
                'error':serializer.errors,
                'message':'Invalid ID'
            })
        
    def patch(self,request):
    
        try:
            student_obj=Student.objects.get(id=request.data['id'])
            serializer=StudentSerializer(student_obj,data=request.data)

            if not serializer.is_valid():
             return Response({
                'status':404,
                'error':serializer.errors,
                'message':'Something went wrong while posting'
            })
            serializer.save()
            return Response({
                'status':200,
                'message':'Data Posted successfully'
            })
        except Exception as e:
          return Response({
                'status':404,
                'error':serializer.errors,
                'message':'Invalid ID'
            })
        
    def delete(self,request):
        try:
            student_obj=Student.objects.get(id=request.data['id'])
            student_obj.delete()
            return Response({
                'status':200,
                'message':'Data successfully Deleted'
            })
        
        except Exception as e:
          return Response({
                'status':404,
                'message':'Invalid ID'
            })


class RegisterAPI(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)

        if not serializer.is_valid():
             return Response({
                'status':404,
                'error':serializer.errors,
                'message':'Something went wrong while authentication'
            })
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        # token_obj, is_created= Token.objects.get_or_create(user=user)
        
        # return Response({
        #         'status':200,
        #         'payload':serializer.data,
        #         'token':str(token_obj),
        #         'message':'Data Posted successfully'
        #     })
        # for generating jwt token manually
        refresh = RefreshToken.for_user(user)
        
        return Response({
                'status':200,
                'payload':serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message':'Data Posted successfully'
            })





