import numpy as np
import matplotlib.pyplot as plt

# -----------------------
# Step 1: Generate Fake Images
# -----------------------
def generate_fake_digit_images(num_images=5):
    # Generate random grayscale images (values between 0 to 255)
    return np.random.randint(200, 256, size=(num_images, 100, 100))

# -----------------------
# Step 2: Normalize Images (0 to 1)
# -----------------------
def normalize_images(images):
    return images / 255.0

# -----------------------
# Step 3: Binarize Images (0 or 1)
# -----------------------
def binarize_images(images, threshold=0.5):
    return (images > threshold).astype(int)

# -----------------------
# Step 4: Flatten Images (28x28 → 784)
# -----------------------
def flatten_images(images):
    num_images = images.shape[0]
    return images.reshape(num_images, -1)

# -----------------------
# Step 5: Compute Statistics
# -----------------------
def image_statistics(flat_images):
    means = np.mean(flat_images, axis=1)
    stds = np.std(flat_images, axis=1)
    return means, stds

# -----------------------
# Main Execution
# -----------------------
if __name__ == "__main__":
    # 1. Generate 5 fake images
    images = generate_fake_digit_images()

    # 2. Normalize
    normalized = normalize_images(images)

    # 3. Binarize
    binarized = binarize_images(normalized)

    # 4. Flatten
    flat_images = flatten_images(binarized)

    # 5. Compute mean & std
    means, stds = image_statistics(flat_images)

    # 6. Show stats
    for idx, (mean, std) in enumerate(zip(means, stds)):
        print(f"Image {idx + 1}: Mean = {mean:.2f}, Std = {std:.2f}")

    # 7. Visualize first image (optional)
    plt.imshow(images[0], cmap='gray')
    plt.title("Sample Fake Digit Image")
    plt.axis('off')
    plt.show()
