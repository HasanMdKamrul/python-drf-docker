
import datetime
import locale

import pytz
from rest_framework import serializers

from .models import Post

time_zone = pytz.timezone('Europe/Berlin')
berlin_standard_time = datetime.datetime.now(time_zone)

berlin_current_time = berlin_standard_time.strftime("%H:%M:%S")


# now = datetime.datetime.now()
# time = now.strftime("%H:%M:%S")

# locale_time = locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

# print(time)




class PostSerializer(serializers.ModelSerializer):
      
    temp_price = serializers.SerializerMethodField()
      
    class Meta:
        model = Post
        fields = (
                    'id',
                    'title',
                    "custom_id",
                    "category",
                    "publish_date",
                    "last_updated",
                    "price",
                    "temp_price"
                   
                  )
        
    # def get_temp_price(self, obj):
    #       if berlin_current_time > "11:00:00" and berlin_current_time < "18:45:00":
    #             return  obj.price * 0.1
    #       else:
    #             return obj.price
    
    def get_temp_price(self, obj):
          if berlin_current_time > "11:00:00" and berlin_current_time < "18:45:00":
                return  obj.price * 0.1
          else:
                return obj.price

         
              
        