from nose.tools import ok_

from callme.app import create_app


class TestExample(object):

    def setup(self):
        self.app = create_app(testing=True)
        self.client = self.app.test_client()

    def test_ok(self):
        result = self.client.get("/")
        ok_(self.app.config["MESSAGE"] in result.data)
