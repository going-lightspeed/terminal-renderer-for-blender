import subprocess

n = int(input("Enter number of first frame: "))
m = int(input("Enter number of last frame: "))
while n <= m:
    print(f"\nRendering frame {n}...")

    enter = subprocess.run(
        ["blender", "-b", "/home/sodium/Downloads/food.blend", "-f", str(n)],
        capture_output=True,
        text=True
    )

    print(enter.stdout)
    print(enter.stderr)
    print("Exit code:", enter.returncode)

    if enter.returncode != 0:
        print(f"Rendering failed at frame {n}.")
        file = open("error.txt", "a")
        file.append("failed frame :",n)
        file.close()
    n = n + 1

print("Rendering loop finished.")
