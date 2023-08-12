from decimal import Decimal

from bs4 import BeautifulSoup

from celery import shared_task

from currency import choices as ch
from currency import consts
from currency.models import Rate, Source

from django.conf import settings
from django.core.mail import send_mail

import requests


def strip_text(strip_str):
    return strip_str.text.strip()


def round_currency(num):
    return Decimal(num).quantize(Decimal('.01'))


def check_and_create(buy_check, sale_check, curr_type_check, source_check):

    last_rate = Rate.objects.filter(
        type=curr_type_check,
        source=source_check,
        ).order_by('created').last()

    if (
        last_rate is None or  # first attempt to parse (last rate does not exist)
        last_rate.sale != sale_check or  # last lase changed
        last_rate.buy != buy_check  # last buy changed
    ):
        Rate.objects.create(
            type=curr_type_check,
            sale=sale_check,
            buy=buy_check,
            source=source_check,
            )


@shared_task
def contact_us(subject, body):
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [settings.SUPPORT_EMAIL],
        fail_silently=False,
    )


@shared_task
def parse_privatbank():
    privatbank_currency_url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(privatbank_currency_url)

    response.raise_for_status()

    rates = response.json()
    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_PRIVATBANK,
        defaults={'name': 'PrivatBank'},
    )[0]

    for rate in rates:
        currency_type = rate['ccy']
        if currency_type in ch.available_currency_types:
            ct = ch.available_currency_types[currency_type]

            sale = round_currency(rate['sale'])
            buy = round_currency(rate['buy'])

            check_and_create(buy_check=buy, sale_check=sale, source_check=source, curr_type_check=ct)


@shared_task
def parse_bank_com_ua():
    currency_url = 'https://bank.com.ua'

    response = requests.get(currency_url)

    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    soup = soup.find('div', {'class': 'course-table__body'})
    rows = soup.find_all('div', {'class': 'course-table__row'})

    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_PIVDENNIY,
        defaults={'name': 'Bank Pivdenniy'}
    )[0]

    for index, row in enumerate(rows):
        if index == 0:
            continue
        wrapper = row.find('div', {'class': 'wrapper'})
        cols = wrapper.findChildren('div')
        name = strip_text(cols[0])[: 3]
        buy = round_currency(strip_text(cols[1]))
        sell = round_currency(strip_text(cols[2]))

        ct = ch.available_currency_types[name]

        check_and_create(buy_check=buy, sale_check=sell, source_check=source, curr_type_check=ct)


@shared_task
def parse_monobank():
    currency_url = 'https://api.monobank.ua/bank/currency'

    response = requests.get(currency_url)

    response.raise_for_status()

    USD_code = 840
    EUR_code = 978
    rates_dict_codes = {USD_code: "USD", EUR_code: "EUR"}
    UAH_code = 980

    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_MONOBANK,
        defaults={'name': 'Monobank'}
    )[0]

    for rate in response.json():
        if (int(rate["currencyCodeA"]) in rates_dict_codes.keys()) and (rate["currencyCodeB"] == UAH_code):
            curr_type = ch.available_currency_types[rates_dict_codes[rate["currencyCodeA"]]]
            buy = round_currency(rate["rateBuy"])
            sell = round_currency(rate["rateSell"])

            check_and_create(curr_type_check=curr_type, source_check=source, sale_check=sell, buy_check=buy)


@shared_task
def parse_vkurse_dp():
    currency_url = 'https://vkurse.dp.ua/course.json'

    response = requests.get(currency_url).json()

    avialable_currencies = {"Dollar": "USD", "Euro": "EUR"}

    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_VKURSE_DP,
        defaults={'name': 'Vkurse.dp'}
    )[0]

    for rate_name in response.keys():
        if rate_name in avialable_currencies.keys():
            buy = round_currency(response[rate_name]["buy"])
            sell = round_currency(response[rate_name]["sale"])

            check_and_create(
                curr_type_check=ch.available_currency_types[avialable_currencies[rate_name]],
                source_check=source,
                sale_check=sell,
                buy_check=buy
                )


@shared_task
def parse_minfin():
    currency_url = 'https://minfin.com.ua/ua/currency/'

    response = requests.get(currency_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    data = soup.find('tbody')

    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_MINFIN,
        defaults={'name': 'Minfin'}
    )[0]

    for rate_info in data.find_all('tr'):
        curr_name = strip_text(rate_info.find('a'))
        if curr_name in ch.available_currency_types:
            details = rate_info.find_all('div', {'type': 'average'})
            for details_num in range(0, len(details), 3):
                buy = strip_text(details[int(details_num)])[:-5]
                buy = round_currency(buy.replace(',', '.'))
                sell = strip_text(details[int(details_num+1)])[:-5]
                sell = round_currency(sell.replace(',', '.'))

                check_and_create(
                    curr_type_check=ch.available_currency_types[curr_name],
                    source_check=source,
                    sale_check=sell,
                    buy_check=buy
                    )
