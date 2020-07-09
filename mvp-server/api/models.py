from django.db import models


class Category(models.Model):
    name = models.CharField('카테고리', max_length=40, null=False)  # 한글표기
    abbr = models.CharField('category', max_length=40, null=False, blank=True, default="")  # 영문표기
    imgSrc = models.CharField('카테고리사진', max_length=300, default="")

    class Meta:
        ordering = ['abbr']
        verbose_name = '카테고리'
        verbose_name_plural = '카테고리'

    def __str__(self):
        return self.abbr


class Store(models.Model):
    name = models.CharField('업체명', max_length=40, null=False)  # 한글표기
    abbr = models.CharField('store', max_length=40, null=False, default="")  # 영문표기
    description = models.TextField('업체설명', max_length=300, null=False)
    # imgSrc = models.ImageField('업체이미지', upload_to='stores/%Y/%m/%d', blank=True)
    imgSrc = models.CharField('업체사진', max_length=300, default="")

    created = models.DateTimeField('업체등록일', auto_now_add=True)
    updated = models.DateTimeField('업체수정일', auto_now=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        related_name='stores',
        verbose_name='카테고리',
    )

    class Meta:
        ordering = ['-created']
        verbose_name = '업체'
        verbose_name_plural = '업체'

    def __str__(self):
        return self.abbr


class Menu(models.Model):
    name = models.CharField('메뉴명', max_length=40, null=False)  # 한글표기
    abbr = models.CharField('menu', max_length=40, null=False, default="")  # 영문표기
    description = models.TextField('메뉴설명', max_length=300, null=False)
    # imgSrc = models.ImageField('메뉴이미지', upload_to='menus/%Y/%m/%d', blank=True)
    imgSrc = models.CharField('메뉴이미지', max_length=300, default="")
    price = models.IntegerField('가격', default=0)

    available_display = models.BooleanField('제품노출여부', default=True)  # 주문 불가능 제품이라도 목록에 노출하는 경우 있음음
    available_order = models.BooleanField('주문가능여부', default=True)

    created = models.DateTimeField('제품등록일', auto_now_add=True)
    updated = models.DateTimeField('제품수정일', auto_now=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        related_name='menus',
        verbose_name='카테고리',
    )
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        null=False,
        related_name='menus',
        verbose_name='업체',
    )

    class Meta:
        ordering = ['-created']
        verbose_name = '제품'
        verbose_name_plural = '제품'

    def __str__(self):
        return self.name

    def tag_price(self):
        return f'{self.price} 원'

