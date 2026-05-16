from ffmpeg_converter import convert


def main():
    print("Hello from crudos!")
    video_name = input("Enter video name (without extension): ").strip()
    if not video_name:
        print("No video name provided. Exiting.")
        return
    convert(video_name)


if __name__ == "__main__":
    main()
