from face_detector import FaceDetector


def main():
    detector = FaceDetector(
        camera_index=0,
        photo_delay=5,
        output_dir='photos'
    )

    detector.run()


if __name__ == "__main__":
    main()


