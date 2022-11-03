from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from bots.browser import Browser
from bots.seller_details import Details

from .serializers import SellerDetails_Serializer

# Create your views here.
# https://shopee.vn/unilever_beauty_premium/

class SellerDetails_View(APIView):
    serializer_class = SellerDetails_Serializer
    def get(self, request, *args, **kwargs):
        URL = self.request.query_params["URL"]
        
        try:
            browser = Browser.get_browser()
        except Exception as e:
            return Response({"Message":f"Browser not Initialized, {e}"}, status.HTTP_403_FORBIDDEN)

        try:
            bot = Details(browser)
            name, followers, chat_performance, joined, rating, url, username , products, following, active = bot.seller_details(URL)
            total_products,total_sold = bot.get_product_details()
            category,sub_category = bot.categories()

            context = {
                "Name": name,
                "Followers": followers,
                "Chat": chat_performance,
                "Joined": joined,
                "Rating": rating,
                "URL": url,
                "Username": username,
                "Products": products,
                "Following": following,
                "Active": active,
                "Total Products": total_products,
                "Total Sold": total_sold,
                "Category": category,
                "Sub-category": sub_category,
            }
            return Response({"Message":"Task Successful", "Info":context}, status.HTTP_200_OK)
        except Exception as e:
            return Response({"Message":f"Failed to get Info, {e}"}, status.HTTP_404_NOT_FOUND)