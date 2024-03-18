def main():
    with open("sky.jpg","rb") as existing_image, open("new_sky.jpg", "wb") as new_image:

        for each_line_bytes in existing_image:
            new_image.write(each_line_bytes)

    with open("new_sky.jpg", "rb") as file2:
        read_data= file2.read()
        print(read_data)

if __name__ == "__main__":
    main()
