from fixtures.utils import user_authorize


def test_correct_username_password():
    user_authorize('supertest', 'superpassword')