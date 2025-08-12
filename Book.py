from enum import Enum

class Status(Enum):
    NOT_STARTED = 'not_started'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

class Book:

    title = ""
    author = ""
    isbn = 0
    status = Status.NOT_STARTED
    date_started = []
    date_completed = []
    rating = 0
    review = ""

    def __init__(self, title, author, isbn, status, date_started, date_completed, rating, review):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status
        self.date_started = date_started
        self.date_completed = date_completed
        self.rating = rating
        self.review = review

    def get_author(self):
        return self.author

    def get_title(self):
        return self.title

    def get_status(self):
        return self.status

    def get_date_started(self):
        return self.date_started

    def get_date_completed(self):
        return self.date_completed

    def get_rating(self):
        return self.rating

    def get_review(self):
        return self.review

    def set_status(self, status):
      self.status = status

    def set_date_started(self, date_started):
        self.date_started = date_started

    def set_date_completed(self, date_completed):
        self.date_completed = date_completed

    def set_rating(self, rating):
        self.rating = rating

    def set_review(self, review):
        self.review = review
