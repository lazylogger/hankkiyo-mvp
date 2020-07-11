from rest_framework import serializers
from .models import Category, Store, Menu, Order


class CategoryListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'abbr', 'imgSrc']


class CategoryDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'abbr']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'abbr', 'price']   # 'tag_price'


class StoreListSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True)
    bestMenus = serializers.SerializerMethodField('get_bestMenus')
    category = serializers.StringRelatedField()

    class Meta:
        model = Store
        fields = ['name', 'abbr', 'imgSrc', 'bestMenus', 'menus', 'category']

    def get_bestMenus(self, store):
        bestmenus = Menu.objects.all()[:2]   # get 2 best menus for this store
        serializer = MenuSerializer(instance=bestmenus, many=True)

        namearray = []
        for data in serializer.data:
            namearray.append(data['name'])

        namestr = ' '.join(namearray)   # 공백 이용해서 붙임

        # return serializer.data
        return namestr


class StoreDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    menus = MenuSerializer(many=True)

    class Meta:
        model = Store
        fields = ['name', 'abbr', 'category', 'imgSrc', 'menus']


class OrderSerializer(serializers.ModelSerializer):
    """
    StringRelatedField 역할 ( menu : 1 -> menu : "1인 후라이드 치킨" )
    POST 목적의 serializer 에는 적합하지 않음.
    menu 항목을 기입하고 POST 요청 해도 menu_id가 null 이 될 수 없다고 나옴.
    따라서 Order 테이블에서 menu 외래키 잡을 때 id가 아닌 name 으로 잡았음.
    그에 따라 Menu 테이블에서 name 은 unique 한 컬럼이어야 함.
    """
    # menu = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ('menu', 'quantity', 'destination',
                  'get_total_price', 'get_order_store', 'get_order_category')

        # extra_kwargs = {"date_ordered": {"read_only": True}}