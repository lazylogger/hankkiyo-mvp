from django.db import models


class Category(models.Model):
    name = models.CharField('카테고리', max_length=40, null=False, unique=True)  # 한글표기
    abbr = models.CharField('category', max_length=40, null=False, unique=True)  # 영문표기
    imgSrc = models.FileField('카테고리사진', upload_to='category', null=False, blank=True)
    # imgSrc = models.CharField('카테고리사진', max_length=300, default="")

    class Meta:
        ordering = ['abbr']
        verbose_name = '카테고리'
        verbose_name_plural = '카테고리'

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField('업체명', max_length=40, null=False, unique=True)  # 한글표기
    abbr = models.CharField('store', max_length=40, null=False, unique=True)  # 영문표기
    imgSrc = models.FileField('업체사진', upload_to='store', null=False, blank=True)
    # imgSrc = models.CharField('업체사진', max_length=300, default="")
    bestMenus = models.CharField('베스트메뉴', max_length=40, null=False)

    '''추후 적용'''
    # description = models.TextField('업체설명', max_length=300, null=False)
    # created = models.DateTimeField('업체등록일', auto_now_add=True)
    # updated = models.DateTimeField('업체수정일', auto_now=True)

    category = models.ForeignKey(
        Category,
        to_field="name", db_column="category",
        on_delete=models.CASCADE,
        null=False,
        related_name='stores',
        verbose_name='카테고리',
    )

    class Meta:
        # ordering = ['-created']
        verbose_name = '업체'
        verbose_name_plural = '업체'

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField('메뉴명', max_length=40, null=False)  # 한글표기
    abbr = models.CharField('menu', max_length=40, null=False, unique=True)  # 영문표기
    # imgSrc = models.FileField('메뉴사진', upload_to='menu', null=False, blank=True)
    # imgSrc = models.CharField('메뉴사진', max_length=300, default="")
    price = models.IntegerField('가격', default=0, null=False)

    '''추후 적용'''
    # description = models.TextField('메뉴설명', max_length=300, null=False)
    # available_display = models.BooleanField('제품노출여부', default=True)  # 주문 불가능 제품이라도 목록에 노출하는 경우 있음음
    # available_order = models.BooleanField('주문가능여부', default=True)

    # created = models.DateTimeField('제품등록일', auto_now_add=True)
    # updated = models.DateTimeField('제품수정일', auto_now=True)

    category = models.ForeignKey(
        Category,
        to_field="name", db_column="category",
        on_delete=models.CASCADE,
        null=False,
        related_name='menus',
        verbose_name='카테고리',
    )
    store = models.ForeignKey(
        Store,
        to_field="name", db_column="store",
        on_delete=models.CASCADE,
        null=False,
        related_name='menus',
        verbose_name='업체',
    )

    class Meta:
        # ordering = ['-created']
        verbose_name = '메뉴'
        verbose_name_plural = '메뉴'

    def __str__(self):
        return self.name

    def tag_price(self):
        return f'{self.price} 원'


class Order(models.Model):
    # 회원 : 주문 = 1 : N (현재 비회원 주문 절차)
    # 메뉴 : 주문 = N : M (메뉴가 속한 가게는 메뉴 모델에서 외래키 잡혀있음)
    # 다대다 관계의 중개모델은 직접 생성하지 않고 자동 'order_menus'
    # ManyToManyField 를 선언한 쪽에서는 해당 필드가 테이블에 생성되지 않는다.
    # (ManyToManyField 와 같은 related 필드는 SQL 문에서 CREATE 가 아닌 것으로 추측된다.)
    menu_abbr = models.ForeignKey(
        Menu,
        to_field="abbr", db_column="menu_abbr",
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='메뉴(영문표기)')
    quantity = models.IntegerField('주문수량', default=1)
    destination = models.CharField('배송지', max_length=500, null=False, blank=False)
    date_ordered = models.DateTimeField('주문일자', auto_now_add=True)

    ### fields made by menu_abbr ###
    menu = models.CharField('메뉴', max_length=40, blank=True)
    category = models.CharField('카테고리명', max_length=40, blank=True)
    store = models.CharField('업체명', max_length=40, blank=True)
    price = models.IntegerField('가격', blank=True)
    # total_price = models.CharField('총가격', max_length=400, blank=True)
    ######
    # 여러 상품 주문 시 tip 을 한번만 받도록 하는 것은 나중에 구현한다.
    # tip = models.IntegerField('배달팁', default=900)
    # total_price = models.IntegerField('결제금액', blank=True)

    class Meta:
        verbose_name = '주문'
        verbose_name_plural = '주문'
        ordering = ('-date_ordered',)  # 최신 주문순

    def __str__(self):
        return f'주문번호 {self.id} ) {self.menu_abbr.name}'

    '''
    def get_order_category(self):
        return self.menu.category.name

    def get_order_store(self):
        return self.menu.store.name

    # 단일 메뉴 or 여러 메뉴 주문 시 총 금액 계산할 함수
    # 현재 수량은 조절 불가능. 체크박스 형태로 주문

    def get_total_price(self):
        # total = 0
        # for order_menu in self.menu:
        total = self.menu.price * self.quantity
        return total
    '''

    def save(self, *args, **kwargs):
        self.menu = self.menu_abbr.name
        self.category = self.menu_abbr.category   # self.get_order_category
        # 함수는 다음과 같이 저장됨 <bound method Order.get_order_store of <Order: 주문번호 : None - 주문메뉴 : 뿌링치즈치킨 반마리>>
        self.store = self.menu_abbr.store   # self.get_order_store
        self.price = self.menu_abbr.price * self.quantity
        # self.total_price = self.price + self.tip

        super(Order, self).save(*args, **kwargs)


