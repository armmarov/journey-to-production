from app import create_app

flask_app = create_app()

def test_health():
  
  with flask_app.test_client() as test_client:
    response = test_client.get("/health")
    status_code = response.status_code

    assert status_code==200

