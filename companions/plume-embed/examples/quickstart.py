from plume_embed import EmbeddingIndex

index = EmbeddingIndex(dim=4)
index.add("alpha", [1, 0, 0, 0])
index.add("beta", [0, 1, 0, 0])
index.add("gamma", [0, 0, 1, 0])

print(index.search([0.8, 0.2, 0, 0], k=2))
