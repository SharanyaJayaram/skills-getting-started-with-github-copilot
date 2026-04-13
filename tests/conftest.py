import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset the activities database before each test"""
    # Store original state
    original_state = {k: {**v, "participants": v["participants"].copy()} for k, v in activities.items()}
    
    yield
    
    # Restore original state after test
    activities.clear()
    activities.update(original_state)
