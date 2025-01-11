from g4f.client import Client
import asyncio


def gpt(promt):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user",
                   "content": f"Тебе нужно побыть в роли модератора чата комментариев в телеграме. Нужно удалять все рекламные сообщения(любое сообщение которое рассказывает о каких либо услугах магазинах и тд) не цензурные выражения."
                              f"Ответь ДА если сообщени нужно удалить и ответь НЕТ если мы не удаляем сообщение. Ниже напиши почему."
                              f"\nФормат ответа: "
                              f"\nДА/НЕТ"
                              f"\nПричина"
                              f"\nВот сообщение которое нужо проверить:"
                              f"\n{promt}"},
                  ],
    )
    return str(response.choices[0].message.content)


def chek(qquestionnaire):
    while True:
        uns = gpt(qquestionnaire)
        unswer = uns.split('\n')
        print(uns)
        if unswer[0].lower()[0:3] == 'нет':
            return [False, f'{uns[4::]}']
        elif unswer[0].lower()[0:2] == 'да':
            return [True, f'{uns[4::]}']
