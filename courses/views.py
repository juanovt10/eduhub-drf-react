from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course
from .serializers import CourseSerializer
from eduhub_drf_api.permissions import IsOwnerOrReadOnly


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


class CourseDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CourseSerializer

    def get_object(self, pk):
        try:
            course = Course.objects.get(pk=pk)
            self.check_object_permissions(self.request, course)
            return course
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(
            course, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(
            course, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


