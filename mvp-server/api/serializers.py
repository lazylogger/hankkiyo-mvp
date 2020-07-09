from rest_framework import serializers
from .models import Category, Store, Menu


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
