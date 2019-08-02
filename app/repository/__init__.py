class Repository(object):
    def __init__(self, adapter=None):
        self.client = adapter()
        
    def find_all(self, selector):
        return self.client.find_all(selector)
    def find  (self, selector):
        return self.client.find(selector)
    def create(self, user):
        return self.client.create(user)
    def update(self, selector, user):
        return self.client.update(selector, user)
    def delete(self, selector):
        return self.client.delete(selector)
    def seeAll(self):
        return self.client.seeAll()

class General_Repository(object):
    def __init__(self, adapter=None):
        self.client = adapter()
        
    def find_all(self, table, selector):
        return self.client.find_all(selector)
    def find  (self, table, selector):
        return self.client.find(selector)
    def create(self, table, element):
        return self.client.create(element)
    def update(self, table, selector, element):
        return self.client.update(selector, element)
    def delete(self, table, selector):
        return self.client.delete(selector)
