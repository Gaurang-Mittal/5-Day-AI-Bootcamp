import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from ultralytics import YOLO
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# =========================================================
# 1. FILE PATH
# =========================================================

folder = Path(__file__).parent

image_path = folder / "traffic.jpg"

print("Image path:", image_path)
print("Image exists:", image_path.exists())


# =========================================================
# 2. LOAD YOLO MODEL
# =========================================================

model = YOLO("yolov8n.pt")


# =========================================================
# 3. DETECT OBJECTS
# =========================================================

results = model(str(image_path))


# =========================================================
# 4. VEHICLE CLASSES
# =========================================================

vehicle_classes = {
    2: "car",
    3: "motorcycle",
    5: "bus",
    7: "truck"
}


# =========================================================
# 5. STORE DETECTION DATA
# =========================================================

data = []


for result in results:

    for box in result.boxes:

        class_id = int(box.cls[0])

        confidence = float(box.conf[0])

        # Only process vehicles
        if class_id not in vehicle_classes:
            continue

        vehicle = vehicle_classes[class_id]

        # Bounding box coordinates
        x1, y1, x2, y2 = box.xyxy[0].tolist()

        # Calculate center
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        # Calculate bounding box area
        width = x2 - x1
        height = y2 - y1

        area = width * height

        data.append({
            "vehicle": vehicle,
            "confidence": confidence,
            "x": center_x,
            "y": center_y,
            "width": width,
            "height": height,
            "area": area
        })


# =========================================================
# 6. CREATE PANDAS DATAFRAME
# =========================================================

df = pd.DataFrame(data)


# =========================================================
# 7. CHECK IF VEHICLES WERE FOUND
# =========================================================

if df.empty:

    print("\nNo vehicles detected.")

else:

    print("\n========================================")
    print("       AI TRAFFIC ANALYZER")
    print("========================================")


    # =====================================================
    # 8. VEHICLE COUNTS
    # =====================================================

    vehicle_counts = df["vehicle"].value_counts()


    print("\nVehicle Count:")

    print(vehicle_counts)


    # =====================================================
    # 9. NUMPY ANALYSIS
    # =====================================================

    total_vehicles = len(df)

    average_confidence = np.mean(
        df["confidence"].values
    )

    average_area = np.mean(
        df["area"].values
    )


    print("\nTotal vehicles:", total_vehicles)

    print(
        "Average confidence:",
        round(average_confidence, 3)
    )

    print(
        "Average vehicle area:",
        round(average_area, 2)
    )


    # =====================================================
    # 10. SAVE DATA
    # =====================================================

    csv_path = folder / "traffic_data.csv"

    df.to_csv(csv_path, index=False)

    print("\nData saved to:")

    print(csv_path)


    # =====================================================
    # 11. TRAFFIC LEVEL
    # =====================================================

    # Simple traffic-level feature
    traffic_features = np.array([
        [
            total_vehicles,
            average_confidence,
            average_area
        ]
    ])


    # We need multiple samples for KMeans.
    # Create small variations based on detected data.

    samples = np.array([
        [
            total_vehicles,
            average_confidence,
            average_area
        ],
        [
            total_vehicles * 0.5,
            average_confidence,
            average_area
        ],
        [
            total_vehicles * 2,
            average_confidence,
            average_area
        ]
    ])


    # Scale data
    scaler = StandardScaler()

    scaled_samples = scaler.fit_transform(samples)


    # KMeans clustering
    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    clusters = kmeans.fit_predict(
        scaled_samples
    )


    # Determine cluster belonging to current image
    current_cluster = clusters[0]


    print(
        "\nTraffic cluster:",
        current_cluster
    )


    # =====================================================
    # 12. MATPLOTLIB - VEHICLE COUNT GRAPH
    # =====================================================

    plt.figure(figsize=(8, 5))

    vehicle_counts.plot(
        kind="bar"
    )

    plt.title("Vehicle Distribution")

    plt.xlabel("Vehicle Type")

    plt.ylabel("Number of Vehicles")

    plt.tight_layout()

    plt.savefig(
        folder / "vehicle_distribution.png"
    )

    plt.show()


    # =====================================================
    # 13. MATPLOTLIB - CONFIDENCE GRAPH
    # =====================================================

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["confidence"],
        bins=10
    )

    plt.title(
        "YOLO Detection Confidence"
    )

    plt.xlabel("Confidence")

    plt.ylabel("Number of Detections")

    plt.tight_layout()

    plt.savefig(
        folder / "confidence_distribution.png"
    )

    plt.show()


    # =====================================================
    # 14. DRAW DETECTIONS USING OPENCV
    # =====================================================

    image = cv2.imread(
        str(image_path)
    )


    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])

            if class_id not in vehicle_classes:
                continue

            confidence = float(box.conf[0])

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0].tolist()
            )

            vehicle = vehicle_classes[class_id]

            label = (
                f"{vehicle} "
                f"{confidence:.2f}"
            )


            # Draw bounding box
            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )


            # Draw label
            cv2.putText(
                image,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )


    # =====================================================
    # 15. SAVE FINAL IMAGE
    # =====================================================

    output_image = folder / "traffic_analysis.jpg"

    cv2.imwrite(
        str(output_image),
        image
    )


    print("\nFinal image saved to:")

    print(output_image)


    print("\n========================================")
    print("          ANALYSIS COMPLETE")
    print("========================================")