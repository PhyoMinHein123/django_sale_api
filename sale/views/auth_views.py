from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Customize the response structure here if needed
        custom_response = {
            'status': '200',
            'message': 'Login successful',
            'data': response.data
        }
        return Response(custom_response)

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Customize the response structure here if needed
        custom_response = {
            'status': '200',
            'message': 'Token refreshed successfully',
            'data': response.data
        }
        return Response(custom_response)

class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_status = renderer_context['response'].status_code
        if 200 <= response_status < 300:
            # Successful response
            return super().render({
                'status': 'success',
                'message': 'OK',
                'data': data
            }, accepted_media_type, renderer_context)
        elif response_status == 400:
            # Bad Request
            return super().render({
                'status': 'error',
                'message': 'Bad Request',
                'data': data
            }, accepted_media_type, renderer_context)
        elif response_status == 401:
            # Unauthorized
            return super().render({
                'status': 'error',
                'message': 'Unauthorized',
                'data': data
            }, accepted_media_type, renderer_context)
        elif response_status == 500:
            # Internal Server Error
            return super().render({
                'status': 'error',
                'message': 'Internal Server Error',
                'data': data
            }, accepted_media_type, renderer_context)
        # Add more conditions for other status codes if needed
        else:
            return super().render(data, accepted_media_type, renderer_context)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == 400:
            # Customize the response structure for 400 Bad Request
            custom_response = {
                'status': '400',
                'message': 'Bad Request',
                'data': response.data
            }
            return Response(custom_response, status=status.HTTP_400_BAD_REQUEST)
        elif response.status_code == 401:
            # Customize the response structure for 401 Unauthorized
            custom_response = {
                'status': '401',
                'message': 'Unauthorized',
                'data': response.data
            }
            return Response(custom_response, status=status.HTTP_401_UNAUTHORIZED)
        
        elif response.status_code == 500:
            # Customize the response structure for 500 Internal Server Error
            custom_response = {
                'status': '500',
                'message': 'Internal Server Error',
                'data': response.data
            }
            return Response(custom_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        elif response.status_code == 200:
            # Customize the response structure for 200 OK
            custom_response = {
                'status': '200',
                'message': 'OK',
                'data': response.data
            }
            return Response(custom_response, status=status.HTTP_200_OK)
        
        elif response.status_code == 201:
            # Customize the response structure for 201 Created
            custom_response = {
                'status': '201',
                'message': 'Created',
                'data': response.data
            }
            return Response(custom_response, status=status.HTTP_201_CREATED)

    return response