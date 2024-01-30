from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course
from .serializers import CourseSerializer


class CourseList(APIView):
    serializer_class = CourseSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(
            courses, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        if not request.user.profile.is_instructor:
            return Response(
                {
                    'You do not have permission to create a course, ' 
                    'only certified instructors can create courses'
                },
                status=status.HTTP_403_FORBIDDEN
            )


        serializer = CourseSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )