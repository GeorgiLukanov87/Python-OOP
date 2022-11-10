from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.build_photos()
        self.index_pages = 0
        self.index_slots = 0

    def build_photos(self):
        result = []
        for _ in range(self.pages):
            result.append([] * self.PHOTOS_PER_PAGE)
        return result

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        over = False
        for el in self.photos:
            over = False
            if len(el) == 4:
                over = True
        if over:
            return 'No more free slots'

        self.index_slots += 1
        if self.index_slots % 5 == 0:
            self.index_slots = 1
            self.index_pages += 1
        self.photos[self.index_pages].append(label)
        return f'{label} photo added successfully on page {self.index_pages + 1} slot {self.index_slots}'

    def display(self):
        result = ''
        for el in self.photos:
            result += '-----------\n'
            counter = 0
            for _ in el:
                counter += 1
                result += '[]' + ' '
                if counter == len(el) - 1:
                    result += '[]'
                    break
            result += '\n'
        result += '-----------'
        return result
