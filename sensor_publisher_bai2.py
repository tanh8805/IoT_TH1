"""Bài 2: mô phỏng sensor gửi nhiệt độ và độ ẩm mỗi 3 giây."""

import json
import random
import time

from mqtt_config import connect, create_client


TOPIC = "iot/lab/sensor01/data"


def main() -> None:
    client = create_client("python-lab-sensor01")
    try:
        connect(client)
        client.loop_start()
        print(f"Da ket noi MQTT. Gui du lieu moi 3 giay len {TOPIC}; Ctrl+C de dung.")
        while True:
            reading = {
                "device_id": "sensor01",
                "temperature": round(random.uniform(20.0, 40.0), 1),
                "humidity": round(random.uniform(30.0, 80.0), 1),
            }
            payload = json.dumps(reading, ensure_ascii=False)
            client.publish(TOPIC, payload, qos=1)
            print(f"Da gui: {payload}")
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nDa dung sensor publisher.")
    except OSError as exc:
        print(f"Loi MQTT: {exc}")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
