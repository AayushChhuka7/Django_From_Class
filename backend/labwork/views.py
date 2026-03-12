from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Student

class StudentLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            # Look up student by username
            student = Student.objects.get(username=username)
            
            # Check if provided password matches the hashed password in DB
            if student.check_password(password):
                refresh = RefreshToken.for_user(student)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
        
        except Student.DoesNotExist:
            pass

        # Return error if credentials fail
        return Response(
            {"error": "Invalid username/password"},
            status=status.HTTP_401_UNAUTHORIZED
        )