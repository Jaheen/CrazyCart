from django.db import models


class Categories(models.Model):
    categoryId = models.AutoField(verbose_name="Category Id", primary_key=True)
    categoryName = models.CharField(verbose_name="Category Name", max_length=30)
    categoryImage = models.ImageField(verbose_name="Category Image", upload_to="Products/Categories")
    def __str__(self):
        return self.categoryName
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Products(models.Model):
    productId = models.AutoField(verbose_name="Product ID", primary_key=True)
    productName = models.CharField(verbose_name="Product Name", max_length=30)
    productCategory = models.ForeignKey("products.Categories", on_delete=models.CASCADE)
    productImage = models.ImageField(verbose_name="Product Image", upload_to="Products/ProductImages")
    productStock = models.IntegerField(verbose_name="Product Stock", default=0)
    productPrice = models.BigIntegerField(verbose_name="Product Price", default=0)
    productSeller = models.CharField(verbose_name="Product Seller", max_length=50)
    productSpecifications = models.TextField(verbose_name="Product Specifications")
    productDescriptions = models.TextField(verbose_name="Product Descriptions")
    countryOfManufacture = models.CharField(verbose_name="Country Of Manufacture", max_length=50)
    warrantyPeriod = models.IntegerField(verbose_name="Warranty Period", default=0)
    noOfPurchases = models.IntegerField(verbose_name="No of Purchases", default=0)
    def __str__(self):
        return self.productName
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        