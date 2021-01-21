from unittest import TestCase
from app import app
from flask import session

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']




    # def test_duplicate_username_rejected(self):

    #     test_user_c = User.register(username='test_user_a', password='test123', email='testuser_c@email.com', state_id='NV')

    #     self.assertFalse(test_user_c)

    # def test_duplicate_email_rejected(self):

    #     test_user_c = User.register(username='test_user_c', password='test123', email='testuser_a@email.com', state_id='NV')

    #     self.assertFalse(test_user_c)

class ViewsLoggedOutTests(TestCase):

    # test if home page loads
    def test_root_route(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="text-center mt-5">Welcome to Lumin </h1>', html)


    # test if bill browse page loads
    def test_bills_route(self):
        with app.test_client() as client:
            resp = client.get('/bills')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<p class="text-center">A place to view and follow bills. </p>', html)

    # test if legislator browse page loads
    def test_legislator_route(self):
        with app.test_client() as client:
            resp = client.get('/legislators')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<p class="text-center">A place to view Legislators. </p>', html)

    # test if login page loads
    def test_login_route(self):
        with app.test_client() as client:
            resp = client.get('/login')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="text-center mt-3">Login</h1>', html)

    # test if signup page loads
    def test_signup_route(self):
        with app.test_client() as client:
            resp = client.get('/signup')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="text-center mt-3">Sign Up</h1>', html)

    # test if view dashboard screen does not load when not logged in and user is rerouted
    def test_view_dashboard_route_lo(self):
        with app.test_client() as client:
            resp = client.get('/dashboard',follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('You must be logged in to do that!', html)

    # test if view profile screen does not load when not logged in and user is rerouted
    def test_view_profile_route_lo(self):
        with app.test_client() as client:
            resp = client.get('/profile',follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('You must be logged in to do that!', html)

    # test if edit profile screen does not load when not logged in and user is rerouted
    def test_edit_profile_route_lo(self):
        with app.test_client() as client:
            resp = client.get('/profile/edit',follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('You must be logged in to do that!', html)

    # test if delete profile screen does not load when not logged in and user is rerouted
    def test_delete_profile_route_lo(self):
        with app.test_client() as client:
            resp = client.get('/profile/delete',follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('You must be logged in to do that!', html)

    # test logout denial when already logged out in another tab
    def test_logout_lo(self):
        with app.test_client() as client:

            resp = client.post("/logout", follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('No user currently logged in!', html)

    # test if legislator page loads
    def test_legislator_view(self):
        with app.test_client() as client:
            resp = client.get('/legislator/L000577')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("View Sponsored Bills", html)

    # test if bill page loads
    def test_bill_view(self):
        with app.test_client() as client:
            resp = client.get('/bills/s5085-116')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('View Full Bill at', html)