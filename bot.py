import asyncio
import requests
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineQuery, InputTextMessageContent, InlineQueryResultArticle

token = "Telegram Bot token"
apiToken = "Api Key"
bot = Bot(token)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start'])
async def echo(msg: Message):
    return await msg.reply("Дай Боже, " + msg.from_user.full_name + "!\nЯ твій синоптик, щоб дізнатись погоду введи "
                                                                    "/weather та назву міста(/allweather для "
                                                                    "детальної інформації)")


@dispatcher.message_handler(commands=['weather'])
async def getWeather(msg: Message):
    getMessage = msg.text
    getMessage = getMessage.split()
    if len(getMessage) == 3:
        city = getMessage[1] + " " + getMessage[2]
    elif len(getMessage) == 2:
        city = getMessage[1]
    else:
        return await msg.reply("Я не знаю де ти. Напиши назву свого міста в форматі '/weather Львів' 😉")
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + apiToken + "&units=metric"
    r = requests.get(url).json()
    temperature = str(r["main"]["temp"]) + "°C. "
    feelsLike = "\nВідчувається як " + str(r["main"]["feels_like"])
    emoji2 = ""
    if r["main"]["feels_like"] < 0:
        emoji2 = "🤧"
    elif r["main"]["feels_like"] >= 0 and r["main"]["feels_like"] < r["main"]["temp"]:
        emoji2 = "🙁"
    elif r["main"]["feels_like"] > r["main"]["temp"]:
        emoji2 = "😌"
    return await msg.reply("Температура в місті " + city + ": " + temperature + feelsLike + emoji2)


