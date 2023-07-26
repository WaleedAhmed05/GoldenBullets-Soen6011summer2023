def test_get_job_posts(client):
    response = client.get('/api/jobs/')
    assert response.status_code == 200
    # Assert that the response is a list
    assert isinstance(response.json, list)

def test_get_job_post_not_found(client):
    response = client.get('/api/jobs/1000000')
    assert response.status_code == 200
    # Assert that the response is a dictionary with the key 'error'
    assert isinstance(response.json, dict) and 'error' in response.json
