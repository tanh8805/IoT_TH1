THUC HANH PYTHON MQTT
=====================

Can chuan bi
------------
- Python 3.x
- Thu vien Python: python -m pip install "paho-mqtt>=1.6,<3"

Broker MQTT
-----------
Broker la may chu trung gian nhan thong diep tu publisher va chuyen cho cac
subscriber da dang ky topic. Bai nay dung broker cong khai HiveMQ tai
broker.hivemq.com:1883, nen khong can cai hay chay Mosquitto. Broker nay dung
chung; khong gui thong tin rieng tu hoac du lieu nhay cam len broker.

Neu lop cap broker khac, dat MQTT_HOST va MQTT_PORT truoc khi chay; neu broker
yeu cau tai khoan, dung MQTT_USERNAME va MQTT_PASSWORD.

Cach chay
---------
Truoc tien cai thu vien o tren. Moi cap chuong trinh can hai terminal rieng,
va khoi dong subscriber/device truoc publisher/controller.

Bai 1 - gui va nhan thong diep:
  Terminal 1: python subscriber_bai1.py
  Terminal 2: python publisher_bai1.py

Publisher cho nhap loi chao; nhap EXIT de ket thuc. Payload gom loi chao va
thong tin hai thanh vien: Bùi Tuấn Anh (B23DCCN012), Trịnh Quốc Đạt
(B23DCCN152).

Bai 2 - mo phong cam bien:
  Terminal 1: python monitor_subscriber_bai2.py
  Terminal 2: python sensor_publisher_bai2.py

Sensor gui JSON moi 3 giay. Monitor hien thi nhiet do, do am va canh bao khi
nhiet do > 35 C hoac do am < 40%. Nhan Ctrl+C de dung.

Bai 3 - dieu khien den:
  Terminal 1: python device_bai3.py
  Terminal 2: python controller_bai3.py

Nhap ON hoac OFF de gui lenh; controller in trang thai phan hoi. Nhap EXIT
hoac nhan Ctrl+C de dung.

Topic su dung
-------------
- Bai 1: iot/lab/message
- Bai 2: iot/lab/sensor01/data
- Bai 3: iot/lab/light01/cmd va iot/lab/light01/status

Cac file bai tap
----------------
publisher_bai1.py, subscriber_bai1.py, sensor_publisher_bai2.py,
monitor_subscriber_bai2.py, device_bai3.py, controller_bai3.py,
mqtt_config.py va README.txt.
