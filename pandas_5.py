import numpy as np
import pandas as pd

authors = pd.DataFrame({"author_id":[1, 2, 3], "author_name":["Тургенев", "Чехов", "Островский"]}, columns=["author_id", "author_name"])
authors

book = pd.DataFrame({"author_id":[1, 1, 1, 2, 2, 3, 3], "book_title":["Отцы и дети", "Рудин", "Дворянское гнездо",
                                                                      "Толстый и тонкий", "Дама с собачкой", "Гроза", "Таланты и поклонники"],
                    "price":[450, 300, 350, 500, 450, 370, 290]})
book

author_price = pd.merge(authors, book, on = "author_id", how = "outer")
author_price

top5 = author_price.nlargest(5, "price")
top5

min_price = author_price.groupby("author_name").agg({"price": "min"})
min_price

max_price = author_price.groupby("author_name").agg({"price": "max"})
max_price

mean_price = author_price.groupby("author_name").agg({"price": "mean"})
mean_price

authors_stat = pd.concat([min_price, max_price, mean_price], axis=1, ignore_index=True)
authors_stat

authors_stat = authors_stat.rename(columns={0:"min_price", 1:"max_price",2:"mean_price"})
authors_stat

cover = pd.DataFrame({"cover":["твердая", "мягкая", "мягкая", "твердая", "твердая", "мягкая", "мягкая"]}, columns=["cover"])
cover

author_price["cover"] = ["твердая", "мягкая", "мягкая", "твердая", "твердая", "мягкая", "мягкая"]
author_price

#?pd.pivot_table

book_info = pd.pivot_table(author_price, values="price", index=["author_name"], columns=["cover"], aggfunc=np.sum, fill_value=0)
book_info

book_info.to_pickle("book_info.pkl")

book_info2 = pd.read_pickle("book_info.pkl")
book_info2

book_info.equals(book_info2)
