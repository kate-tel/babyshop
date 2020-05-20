from seleniumbase import BaseCase
from baby_object import BoboChoses

class NavigationTest(BaseCase):

    def setUp(self):
        super(NavigationTest, self).setUp()
        self.base_url = 'https://www.babyshop.com'
        self.menu_dict = {'Brands':['//a[@data-class="brand"]',self.base_url+'/brands/s/618']}

    def test_menu(self):
        # Откроем сайт
        self.get(self.base_url)
        for item in self.menu_dict:
            print(f'Menu {item}')
            self.click(self.menu_dict[item][0])
            # получаем текущий урл в переменную curr_url
            curr_url = self.get_current_url()
            # проверка соответствия полученного и ожидаемого урл
            self.assert_true(curr_url == self.menu_dict[item][1])

    def test_search(self):
        self.get(self.base_url)
        self.update_text('input[name="key"]', "Sirona S i-Size Car Seat\n")
        number = len(self.find_elements('article'))
        self.assert_equal(number, 5)

    def test_basket(self):
        self.open(self.base_url+'/bobo-choses/s/466')
        self.click(BoboChoses.dresses, timeout=12)
        self.hover_and_click(BoboChoses.article, BoboChoses.quickshop)
        self.click(BoboChoses.drop_down)
        self.click(BoboChoses.option)
        self.click(BoboChoses.add_cart)
        name = self.get_text(BoboChoses.p_name)[:26]
        self.click(BoboChoses.checkout)
        self.assert_text_visible(name)
        self.click(BoboChoses.delete)
        self.assert_text_visible(BoboChoses.msg)
        self.sleep(1)

    def test_lang(self):
        self.open(self.menu_dict['Brands'][1])
        self.click(BoboChoses.DG)
        eng = self.get_text(BoboChoses.filter_by)
        price = self.get_text(BoboChoses.price)
        self.click(BoboChoses.region_change)
        self.click_link_text('Русский')
        url = self.get_current_url()
        # Check url change
        self.assertEqual(url, BoboChoses.ru_url)
        self.click(BoboChoses.brands)
        self.click(BoboChoses.DG)
        ru = self.get_text(BoboChoses.filter_by)
        ru_price = self.get_text(BoboChoses.price)
        # Check site language changed
        self.assertNotEqual(eng, ru)
        # Check price (currency and number) changed
        self.assertNotEqual(price, ru_price)
        self.sleep(2)

    def test_buy(self):
        self.open(self.base_url+'/bobo-choses/s/466')
        self.click(BoboChoses.dresses, timeout=12)
        self.hover_and_click(BoboChoses.article, BoboChoses.quickshop)
        self.click(BoboChoses.drop_down)
        self.click(BoboChoses.option)
        self.click(BoboChoses.add_cart)
        self.click(BoboChoses.checkout)
        self.update_text(BoboChoses.email, 'b9euqngtxy@1secmail.net')
        self.update_text(BoboChoses.firstName, 'George')
        self.update_text(BoboChoses.lastName, 'Call')
        self.update_text(BoboChoses.adress, 'Daalmeereiland 40')
        self.update_text(BoboChoses.postal_code, '1827KX')
        self.update_text(BoboChoses.city, 'Alkmaar')
        self.update_text(BoboChoses.phone, '0629564634')
        # self.click(BoboChoses.submit)
        self.sleep(5)
