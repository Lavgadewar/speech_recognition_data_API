from rest_framework.views import APIView
#  from data_api.models import  Data
# from data_api.serilizers import DataSerializers
from rest_framework.response import Response
# from rest_framework import status


# Create your views here.

class DataList(APIView):
    def  get(self,request) :
        # books =  Data.objects.all() 
        # seriallizer = DataSerializers(books, many=True)
        # return Response(seriallizer.data)
         return Response([
            {
             'id' : 1,
             'title': "india is an independent country"
            },
            {
             'id' : 2,
             'title': "delhi is the capital of india"
            }
            ] )
