import json
import datetime

WEATHER_JSON: str = "weather.json"


def get_daily_weather(path: str) -> list:
    with open(path) as weather_json:
        weather_data: dict = json.loads(weather_json.read())
    return weather_data["daily"]


def filter_rainy_days(daily_weather: list) -> list:
    return list(filter(lambda dw: dw['weather'][0]['main'] == 'Rain', daily_weather))


def sort_by_date(days: list) -> list:
    sorted_days: list = sorted(days, key=lambda s: int(s['dt']), reverse=True)
    return sorted_days


def extract_date_from_day(day: dict) -> str:
    return datetime.datetime.fromtimestamp(day['dt']).strftime('%d %b %Y')


if __name__ == '__main__':
    weather_data: list = get_daily_weather(WEATHER_JSON)
    rainy_days: list = filter_rainy_days(weather_data)
    rainy_days: list = sort_by_date(rainy_days)

    response: dict = {
        "Answer": "Yes" if len(rainy_days) else "No",
        "Date": extract_date_from_day(rainy_days[0] if len(rainy_days) else weather_data[-1])
    }

    # write_to_webhook(json_result)
