from coding_challenge_restful.resources.sku import SKU
from coding_challenge_restful.utils import URLS

urls = [
    URLS(resource=SKU, endpoint=['skus'], name='sku_data'),
]
