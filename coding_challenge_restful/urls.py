from coding_challenge_restful.resources.products import Products
from coding_challenge_restful.resources.upload_file import UploadFile
from coding_challenge_restful.utils import URLS
urls = [
    URLS(resource=Products, endpoint=['products'], name='products'),
    URLS(resource=UploadFile, endpoint=[''], name='upload_file'),
]
