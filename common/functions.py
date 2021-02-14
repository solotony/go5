#    ____            _           _____
#   / ___|    ___   | |   ___   |_   _|   ___    _ __    _   _
#   \___ \   / _ \  | |  / _ \    | |    / _ \  | '_ \  | | | |
#    ___) | | (_) | | | | (_) |   | |   | (_) | | | | | | |_| |
#   |____/   \___/  |_|  \___/    |_|    \___/  |_| |_|  \__, |
#   1998-2020 (c) SoloTony.com                           |___/
#   v 1.0

import os
from transliterate import slugify
from time import strftime
import re
import logging

logger_hashtags = logging.getLogger('hashtags')

def get_upload_path(folder:str, filename:str)->str:
    '''
        Возвращает путь для сохранения объекта (файла, изображения)
    '''
    file_name, file_extension = os.path.splitext(filename)
    return os.path.join('media', folder, strftime("%Y/%m/%d/"), slugify(file_name, 'ru') + file_extension)

re_hashtag = re.compile(r'##([a-z0-9#_.-]+)##', flags=re.IGNORECASE)

def mytags(str:str)->str:
    '''
        выполняет подстановку хештегов для моих текстов
        ##EMAIL##  ##FEEDBACK##  ##CONTEXT_BRIEF##
    '''

    from solotony.functions import get_hashtags
    HASHTAGS = get_hashtags()

    page_hashtags = re_hashtag.findall(str)
    for hashtag in page_hashtags:
        if hashtag in HASHTAGS:
            str = str.replace('##'+hashtag+'##', HASHTAGS.get(hashtag, ''))
        else:
            logger_hashtags.error('unknown tag ##{}## in text '.format(hashtag))

    # TODO - переделать на обащения к записям !!!

    # str = str.replace('##PORTFOLIO_CAT#tehzadanie##', '<a href="/portfolio/category/tehzadanie">портфолио - Техзадание</a>')
    # str = str.replace('##PORTFOLIO-CAT-URL#tehzadanie##', '/portfolio/category/tehzadanie')
    # str = str.replace('##PORTFOLIO_TAG#magaziny##', '<a href="/portfolio/tag/magaziny">портфолио - интернет-магазины</a>')
    # str = str.replace('##PORTFOLIO-TAG-URL#magaziny##', '/portfolio/category/magaziny')
    # str = str.replace('##SERVICE#base-seo##', '<a href="/services/base-seo">первичная регистрация в поисковых сервисах</a>')
    # str = str.replace('##SERVICE#consultatuion##', '<a href="/services/consultatuion">консультация</a>')
    # str = str.replace('##SERVICE#context##', '<a href="/services/context">контекстная реклама</a>')
    # str = str.replace('##SERVICE#copywriting##', '<a href="/services/copywriting">написание текстов</a>')
    # str = str.replace('##SERVICE#end-to-end-landing##', '<a href="/services/end-to-end-landing">создание лендинга "под ключ"</a>')
    # str = str.replace('##SERVICE#integration1с##', '<a href="/services/integration1с">интеграция с 1С</a>')
    # str = str.replace('##SERVICE#landing##', '<a href="/services/landing">создание лендинга</a>')
    # str = str.replace('##SERVICE#seo##', '<a href="/services/seo">оптимизация сайта</a>')
    # str = str.replace('##SERVICE#shop##', '<a href="/services/shop">создание интернет-магазина</a>')
    # str = str.replace('##SERVICE#site-create##', '<a href="/services/site">создание сайта</a>')
    # str = str.replace('##SERVICE#site-promotion##', '<a href="/services/site-promotion">продвижение сайтов</a>')
    # str = str.replace('##SERVICE#site-vizitka##', '<a href="/services/vizitka">создание сайта визитки</a>')
    # str = str.replace('##SERVICE#tehzadanie##', '<a href="/services/tehzadanie">написание технического задания</a>')
    # str = str.replace('##SERVICE-PRICE#base-seo##', '5000 рублей')
    # str = str.replace('##SERVICE-PRICE#bitrix##', '50000 рублей')
    # str = str.replace('##SERVICE-PRICE#consultatuion##', '5000 рублей')
    # str = str.replace('##SERVICE-PRICE#copywriting##', '500 рублей за текст')
    # str = str.replace('##SERVICE-PRICE#end-to-end-landing##', '50000 рублей')
    # str = str.replace('##SERVICE-PRICE#landing##', '10000 рублей')
    # str = str.replace('##SERVICE-PRICE#per-hour##', '900 рублей в час')
    # str = str.replace('##SERVICE-PRICE#semantic##', '5000 руб')
    # str = str.replace('##SERVICE-PRICE#seo-audit##', '2000 руб')
    # str = str.replace('##SERVICE-PRICE#shop##', '80000 рублей')
    # str = str.replace('##SERVICE-PRICE#site-vizitka##', '20000 рублей')
    # str = str.replace('##SERVICE-PRICE#vizitka##', '20000 рублей')
    # str = str.replace('##SERVICE-PRICE#wordpress##', '20000 рублей')
    # str = str.replace('##SERVICE-URL#behavioral##', '/services/behavioral')
    # str = str.replace('##SERVICE-URL#bitrix##', '/services/bitrix')
    # str = str.replace('##SERVICE-URL#context##', '/services/context')
    # str = str.replace('##SERVICE-URL#end-to-end-landing##', '/services/end-to-end-landing')
    # str = str.replace('##SERVICE-URL#landing##', '/services/landing')
    # str = str.replace('##SERVICE-URL#link-promotion##', '/services/link-promotion')
    # str = str.replace('##SERVICE-URL#per-hour##', '/services/per-hour')
    # str = str.replace('##SERVICE-URL#semantic##', '/services/semantic')
    # str = str.replace('##SERVICE-URL#seo##', '/services/seo')
    # str = str.replace('##SERVICE-URL#seo-audit##', '/services/seo-audit')
    # str = str.replace('##SERVICE-URL#shop##', '/services/shop')
    # str = str.replace('##SERVICE-URL#tehzadanie##', '/services/tehzadanie')
    # str = str.replace('##SERVICE-URL#vizitka##', '/services/vizitka')
    # str = str.replace('##SERVICE-URL#wordpress##', '/services/wordpress')

    # str = str.replace('##SERVICE-ABL#site-promotion##', '<a href="/services/site-promotion">продвижением сайтов</a>')
    # str = str.replace('##SERVICE-GEN#bitrix##', 'создания сайта на битриксе')
    str = str.replace('##SERVICE-GEN#consultatuion##', '<a href="/services/consultatuion">консультации</a>')
    str = str.replace('##SERVICE-GEN#context##', '<a href="/services/context">контекстной рекламы</a>')
    str = str.replace('##SERVICE-GEN#shop##', '<a href="/services/shop">создания интернет магазинов</a>')
    str = str.replace('##SERVICE-GEN#site-create##', '<a href="/services/site">создания сайтов</a>')
    str = str.replace('##SERVICE-GEN#site-vizitka##', '<a href="/services/vizitka">создания сайта визитки</a>')
    str = str.replace('##SERVICE-GEN#wordpress##', 'создания сайта на wordpress')
    str = str.replace('##SERVICE-GET#base-seo##', '<a href="/services/base-seo">первичную регистрацию в поисковых сервисах</a>')
    str = str.replace('##PAGES-URL#select-engine##', '/select-engine')
    str = str.replace('##SERVICE-TERM#shop##', '<a href="/services/shop">интернет-магазин</a>')
    str = str.replace('##SERVICE-TERM#site-vizitka##', '<a href="/services/vizitka">сайт визитка</a>')
    str = str.replace('##SERVICE-TERM-GEN#site-vizitka##', '<a href="/services/vizitka">сайта визитки</a>')

    str = str.replace('##EMAIL##', '<a href="mailto">as@solotony.com</a>')
    str = str.replace('##ADDRESS-SPB##', 'Ленинский проспект, дом 95, кафе Евразия')
    str = str.replace('##FEEDBACK##', '<a href="/forms/feedback">написать письмо с сайта</a>')
    str = str.replace('##CONTEXT_BRIEF##', '<a href="/forms/context-brief">бриф на настройку контекстной рекламы</a>')
    str = str.replace('##SITE_BRIEF##', '<a href="/forms/site-brief">бриф на создание сайта</a>')
    str = str.replace('##SHOP_BRIEF##', '<a href="/forms/shop-brief">бриф на создание интернет-магазина</a>')
    str = str.replace('##SEO_BRIEF##', '<a href="/forms/seo-brief">бриф на продвижение сайта</a>')
    str = str.replace('##SEND_ME##', '<a href="/forms/feedback">вышлите мне</a>')

    return str


def get_client_ip(request):

    ip_address = '127.0.0.1'

    if request.META.get('REMOTE_ADDR'):
        ip_address = request.META.get('REMOTE_ADDR')
    if request.META.get('HTTP_CLIENT_IP'):
        ip_address = request.META.get('HTTP_CLIENT_IP')
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        for ip in str(request.META.get('HTTP_X_FORWARDED_FOR')).split(','):
            ip_address = ip.strip()
    if request.META.get('HTTP_X_FORWARDED'):
        ip_address = request.META.get('HTTP_X_FORWARDED')
    elif request.META.get('HTTP_X_CLUSTER_CLIENT_IP'):
        ip_address = request.META.get('HTTP_X_CLUSTER_CLIENT_IP')
    elif request.META.get('HTTP_FORWARDED_FOR'):
        ip_address = request.META.get('HTTP_FORWARDED_FOR')
    elif request.META.get('HTTP_FORWARDED_FOR'):
        ip_address = request.META.get('HTTP_FORWARDED_FOR')
    elif request.META.get('HTTP_X_REAL_IP'):
        ip_address = request.META.get('HTTP_X_REAL_IP')

    return ip_address

