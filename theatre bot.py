import telebot
from bs4 import BeautifulSoup
import requests
from PIL import Image

bot = telebot.TeleBot("TOKEN")
message1 = None
dict = {1: "Театр был основан 22 декабря 1906 года",
        2: "Первая труппа театра, игравшая во всех постановках первые несколько лет существования театра,"
           " называлась \"Сайяр\", что в переводе с татарского означает \"Передвижник\"(так назвал труппу народный поэт Габдулла Тукай)",
        3: "Основателем первой профессиональной татарской театральной труппы является оренбургский учитель, многогранная личность Ильяс "
           "Кудашев-Ашказарский (1884-1942). Позднее в труппу был принят артист, режиссер Габдулла Кариев (1886-1920), ставший ее руководителем"
           " и еще при жизни названный \"отцом татарского театра\".",
        4: "В 1923 году в г. Казани открывается театральный техникум, педагогами которого становятся ведущие мастера татарской сцены(многие из них - артисты театра им. Камала)",
        5: "В 1966 году на должность главного режиссера приходит Марсель Салимжанов (1934-2002). С его именем связана славная пора зрелого театрального искусства Татарстана. "
           "С первых постановок становится ясно, что в театр пришел лидер, творец, утверждающий диктатуру режиссуры. Под его руководством было поставлено множество пьес, "
           "сыскавших ошеломительный успех среди зрителей и критиков",
        6: "Множество пьес, поставленных в этом театре были удостоены премий. Таковых огромное множество, поэтому назову вам самые важные и авторитетные:"
           "1) Премия им. Габдуллы Тукая, спектакль \"Без ветрил\" 1958г."
           "2) Государственная премия РСФСР им. К.С.Станиславского, актер Ринат Тазетдинов 1985г."
           "3) “Золотая маска” в номинации “За честь и достоинство”, режиссёр М. Х. Салимжанов 2001г."
           "и многие-многие другие",
        7: "Международный театральный фестиваль тюркских народов \"Науруз\" и  Всероссийский фестиваль молодой татарской режиссуры \"Ремесло\" ",
        8: "Театр активно гастролировал по России, ближнему и дальнему Зарубежью и завоевал большой успех у зрителей Казахстана, Кыргызстана, Азербайджана, Литвы"
           "Латвии, Эстонии, Германии, Финляндии, Турции, Великобритании, Колумбии, Испании, Китая, Венгрии и др.",
        9: "В настоящий момент директором театра является Якупов Ильфир Ильшатович, а главным режиссёром Бикчантаев Фарид Рафкатович",
        10_1: "1. Значительная часть действия российского комедийного фильма \"Сокровища O.K.\" проходит на крыше, сцене и в зрительном "
              "зале театра, а из подвала театра герои фильма нашли ход к заветным сокровищам. Кроме этого в фильме снимались ряд актеров Театра им. Камала: Рамиль Тухватуллин, Халима Искандерова и др.\n",
        10_2: "2. Во время Великой Отечественной войны сотрудниками театра было собрано и направлено в фонд Победы 120 тыс. руб. После этого Иосиф Виссарионович Сталин направил благодарственное письмо, "
              "в котором передал «свой братский привет». Это письмо и по сей день хранится в музее при театре.\n",
        10_3: "3. К столетию в театре работники музея подготовили уголок с интерьером комнаты и личными вещами Галиаскара Камала. Там стоит книжный шкаф, большой писательский стол, венские стулья, буфет, "
              "зеркало и часы. Самые дорогие экспонаты музея театра Камала — это личные вещи Карима Тинчурина. Он стал жертвой сталинизма. В 1937 году его арестовали, а уже в 1938-м расстреляли. Его жена "
              "Захида Тинчурина в течение многих лет хранила личные вещи драматурга. Позже их передали на хранение в театр им. Г. Камала. Самым дорогим и ценным экспонатом театра являются золотые часы Карима Тинчурина, подаренные ему труппой «Сайяр».\n",
        10_4: "4. На постановке спектакля «Банкрот» по сцене театра ходил трамвай. Из-за того, что настоящий трамвай сцена бы не выдержала, бутафоры обратились к инженерам, занимающимися проектировкой трамваев(в том числе МТВ-82). Совместными усилиями "
              "был изобртетён облегчённый и, что самое важное, самоходный трамвай.\n",
        10_5: "5. В 2001 года один из режиссеров Театра Камала Марсель Салимжанов был отмечен престижной росийской национальной театральнйо премией «Золотая маска»"}


@bot.message_handler(commands=['start'])
def welcome(message):
    global message1
    message1 = message
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Узнать о театре")
    item2 = telebot.types.KeyboardButton("Последние новости")
    item3 = telebot.types.KeyboardButton('Начать новый сеанс')
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, я могу ответить на интересующие "
                     "вас вопросы или предложить последние новости о театре".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, lalala)


