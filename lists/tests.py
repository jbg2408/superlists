from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        # resolve is the function Django uses to :
        #   resolve URLs and find what view function they map to.
        #   found.func says: what function
             
        # This asserst that found.func '/' or ''
        # is mapped (in urls.py) to home_page
        # So it appears re
        print(found)
        #.ResolverMatch(func=lists.views.home_page, args=(), kwargs={}, url_name=home, app_name=None, namespaces=[])
        print(found.func)
        ##   <function home_page at 0x0000000003FB0840>
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # This calls the home_page function, passing a request
        # then checks the returned response for the correct info.
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'A new list item'}
        )
        self.assertEqual(response.content.decode(), expected_html)
