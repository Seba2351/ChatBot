import random


def random_string():
    random_list = [
        "Spróbuj napisać coś bardziej sensownego.",
        "Och! Wygląda na to, że napisałeś coś, czego jeszcze nie rozumiem",
        "Strasznie przepraszam, nie do końca zrozumiałem.",
        "Jeszcze nie mogę odpowiedzieć, proszę spróbuj zapytać o coś innego",
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]