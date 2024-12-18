from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated

from .models import DataField
from .serializers import DataFieldSerializer, RegisterSerializer

class RegisterView(APIView):
    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DataFieldView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            entry = DataField.objects.filter(user=request.user)
            serializer = DataFieldSerializer(entry, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self,request):
        try:
            serializer = DataFieldSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateDataFieldView(APIView):
    permission_classes = [permissions.IsAdminUser]
    def put(self,request,pk):
        try:
            entry = DataField.objects.get(pk=pk)
        except DataField.DoesNotExist:
            return Response({"error":"Data with id not found"}, status=status.HTTP_404_NOT_FOUND)
        status = request.data.get('status')
        if status not in ['Done', 'Not Done']:
            return Response({"error":"Invalid status data"} ,status=status.HTTP_400_BAD_REQUEST)
        entry.status = status
        entry.save()
        return Response({"message":"status updated successfully!"}, status=status.HTTP_200_OK)