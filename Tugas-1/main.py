from src.image_convert import convert_image

def main():
    image_path = 'images/people.png'
    try:
        convert_image(image_path)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()