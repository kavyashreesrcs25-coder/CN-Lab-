
def main():
    capacity = int(input("Enter bucket size: "))
    rate = int(input("Enter processing rate: "))
    seconds = int(input("Enter number of seconds: "))

    packets = []

    for i in range(seconds):
        size = int(input(f"Enter packet size at {i + 1} sec: "))
        packets.append(size)

    count = 0

    print("\nSec | Received | Sent | Left | Dropped")

    for i in range(seconds):
        count += packets[i]

        dropped = 0

        if count > capacity:
            dropped = count - capacity
            count = capacity

        sent = min(count, rate)
        count -= sent

        print(i + 1, "  |", packets[i], "       |",
              sent, "  |", count, "   |", dropped)

    while count > 0:
        sent = min(count, rate)
        count -= sent

        print("   | 0        |", sent, "  |",
              count, "   | 0")


if __name__ == "__main__":
    main()
