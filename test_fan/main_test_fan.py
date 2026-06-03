from fan_class import Fan

def TestFan():
    fan1 = Fan()
    fan1.setSpeed(Fan.FAST)
    fan1.setRadius(10)
    fan1.setColor("yellow")
    fan1.setOn(True)

    fan2 = Fan()
    fan2.setSpeed(Fan.MEDIUM)
    fan2.setRadius(5)
    fan2.setColor("blue")
    fan2.setOn(False)

    print("=" * 30)
    print("Fan 1")
    print("=" * 30)
    print(fan1)

    print()
    print("=" * 30)
    print("Fan 2")
    print("=" * 30)
    print(fan2)


if __name__ == "__main__":
    TestFan()