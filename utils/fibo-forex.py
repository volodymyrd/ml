import mechanize


def fill_form(url, form_name, pair, interval, start_date, end_date):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.open(url)
    br.select_form(name=form_name)

    pair_input = br.find_control(id='QuoteDownloadModel_val')
    pair_input.readonly = False
    pair_input.value = pair

    interval_input = br.find_control(id='QuoteDownloadModel_interval')
    interval_input.readonly = False
    interval_input.value = interval

    start_date_input = br.find_control(id='QuoteDownloadModel_startdata')
    start_date_input.readonly = False
    start_date_input.value = start_date

    end_date_input = br.find_control(id='QuoteDownloadModel_enddata')
    end_date_input.readonly = False
    end_date_input.value = end_date

    response2 = br.submit()
    with open(pair + "_" + interval + "_" + start_date + "_" + end_date + ".zip", 'w') as f:
        f.write(response2.read())


if __name__ == '__main__':
    fill_form("https://www.fibo-forex.org/analytics/quotesArchive",
              "quotesArchiveForm",
              "EURPLN",
              "60",
              '2005-07-21',
              '2018-08-07')
