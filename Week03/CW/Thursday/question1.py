BOOKS = (
(1, "داستان", 1943, "آنتوان دو سنت اگزوپری", "شازده کوچولو", True),
(2, "تخیلی-علمی", 1949, "جورج اورول", "1984", True),
(3, "اقتصاد", 1776, "آدام اسمیت", "ثروت ملل", False),
(4, "تاریخ", 2011, "یووال نوح هراری", "انسان خردمند", True),
(5, "داستان", 1988, "پائولو کوئلیو", "کیمیاگر", True),
(6, "داستان", 1967, "گابریل گارسیا مارکز", "صد سال تنهایی", False),
(7, "فانتزی", 1997, "جی. کی. رولینگ", "هری پاتر و سنگ جادو", True),
(8, "تاریخ", 1925, "آدولف هیتلر", "نبرد من", True),
(9, "اقتصاد", 1997, "رابرت کیوساکی", "پدر پولدار پدر بی‌پول", True),
(10, "شعر", 1390, "حافظ شیرازی", "دیوان حافظ", True)
)

book_list = []

for book in BOOKS:
    book_dict: dict = {
        "id": book[0],
        "title": book[1],
        "author": book[2],
        "publish date": book[3],
        "gener": book[4],
        "available": book[5]
    }

    book_list.append(book_dict)

print("Books".center(60, "-"))
print("id\ttitle\tauthor\tpublish date\tgener\tavailable")
for book in book_list:
    print(book["id"], book["title"], book["author"], 
          book["publish date"], book["gener"], book["available"], sep="\t")
