# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    weather_data: dict = read_from_api()
    rainy_day: dict = find_rainy_day()
    if not rainy_day:
        rainy_day = days[-1]

    json_result = to_json(rainy_day)
    write_to_webhook(json_result)


