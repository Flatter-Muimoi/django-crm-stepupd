from django.db import models
from django.contrib.auth.models import User # Django標準のユーザーモデルをインポート
# タグモデル
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
# 顧客モデル
class Customer(models.Model):
    class Prefecture(models.TextChoices):
        HOKKAIDO = '北海道', '北海道'
        AOMORI = '青森県', '青森県'
        IWATE = '岩手県', '岩手県'
        MIYAGI = '宮城県', '宮城県'
        AKITA = '秋田県', '秋田県'
        YAMAGATA = '山形県', '山形県'
        FUKUSHIMA = '福島県', '福島県'
        IBARAKI = '茨城県', '茨城県'
        TOCHIGI = '栃木県', '栃木県'
        GUNMA = '群馬県', '群馬県'
        SAITAMA = '埼玉県', '埼玉県'
        CHIBA = '千葉県', '千葉県'
        TOKYO = '東京都', '東京都'
        KANAGAWA = '神奈川県', '神奈川県'
        NIIGATA = '新潟県', '新潟県'
        TOYAMA = '富山県', '富山県'
        ISHIKAWA = '石川県', '石川県'
        FUKUI = '福井県', '福井県'
        YAMANASHI = '山梨県', '山梨県'
        NAGANO = '長野県', '長野県'
        GIFU = '岐阜県', '岐阜県'
        SHIZUOKA = '静岡県', '静岡県'
        AICHI = '愛知県', '愛知県'
        MIE = '三重県', '三重県'
        SHIGA = '滋賀県', '滋賀県'
        KYOTO = '京都府', '京都府'
        OSAKA = '大阪府', '大阪府'
        HYOGO = '兵庫県', '兵庫県'
        NARA = '奈良県', '奈良県'
        WAKAYAMA = '和歌山県', '和歌山県'
        TOTTORI = '鳥取県', '鳥取県'
        SHIMANE = '島根県', '島根県'
        OKAYAMA = '岡山県', '岡山県'
        HIROSHIMA = '広島県', '広島県'
        YAMAGUCHI = '山口県', '山口県'
        TOKUSHIMA = '徳島県', '徳島県'
        KAGAWA = '香川県', '香川県'
        EHIME = '愛媛県', '愛媛県'
        KOCHI = '高知県', '高知県'
        FUKUOKA = '福岡県', '福岡県'
        SAGA = '佐賀県', '佐賀県'
        NAGASAKI = '長崎県', '長崎県'
        KUMAMOTO = '熊本県', '熊本県'
        OITA = '大分県', '大分県'
        MIYAZAKI = '宮崎県', '宮崎県'
        KAGOSHIMA = '鹿児島県', '鹿児島県'
        OKINAWA = '沖縄県', '沖縄県'

    company_name = models.CharField(max_length=20, verbose_name="会社名")
    state_name = models.CharField(max_length=10, choices=Prefecture.choices,blank=True, verbose_name="都道府県")
    contact_name = models.CharField(max_length=50, verbose_name="担当者名")
    email = models.EmailField(max_length=100, unique=True, verbose_name="メールアドレス")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="電話番号")
    # 【応用】Django標準のUserモデルと連携。顧客の「担当営業」を示す
    # 担当者が削除されても顧客情報は消さない (SET_NULL)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
    verbose_name="担当営業")
    # 【応用】Tagモデルと多対多で連携
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="タグ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    def __str__(self):
        return self.company_name # Adminサイトなどで見やすくするため
# 商談履歴モデル
class Activity(models.Model):
    # 進捗ステータスの選択肢
    STATUS_CHOICES = (
    ('APPO', 'アポ'),
    ('MEETING', '商談中'),
    ('PROPOSAL', '提案中'),
    ('WON', '受注'),
    ('LOST', '失注'),
    )
    # 【重要】Customerモデルと1対多で連携
    # 顧客が削除されたら、関連する商談履歴も一緒に削除する (CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="顧客")
    activity_date = models.DateField(verbose_name="商談日")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='APPO',
    verbose_name="進捗")
    note = models.TextField(verbose_name="商談メモ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    def __str__(self):
        return f"{self.customer.company_name} - {self.get_status_display()}" # どの顧客のどの商談か分かりやすく

    class Meta:
        verbose_name = "Activities"
        verbose_name_plural = "Activities"
       