"""Bài 1: publish lời chào lên topic iot/lab/message."""

from mqtt_config import connect, create_client


TOPIC = "iot/lab/message"


def main() -> None:
    students = "B23DCCN012 - Bùi Tuấn Anh; B23DCCN152 - Trịnh Quốc Đạt"
    client = create_client("python-lab-bai1-publisher")
    try:
        connect(client)
        client.loop_start()
        print(f"Da ket noi MQTT. Topic: {TOPIC}")
        print("Nhap loi chao; nhap EXIT de ket thuc.")
        while True:
            greeting = input("Noi dung: ").strip()
            if greeting.upper() == "EXIT":
                break
            if not greeting:
                continue
            payload = f"{greeting} - {students}"
            info = client.publish(TOPIC, payload, qos=1)
            info.wait_for_publish()
            print(f"Da gui: {payload}")
    except (OSError, KeyboardInterrupt) as exc:
        if isinstance(exc, OSError):
            print(f"Loi MQTT: {exc}")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
