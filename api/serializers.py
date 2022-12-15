from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    labels = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'labels', 'quantity', 'price')

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('id', 'name')

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Cart
        fields = ('id', 'product', 'quantity')