from seleniumbase import BaseCase
from baby_object import BoboChoses


class BabyshopTestClass(BaseCase):

    def setUp(self):
        super(BabyshopTestClass, self).setUp()
        self.base_url = 'https://www.babyshop.com'
        self.menu_dict = {'Brands': ['//a[@data-class="brand"]',
                          self.base_url+'/brands/s/618']}

    def test_menu(self):
        # This test checks that user can navigate a website via menu links

        self.get(self.base_url)
        for item in self.menu_dict:
            print(f'Menu {item}')
            self.click(self.menu_dict[item][0])
            curr_url = self.get_current_url()
            self.assert_true(curr_url == self.menu_dict[item][1])

    def test_search(self):
        # This test checks that a certain number of results is displayed
        #  for a particular search input

        self.get(self.base_url)
        self.update_text('input[name="key"]', "Sirona S i-Size Car Seat\n")
        number = len(self.find_elements('article'))
        self.assert_equal(number, 5)

    def test_cart(self):
        # This test checks that:
        # - user can add an item to cart;
        # - user can delete an item from cart

        self.open(self.base_url+'/bobo-choses/s/466')
        self.hover_and_click(BoboChoses.article, BoboChoses.quickshop)
        self.click(BoboChoses.drop_down)
        self.click(BoboChoses.option)
        self.click(BoboChoses.add_cart)
        name = self.get_text(BoboChoses.p_name)[:26]
        self.click(BoboChoses.checkout)
        self.assert_text_visible(name)
        self.click(BoboChoses.delete)
        self.assert_text_visible(BoboChoses.cart_empty)

    def test_lang(self):
        # This test checks that:
        # - region and language are changed;
        # - site language and product prices are adopted

        self.open(self.menu_dict['Brands'][1])
        self.click(BoboChoses.dolce_gabbana)
        eng = self.get_text(BoboChoses.filter_by)
        price = self.get_text(BoboChoses.price)
        self.click(BoboChoses.region_change)
        self.click_link_text('Русский')
        url = self.get_current_url()
        # Check url change
        self.assertEqual(url, BoboChoses.ru_url)
        self.click(BoboChoses.brands)
        self.click(BoboChoses.dolce_gabbana)
        ru = self.get_text(BoboChoses.filter_by)
        ru_price = self.get_text(BoboChoses.price)
        # Check site language has changed
        self.assertNotEqual(eng, ru)
        # Check that the price has changed
        self.assertNotEqual(price, ru_price)

    def test_checkout(self):
        # This test checks that:
        # - item can be added to cart
        # Checkout is not performed fully as it is a working website.
        # In my magento2.test project checkout is tested fully in demo website.

        self.open(self.base_url+'/bobo-choses/s/466')
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
