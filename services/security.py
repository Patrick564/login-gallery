from passlib.context import CryptContext


crypt_context = CryptContext(
    schemes=['bcrypt'],
    bcrypt__rounds=13,
    deprecated='auto'
)
