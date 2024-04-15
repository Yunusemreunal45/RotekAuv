import cv2

# Video kaynağını belirleme
cap = cv2.VideoCapture(0)

while True:
    # Frame okuma
    ret, frame = cap.read()

    # Kırmızı renk aralığına göre filtreleme
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = (0, 50, 50)
    upper_red = (10, 255, 255)
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Cismin yüzeyindeki pikselleri belirleme
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        # En büyük contour'u seçme
        c = max(contours, key=cv2.contourArea)

        # Orta noktayı hesaplama
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0

        # Orta noktanın görüntülenmesi
        cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)
        cv2.drawContours(frame, [c], -1, (0, 0, 255), 5)

    # Görüntüyü gösterme
    cv2.imshow("Frame", frame)

    # Döngüyü kesme
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Kaynakları serbest bırakma
cap.release()
cv2.destroyAllWindows()
