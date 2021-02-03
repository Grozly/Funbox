from app.views import REDIS_CONNECTION, STREAM


# API testing status code
def test_post_visited_links_good(visited_links_good):
    assert visited_links_good.status_code == 201


# Checking the presence of a stream in Redis
def test_post_visited_links_check_redis(visited_links_good):
    assert REDIS_CONNECTION.xlen(STREAM) >= 1


# API testing status code
def test_post_visited_links_fail(visited_links_fail):
    assert visited_links_fail.status_code == 400


# API testing status code
def test_get_visited_domains_good(visited_domains_good):
    assert visited_domains_good.status_code == 200


# Checking the presence of a stream in Redis
def test_get_visited_domains_check_redis(visited_domains_good):
    assert REDIS_CONNECTION.xlen(STREAM) >= 1


# Checking data in Redis
def test_get_visited_domains_check_redis_data(visited_domains_good):
    redis_data = REDIS_CONNECTION.xrange(STREAM, "-", "+")
    test_redis_item1 = redis_data[0][1].values()
    test_redis_item2 = redis_data[1][1].values()
    test_redis_item3 = redis_data[2][1].values()
    test_redis_item4 = redis_data[3][1].values()
    test_array = []
    for value in test_redis_item1:
        test_array.append(value.decode("utf-8"))
    for value in test_redis_item2:
        test_array.append(value.decode("utf-8"))
    for value in test_redis_item3:
        test_array.append(value.decode("utf-8"))
    for value in test_redis_item4:
        test_array.append(value.decode("utf-8"))
    assert "youtube.com" in test_array
    assert "ya.ru" in test_array
    assert "funbox.ru" in test_array
    assert "stackoverflow.com" in test_array


# API testing status code
def test_get_visited_domains_fail(visited_domains_fail):
    assert visited_domains_fail.status_code == 400


# Application function testing lenght
def test_unique_cleaned_domain(unique_cleaned_domain_good):
    assert len(unique_cleaned_domain_good) == 4


# Application function testing data
def test_unique_cleaned_domain_data(unique_cleaned_domain_good):
    assert "youtube.com" in unique_cleaned_domain_good
    assert "ya.ru" in unique_cleaned_domain_good
    assert "funbox.ru" in unique_cleaned_domain_good
    assert "stackoverflow.com" in unique_cleaned_domain_good


# Application function testing type
def test_is_valid_url_type(is_valid_url_good):
    assert type(is_valid_url_good) == type([])


# Application function testing data
def test_is_valid_url_data(is_valid_url_good):
    assert is_valid_url_good == ["ya.ru"]
