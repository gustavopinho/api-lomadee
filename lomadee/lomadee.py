import requests

class Lomadee():

    sandbox_url = "https://sandbox-api.lomadee.com/v2/{0}/{1}"
    production_url = "https://api.lomadee.com/v2/{0}/{1}"

    def __init__(self, app_token, source_id, sandbox=False):

        self.app_token = app_token
        self.source_id = source_id
        self.sandbox = sandbox

    def get_url(self, resource):
        if self.sandbox:
            return self.sandbox_url.format(self.app_token, resource)
        return self.production_url.format(self.app_token, resource)

    def get_params(self, **params):
        params.update({
            'sourceId': self.source_id
        })
        return params

    def get(self, resource, **params):

        response = requests.get(
            self.get_url(resource),
            params=self.get_params(**params)
        ).json()
        return response


class Offer(Lomadee):
    
    def bestsellers(self, **params):
        resource = "offer/_bestsellers"
        return self.get(resource, **params)

    def search(self, **params):
        resource = "offer/_search"
        return self.get(resource, **params)

    def offer(self, offer_id, **params):
        resource = "offer/_id/{0}".format(offer_id)
        return self.get(resource, **params)

    
    def category(self, category_id, **params):
        resource = "offer/_category/{0}".format(category_id)
        return self.get(resource, **params)

    def product(self, product_id, **params):
        resource = "offer/_product/{0}".format(product_id)
        return self.get(resource, **params)

    def store(self, store_id, **params):
        resource = "offer/_store/{0}".format(store_id)
        return self.get(resource, **params)


class Product(Lomadee):

    def bestsellers(self, **params):
        resource = "product/_bestsellers"
        return self.get(resource, **params)

    def search(self, **params):
        resource = "product/_search"
        return self.get(resource, **params)

    def category(self, category_id, **params):
        resource = "product/_category/{0}".format(category_id)
        return self.get(resource, **params)

    def product(self, product_id, **params):
        resource = "product/_id/{0}".format(product_id)
        return self.get(resource, **params)


class Category(Lomadee):

    def bestsellers(self, **params):
        resource = "category/_bestsellers"
        return self.get(resource, **params)

    def search(self, **params):
        resource = "category/_search"
        return self.get(resource, **params)

    def all(self, **params):
        resource = "category/_all"
        return self.get(resource, **params)

    def category(self, category_id, **params):
        resource = "category/_id/{0}".format(category_id)
        return self.get(resource, **params)


class Store(Lomadee):

    def all(self, **params):
        resource = "store/_all"
        return self.get(resource, **params)


class DeepLink(Lomadee):

    def create(self, **params):
        resource = "deeplink/_create"
        return self.get(resource, **params)


class Coupon(Lomadee):

    def all(self, **params):
        resource = "coupon/_all"
        return self.get(resource, **params)

    def coupon(self, coupon_id, **params):
        resource = "coupon/_id/{0}".format(coupon_id)
        return self.get(resource, **params)

    def category(self, category_id, **params):
        resource = "coupon/_categories/{0}".format(category_id)
        return self.get(resource, **params)
    
    def store(self, store_id, **params):
        resource = "coupon/_stores/{0}".format(store_id)
        return self.get(resource, **params)