@dispatcher.message_handler(commands=['allweather'])
async def getWeather(msg: Message):
    getMessage = msg.text
    getMessage = getMessage.split()
    if len(getMessage) == 3:
        city = getMessage[1] + " " + getMessage[2]
    elif len(getMessage) == 2:
        city = getMessage[1]
    else:
        return await msg.reply("Я не знаю де ти. Напиши назву свого міста в форматі '/allweather Львів' 😉")
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + apiToken + "&units=metric"
    r = requests.get(url).json()
    temperature = str(r["main"]["temp"]) + "°C. "
    feelsLike = " Відчувається як " + str(r["main"]["feels_like"]) + "°C. "
    tempMin = "\n\nМінімальна температура " + str(r["main"]["temp_min"]) + "°, "
    tempMax = "максимальна температура " + str(r["main"]["temp_max"]) + "°C. "
    pressure = "Тиск " + str(r["main"]["pressure"]) + "hPa, "
    humidity = "вологість " + str(r["main"]["humidity"]) + "%. "
    windSpeed = "Швидкість вітру " + str(r["wind"]["speed"]) + "m/s, "
    windDeg = "напрям " + str(r["wind"]["deg"]) + "°. "
    visibility = int(r["visibility"]) / 1000
    visibility = "Видимість " + str(visibility) + "km"
    description = (r["weather"][0]["description"])
    emoji = ""
    if description == "clear sky":
        if (r["weather"][0]["icon"])[2] == "d":
            emoji = "☀"
        else:
            emoji = "🌕"
        description = "Небо чисте."
    elif description == "few clouds" or description == "few clouds: 11-25%":
        emoji = "🌤"
        description = "Переважно ясно."
    elif description == "scattered clouds" or description == "scattered clouds: 25-50%":
        emoji = "⛅"
        description = "Хмарно."
    elif description == "broken clouds" or description == "broken clouds: 51-84%":
        emoji = "⛅"
        description = "Сильно хмарно."
    elif description == "overcast clouds: 85-100%":
        emoji = "⛅"
        description = "Дуже хмарно"
    elif description == "shower rain":
        emoji = "🌧"
        description = "Злива. Візьміть з собою зонтик☔🙃, а краще сидіть вдома."
    elif description == "rain":
        emoji = "🌦"
        description = "Дощ. Не забудьте зонтик☔🙃"
    elif description == "light rain":
        emoji = "🌦"
        description = "Легенький дощ."
    elif description == "moderate rain":
        emoji = "🌦"
        description = "Помірний дощ."
    elif description == "heavy intensity rain":
        emoji = "🌦"
        description = "Сильний інтенсивний дощ"
    elif description == "very heavy rain":
        emoji = "🌦"
        description = "Дуже сильний дощ."
    elif description == "extreme rain":
        emoji = "🌦"
        description = "Мокрий сніг."
    elif description == "freezing rain":
        emoji = "🌦"
        description = "Морозний дощ, можливо сніг."
    elif description == "light intensity shower rain":
        emoji = "🌦"
        description = "Легенький інтенсивний дощ."
    elif description == "shower rain":
        emoji = "🌦"
        description = "Зливний дощ."
    elif description == "heavy intensity shower rain":
        emoji = "🌦"
        description = "Сильний інтенсивний дощ."
    elif description == "ragged shower rain":
        emoji = "🌦"
        description = "Рваний дощ."
    elif description == "thunderstorm":
        emoji = "⛈"
        description = "Гроза. Не зламайте зонтик зонтик☔🙃, або сидіть вдома."
    elif description == "thunderstorm with light rain":
        emoji = "⛈"
        description = "Гроза з легеньким дощиком."
    elif description == "thunderstorm with rain":
        emoji = "⛈"
        description = "Гроза з дощем."
    elif description == "thunderstorm with heavy rainn":
        emoji = "⛈"
        description = "Гроза з сильним дощиком."
    elif description == "light thunderstorm":
        emoji = "⛈"
        description = "Легенька гроза."
    elif description == "heavy thunderstorm":
        emoji = "⛈"
        description = "Сильна гроза."
    elif description == "ragged thunderstorm":
        emoji = "⛈"
        description = "Рвана гроза."
    elif description == "thunderstorm with light drizzle":
        emoji = "⛈"
        description = "Гроза з невеликою мрякою."
    elif description == "thunderstorm with drizzle":
        emoji = "⛈"
        description = "Гроза з мрякою."
    elif description == "thunderstorm with heavy drizzle":
        emoji = "⛈"
        description = "Гроза з сильною мрякою."
    elif description == "light intensity drizzle":
        emoji = "⛈"
        description = "Легенька інтенсивна мряка."
    elif description == "drizzle":
        emoji = "🌧"
        description = "Мряка."
    elif description == "heavy intensity drizzle":
        emoji = "🌧"
        description = "Сильна інтенсивна мряка."
    elif description == "light intensity drizzle rain":
        emoji = "🌧"
        description = "Легенький інтенсивний сиплий дощ."
    elif description == "drizzle rain":
        emoji = "🌧"
        description = "Сиплий дощ."
    elif description == "heavy intensity drizzle rain":
        emoji = "🌧"
        description = "Сильний інтенсивний сиплий дощ."
    elif description == "shower rain and drizzle":
        emoji = "🌧"
        description = "Злива і мряка"
    elif description == "heavy shower rain and drizzle":
        emoji = "🌧"
        description = "Сильна злива і мряка"
    elif description == "shower drizzle":
        emoji = "🌧"
        description = "Гроза-мряка"
    elif description == "snow":
        emoji = "🌨"
        description = "Сніг❄"
    elif description == "light snow":
        emoji = "🌨"
        description = "Невеликий сніг❄"
    elif description == "Heavy snow":
        emoji = "🌨"
        description = "Сильний сніг❄"
    elif description == "Sleet":
        emoji = "🌨"
        description = "Мокрий сніг❄"
    elif description == "Light shower sleet":
        emoji = "🌨"
        description = "Невеликий мокрий сніг❄"
    elif description == "Shower sleet":
        emoji = "🌨"
        description = "Душовий мокрий сніг❄"
    elif description == "Light rain and snow":
        emoji = "🌨"
        description = "Невеликий дощ і сніг❄"
    elif description == "Rain and snow":
        emoji = "🌨"
        description = "Дощ і сніг❄"
    elif description == "Light shower snow":
        emoji = "🌨"
        description = "Легенький густий сніг❄"
    elif description == "Shower snow":
        emoji = "🌨"
        description = "Густий сніг❄"
    elif description == "Heavy shower snow":
        emoji = "🌨"
        description = "Сильний густий сніг❄"
    elif description == "mist":
        emoji = "🌫"
        description = "Туман."
    elif description == "Smoke":
        emoji = "🌫"
        description = "Дим."
    elif description == "Haze":
        emoji = "🌫"
        description = "Затуманено."
    elif description == "sand/ dust whirls":
        emoji = "🌫"
        description = "Пісок."
    elif description == "fog":
        emoji = "🌫"
        description = "Туман."
    elif description == "sand":
        emoji = "🌫"
        description = "Пісок."
    elif description == "dust":
        emoji = "🌫"
        description = "Пил."
    elif description == "volcanic ash":
        emoji = "🌫"
        description = "Вулканічний попил."
    elif description == "squalls":
        emoji = "🌫"
        description = "Шквал."
    elif description == "tornado":
        emoji = "🌫"
        description = "Смерч."
    else:
        description = description

    emoji2 = ""
    if r["main"]["feels_like"] < 0:
        emoji2 = "🤧"
    elif r["main"]["feels_like"] <= 0 and r["main"]["feels_like"] < r["main"]["temp"]:
        emoji2 = "😟"
    elif r["main"]["feels_like"] > r["main"]["temp"]:
        emoji2 = "😌"
        
    answer = "Зараз температура у місті " + city + " : " + temperature + emoji + description + feelsLike + emoji2 \
             + tempMin + tempMax + pressure + humidity + windSpeed + windDeg + visibility
    return await msg.reply(answer)


