from CryptoMath.cryptomath import CryptoMath

def test_modpow():
    assert 1 == CryptoMath.modpow(2, 2, 3)

