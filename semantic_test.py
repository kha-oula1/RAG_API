import requests

def test_kubernetes_query():
    url = "http://127.0.0.1:8000/query"
    params = {"q": "What is Kubernetes?"}

    response = requests.post(url, params=params)

    if response.status_code != 200:
        raise Exception(
            f"Server returned {response.status_code}: {response.text}"
        )

    data = response.json()
    answer = data.get("answer", "")

    if not answer:
        raise AssertionError("API returned an empty answer")

    # Check for key concepts
    answer_lower = answer.lower()

    assert "kubernetes" in answer_lower, \
        "Missing 'Kubernetes' keyword"

    assert "container" in answer_lower or "orchestration" in answer_lower, \
        "Answer does not contain relevant Kubernetes concepts"

    print("Kubernetes query test passed")


if __name__ == "__main__":
    test_kubernetes_query()
    print("All semantic tests passed!")