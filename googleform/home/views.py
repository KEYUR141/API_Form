from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Form, User
from .serializers import FormSerializers
class FormAPI(APIView):
    
    def get(self,request):

        return Response({
            'Status:': True,
            'Message':"Get CALLED"
        })
    
    def post(self,request):
        try:
            data = request.data
            user = User.objects.first()
            form = Form().create_blank_form(user)
            serializer = FormSerializers(form)
            return Response({
                "Status":True,
                "Message":"Form Created Successfully",
                "Data": serializer.data
            })
        except Exception as e:
            return Response({  
                "Status":False,
                "Message":str(e)
            })
        
    def patch(self,request):
        try:
            data =request.data
            if not data.get('form_id'):
                return Response({
                "Status":False,
                "Message":"Form ID required",
                "Data": {}
            })

            form_obj = Form.objects.filter(id = data.get('form_id'))

            if form_obj.exists():
                serializers = FormSerializers(form_obj[0], data=data, partial=True)
                if serializers.is_valid():
                    serializers.save()
                    return Response({
                    "Status":True,
                    "Message":"Form Updated Successfully",
                    "Data": serializers.data
                    })
                return Response({
                    "Status":False,
                    "Message":"Form Not Updated",
                    "Data": serializers.errors
                })
            return Response({
                    "Status":False,
                    "Message":"Invalid Form ID Not Updated",
                    "Data": {}
                })
        
        except Exception as e:
            return Response({  
                "Status":False,
                "Message":str(e)
            })