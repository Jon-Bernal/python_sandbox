with open("try_me_result.py", "w") as file_handler:
    file_handler.write("print('Hello World!!!!!')")
    file_handler.close()

with open("try_me_result.py", "r") as fh:
    content = fh.read()
    fh.close()
    print(content)

with open("try_me_result.py", "a") as fh:
    fh.write("\nTesting line #2")
    fh.close()

with open("try_me_result.py", "r") as fh:
    content = fh.read()
    fh.close()
    print(content)