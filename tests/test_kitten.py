from odoo.tests.common import TransactionCase


class TestKitten(TransactionCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        user_admin = self.env.ref("base.user_admin")
        self.env = self.env(user=user_admin)
        self.Kitten = self.env["cattery.kitten"]
        self.kitten1 = self.Kitten.create({"name": "Zora", "breed": "Maine Coon"})


def test_kitten_create(self):
    "Available kittens are active by default"
    self.assertEqual(self.kitten1.active, True)
