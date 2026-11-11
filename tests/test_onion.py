from onionindex.onion import extract_host, is_valid_v3

DDG = "duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion"


def test_real_address_is_valid():
    assert is_valid_v3(DDG)


def test_single_character_typo_is_rejected():
    typo = "duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczae.onion"
    assert not is_valid_v3(typo)


def test_v2_and_garbage_are_rejected():
    assert not is_valid_v3("expyuzz4wqqyqhjn.onion")
    assert not is_valid_v3("example.com")
    assert not is_valid_v3("")


def test_extract_host_normalises_urls():
    assert extract_host(f"HTTPS://{DDG.upper()}/html/?q=1") == DDG
    assert extract_host(f"{DDG}:80") == DDG
    assert extract_host("https://example.com/") is None
    assert extract_host(None) is None


def test_subdomain_is_kept(onion):
    host = "search." + onion("x")
    assert extract_host(f"https://{host}/search?q=a") == host
