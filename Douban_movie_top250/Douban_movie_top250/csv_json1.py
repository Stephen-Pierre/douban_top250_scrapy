import pandas as pd
path = "D:\\Users\\shandaiwang\\PycharmProjects\\pythonProject2\\douban_top250_scrapy\\douban_top250_scrapy\\Douban_movie_top250\\movies_info.csv"
# path1 = "Douban_movie_top250\\movies_info.csv"
csv_data = pd.read_csv(path)
csv_data.to_json("movies_info.json", orient = "records")