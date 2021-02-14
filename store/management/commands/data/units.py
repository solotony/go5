from django.utils.translation import gettext_lazy as _


UNITS = [
    (16,        _('Length'),                    _('INCH'),                   _('Inch'),              2,      None,     _('"')),
    (17,        _('Weight'),                    _('KG'),                     _('kilogram'),          1,      1000,    _('kg')),
    (18,        _('Frequency'),                 _('MHZ'),                    _('megahertz'),         1,      1e+6,    _('MHz')),
    (19,        _('Byte size'),                 _('MB'),                     _('megabyte'),          1,      1e+6,    _('MB')),
    (20,        _('Byte size'),                 _('GB'),                     _('gigabyte'),          1,      1e+9,    _('GB')),
    (22,        _('Bit speed'),                 _('KBIT_S'),                 _('kilobit per second'),1,      1000,    _('кбит/с')),
    (23,        _('Bit speed'),                 _('MBIT_S'),                 _('megabit per second'),1,      1e+6,    _('Мбит/с')),
    (24,        _('Length'),                    _('MM'),                     _('millimetre'),        1,      1,       _('mm')),
    (27,        _('Time'),                      _('MS'),                     _('millisecond'),       1,      None,   _('ms')),
    (28,        _('Frequency'),                 _('RPM'),                    _('revolutions per minute'), 0, 60,      _('RPM')),
    (31,        _('Frequency'),                 _('KHZ'),                    _('kilohertz'),         1,      1000,    _('kHz')),
    (32,        _('Corner'),                    _('DEG'),                    _('degree'),            0,      None,       _('°')),
    (34,        _('Length'),                    _('CM'),                     _('cantimetre'),        1,      10,      _('cm')),
    (35,        _('Resolution'),                _('DPI'),                    _('dot per inch'),      2,      None,       _('DPI')),
    (36,        _('Frequency'),                 _('HZ'),                     _('hetrz'),             1,      1,       _('Hz')),
    (37,        _('Frequency'),                 _('GHZ'),                    _('gigahetrz'),         1,      1e+9,    _('GHz')),
    (38,        _('Weight'),                    _('G'),                      _('gram'),              1,      1,       _('g')),
    (40,        _('Byte speed'),                _('MB_S'),                   _('megabyte per second'),1,     None,       _('MB/s')),
    (41,        _('Electric current'),          _('A'),                      _('ampere '),           0,      None,       _('A')),
    (42,        _('Voltage'),                   _('V'),                      _('volt'),              0,      None,       _('V')),
    (43,        _('luminance'),                 _('CD_M2'),                  _('candela per square metre'),1,None,       _('cd/m²')),
    (44,        _('Power'),                     _('W'),                      _('watt'),              0,      None,       _('W')),
    (45,        _('Bit size'),                  _('MBIT'),                   _('megabit'),           0,      None,       _('Mbit')),
    (46,        _('Time'),                      _('HOUR'),                   _('hour'),              0,      None,       _('h')),
    (47,        _('Byte size'),                 _('KB'),                     _('kilobyte'),          0,      1000,    _('KB')),
    (50,        _('Bit size'),                  _('BIT'),                    _('bit'),               0,      1,       _('бит')),
    (51,        _('Electric charge'),           _('MA_H'),                   _('milliampere hour'),  0,      None,       _('mAh')),
    (54,        _('Length'),                    _('M'),                      _('metre'),             0,      1000,    _('m')),
    (58,        _(''),                          _('CPM'),                       _(''),                  0,      None,       _('cpm')),
    (59,        _(''),                          _('PPM'),                       _(''),                  0,      None,       _('ppm')),
    (60,        _('Time'),                      _('SECOND'),                 _('second'),            0,      None,       _('s')),
    (64,        _(''),                          _('PERCENT'),                       _(''),                  0,      None,       _('%')),
    (65,        _('Temperature'),               _('CELSIUS'),                _('degree Celsius'),    0,      None,       _('°C')),
    (66,        _('Time'),                      _('MINUTE'),                 _('minute'),            0,      None,       _('min')),
    (68,        _(''),                          _('GBIT_S'),                     _(''),                  0,      None,       _('Gbit/s')),
    (70,        _('Length'),                    _('MICRON'),                 _('micrometre'),        0,      1e-6,    _('µm')),
    (72,        _(''),                          _('GEE'),                       _(''),                  0,      None,       _('G')),
    (73,        _('Electric current'),          _('MA'),                     _('milliampere'),       1,      1e-3,    _('mA')),
    (75,        _(''),                          _(''),                       _(''),                  0,      None,       _('лет')),
    (76,        _(''),                          _(''),                       _(''),                  0,      None,       _('dB')),
    (77,        _(''),                          _(''),                       _(''),                  0,      None,       _('стр/мес')),
    (80,        _(''),                          _(''),                       _(''),                  0,      None,       _('VA')),
    (81,        _(''),                          _(''),                       _(''),                  0,      None,       _('J')),
    (82,        _(''),                          _(''),                       _(''),                  0,      None,       _('cpi')),
    (83,        _(''),                          _(''),                       _(''),                  0,      None,       _('cps')),
    (84,        _(''),                          _(''),                       _(''),                  0,      None,       _('lpm')),
    (85,        _(''),                          _(''),                       _(''),                  0,      None,       _('fps')),
    (87,        _(''),                          _(''),                       _(''),                  0,      None,       _('Ω')),
    (90,        _(''),                          _(''),                       _(''),                  0,      None,       _('лм')),
    (91,        _(''),                          _(''),                       _(''),                  0,      None,       _('°F')),
    (98,        _(''),                          _(''),                       _(''),                  0,      None,       _('nm')),
    (99,        _(''),                          _(''),                       _(''),                  0,      None,       _('dBi')),
    (100,       _('Volume'),                    _('L'),                      _('litre'),             1,      1000,    _('L')),
    (103,       _(''),                          _(''),                       _(''),                  0,      None,       _('кВт·ч')),
    (105,       _(''),                          _(''),                       _(''),                  0,      None,       _('N')),
    (107,       _(''),                          _(''),                       _(''),                  0,      None,       _('диск (ов)')),
    (109,       _(''),                          _(''),                       _(''),                  0,      None,       _('BTU/ч')),
    (112,       _(''),                          _(''),                       _(''),                  0,      None,       _('символов')),
    (116,       _(''),                          _(''),                       _(''),                  0,      None,       _('с/стор')),
    (120,       _(''),                          _(''),                       _(''),                  0,      None,       _('адресатов')),
    (121,       _(''),                          _(''),                       _(''),                  0,      None,       _('ips')),
    (122,       _(''),                          _(''),                       _(''),                  0,      None,       _('мм/с')),
    (126,       _(''),                          _(''),                       _(''),                  0,      None,       _('млн. симв.')),
    (127,       _('Weight'),                    _('LBS'),                    _('pound'),             2,      None,       _('lbs')),
    (132,       _(''),                          _(''),                       _(''),                  0,      None,       _('скоб')),
    (138,       _(''),                          _(''),                       _(''),                  0,      None,       _('дюйм/мин')),
    (142,       _('Volume'),                    _('ML'),                     _('milliliter'),        1,      None,       _('ml')),
    (143,       _(''),                          _(''),                       _(''),                  0,      None,       _('мес')),
    (144,       _('Count'),                     _('ITEM'),                   _(''),                  0,      None,       _('шт')),
    (146,       _('Volume'),                    _('CM_3'),                   _('cantimetre³'),       1,      None,       _('cm³')),
    (156,       _(''),                          _(''),                       _(''),                  0,      None,       _('g/m²')),
    (159,       _(''),                          _(''),                       _(''),                  0,      None,       _('TB')),
    (160,       _(''),                          _(''),                       _(''),                  0,      None,       _('GB/s')),
    (165,       _(''),                          _(''),                       _(''),                  0,      None,       _('MP')),
    (169,       _(''),                          _(''),                       _(''),                  0,      None,       _('кВт·ч/неделя')),
    (175,       _(''),                          _(''),                       _(''),                  0,      None,       _('диск/ч')),
    (176,       _(''),                          _(''),                       _(''),                  0,      None,       _('GT/s')),
    (181,       _(''),                          _(''),                       _(''),                  0,      None,       _('dBmW')),
    (185,       _(''),                          _(''),                       _(''),                  0,      None,       _('lps')),
    (196,       _(''),                          _(''),                       _(''),                  0,      None,       _('Mpps')),
    (206,       _(''),                          _(''),                       _(''),                  0,      None,       _('ipm')),
    (210,       _(''),                          _(''),                       _(''),                  0,      None,       _('IOPS')),
    (211,       _(''),                          _(''),                       _(''),                  0,      None,       _('Wh')),
    (222,       _(''),                          _(''),                       _(''),                  0,      None,       _('точка')),
    (224,       _(''),                          _(''),                       _(''),                  0,      None,       _('mmH2O')),
    (228,       _(''),                          _(''),                       _(''),                  0,      None,       _('µs')),
    (229,       _(''),                          _(''),                       _(''),                  0,      None,       _('mm²')),
    (237,       _(''),                          _(''),                       _(''),                  0,      None,       _('pph')),
    (243,       _(''),                          _(''),                       _(''),                  0,      None,       _('ppi')),
    (299,       _(''),                          _(''),                       _(''),                  0,      None,       _('pps')),
    (439,       _(''),                          _(''),                       _(''),                  0,      None,       _('лет 2')),
    (443,       _(''),                          _(''),                       _(''),                  0,      None,       _('pl')),

    (39, _('Count'), _(''), _(''), 0, None, _('пикселей')),
    (55, _('Count'), _(''), _(''), 0, None, _('страниц')),
    (56, _('Count'), _(''), _(''), 0, None, _('записей')),
    (61, _('Count'), _(''), _(''), 0, None, _('копий')),
    (62, _('Count'), _(''), _(''), 0, None, _('листов')),
    (316, _('Count'), _(''), _(''), 0, None, _('скан')),
    (349, _('Count'), _(''), _(''), 0, None, _('канала')),
    (350, _('Count'), _(''), _(''), 0, None, _('лампы')),
    (354, _('Count'), _(''), _(''), 0, None, _('клавиши')),
    (362, _('Count'), _(''), _(''), 0, None, _('полка(и)')),
    (363, _('Count'), _(''), _(''), 0, None, _('ящик(и)')),
    (373, _('Count'), _(''), _(''), 0, None, _('символы')),
    (375, _('Count'), _(''), _(''), 0, None, _('цвета')),
    (378, _('Count'), _(''), _(''), 0, None, _('вентилятор(ы)')),
    (384, _('Count'), _(''), _(''), 0, None, _('розетка(и)')),
    (386, _('Count'), _(''), _(''), 0, None, _('колесо(а)')),
    (429, _('Count'), _(''), _(''), 0, None, _('лицензия(и)')),
    (69, _('Count'), _(''), _(''), 0, None, _('линий')),
    (164, _('Count'), _(''), _(''), 0, None, _('млн. отрезаний')),
    (444, _('Count'), _(''), _(''), 0, None, _('точки/строка')),
    (86, _('Count'), _(''), _(''), 0, None, _('пользов.')),
    (89, _('Count'), _(''), _(''), 0, None, _('снимков')),
    (154, _('Count'), _(''), _(''), 0, None, _('этикетка (-ок)')),

    (21, _('Count'), _(''), _(''), 0, None, _('x')),
    (26, _('Count'), _(''), _(''), 0, None, _('None')),
    (29, _('Count'), _(''), _(''), 0, None, _('None 2')),
    (33, _('Count'), _(''), _(''), 0, None, _('x 2')),
    (30, _('Count'), _(''), _(''), 0, None, _('M 2')),
]


