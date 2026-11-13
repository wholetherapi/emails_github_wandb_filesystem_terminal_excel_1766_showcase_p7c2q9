from plume_embed import EmbeddingIndex


def test_roundtrip_prefers_closest_vector():
    index = EmbeddingIndex(dim=3)
    index.add("left", [1, 0, 0])
    index.add("right", [0, 1, 0])
    results = index.search([0.9, 0.1, 0], k=1)
    assert results[0][0] == "left"


def test_dimension_validation():
    index = EmbeddingIndex(dim=2)
    try:
        index.add("bad", [1, 2, 3])
    except ValueError as exc:
        assert "expected 2 dimensions" in str(exc)
    else:
        raise AssertionError("expected ValueError")
