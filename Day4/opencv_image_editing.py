
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("img.jpg")

if image is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Convert BGR to RGB for Matplotlib
original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 1. Resize image
resized = cv2.resize(image, (300, 300))

# 2. Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Crop image (center crop)
h, w = image.shape[:2]
cropped = image[h//4:3*h//4, w//4:3*w//4]

# 4. Adjust brightness and contrast
bright = cv2.convertScaleAbs(
    image, alpha=1.3, beta=40
)

# 5. Apply Gaussian blur
blurred = cv2.GaussianBlur(image, (15, 15), 0)

# 6. Detect edges
edges = cv2.Canny(gray, 100, 200)

# 7. Flip image horizontally
flipped = cv2.flip(image, 1)

# 8. Rotate image 90 degrees
rotated = cv2.rotate(
    image, cv2.ROTATE_90_CLOCKWISE
)

# 9. Add text to image
text_image = image.copy()
cv2.putText(
    text_image,
    "OpenCV Image Editing",
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
)

# Convert images to RGB for display
images = [
    ("Original", original),
    ("Resized", cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)),
    ("Grayscale", gray),
    ("Cropped", cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)),
    ("Brightness + Contrast", cv2.cvtColor(bright, cv2.COLOR_BGR2RGB)),
    ("Gaussian Blur", cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB)),
    ("Edge Detection", edges),
    ("Flipped", cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)),
    ("Rotated", cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)),
    ("Text Overlay", cv2.cvtColor(text_image, cv2.COLOR_BGR2RGB))
]

# Display all results
plt.figure(figsize=(15, 12))

for i, (title, img) in enumerate(images):
    plt.subplot(3, 4, i + 1)
    plt.imshow(img, cmap="gray" if len(img.shape) == 2 else None)
    plt.title(title)
    plt.axis("off")

plt.tight_layout()
plt.show()

# Save edited image
cv2.imwrite("edited_image.jpg", text_image)

print("Image editing completed!")
print("Edited image saved as edited_image.jpg")