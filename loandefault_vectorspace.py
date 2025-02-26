## Vector Space Representation
from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([
    [750, 50000, 0.3],
    [680, 60000, 0.25],
    [720, 55000, 0.35]
])

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)
print("Vector Space Representation:", data_scaled)

## Applying PCA
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)
print("Reduced Dimensions:", data_pca)