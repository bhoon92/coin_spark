#import jwt   # PyJWT 
import jwt
import uuid

def create_auth_token():
    payload = {
        'access_key': 'wVU0IDw3qUOAEmqikohl2JuxcILtD3B3rCSC69RY',
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, 'Q6Nx7UJeCqjqnSZx79SrfGxPHvn7nkBeVOMZixhs')
    authorization_token = 'Bearer {}'.format(jwt_token)

create_auth_token