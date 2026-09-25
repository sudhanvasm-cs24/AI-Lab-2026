room_a = input("ROOM_A enter clean/dirty (c/d): ")
room_b = input("ROOM_B enter clean/dirty (c/d): ")
rooms = [room_a, room_b]
vacuum = int(input("Enter initial position of vacuum cleaner(1-A)(2-B): ")) - 1


for i in range(4):
    current_room_label = 'A' if vacuum == 0 else 'B'
    current_status = rooms[vacuum]

    print(f"\n[Step {i+1}] Vacuum is in Room {current_room_label}")


    if current_status == "d":
        print(f"Action: Perceived DIRTY -> CLEANING Room {current_room_label}")
        rooms[vacuum] = "c"
    else:
        print(f"Action: Perceived CLEAN -> MOVING to next room")
        vacuum = (vacuum + 1) % len(rooms)
