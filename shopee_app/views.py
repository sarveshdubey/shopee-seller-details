from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from bots.browser import Browser
from bots.seller_details import Details
from bots.product_links import Links
from bots.product_details import ProductDetails

from .serializers import SellerDetails_Serializer,GetLinks_Serializer, ProductDetails_Serializer

# Create your views here.
# https://shopee.vn/unilever_beauty_premium/

class SellerDetails_View(APIView):
    serializer_class = SellerDetails_Serializer
    def get(self, request, *args, **kwargs):
        data = self.request.query_params
        print('data', data)
        
        if data:
            try:
                URL = data["url"]
            except:
                return Response({'message': f'Invalid parameter, please use url as parameter.', 'status': 400}, 400)
            if URL:
        
                try:
                    browser = Browser.get_browser()

                except Exception as e:
                    return Response({"Message":f"Browser not Initialized, {str(e)}", 'status': 403}, status.HTTP_403_FORBIDDEN)

                try:
                    bot = Details(browser)
                    response = bot.seller_details(URL)
                    if response == "404":
                        return Response({"Message":f"Failed to get Info, 404 Product Not Found"}, status.HTTP_404_NOT_FOUND)
                    elif response == "404VN":
                        return Response({"Message":f"Failed to get Info, 404 Product Not Found"}, status.HTTP_404_NOT_FOUND)
                    elif response == "login":
                        return Response({"Message":f"Failed to get Info, Login Found"}, status.HTTP_404_NOT_FOUND)
                    else:
                        return Response({"Message":"Task Successful", "Info":response}, status.HTTP_200_OK)
                except Exception as e:
                    return Response({"Message":f"Failed to get Info, {str(e)}"}, status.HTTP_404_NOT_FOUND)
            else:
                return Response({'Message': "Parameter 'url' can't be empty!", 'status': 400}, 400)
        else:
            return Response({'Message': "Parameter- 'url' missing.", 'status': 400}, 400)


class GetLinks_View(APIView):
    serializer_class = GetLinks_Serializer
    def get(self, request, *args, **kwargs):
        data = self.request.query_params
        print('data', data)
        
        if data:
            try:
                URL = data["url"]
            except:
                return Response({'message': f'Invalid parameter, please use url as parameter.', 'status': 400}, 400)
            if URL:
        
                try:
                    browser = Browser.get_browser()
                except Exception as e:
                    return Response({"Message":f"Browser not Initialized, {str(e)}", 'status': 403}, status.HTTP_403_FORBIDDEN)

                try:
                    bot = Links(browser)
                    response = bot.get_links(URL)
                    if response == "404":
                        return Response({"Message":f"Failed to get Info, 404 Product Not Found"}, status.HTTP_404_NOT_FOUND)
                    elif response == "404VN":
                        return Response({"Message":f"Failed to get Info, 404 Product Not Found"}, status.HTTP_404_NOT_FOUND)
                    elif response == "login":
                        return Response({"Message":f"Failed to get Info, Login Found"}, status.HTTP_404_NOT_FOUND)
                    else:
                        return Response({"Message":"Task Successful", "Info":response}, status.HTTP_200_OK)
                except Exception as e:
                    return Response({"Message":f"Failed to get Info, {str(e)}"}, status.HTTP_404_NOT_FOUND)
            else:
                return Response({'Message': "Parameter 'url' can't be empty!", 'status': 400}, 400)
        else:
            return Response({'Message': "Parameter- 'url' missing.", 'status': 400}, 400)


class ProductDetails_View(APIView):
    serializer_class = ProductDetails_Serializer
    def get(self, request, *args, **kwargs):
        data = self.request.query_params
        print('data', data)
        
        if data:
            try:
                URL = data["url"]
            except:
                return Response({'message': f'Invalid parameter, please use url as parameter.', 'status': 400}, 400)
            if URL:
        
                try:
                    browser = Browser.get_browser()

                except Exception as e:
                    return Response({"Message":f"Browser not Initialized, {str(e)}", 'status': 403}, status.HTTP_403_FORBIDDEN)

                try:
                    bot = ProductDetails(browser)
                    response = bot.get_links(URL)
                    if response == "404":
                        return Response({"Message":f"Failed to get Info, 404 Product Not Found"}, status.HTTP_404_NOT_FOUND)
                    elif response == "404VN":
                        return Response({"Message":f"Failed to get Info, 404 Product Not Found"}, status.HTTP_404_NOT_FOUND)
                    elif response == "login":
                        return Response({"Message":f"Failed to get Info, Login Found"}, status.HTTP_404_NOT_FOUND)
                    else:
                        return Response({"Message":"Task Successful", "Info":response}, status.HTTP_200_OK)
                except Exception as e:
                    return Response({"Message":f"Failed to get Info, {str(e)}"}, status.HTTP_404_NOT_FOUND)
            else:
                return Response({'Message': "Parameter 'url' can't be empty!", 'status': 400}, 400)
        else:
            return Response({'Message': "Parameter- 'url' missing.", 'status': 400}, 400)

        





