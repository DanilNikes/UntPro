
class Film:
    def __init__(self, film_dict=None):
        self.id = film_dict["_id"]
        self.title = film_dict["title"]
        self.original_title = film_dict["original_title"]
        self.year = film_dict["year"]
        self.duration = film_dict["duration"]
        self.genres = film_dict["genres"]
        self.poster_url = film_dict["poster_url"]
        self.countries = film_dict["countries"]
        self.film_url = film_dict["film_url"]
        self.director = film_dict["director"]
        self.writers = film_dict["writers"]
        self.stars = film_dict["stars"]
        self.comments = film_dict["comments"]
        # self.trailer_url = film_dict("trailer_url")
        #


    def dict_convert(self):
        return {"_id": self.id,
                "title": self.title,
                "original_title": self.original_title,
                "year": self.year,
                "duration": self.duration,
                "genres": self.genres,
                "poster_url": self.poster_url,
                "countries": self.countries,
                "film_url": self.film_url,
                "director": self.director,
                "writers": self.writers,
                "stars": self.stars,
                "comments": self.comments
                }

def film_list_returner(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        if result:
            return [item for item in result]
        else:
            return 'empty'
    return wrapper

class FilmList:
    def __init__(self):
        self.film_list = []

    def add_film(self, film=Film):
        self.film_list.append(film)

    @film_list_returner
    def show_list(self):
        return self.film_list