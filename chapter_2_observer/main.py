from subject import WeatherData
from observer import CurrentConditionsDisplay, StatisticDisplay, ForecastDisplay


if __name__ == "__main__":
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    statistic_display = StatisticDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 70, 29.2)
    print('----------------forecast display unsubscribe------------------')
    weather_data.remove_observer(forecast_display)
    weather_data.set_measurements(80, 70, 29.2)
    weather_data.set_measurements(82, 70, 29.2)
    print('----------------statistic display unsubscribe------------------')
    weather_data.remove_observer(statistic_display)
    weather_data.set_measurements(80, 65, 29.2)
    print('----------------forecast display re-subscribe------------------')
    weather_data.register_observer(forecast_display)
    weather_data.set_measurements(85, 60, 29.2)
