import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def test_client() -> TestClient:
    from src.main import create_app

    return TestClient(create_app())