@dispatcher.inline_handler()
async def inline(inlineQuery : InlineQuery):
    city = inlineQuery.query
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid="\
          + apiToken + "&units=metric"
    r = requests.get(url).json()
    temperature = str(r["main"]["temp"]) + "°C. "
    feelsLike = " Відчувається як " + str(r["main"]["feels_like"]) + "°C. "
    tempMin = "\n\nМінімальна температура " + str(r["main"]["temp_min"]) + "°, "
    tempMax = "максимальна температура " + str(r["main"]["temp_max"]) + "°C. "
    pressure = "Тиск " + str(r["main"]["pressure"]) + "hPa, "
    humidity = "вологість " + str(r["main"]["humidity"]) + "%. "
    windSpeed = "Швидкість вітру " + str(r["wind"]["speed"]) + "m/s, "
    windDeg = "напрям " + str(r["wind"]["deg"]) + "°. "
    visibility = int(r["visibility"])/1000
    visibility = "Видимість " + str(visibility) + "km"
    description = (r["weather"][0]["description"])
    emoji = ""
    if description == "clear sky":
        if (r["weather"][0]["icon"])[2] == "d":
            emoji = "☀"
        else:
            emoji = "🌕"
        description = "Небо чисте."
    elif description == "few clouds" or description == "few clouds: 11-25%":
        emoji = "🌤"
        description = "Переважно ясно."
    elif description == "scattered clouds" or description == "scattered clouds: 25-50%":
        emoji = "⛅"
        description = "Хмарно."
    elif description == "broken clouds" or description == "broken clouds: 51-84%":
        emoji = "⛅"
        description = "Сильно хмарно."
    elif description == "overcast clouds: 85-100%":
        emoji = "⛅"
        description = "Дуже хмарно"
    elif description == "shower rain":
        emoji = "🌧"
        description = "Злива. Візьміть з собою зонтик☔🙃, а краще сидіть вдома."
    elif description == "rain":
        emoji = "🌦"
        description = "Дощ. Не забудьте зонтик☔🙃"
    elif description == "light rain":
        emoji = "🌦"
        description = "Легенький дощ."
    elif description == "moderate rain":
        emoji = "🌦"
        description = "Помірний дощ."
    elif description == "heavy intensity rain":
        emoji = "🌦"
        description = "Сильний інтенсивний дощ"
    elif description == "very heavy rain":
        emoji = "🌦"
        description = "Дуже сильний дощ."
    elif description == "extreme rain":
        emoji = "🌦"
        description = "Мокрий сніг."
    elif description == "freezing rain":
        emoji = "🌦"
        description = "Морозний дощ, можливо сніг."
    elif description == "light intensity shower rain":
        emoji = "🌦"
        description = "Легенький інтенсивний дощ."
    elif description == "shower rain":
        emoji = "🌦"
        description = "Зливний дощ."
    elif description == "heavy intensity shower rain":
        emoji = "🌦"
        description = "Сильний інтенсивний дощ."
    elif description == "ragged shower rain":
        emoji = "🌦"
        description = "Рваний дощ."
    elif description == "thunderstorm":
        emoji = "⛈"
        description = "Гроза. Не зламайте зонтик зонтик☔🙃, або сидіть вдома."
    elif description == "thunderstorm with light rain":
        emoji = "⛈"
        description = "Гроза з легеньким дощиком."
    elif description == "thunderstorm with rain":
        emoji = "⛈"
        description = "Гроза з дощем."
    elif description == "thunderstorm with heavy rainn":
        emoji = "⛈"
        description = "Гроза з сильним дощиком."
    elif description == "light thunderstorm":
        emoji = "⛈"
        description = "Легенька гроза."
    elif description == "heavy thunderstorm":
        emoji = "⛈"
        description = "Сильна гроза."
    elif description == "ragged thunderstorm":
        emoji = "⛈"
        description = "Рвана гроза."
    elif description == "thunderstorm with light drizzle":
        emoji = "⛈"
        description = "Гроза з невеликою мрякою."
    elif description == "thunderstorm with drizzle":
        emoji = "⛈"
        description = "Гроза з мрякою."
    elif description == "thunderstorm with heavy drizzle":
        emoji = "⛈"
        description = "Гроза з сильною мрякою."
    elif description == "light intensity drizzle":
        emoji = "⛈"
        description = "Легенька інтенсивна мряка."
    elif description == "drizzle":
        emoji = "🌧"
        description = "Мряка."
    elif description == "heavy intensity drizzle":
        emoji = "🌧"
        description = "Сильна інтенсивна мряка."
    elif description == "light intensity drizzle rain":
        emoji = "🌧"
        description = "Легенький інтенсивний сиплий дощ."
    elif description == "drizzle rain":
        emoji = "🌧"
        description = "Сиплий дощ."
    elif description == "heavy intensity drizzle rain":
        emoji = "🌧"
        description = "Сильний інтенсивний сиплий дощ."
    elif description == "shower rain and drizzle":
        emoji = "🌧"
        description = "Злива і мряка"
    elif description == "heavy shower rain and drizzle":
        emoji = "🌧"
        description = "Сильна злива і мряка"
    elif description == "shower drizzle":
        emoji = "🌧"
        description = "Гроза-мряка"
    elif description == "snow":
        emoji = "🌨"
        description = "Сніг❄"
    elif description == "light snow":
        emoji = "🌨"
        description = "Невеликий сніг❄"
    elif description == "Heavy snow":
        emoji = "🌨"
        description = "Сильний сніг❄"
    elif description == "Sleet":
        emoji = "🌨"
        description = "Мокрий сніг❄"
    elif description == "Light shower sleet":
        emoji = "🌨"
        description = "Невеликий мокрий сніг❄"
    elif description == "Shower sleet":
        emoji = "🌨"
        description = "Душовий мокрий сніг❄"
    elif description == "Light rain and snow":
        emoji = "🌨"
        description = "Невеликий дощ і сніг❄"
    elif description == "Rain and snow":
        emoji = "🌨"
        description = "Дощ і сніг❄"
    elif description == "Light shower snow":
        emoji = "🌨"
        description = "Легенький густий сніг❄"
    elif description == "Shower snow":
        emoji = "🌨"
        description = "Густий сніг❄"
    elif description == "Heavy shower snow":
        emoji = "🌨"
        description = "Сильний густий сніг❄"
    elif description == "mist":
        emoji = "🌫"
        description = "Туман."
    elif description == "Smoke":
        emoji = "🌫"
        description = "Дим."
    elif description == "Haze":
        emoji = "🌫"
        description = "Затуманено."
    elif description == "sand/ dust whirls":
        emoji = "🌫"
        description = "Пісок."
    elif description == "fog":
        emoji = "🌫"
        description = "Туман."
    elif description == "sand":
        emoji = "🌫"
        description = "Пісок."
    elif description == "dust":
        emoji = "🌫"
        description = "Пил."
    elif description == "volcanic ash":
        emoji = "🌫"
        description = "Вулканічний попил."
    elif description == "squalls":
        emoji = "🌫"
        description = "Шквал."
    elif description == "tornado":
        emoji = "🌫"
        description = "Смерч."
    else:
        description = description
        
    icon = "http://openweathermap.org/img/wn/" + (r["weather"][0]["icon"]) + "@4x.png"
    
    emoji2 = ""
    if r["main"]["feels_like"] < 0:
        emoji2 = "🤧"
    elif r["main"]["feels_like"] <= 0 and r["main"]["feels_like"] < r["main"]["temp"]:
        emoji2 = "😟"
    elif r["main"]["feels_like"] > r["main"]["temp"]:
        emoji2 = "😌"
    id = "1"
    warmIcon = "https://memepedia.ru/wp-content/uploads/2018/07/cover-3-1.jpg"
    coldIcon = "https://risovach.ru/upload/2016/01/mem/kot_102256910_orig_.jpg"
    
    title = "Температура в місті " + city + ": " + temperature + emoji
    inputTextMessageContent = InputTextMessageContent("Зараз температура у місті " + city + " : " + temperature +
                                                      emoji + description + feelsLike + emoji2 + tempMin + tempMax +
                                                      pressure + humidity + windSpeed + windDeg + visibility)
    item = InlineQueryResultArticle(
        id = id,
        title = title,
        input_message_content=inputTextMessageContent,
        thumb_url=icon,
        description="Твій персональний бот-синоптик"
    )
    await bot.answer_inline_query(inlineQuery.id, results=[item], cache_time=1)
    
asyncio.run(dispatcher.start_polling())