@bot.message_handler(content_types=['text'])
def lalala(message):
    global length
    if message.text == 'Узнать о театре':
        keyboard1 = telebot.types.InlineKeyboardMarkup()
        key_1 = telebot.types.InlineKeyboardButton(text="В каком году был основан театр?", callback_data='1')
        keyboard1.add(key_1)
        key_2 = telebot.types.InlineKeyboardButton(text="Как называлась первая труппа?", callback_data='2')
        keyboard1.add(key_2)
        key_3 = telebot.types.InlineKeyboardButton(text="Кто основатель театра?", callback_data='3')
        keyboard1.add(key_3)
        key_4 = telebot.types.InlineKeyboardButton(text="В каком году открылся первый Казанский театральный техникум?",
                                                   callback_data='4')
        keyboard1.add(key_4)
        key_5 = telebot.types.InlineKeyboardButton(text="Кто такой Марсель Салимжанов?", callback_data='5')
        keyboard1.add(key_5)
        key_6 = telebot.types.InlineKeyboardButton(text="Лауреаты каких премий стали артисты театра?",
                                                   callback_data='6')
        keyboard1.add(key_6)
        key_7 = telebot.types.InlineKeyboardButton(text="Какие фестивали проводил театр?", callback_data='7')
        keyboard1.add(key_7)
        key_8 = telebot.types.InlineKeyboardButton(text="По каким странам гастролировал театр?", callback_data='8')
        keyboard1.add(key_8)
        key_9 = telebot.types.InlineKeyboardButton(text="Кто сейчас руководит театром?", callback_data='9')
        keyboard1.add(key_9)
        key_10 = telebot.types.InlineKeyboardButton(text="Хочу узнать интересные факты", callback_data='10')
        keyboard1.add(key_10)
        bot.send_message(message.chat.id, text="Выберите один из популярных вопросов:", reply_markup=keyboard1)
    elif message.text == "Последние новости":
        data = 'https://kamalteatr.ru/about-the-theatre/media/'
        r = requests.get(data).text
        s = BeautifulSoup(r, 'html.parser')
        mas = []
        mas_date = []
        for item in s.find_all('h2'):
            if str(item.string) != 'Спонсоры' and str(item.string).strip() is not None:
                if 'Ильшат Латыпов' not in str(item.string):
                    mas.append(str(item.string))
                else:
                    break
        for el in s.find_all('div'):
            if str(type(el.get('class'))) == "<class 'list'>":
                if el.get('class') == ["date"]:
                    if str(el.string) not in mas_date:
                        mas_date.append(str(el.string))
        if len(mas) != len(mas_date):
            length = min(len(mas), len(mas_date))
        for i in range(length):
            if len(mas_date[i].split()) == 1:
                index = 0
            else:
                index = 1
            bot.send_message(message.chat.id, mas[i] + "\n" + mas_date[i].split()[index])
        else:
            bot.send_message(message.chat.id, "Последние новости закончились")
    elif message.text == 'Начать новый сеанс':
        global message1
        message1 = message
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("Узнать о театре")
        item2 = telebot.types.KeyboardButton("Последние новости")
        item3 = telebot.types.KeyboardButton('Начать новый сеанс')
        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id,
                         "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, я могу ответить на интересующие "
                         "вас вопросы или предложить последние новости о театре".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю. Попробуйте задать другой вопрос')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global message1
    if call.data == "10":
        im1 = Image.open("10_1.jpg")
        im2 = Image.open("10_2.jpg")
        im3 = Image.open("10_3.jpg")
        im4 = Image.open("10_4.jpg")
        im5 = Image.open("10_5.jpg")
        bot.send_message(message1.chat.id, dict[10_1])
        bot.send_photo(message1.chat.id, im1)
        bot.send_message(message1.chat.id, dict[10_2])
        bot.send_photo(message1.chat.id, im2)
        bot.send_message(message1.chat.id, dict[10_3])
        bot.send_photo(message1.chat.id, im3)
        bot.send_message(message1.chat.id, dict[10_4])
        bot.send_photo(message1.chat.id, im4)
        bot.send_message(message1.chat.id, dict[10_5])
        bot.send_photo(message1.chat.id, im5)
    ns = [1, 2, 3, 4, 5, 9]
    for i in range(1, 10):
        if call.data == str(i):
            bot.send_message(message1.chat.id, dict[i])
            if i in ns:
                im = Image.open(str(i) + ".jpg")
                bot.send_photo(message1.chat.id, im)
                break


bot.polling(none_stop=True)
