from unittest import TestCase
from isp2lb.decorator import key
# из файла isp2lb.decorator импортируется функция key
# вызов assertEqual(), assertNotEqual() для проверки ожидаемого результата;
# assertTrue() или assertFalse() для проверки условия; assertRaises() для проверки, что метод порождает исключение
class Test(TestCase):
    def test_key(self):
        self.assertEqual(key(5, 5), "55")

    def test_wrong_key(self):
        self.assertNotEqual(key(6, 5), 8)
