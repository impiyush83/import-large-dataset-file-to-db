from coding_challenge_restful.resources.products import Products
from coding_challenge_restful.utils import URLS

urls = [
    URLS(resource=Products, endpoint=['products'], name='products'),
]
