import cv2
import time
import os


class FaceDetector:
    def __init__(self, camera_index=0, photo_delay=5, output_dir='photos'):
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        self.cap = cv2.VideoCapture(camera_index)

        self.take_photo = False
        self.detection_time = None
        self.photo_delay = photo_delay
        self.last_photo_time = 0
        self.cooldown = 10

        self.ui_on = True
        self.save_ui = True
        self.show_boxes = True
        self.save_boxes = True

        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

        self.faces_detected = 0
        self.photos_taken = 0
        self.start_time = time.time()

    def set_ui_settings(self, ui_on, save_ui, show_boxes=None, save_boxes=None):
        self.ui_on = ui_on
        self.save_ui = save_ui
        if show_boxes is not None:
            self.show_boxes = show_boxes
        else:
            self.show_boxes = save_ui
        if save_boxes is not None:
            self.save_boxes = save_boxes
        else:
            self.save_boxes = save_ui

    def set_cooldown(self, cooldown):
        self.cooldown = cooldown

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        return faces

    def draw_boxes(self, frame, faces):
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return frame

    def process_frame(self, frame):
        faces = self.detect_faces(frame)

        current_time = time.time()
        cooldown_remaining = max(0, self.cooldown - (current_time - self.last_photo_time))
        in_cooldown = cooldown_remaining > 0

        if len(faces) > 0 and not self.take_photo and not in_cooldown:
            self.faces_detected += len(faces)
            self.take_photo = True
            self.detection_time = current_time
            print(f"Yüz algılandı! {self.photo_delay} saniye sonra fotograf çekilecek...")

        frame_with_ui = frame.copy()

        if self.show_boxes or (self.take_photo and self.save_boxes):
            frame_with_ui = self.draw_boxes(frame_with_ui, faces)

        if self.take_photo:
            elapsed_time = current_time - self.detection_time

            if self.ui_on or (self.save_ui and self.take_photo):
                countdown = max(0, self.photo_delay - int(elapsed_time))
                cv2.putText(frame_with_ui, f"Fotograf: {countdown}s", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                cv2.putText(frame_with_ui, f"Cooldown: {int(cooldown_remaining)}s", (10, 170),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255) if in_cooldown else (0, 255, 0), 2)

            if elapsed_time >= self.photo_delay:
                if self.save_ui and self.save_boxes:
                    photo_frame = frame_with_ui
                elif self.save_ui:
                    photo_frame = frame.copy()
                    cv2.putText(photo_frame, f"Fotograf: 0s", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    photo_frame = frame

                self._take_photo(photo_frame)
                self.take_photo = False
                self.last_photo_time = time.time()
        else:
            if self.ui_on and in_cooldown:
                cv2.putText(frame_with_ui, f"Cooldown: {int(cooldown_remaining)}s", (10, 170),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        self._display_stats(frame_with_ui if self.ui_on else frame)

        return frame_with_ui if self.ui_on or (self.take_photo and self.show_boxes) else frame

    def _take_photo(self, frame):
        photo_name = os.path.join(self.output_dir, f"foto_{int(time.time())}.jpg")
        cv2.imwrite(photo_name, frame)
        self.photos_taken += 1
        print(f"Fotograf çekildi: {photo_name}")

    def _display_stats(self, frame):
        elapsed_time = time.time() - self.start_time
        fps = self.photos_taken / elapsed_time if elapsed_time > 0 else 0

        if self.ui_on:
            cv2.putText(frame, f"FPS: {fps:.2f}", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, f"Yuzler: {self.faces_detected}", (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, f"Fotograflar: {self.photos_taken}", (10, 130),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def run(self):
        self._get_user_settings()

        while True:
            ret, frame = self.cap.read()

            if not ret:
                break

            frame = self.process_frame(frame)

            cv2.imshow('Yuz Tanima - Foto Cekme', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.release()

    def _get_user_settings(self):
        print("\n--- Ayarları Yapılandırın ---")

        ui_on = input("UI elemanlarını gösterilsin mi? (e/h): ").lower() == 'e'

        save_ui = input("UI elemanları fotograflara kaydedilsin mi? (e/h): ").lower() == 'e'

        show_boxes = input("Mavi yüz kutuları gösterilsin mi? (e/h): ").lower() == 'e'

        save_boxes = input("Mavi yüz kutuları fotograflara kaydedilsin mi? (e/h): ").lower() == 'e'

        self.set_ui_settings(ui_on, save_ui, show_boxes, save_boxes)

        try:
            cooldown = float(input("fotograf çekme cooldown süresi (saniye): "))
            self.set_cooldown(max(0, cooldown))
        except ValueError:
            print("Geçersiz giriş, varsayılan cooldown (10s) kullanılacak.")
            self.set_cooldown(10)

        print("\nProgram başlatılıyor...\n")