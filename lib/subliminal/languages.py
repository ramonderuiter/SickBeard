# -*- coding: utf-8 -*-
#
# Subliminal - Subtitles, faster than your thoughts
# Copyright (c) 2011 Antoine Bertin <diaoulael@gmail.com>
#
# This file is part of Subliminal.
#
# Subliminal is free software; you can redistribute it and/or modify it under
# the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Subliminal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


def convert_language(language, to_iso, from_iso=None):
    # if no from_iso is given, try to guess it
    if from_iso == None:
        if language.startswith(language[:1].upper()):
            from_iso = 0
        elif len(language) == 2:
            from_iso = 1
        elif len(language) == 3:
            from_iso = 2
        else:
            raise ValueError('Invalid input language format')
    if isinstance(language, unicode):
        language = language.encode('utf-8')
    converted_language = None
    for language_tuple in LANGUAGES:
        if language_tuple[from_iso] == language and language_tuple[to_iso]:
            converted_language = language_tuple[to_iso]
            break
    return converted_language

def list_languages(iso):
    return [l[iso] for l in LANGUAGES if l[iso]]

# ISO-639-2 languages list from http://www.loc.gov/standards/iso639-2/ISO-639-2_utf-8.txt
# + ('Brazilian', 'po', 'pob')
LANGUAGES = [('Afar', 'aa', 'aar'), 
             ('Abkhazian', 'ab', 'abk'), 
             ('Achinese', '', 'ace'), 
             ('Acoli', '', 'ach'), 
             ('Adangme', '', 'ada'), 
             ('Adyghe; Adygei', '', 'ady'), 
             ('Afro-Asiatic languages', '', 'afa'), 
             ('Afrihili', '', 'afh'), 
             ('Afrikaans', 'af', 'afr'), 
             ('Ainu', '', 'ain'), 
             ('Akan', 'ak', 'aka'), 
             ('Akkadian', '', 'akk'), 
             ('Albanian', 'sq', 'alb'), 
             ('Aleut', '', 'ale'), 
             ('Algonquian languages', '', 'alg'), 
             ('Southern Altai', '', 'alt'), 
             ('Amharic', 'am', 'amh'), 
             ('English, Old (ca.450-1100)', '', 'ang'), 
             ('Angika', '', 'anp'), 
             ('Apache languages', '', 'apa'), 
             ('Arabic', 'ar', 'ara'), 
             ('Official Aramaic (700-300 BCE); Imperial Aramaic (700-300 BCE)', '', 'arc'), 
             ('Aragonese', 'an', 'arg'), 
             ('Armenian', 'hy', 'arm'), 
             ('Mapudungun; Mapuche', '', 'arn'), 
             ('Arapaho', '', 'arp'), 
             ('Artificial languages', '', 'art'), 
             ('Arawak', '', 'arw'), 
             ('Assamese', 'as', 'asm'), 
             ('Asturian; Bable; Leonese; Asturleonese', '', 'ast'), 
             ('Athapascan languages', '', 'ath'), 
             ('Australian languages', '', 'aus'), 
             ('Avaric', 'av', 'ava'), 
             ('Avestan', 'ae', 'ave'), 
             ('Awadhi', '', 'awa'), 
             ('Aymara', 'ay', 'aym'), 
             ('Azerbaijani', 'az', 'aze'), 
             ('Banda languages', '', 'bad'), 
             ('Bamileke languages', '', 'bai'), 
             ('Bashkir', 'ba', 'bak'), 
             ('Baluchi', '', 'bal'), 
             ('Bambara', 'bm', 'bam'), 
             ('Balinese', '', 'ban'), 
             ('Basque', 'eu', 'baq'), 
             ('Basa', '', 'bas'), 
             ('Baltic languages', '', 'bat'), 
             ('Beja; Bedawiyet', '', 'bej'), 
             ('Belarusian', 'be', 'bel'), 
             ('Bemba', '', 'bem'), 
             ('Bengali', 'bn', 'ben'), 
             ('Berber languages', '', 'ber'), 
             ('Bhojpuri', '', 'bho'), 
             ('Bihari languages', 'bh', 'bih'), 
             ('Bikol', '', 'bik'), 
             ('Bini; Edo', '', 'bin'), 
             ('Bislama', 'bi', 'bis'), 
             ('Siksika', '', 'bla'), 
             ('Bantu (Other)', '', 'bnt'), 
             ('Bosnian', 'bs', 'bos'), 
             ('Braj', '', 'bra'), 
             ('Breton', 'br', 'bre'), 
             ('Batak languages', '', 'btk'), 
             ('Buriat', '', 'bua'), 
             ('Buginese', '', 'bug'), 
             ('Bulgarian', 'bg', 'bul'), 
             ('Burmese', 'my', 'bur'), 
             ('Blin; Bilin', '', 'byn'), 
             ('Caddo', '', 'cad'), 
             ('Central American Indian languages', '', 'cai'), 
             ('Galibi Carib', '', 'car'), 
             ('Catalan; Valencian', 'ca', 'cat'), 
             ('Caucasian languages', '', 'cau'), 
             ('Cebuano', '', 'ceb'), 
             ('Celtic languages', '', 'cel'), 
             ('Chamorro', 'ch', 'cha'), 
             ('Chibcha', '', 'chb'), 
             ('Chechen', 'ce', 'che'), 
             ('Chagatai', '', 'chg'), 
             ('Chinese', 'zh', 'chi'), 
             ('Chuukese', '', 'chk'), 
             ('Mari', '', 'chm'), 
             ('Chinook jargon', '', 'chn'), 
             ('Choctaw', '', 'cho'), 
             ('Chipewyan; Dene Suline', '', 'chp'), 
             ('Cherokee', '', 'chr'), 
             ('Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic', 'cu', 'chu'), 
             ('Chuvash', 'cv', 'chv'), 
             ('Cheyenne', '', 'chy'), 
             ('Chamic languages', '', 'cmc'), 
             ('Coptic', '', 'cop'), 
             ('Cornish', 'kw', 'cor'), 
             ('Corsican', 'co', 'cos'), 
             ('Creoles and pidgins, English based', '', 'cpe'), 
             ('Creoles and pidgins, French-based ', '', 'cpf'), 
             ('Creoles and pidgins, Portuguese-based ', '', 'cpp'), 
             ('Cree', 'cr', 'cre'), 
             ('Crimean Tatar; Crimean Turkish', '', 'crh'), 
             ('Creoles and pidgins ', '', 'crp'), 
             ('Kashubian', '', 'csb'), 
             ('Cushitic languages', '', 'cus'), 
             ('Czech', 'cs', 'cze'), 
             ('Dakota', '', 'dak'), 
             ('Danish', 'da', 'dan'), 
             ('Dargwa', '', 'dar'), 
             ('Land Dayak languages', '', 'day'), 
             ('Delaware', '', 'del'), 
             ('Slave (Athapascan)', '', 'den'), 
             ('Dogrib', '', 'dgr'), 
             ('Dinka', '', 'din'), 
             ('Divehi; Dhivehi; Maldivian', 'dv', 'div'), 
             ('Dogri', '', 'doi'), 
             ('Dravidian languages', '', 'dra'), 
             ('Lower Sorbian', '', 'dsb'), 
             ('Duala', '', 'dua'), 
             ('Dutch, Middle (ca.1050-1350)', '', 'dum'), 
             ('Dutch; Flemish', 'nl', 'dut'), 
             ('Dyula', '', 'dyu'), 
             ('Dzongkha', 'dz', 'dzo'), 
             ('Efik', '', 'efi'), 
             ('Egyptian (Ancient)', '', 'egy'), 
             ('Ekajuk', '', 'eka'), 
             ('Elamite', '', 'elx'), 
             ('English', 'en', 'eng'), 
             ('English, Middle (1100-1500)', '', 'enm'), 
             ('Esperanto', 'eo', 'epo'), 
             ('Estonian', 'et', 'est'), 
             ('Ewe', 'ee', 'ewe'), 
             ('Ewondo', '', 'ewo'), 
             ('Fang', '', 'fan'), 
             ('Faroese', 'fo', 'fao'), 
             ('Fanti', '', 'fat'), 
             ('Fijian', 'fj', 'fij'), 
             ('Filipino; Pilipino', '', 'fil'), 
             ('Finnish', 'fi', 'fin'), 
             ('Finno-Ugrian languages', '', 'fiu'), 
             ('Fon', '', 'fon'), 
             ('French', 'fr', 'fre'), 
             ('French, Middle (ca.1400-1600)', '', 'frm'), 
             ('French, Old (842-ca.1400)', '', 'fro'), 
             ('Northern Frisian', '', 'frr'), 
             ('Eastern Frisian', '', 'frs'), 
             ('Western Frisian', 'fy', 'fry'), 
             ('Fulah', 'ff', 'ful'), 
             ('Friulian', '', 'fur'), 
             ('Ga', '', 'gaa'), 
             ('Gayo', '', 'gay'), 
             ('Gbaya', '', 'gba'), 
             ('Germanic languages', '', 'gem'), 
             ('Georgian', 'ka', 'geo'), 
             ('German', 'de', 'ger'), 
             ('Geez', '', 'gez'), 
             ('Gilbertese', '', 'gil'), 
             ('Gaelic; Scottish Gaelic', 'gd', 'gla'), 
             ('Irish', 'ga', 'gle'), 
             ('Galician', 'gl', 'glg'), 
             ('Manx', 'gv', 'glv'), 
             ('German, Middle High (ca.1050-1500)', '', 'gmh'), 
             ('German, Old High (ca.750-1050)', '', 'goh'), 
             ('Gondi', '', 'gon'), 
             ('Gorontalo', '', 'gor'), 
             ('Gothic', '', 'got'), 
             ('Grebo', '', 'grb'), 
             ('Greek, Ancient (to 1453)', '', 'grc'), 
             ('Greek, Modern (1453-)', 'el', 'gre'), 
             ('Guarani', 'gn', 'grn'), 
             ('Swiss German; Alemannic; Alsatian', '', 'gsw'), 
             ('Gujarati', 'gu', 'guj'), 
             ('Gwich\'in', '', 'gwi'), 
             ('Haida', '', 'hai'), 
             ('Haitian; Haitian Creole', 'ht', 'hat'), 
             ('Hausa', 'ha', 'hau'), 
             ('Hawaiian', '', 'haw'), 
             ('Hebrew', 'he', 'heb'), 
             ('Herero', 'hz', 'her'), 
             ('Hiligaynon', '', 'hil'), 
             ('Himachali languages; Western Pahari languages', '', 'him'), 
             ('Hindi', 'hi', 'hin'), 
             ('Hittite', '', 'hit'), 
             ('Hmong; Mong', '', 'hmn'), 
             ('Hiri Motu', 'ho', 'hmo'), 
             ('Croatian', 'hr', 'hrv'), 
             ('Upper Sorbian', '', 'hsb'), 
             ('Hungarian', 'hu', 'hun'), 
             ('Hupa', '', 'hup'), 
             ('Iban', '', 'iba'), 
             ('Igbo', 'ig', 'ibo'), 
             ('Icelandic', 'is', 'ice'), 
             ('Ido', 'io', 'ido'), 
             ('Sichuan Yi; Nuosu', 'ii', 'iii'), 
             ('Ijo languages', '', 'ijo'), 
             ('Inuktitut', 'iu', 'iku'), 
             ('Interlingue; Occidental', 'ie', 'ile'), 
             ('Iloko', '', 'ilo'), 
             ('Interlingua (International Auxiliary Language Association)', 'ia', 'ina'), 
             ('Indic languages', '', 'inc'), 
             ('Indonesian', 'id', 'ind'), 
             ('Indo-European languages', '', 'ine'), 
             ('Ingush', '', 'inh'), 
             ('Inupiaq', 'ik', 'ipk'), 
             ('Iranian languages', '', 'ira'), 
             ('Iroquoian languages', '', 'iro'), 
             ('Italian', 'it', 'ita'), 
             ('Javanese', 'jv', 'jav'), 
             ('Lojban', '', 'jbo'), 
             ('Japanese', 'ja', 'jpn'), 
             ('Judeo-Persian', '', 'jpr'), 
             ('Judeo-Arabic', '', 'jrb'), 
             ('Kara-Kalpak', '', 'kaa'), 
             ('Kabyle', '', 'kab'), 
             ('Kachin; Jingpho', '', 'kac'), 
             ('Kalaallisut; Greenlandic', 'kl', 'kal'), 
             ('Kamba', '', 'kam'), 
             ('Kannada', 'kn', 'kan'), 
             ('Karen languages', '', 'kar'), 
             ('Kashmiri', 'ks', 'kas'), 
             ('Kanuri', 'kr', 'kau'), 
             ('Kawi', '', 'kaw'), 
             ('Kazakh', 'kk', 'kaz'), 
             ('Kabardian', '', 'kbd'), 
             ('Khasi', '', 'kha'), 
             ('Khoisan languages', '', 'khi'), 
             ('Central Khmer', 'km', 'khm'), 
             ('Khotanese; Sakan', '', 'kho'), 
             ('Kikuyu; Gikuyu', 'ki', 'kik'), 
             ('Kinyarwanda', 'rw', 'kin'), 
             ('Kirghiz; Kyrgyz', 'ky', 'kir'), 
             ('Kimbundu', '', 'kmb'), 
             ('Konkani', '', 'kok'), 
             ('Komi', 'kv', 'kom'), 
             ('Kongo', 'kg', 'kon'), 
             ('Korean', 'ko', 'kor'), 
             ('Kosraean', '', 'kos'), 
             ('Kpelle', '', 'kpe'), 
             ('Karachay-Balkar', '', 'krc'), 
             ('Karelian', '', 'krl'), 
             ('Kru languages', '', 'kro'), 
             ('Kurukh', '', 'kru'), 
             ('Kuanyama; Kwanyama', 'kj', 'kua'), 
             ('Kumyk', '', 'kum'), 
             ('Kurdish', 'ku', 'kur'), 
             ('Kutenai', '', 'kut'), 
             ('Ladino', '', 'lad'), 
             ('Lahnda', '', 'lah'), 
             ('Lamba', '', 'lam'), 
             ('Lao', 'lo', 'lao'), 
             ('Latin', 'la', 'lat'), 
             ('Latvian', 'lv', 'lav'), 
             ('Lezghian', '', 'lez'), 
             ('Limburgan; Limburger; Limburgish', 'li', 'lim'), 
             ('Lingala', 'ln', 'lin'), 
             ('Lithuanian', 'lt', 'lit'), 
             ('Mongo', '', 'lol'), 
             ('Lozi', '', 'loz'), 
             ('Luxembourgish; Letzeburgesch', 'lb', 'ltz'), 
             ('Luba-Lulua', '', 'lua'), 
             ('Luba-Katanga', 'lu', 'lub'), 
             ('Ganda', 'lg', 'lug'), 
             ('Luiseno', '', 'lui'), 
             ('Lunda', '', 'lun'), 
             ('Luo (Kenya and Tanzania)', '', 'luo'), 
             ('Lushai', '', 'lus'), 
             ('Macedonian', 'mk', 'mac'), 
             ('Madurese', '', 'mad'), 
             ('Magahi', '', 'mag'), 
             ('Marshallese', 'mh', 'mah'), 
             ('Maithili', '', 'mai'), 
             ('Makasar', '', 'mak'), 
             ('Malayalam', 'ml', 'mal'), 
             ('Mandingo', '', 'man'), 
             ('Maori', 'mi', 'mao'), 
             ('Austronesian languages', '', 'map'), 
             ('Marathi', 'mr', 'mar'), 
             ('Masai', '', 'mas'), 
             ('Malay', 'ms', 'may'), 
             ('Moksha', '', 'mdf'), 
             ('Mandar', '', 'mdr'), 
             ('Mende', '', 'men'), 
             ('Irish, Middle (900-1200)', '', 'mga'), 
             ('Mi\'kmaq; Micmac', '', 'mic'), 
             ('Minangkabau', '', 'min'), 
             ('Uncoded languages', '', 'mis'), 
             ('Mon-Khmer languages', '', 'mkh'), 
             ('Malagasy', 'mg', 'mlg'), 
             ('Maltese', 'mt', 'mlt'), 
             ('Manchu', '', 'mnc'), 
             ('Manipuri', '', 'mni'), 
             ('Manobo languages', '', 'mno'), 
             ('Mohawk', '', 'moh'), 
             ('Mongolian', 'mn', 'mon'), 
             ('Mossi', '', 'mos'), 
             ('Multiple languages', '', 'mul'), 
             ('Munda languages', '', 'mun'), 
             ('Creek', '', 'mus'), 
             ('Mirandese', '', 'mwl'), 
             ('Marwari', '', 'mwr'), 
             ('Mayan languages', '', 'myn'), 
             ('Erzya', '', 'myv'), 
             ('Nahuatl languages', '', 'nah'), 
             ('North American Indian languages', '', 'nai'), 
             ('Neapolitan', '', 'nap'), 
             ('Nauru', 'na', 'nau'), 
             ('Navajo; Navaho', 'nv', 'nav'), 
             ('Ndebele, South; South Ndebele', 'nr', 'nbl'), 
             ('Ndebele, North; North Ndebele', 'nd', 'nde'), 
             ('Ndonga', 'ng', 'ndo'), 
             ('Low German; Low Saxon; German, Low; Saxon, Low', '', 'nds'), 
             ('Nepali', 'ne', 'nep'), 
             ('Nepal Bhasa; Newari', '', 'new'), 
             ('Nias', '', 'nia'), 
             ('Niger-Kordofanian languages', '', 'nic'), 
             ('Niuean', '', 'niu'), 
             ('Norwegian Nynorsk; Nynorsk, Norwegian', 'nn', 'nno'), 
             ('Bokmål, Norwegian; Norwegian Bokmål', 'nb', 'nob'), 
             ('Nogai', '', 'nog'), 
             ('Norse, Old', '', 'non'), 
             ('Norwegian', 'no', 'nor'), 
             ('N\'Ko', '', 'nqo'), 
             ('Pedi; Sepedi; Northern Sotho', '', 'nso'), 
             ('Nubian languages', '', 'nub'), 
             ('Classical Newari; Old Newari; Classical Nepal Bhasa', '', 'nwc'), 
             ('Chichewa; Chewa; Nyanja', 'ny', 'nya'), 
             ('Nyamwezi', '', 'nym'), 
             ('Nyankole', '', 'nyn'), 
             ('Nyoro', '', 'nyo'), 
             ('Nzima', '', 'nzi'), 
             ('Occitan (post 1500); Provençal', 'oc', 'oci'), 
             ('Ojibwa', 'oj', 'oji'), 
             ('Oriya', 'or', 'ori'), 
             ('Oromo', 'om', 'orm'), 
             ('Osage', '', 'osa'), 
             ('Ossetian; Ossetic', 'os', 'oss'), 
             ('Turkish, Ottoman (1500-1928)', '', 'ota'), 
             ('Otomian languages', '', 'oto'), 
             ('Papuan languages', '', 'paa'), 
             ('Pangasinan', '', 'pag'), 
             ('Pahlavi', '', 'pal'), 
             ('Pampanga; Kapampangan', '', 'pam'), 
             ('Panjabi; Punjabi', 'pa', 'pan'), 
             ('Papiamento', '', 'pap'), 
             ('Palauan', '', 'pau'), 
             ('Persian, Old (ca.600-400 B.C.)', '', 'peo'), 
             ('Persian', 'fa', 'per'), 
             ('Philippine languages', '', 'phi'), 
             ('Phoenician', '', 'phn'), 
             ('Pali', 'pi', 'pli'), 
             ('Polish', 'pl', 'pol'), 
             ('Pohnpeian', '', 'pon'), 
             ('Portuguese', 'pt', 'por'), 
             ('Prakrit languages', '', 'pra'), 
             ('Provençal, Old (to 1500)', '', 'pro'), 
             ('Pushto; Pashto', 'ps', 'pus'), 
             ('Reserved for local use', '', 'qaa-qtz'), 
             ('Quechua', 'qu', 'que'), 
             ('Rajasthani', '', 'raj'), 
             ('Rapanui', '', 'rap'), 
             ('Rarotongan; Cook Islands Maori', '', 'rar'), 
             ('Romance languages', '', 'roa'), 
             ('Romansh', 'rm', 'roh'), 
             ('Romany', '', 'rom'), 
             ('Romanian; Moldavian; Moldovan', 'ro', 'rum'), 
             ('Rundi', 'rn', 'run'), 
             ('Aromanian; Arumanian; Macedo-Romanian', '', 'rup'), 
             ('Russian', 'ru', 'rus'), 
             ('Sandawe', '', 'sad'), 
             ('Sango', 'sg', 'sag'), 
             ('Yakut', '', 'sah'), 
             ('South American Indian (Other)', '', 'sai'), 
             ('Salishan languages', '', 'sal'), 
             ('Samaritan Aramaic', '', 'sam'), 
             ('Sanskrit', 'sa', 'san'), 
             ('Sasak', '', 'sas'), 
             ('Santali', '', 'sat'), 
             ('Sicilian', '', 'scn'), 
             ('Scots', '', 'sco'), 
             ('Selkup', '', 'sel'), 
             ('Semitic languages', '', 'sem'), 
             ('Irish, Old (to 900)', '', 'sga'), 
             ('Sign Languages', '', 'sgn'), 
             ('Shan', '', 'shn'), 
             ('Sidamo', '', 'sid'), 
             ('Sinhala; Sinhalese', 'si', 'sin'), 
             ('Siouan languages', '', 'sio'), 
             ('Sino-Tibetan languages', '', 'sit'), 
             ('Slavic languages', '', 'sla'), 
             ('Slovak', 'sk', 'slo'), 
             ('Slovenian', 'sl', 'slv'), 
             ('Southern Sami', '', 'sma'), 
             ('Northern Sami', 'se', 'sme'), 
             ('Sami languages', '', 'smi'), 
             ('Lule Sami', '', 'smj'), 
             ('Inari Sami', '', 'smn'), 
             ('Samoan', 'sm', 'smo'), 
             ('Skolt Sami', '', 'sms'), 
             ('Shona', 'sn', 'sna'), 
             ('Sindhi', 'sd', 'snd'), 
             ('Soninke', '', 'snk'), 
             ('Sogdian', '', 'sog'), 
             ('Somali', 'so', 'som'), 
             ('Songhai languages', '', 'son'), 
             ('Sotho, Southern', 'st', 'sot'), 
             ('Spanish; Castilian', 'es', 'spa'), 
             ('Sardinian', 'sc', 'srd'), 
             ('Sranan Tongo', '', 'srn'), 
             ('Serbian', 'sr', 'srp'), 
             ('Serer', '', 'srr'), 
             ('Nilo-Saharan languages', '', 'ssa'), 
             ('Swati', 'ss', 'ssw'), 
             ('Sukuma', '', 'suk'), 
             ('Sundanese', 'su', 'sun'), 
             ('Susu', '', 'sus'), 
             ('Sumerian', '', 'sux'), 
             ('Swahili', 'sw', 'swa'), 
             ('Swedish', 'sv', 'swe'), 
             ('Classical Syriac', '', 'syc'), 
             ('Syriac', '', 'syr'), 
             ('Tahitian', 'ty', 'tah'), 
             ('Tai languages', '', 'tai'), 
             ('Tamil', 'ta', 'tam'), 
             ('Tatar', 'tt', 'tat'), 
             ('Telugu', 'te', 'tel'), 
             ('Timne', '', 'tem'), 
             ('Tereno', '', 'ter'), 
             ('Tetum', '', 'tet'), 
             ('Tajik', 'tg', 'tgk'), 
             ('Tagalog', 'tl', 'tgl'), 
             ('Thai', 'th', 'tha'), 
             ('Tibetan', 'bo', 'tib'), 
             ('Tigre', '', 'tig'), 
             ('Tigrinya', 'ti', 'tir'), 
             ('Tiv', '', 'tiv'), 
             ('Tokelau', '', 'tkl'), 
             ('Klingon; tlhIngan-Hol', '', 'tlh'), 
             ('Tlingit', '', 'tli'), 
             ('Tamashek', '', 'tmh'), 
             ('Tonga (Nyasa)', '', 'tog'), 
             ('Tonga (Tonga Islands)', 'to', 'ton'), 
             ('Tok Pisin', '', 'tpi'), 
             ('Tsimshian', '', 'tsi'), 
             ('Tswana', 'tn', 'tsn'), 
             ('Tsonga', 'ts', 'tso'), 
             ('Turkmen', 'tk', 'tuk'), 
             ('Tumbuka', '', 'tum'), 
             ('Tupi languages', '', 'tup'), 
             ('Turkish', 'tr', 'tur'), 
             ('Altaic languages', '', 'tut'), 
             ('Tuvalu', '', 'tvl'), 
             ('Twi', 'tw', 'twi'), 
             ('Tuvinian', '', 'tyv'), 
             ('Udmurt', '', 'udm'), 
             ('Ugaritic', '', 'uga'), 
             ('Uighur; Uyghur', 'ug', 'uig'), 
             ('Ukrainian', 'uk', 'ukr'), 
             ('Umbundu', '', 'umb'), 
             ('Undetermined', '', 'und'), 
             ('Urdu', 'ur', 'urd'), 
             ('Uzbek', 'uz', 'uzb'), 
             ('Vai', '', 'vai'), 
             ('Venda', 've', 'ven'), 
             ('Vietnamese', 'vi', 'vie'), 
             ('Volapük', 'vo', 'vol'), 
             ('Votic', '', 'vot'), 
             ('Wakashan languages', '', 'wak'), 
             ('Walamo', '', 'wal'), 
             ('Waray', '', 'war'), 
             ('Washo', '', 'was'), 
             ('Welsh', 'cy', 'wel'), 
             ('Sorbian languages', '', 'wen'), 
             ('Walloon', 'wa', 'wln'), 
             ('Wolof', 'wo', 'wol'), 
             ('Kalmyk; Oirat', '', 'xal'), 
             ('Xhosa', 'xh', 'xho'), 
             ('Yao', '', 'yao'), 
             ('Yapese', '', 'yap'), 
             ('Yiddish', 'yi', 'yid'), 
             ('Yoruba', 'yo', 'yor'), 
             ('Yupik languages', '', 'ypk'), 
             ('Zapotec', '', 'zap'), 
             ('Blissymbols; Blissymbolics; Bliss', '', 'zbl'), 
             ('Zenaga', '', 'zen'), 
             ('Zhuang; Chuang', 'za', 'zha'), 
             ('Zande languages', '', 'znd'), 
             ('Zulu', 'zu', 'zul'), 
             ('Zuni', '', 'zun'), 
             ('No linguistic content; Not applicable', '', 'zxx'), 
             ('Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki', '', 'zza'),
             ('Brazilian', 'po', 'pob')]
