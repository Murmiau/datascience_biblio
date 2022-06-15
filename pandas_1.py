import numpy as np
import pandas as pd

authors = pd.DataFrame({"author_id":[1, 2, 3], "author_name":["Тургенев", "Чехов", "Островский"]}, columns=["author_id", "author_name"])
authors

book = pd.DataFrame({"author_id":[1, 1, 1, 2, 2, 3, 3], "book_title":["Отцы и дети", "Рудин", "Дворянское гнездо",
                                                                      "Толстый и тонкий", "Дама с собачкой", "Гроза", "Таланты и поклонники"],
                    "price":[450, 300, 350, 500, 450, 370, 290]})
book
