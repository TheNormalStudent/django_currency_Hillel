from currency.tasks import parse_privatbank, parse_monobank, parse_vkurse_dp
from currency.models import Rate

from unittest.mock import MagicMock

def unique(response, response2, mock, parse):
    initial_num_rate = Rate.objects.all().count()
    requests_get_mock = mock.patch('requests.get')
    requests_get_mock.return_value = MagicMock(json=lambda: response)

    parse()
    assert Rate.objects.all().count() == initial_num_rate + 2

    parse()
    assert Rate.objects.all().count() == initial_num_rate + 2

    requests_get_mock.return_value = MagicMock(json=lambda: response2 )

    parse()
    assert Rate.objects.all().count() == initial_num_rate + 4


def test_parse_privatbank(mocker):
    privat_response = [
        {"ccy":"EUR","base_ccy":"UAH","buy":"40.10000","sale":"41.10000"},
        {"ccy":"USD","base_ccy":"UAH","buy":"37.50000","sale":"38.10000"}]

    privat_response2 = [
        {"ccy":"EUR","base_ccy":"UAH","buy":"40.00000","sale":"41.10000"},
        {"ccy":"USD","base_ccy":"UAH","buy":"37.40000","sale":"38.10000"}]

    unique(privat_response, privat_response2, mocker, parse_privatbank)


def test_parse_monobank(mocker):
    mono_response = [
    {"currencyCodeA":840,"currencyCodeB":980,"date":1694898073,"rateBuy":36.65,"rateCross":0,"rateSell":37.4406},
    {"currencyCodeA":978,"currencyCodeB":980,"date":1694898073,"rateBuy":39.03,"rateCross":0,"rateSell":40.4008}]

    mono_response2 = [
    {"currencyCodeA":840,"currencyCodeB":980,"date":1694898073,"rateBuy":36.66,"rateCross":0,"rateSell":37.4406},
    {"currencyCodeA":978,"currencyCodeB":980,"date":1694898073,"rateBuy":39.04,"rateCross":0,"rateSell":40.4008}]

    unique(mono_response, mono_response2, mocker, parse_monobank)



def test_parse_vkurse(mocker):
    vkurse_response = { "Dollar" : {
		"buy" : "38.10",
		"sale" : "38.35"
	},
	"Euro" : {
		"buy" : "41.00",
		"sale" : "41.20"
	},
	"Pln" : {
		"buy" : "8.70",
		"sale" : "9.00"
	}}

    vkurse_response2 = { "Dollar" : {
		"buy" : "38.20",
		"sale" : "38.35"
	},
	"Euro" : {
		"buy" : "41.10",
		"sale" : "41.20"
	},
	"Pln" : {
		"buy" : "8.70",
		"sale" : "9.00"
	}}

    unique(vkurse_response, vkurse_response2, mocker, parse_vkurse_dp)