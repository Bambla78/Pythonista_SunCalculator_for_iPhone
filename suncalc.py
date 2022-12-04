#!python3

from __future__ import print_function

import datetime
import json
import math
import os
import time
import urllib.parse
import urllib.request
from calendar import monthrange
from datetime import timedelta, timezone
from io import BytesIO
from math import *
from pathlib import Path
from random import random, randrange

import appex
import clipboard
import console
import dialogs
import location
import numpy as np
import objc_util
import photos
import pytz
import requests
import ui
from odf import teletype
from odf.office import FontFaceDecls
from odf.opendocument import OpenDocumentText
from odf.style import (
    FontFace,
    GraphicProperties,
    ListLevelProperties,
    ParagraphProperties,
    Style,
    TableCellProperties,
    TabStop,
    TabStops,
    TextProperties,
)
from odf.table import Table, TableCell, TableColumn, TableRow
from odf.text import (
    A,
    H,
    LineBreak,
    List,
    ListItem,
    ListLevelStyleBullet,
    ListLevelStyleNumber,
    ListStyle,
    Note,
    NoteBody,
    NoteCitation,
    P,
    S,
    Section,
    Span,
)
from PIL import Image
from pylab import *
from timezonefinder import TimezoneFinder

import arrow

#from odf import style as odfstyle

global flag, flag2, norise, pi
pi=3.14159265359

tznames = [
	
	{'title': 'Africa/Abidjan											UTC +0', 'tzn': 'Africa/Abidjan', 'utc': '0', 'dst': '0'},
	{'title': 'Africa/Accra											UTC +0', 'tzn': 'Africa/Accra', 'utc': '0', 'dst': '0'},
	{'title': 'Africa/Algiers											UTC +1', 'tzn': 'Africa/Algiers', 'utc': '1', 'dst': '1'},
	{'title': 'Africa/Bissau											UTC +0', 'tzn': 'Africa/Bissau', 'utc': '0', 'dst': '0'},
	{'title': 'Africa/Cairo											UTC +2', 'tzn': 'Africa/Cairo', 'utc': '2', 'dst': '2'},
	{'title': 'Africa/Casablanca										UTC +1', 'tzn': 'Africa/Casablanca', 'utc': '1', 'dst': '0'},
	{'title': 'Africa/Ceuta											UTC +1', 'tzn': 'Africa/Ceuta', 'utc': '1', 'dst': '2'},
	{'title': 'Africa/El_Aaiun									UTC +1', 'tzn': 'Africa/El_Aaiun', 'utc': '1', 'dst': '0'},
	{'title': 'Africa/Johannesburg								UTC +2', 'tzn': 'Africa/Johannesburg', 'utc': '2', 'dst': '2'},
	{'title': 'Africa/Juba											UTC +2', 'tzn': 'Africa/Juba', 'utc': '2', 'dst': '2'},
	{'title': 'Africa/Khartoum									UTC +2', 'tzn': 'Africa/Khartoum', 'utc': '2', 'dst': '2'},
	{'title': 'Africa/Lagos											UTC +1', 'tzn': 'Africa/Lagos', 'utc': '1', 'dst': '1'},
	{'title': 'Africa/Maputo										UTC +2', 'tzn': 'Africa/Maputo', 'utc': '2', 'dst': '2'},
	{'title': 'Africa/Monrovia									UTC +0', 'tzn': 'Africa/Monrovia', 'utc': '0', 'dst': '0'},
	{'title': 'Africa/Nairobi										UTC +3', 'tzn': 'Africa/Nairobi', 'utc': '3', 'dst': '3'},
	{'title': 'Africa/Ndjamena									UTC +1', 'tzn': 'Africa/Ndjamena', 'utc': '1', 'dst': '1'},
	{'title': 'Africa/Sao_Tome									UTC +0', 'tzn': 'Africa/Sao_Tome', 'utc': '0', 'dst': '0'},
	{'title': 'Africa/Tripoli										UTC +2', 'tzn': 'Africa/Tripoli', 'utc': '2', 'dst': '2'},
	{'title': 'Africa/Tunis											UTC +1', 'tzn': 'Africa/Tunis', 'utc': '1', 'dst': '1'},
	{'title': 'Africa/Windhoek									UTC +2', 'tzn': 'Africa/Windhoek', 'utc': '2', 'dst': '2'},
	{'title': 'America/Adak											UTC -10', 'tzn': 'America/Adak', 'utc': '-10', 'dst': '-9'},
	{'title': 'America/Anchorage								UTC -9', 'tzn': 'America/Anchorage', 'utc': '-9', 'dst': '-8'},
	{'title': 'America/Araguaina								UTC -3', 'tzn': 'America/Araguaina', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Argentina/Buenos_Aires				UTC -3', 'tzn': 'America/Argentina/Buenos_Aires', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Argentina/Catamarca					UTC -3', 'tzn': 'America/Argentina/Catamarca', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Argentina/Cordoba						UTC -3', 'tzn': 'America/Argentina/Cordoba', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Argentina/Jujuy							UTC -3', 'tzn': 'America/Argentina/Jujuy', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Argentina/La_Rioja						UTC -3', 'tzn': 'America/Argentina/La_Rioja', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Argentina/Mendoza						UTC -3', 'tzn': 'America/Argentina/Mendoza', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Argentina/Rio_Gallegos				UTC -3', 'tzn': 'America/Argentina/Rio_Gallegos', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Argentina/Salta							UTC -3', 'tzn': 'America/Argentina/Salta', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Argentina/San_Juan						UTC -3', 'tzn': 'America/Argentina/San_Juan', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Argentina/San_Luis						UTC -3', 'tzn': 'America/Argentina/San_Luis', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Argentina/Tucuman						UTC -3', 'tzn': 'Africa/Abidjan', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Argentina/Ushuaia						UTC -3', 'tzn': 'America/Argentina/Ushuaia', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Asuncion											UTC -4', 'tzn': 'America/Asuncion', 'utc': '-4', 'dst': '-3'},
	{'title': 'America/Atikokan											UTC -5', 'tzn': 'America/Atikokan', 'utc': '-5', 'dst': '-5'},
	{'title': 'America/Bahia												UTC -3', 'tzn': 'America/Bahia', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Bahia_Banderas								UTC -6', 'tzn': 'America/Bahia_Banderas', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/Barbados											UTC -4', 'tzn': 'America/Barbados', 'utc': '-4', 'dst': '-4'},
	{'title': 'America/Belem												UTC -3', 'tzn': 'America/Belem', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Belize												UTC -6', 'tzn': 'America/Belize', 'utc': '-6', 'dst': '-6'},
	{'title': 'America/Blanc-Sablon									UTC -4', 'tzn': 'America/Blanc-Sablon', 'utc': '-4', 'dst': '-4:'},
	{'title': 'America/Boa_Vista										UTC -4', 'tzn': 'America/Boa_Vista', 'utc': '-4', 'dst': '-4'},
	{'title': 'America/Bogota												UTC -5', 'tzn': 'America/Bogota', 'utc': '-5', 'dst': '-5'},
	{'title': 'America/Boise												UTC -7', 'tzn': 'America/Boise', 'utc': '-7', 'dst': '-6'},
	{'title': 'America/Cambridge_Bay								UTC -7', 'tzn': 'America/Cambridge_Bay', 'utc': '-7', 'dst': '-6'},
	{'title': 'America/Campo_Grande									UTC -4', 'tzn': 'America/Campo_Grande', 'utc': '-4', 'dst': '-4'},
	{'title': 'America/Cancun												UTC -5', 'tzn': 'America/Cancun', 'utc': '-5', 'dst': '-5'},
	{'title': 'America/Caracas											UTC -4', 'tzn': 'America/Caracas', 'utc': '-4', 'dst': '-4'},
	{'title': 'America/Cayenne											UTC -3', 'tzn': 'America/Cayenne', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Chicago											UTC -6', 'tzn': 'America/Chicago', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/Chihuahua										UTC -7', 'tzn': 'America/Chihuahua', 'utc': '-7', 'dst': '-6'},
	{'title': 'America/Costa_Rica										UTC -6', 'tzn': 'America/Costa_Rica', 'utc': '-6', 'dst': '-6'},
	{'title': 'America/Creston											UTC -7', 'tzn': 'America/Creston', 'utc': '-7', 'dst': '-7'},
	{'title': 'America/Cuiaba												UTC -4', 'tzn': 'America/Cuiaba', 'utc': '-4', 'dst': '-4'},
	{'title': 'America/Curacao											UTC -4', 'tzn': 'America/Curacao', 'utc': '-4', 'dst': '-4'},
	{'title': 'America/Danmarkshavn									UTC +0', 'tzn': 'America/Danmarkshavn', 'utc': '0', 'dst': '0'},
	{'title': 'America/Dawson												UTC -7', 'tzn': 'America/Dawson', 'utc': '-7', 'dst': '-7'},
	{'title': 'America/Dawson_Creek									UTC -7', 'tzn': 'America/Dawson_Creek', 'utc': '-7', 'dst': '-7'},
	{'title': 'America/Denver												UTC -7', 'tzn': 'America/Denver', 'utc': '-7', 'dst': '-6'},
	{'title': 'America/Detroit											UTC -5', 'tzn': 'America/Detroit', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Edmonton											UTC -7', 'tzn': 'America/Edmonton', 'utc': '-7', 'dst': '-6'},
	{'title': 'America/Eirunepe											UTC -5', 'tzn': 'America/Eirunepe', 'utc': '-5', 'dst': '-5'},
	{'title': 'America/El_Salvador									UTC -6', 'tzn': 'America/El_Salvador', 'utc': '-6', 'dst': '-6'},
	{'title': 'America/Fort_Nelson									UTC -7', 'tzn': 'America/Fort_Nelson', 'utc': '-7', 'dst': '-7'},
	{'title': 'America/Fortaleza										UTC -3', 'tzn': 'America/Fortaleza', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Glace_Bay										UTC -4', 'tzn': 'America/Glace_Bay', 'utc': '-4', 'dst': '-3'},
	{'title': 'America/Goose_Bay										UTC -4', 'tzn': 'America/Goose_Bay', 'utc': '-4', 'dst': '-3'},
	{'title': 'America/Grand_Turk										UTC -5', 'tzn': 'America/Grand_Turk', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Guatemala										UTC -6', 'tzn': 'America/Guatemala', 'utc': '-6', 'dst': '-6'},
	{'title': 'America/Guayaquil										UTC -5', 'tzn': 'America/Guayaquil', 'utc': '-5', 'dst': '-5'},
	{'title': 'America/Guyana												UTC -4', 'tzn': 'America/Guyana', 'utc': '-4', 'dst': '-4'},
	{'title': 'America/Halifax											UTC -4', 'tzn': 'America/Halifax', 'utc': '-4', 'dst': '-3'},
	{'title': 'America/Havana												UTC -5', 'tzn': 'America/Havana', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Hermosillo										UTC -7', 'tzn': 'America/Hermosillo', 'utc': '-7', 'dst': '-7'},
	{'title': 'America/Indiana/Indianapolis					UTC -5', 'tzn': 'America/Indiana/Indianapolis', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Indiana/Knox									UTC -6', 'tzn': 'America/Indiana/Knox', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/Indiana/Marengo							UTC -5', 'tzn': 'America/Indiana/Marengo', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Indiana/Petersburg						UTC -5', 'tzn': 'America/Indiana/Petersburg', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Indiana/Tell_City						UTC -6', 'tzn': 'America/Indiana/Tell_City', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/Indiana/Vevay								UTC -5', 'tzn': 'America/Indiana/Vevay', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Indiana/Vincennes						UTC -5', 'tzn': 'America/Indiana/Vincennes', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Indiana/Winamac							UTC -5', 'tzn': 'America/Indiana/Winamac', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Inuvik												UTC -7', 'tzn': 'America/Inuvik', 'utc': '-7', 'dst': '-6'},
	{'title': 'America/Iqaluit											UTC -5', 'tzn': 'America/Iqaluit', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Jamaica											UTC -5', 'tzn': 'America/Jamaica', 'utc': '-5', 'dst': '-5'},
	{'title': 'America/Juneau												UTC -9', 'tzn': 'America/Juneau', 'utc': '-9', 'dst': '-8'},
	{'title': 'America/Kentucky/Louisville					UTC -5', 'tzn': 'America/Kentucky/Louisville', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Kentucky/Monticello					UTC -5', 'tzn': 'America/Kentucky/Monticello', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/La_Paz												UTC -4', 'tzn': 'America/La_Paz', 'utc': '-4', 'dst': '-4'},
	{'title': 'America/Lima													UTC -5', 'tzn': 'America/Lima', 'utc': '-5', 'dst': '-5'},
	{'title': 'America/Los_Angeles									UTC -8', 'tzn': 'America/Los_Angeles', 'utc': '-8', 'dst': '-7'},
	{'title': 'America/Maceio												UTC -3', 'tzn': 'America/Maceio', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Managua											UTC -6', 'tzn': 'America/Managua', 'utc': '-6', 'dst': '-6'},
	{'title': 'America/Manaus												UTC -4', 'tzn': 'America/Manaus', 'utc': '-4', 'dst': '-4'},
	{'title': 'America/Martinique										UTC -4', 'tzn': 'America/Martinique', 'utc': '-4', 'dst': '-4'},
	{'title': 'America/Matamoros										UTC -6', 'tzn': 'America/Matamoros', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/Mazatlan											UTC -7', 'tzn': 'America/Mazatlan', 'utc': '-7', 'dst': '-6'},
	{'title': 'America/Menominee										UTC -6', 'tzn': 'America/Menominee', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/Merida												UTC -6', 'tzn': 'America/Merida', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/Metlakatla										UTC -9', 'tzn': 'America/Metlakatla', 'utc': '-9', 'dst': '-8'},
	{'title': 'America/Mexico_City									UTC -6', 'tzn': 'America/Mexico_City', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/Miquelon											UTC -3', 'tzn': 'America/Miquelon', 'utc': '-3', 'dst': '-2'},
	{'title': 'America/Moncton											UTC -4', 'tzn': 'America/Moncton', 'utc': '-4', 'dst': '-3'},
	{'title': 'America/Monterrey										UTC -6', 'tzn': 'America/Monterrey', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/Montevideo										UTC -3', 'tzn': 'America/Montevideo', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Nassau												UTC -5', 'tzn': 'America/Nassau', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/New_York											UTC -5', 'tzn': 'America/New_York', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Nipigon											UTC -5', 'tzn': 'America/Nipigon', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Nome													UTC -9', 'tzn': 'America/Nome', 'utc': '-9', 'dst': '-8'},
	{'title': 'America/Noronha											UTC -2', 'tzn': 'America/Noronha', 'utc': '-2', 'dst': '-2'},
	{'title': 'America/North_Dakota/Beulah					UTC -6', 'tzn': 'America/North_Dakota/Beulah', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/North_Dakota/Center					UTC -6', 'tzn': 'America/North_Dakota/Center', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/North_Dakota/New_Salem				UTC -6', 'tzn': 'America/North_Dakota/New_Salem', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/Nuuk													UTC -3', 'tzn': 'America/Nuuk', 'utc': '-3', 'dst': '-2'},
	{'title': 'America/Ojinaga											UTC -7', 'tzn': 'America/Ojinaga', 'utc': '-7', 'dst': '-6'},
	{'title': 'America/Panama												UTC -5', 'tzn': 'America/Panama', 'utc': '-5', 'dst': '-5'},
	{'title': 'America/Pangnirtung									UTC -5', 'tzn': 'America/Pangnirtung', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Paramaribo										UTC -3', 'tzn': 'America/Paramaribo', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Phoenix											UTC -7', 'tzn': 'America/Phoenix', 'utc': '-7', 'dst': '-7'},
	{'title': 'America/Port-au-Prince								UTC -5', 'tzn': 'America/Port-au-Prince', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Port_of_Spain								UTC -4', 'tzn': 'America/Port_of_Spain', 'utc': '-4', 'dst': '-4'},
	{'title': 'America/Porto_Velho									UTC -4', 'tzn': 'America/Porto_Velho', 'utc': '-4', 'dst': '-4'},
	{'title': 'America/Puerto_Rico									UTC -4', 'tzn': 'America/Puerto_Rico', 'utc': '-4', 'dst': '-4'},
	{'title': 'America/Punta_Arenas									UTC -3', 'tzn': 'America/Punta_Arenas', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Rainy_River									UTC -6', 'tzn': 'America/Rainy_River', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/Rankin_Inlet									UTC -6', 'tzn': 'America/Rankin_Inlet', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/Recife												UTC -3', 'tzn': 'America/Recife', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Regina												UTC -6', 'tzn': 'America/Regina', 'utc': '-6', 'dst': '-6'},
	{'title': 'America/Resolute											UTC -6', 'tzn': 'America/Resolute', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/Rio_Branco										UTC -5', 'tzn': 'America/Rio_Branco', 'utc': '-5', 'dst': '-5'},
	{'title': 'America/Santarem											UTC -3', 'tzn': 'America/Santarem', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Santiago											UTC -4', 'tzn': 'America/Santiago', 'utc': '-4', 'dst': '-3'},
	{'title': 'America/Santo_Domingo								UTC -4', 'tzn': 'America/Santo_Domingo', 'utc': '-4', 'dst': '-4'},
	{'title': 'America/Sao_Paulo										UTC -3', 'tzn': 'America/Sao_Paulo', 'utc': '-3', 'dst': '-3'},
	{'title': 'America/Scoresbysund									UTC -1', 'tzn': 'America/Scoresbysund', 'utc': '-1', 'dst': '0'},
	{'title': 'America/Sitka												UTC -9', 'tzn': 'America/Sitka', 'utc': '-9', 'dst': '-8'},
	{'title': 'America/St_Johns											UTC -3.5', 'tzn': 'America/St_Johns', 'utc': '-3.5', 'dst': '-2.5'},
	{'title': 'America/Swift_Current								UTC -6', 'tzn': 'America/Swift_Current', 'utc': '-6', 'dst': '-6'},
	{'title': 'America/Tegucigalpa									UTC -6', 'tzn': 'America/Tegucigalpa', 'utc': '-6', 'dst': '-6'},
	{'title': 'America/Thule												UTC -4', 'tzn': 'America/Thule', 'utc': '-4', 'dst': '-3'},
	{'title': 'America/Thunder_Bay									UTC -5', 'tzn': 'America/Thunder_Bay', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Tijuana											UTC -8', 'tzn': 'America/Tijuana', 'utc': '-8', 'dst': '-7'},
	{'title': 'America/Toronto											UTC -5', 'tzn': 'America/Toronto', 'utc': '-5', 'dst': '-4'},
	{'title': 'America/Vancouver										UTC -8', 'tzn': 'America/Vancouver', 'utc': '-8', 'dst': '-7'},
	{'title': 'America/Whitehorse										UTC -7', 'tzn': 'America/Whitehorse', 'utc': '-7', 'dst': '-7'},
	{'title': 'America/Winnipeg											UTC -6', 'tzn': 'America/Winnipeg', 'utc': '-6', 'dst': '-5'},
	{'title': 'America/Yakutat											UTC -9', 'tzn': 'America/Yakutat', 'utc': '-9', 'dst': '-8'},
	{'title': 'America/Yellowknife									UTC -7', 'tzn': 'America/Yellowknife', 'utc': '-7', 'dst': '-6'},
	{'title': 'Antarctica/Casey											UTC +11', 'tzn': 'Antarctica/Casey', 'utc': '11', 'dst': '11'},
	{'title': 'Antarctica/Davis											UTC +7', 'tzn': 'Antarctica/Davis', 'utc': '7', 'dst': '7'},
	{'title': 'Antarctica/DumontDUrville						UTC +10', 'tzn': 'Antarctica/DumontDUrville', 'utc': '10', 'dst': '10'},
	{'title': 'Antarctica/Macquarie									UTC +10', 'tzn': 'Antarctica/Macquarie', 'utc': '10', 'dst': '11'},
	{'title': 'Antarctica/Mawson										UTC +5', 'tzn': 'Antarctica/Mawson', 'utc': '5', 'dst': '5'},
	{'title': 'Antarctica/Palmer										UTC -3', 'tzn': 'Antarctica/Palmer', 'utc': '-3', 'dst': '-3'},
	{'title': 'Antarctica/Rothera										UTC -3', 'tzn': 'Antarctica/Rothera', 'utc': '-3', 'dst': '-3'},
	{'title': 'Antarctica/Syowa											UTC +3', 'tzn': 'Antarctica/Syowa', 'utc': '3', 'dst': '3'},
	{'title': 'Antarctica/Troll											UTC +0', 'tzn': 'Antarctica/Troll', 'utc': '0', 'dst': '2'},
	{'title': 'Antarctica/Vostok										UTC +6', 'tzn': 'Antarctica/Vostok', 'utc': '6', 'dst': '6'},
	{'title': 'Asia/Almaty													UTC +6', 'tzn': 'Asia/Almaty', 'utc': '6', 'dst': '6'},
	{'title': 'Asia/Amman														UTC +2', 'tzn': 'Asia/Amman', 'utc': '2', 'dst': '3'},
	{'title': 'Asia/Anadyr													UTC +12', 'tzn': 'Asia/Anadyr', 'utc': '+12', 'dst': '+12'},
	{'title': 'Asia/Aqtau														UTC +5', 'tzn': 'Asia/Aqtau', 'utc': '5', 'dst': '5'},
	{'title': 'Asia/Aqtobe													UTC +5', 'tzn': 'Asia/Aqtobe', 'utc': '5', 'dst': '5'},
	{'title': 'Asia/Ashgabat												UTC +5', 'tzn': 'Asia/Ashgabat', 'utc': '5', 'dst': '5'},
	{'title': 'Asia/Ashkhabad												UTC +5', 'tzn': 'Asia/Ashkhabad', 'utc': '5', 'dst': '5'},
	{'title': 'Asia/Atyrau													UTC +5', 'tzn': 'Asia/Atyrau', 'utc': '5', 'dst': '5'},
	{'title': 'Asia/Baghdad													UTC +3', 'tzn': 'Asia/Baghdad', 'utc': '3', 'dst': '3'},
	{'title': 'Asia/Baku														UTC +4', 'tzn': 'Asia/Baku', 'utc': '4', 'dst': '4'},
	{'title': 'Asia/Bangkok													UTC +7', 'tzn': 'Asia/Bangkok', 'utc': '7', 'dst': '7'},
	{'title': 'Asia/Barnaul													UTC +7', 'tzn': 'Asia/Barnaul', 'utc': '7', 'dst': '7'},
	{'title': 'Asia/Beirut													UTC +2', 'tzn': 'Asia/Beirut', 'utc': '2', 'dst': '3'},
	{'title': 'Asia/Bishkek													UTC +6', 'tzn': 'Asia/Bishkek', 'utc': '6', 'dst': '6'},
	{'title': 'Asia/Brunei													UTC +8', 'tzn': 'Asia/Brunei', 'utc': '8', 'dst': '8'},
	{'title': 'Asia/Chita														UTC +9', 'tzn': 'Asia/Chita', 'utc': '9', 'dst': '9'},
	{'title': 'Asia/Choibalsan											UTC +8', 'tzn': 'Asia/Choibalsan', 'utc': '8', 'dst': '8'},
	{'title': 'Asia/Colombo													UTC 5.5', 'tzn': 'Asia/Colombo', 'utc': '5.5', 'dst': '5.5'},
	{'title': 'Asia/Damascus												UTC +2', 'tzn': 'Asia/Damascus', 'utc': '2', 'dst': '3'},
	{'title': 'Asia/Dhaka														UTC +6', 'tzn': 'Asia/Dhaka', 'utc': '6', 'dst': '6'},
	{'title': 'Asia/Dili														UTC +9', 'tzn': 'Asia/Dili', 'utc': '9', 'dst': '9'},
	{'title': 'Asia/Dubai														UTC +4', 'tzn': 'Asia/Dubai', 'utc': '4', 'dst': '4'},
	{'title': 'Asia/Dushanbe												UTC +5', 'tzn': 'Asia/Dushanbe', 'utc': '5', 'dst': '5'},
	{'title': 'Asia/Famagusta												UTC +2', 'tzn': 'Asia/Famagusta', 'utc': '2', 'dst': '3'},
	{'title': 'Asia/Gaza														UTC +2', 'tzn': 'Asia/Gaza', 'utc': '2', 'dst': '3'},
	{'title': 'Asia/Hebron													UTC +2', 'tzn': 'Asia/Hebron', 'utc': '2', 'dst': '3'},
	{'title': 'Asia/Ho_Chi_Minh											UTC +7', 'tzn': 'Asia/Ho_Chi_Minh', 'utc': '7', 'dst': '7'},
	{'title': 'Asia/Hong_Kong												UTC +8', 'tzn': 'Asia/Hong_Kong', 'utc': '8', 'dst': '8'},
	{'title': 'Asia/Hovd														UTC +7', 'tzn': 'Asia/Hovd', 'utc': '7', 'dst': '7'},
	{'title': 'Asia/Irkutsk													UTC +8', 'tzn': 'Asia/Irkutsk', 'utc': '8', 'dst': '8'},
	{'title': 'Asia/Jakarta													UTC +7', 'tzn': 'Asia/Jakarta', 'utc': '7', 'dst': '7'},
	{'title': 'Asia/Jayapura												UTC +9', 'tzn': 'Asia/Jayapura', 'utc': '9', 'dst': '9'},
	{'title': 'Asia/Jerusalem												UTC +2', 'tzn': 'Asia/Jerusalem', 'utc': '2', 'dst': '3'},
	{'title': 'Asia/Kabul														UTC 4.5', 'tzn': 'Asia/Kabul', 'utc': '4.5', 'dst': '4.5'},
	{'title': 'Asia/Kamchatka												UTC +12', 'tzn': 'Asia/Kamchatka', 'utc': '+12', 'dst': '+12'},
	{'title': 'Asia/Karachi													UTC +5', 'tzn': 'Asia/Karachi', 'utc': '5', 'dst': '5'},
	{'title': 'Asia/Kathmandu												UTC +5.75', 'tzn': 'Asia/Kathmandu', 'utc': '5.75', 'dst': '5.75'},
	{'title': 'Asia/Khandyga												UTC +9', 'tzn': 'Asia/Khandyga', 'utc': '9', 'dst': '9'},
	{'title': 'Asia/Kolkata													UTC 5.5', 'tzn': 'Asia/Kolkata', 'utc': '5.5', 'dst': '5.5'},
	{'title': 'Asia/Krasnoyarsk											UTC +7', 'tzn': 'Asia/Krasnoyarsk', 'utc': '7', 'dst': '7'},
	{'title': 'Asia/Kuala_Lumpur										UTC +8', 'tzn': 'Asia/Kuala_Lumpur', 'utc': '8', 'dst': '8'},
	{'title': 'Asia/Kuching													UTC +8', 'tzn': 'Asia/Kuching', 'utc': '8', 'dst': '8'},
	{'title': 'Asia/Macau														UTC +8', 'tzn': 'Asia/Macau', 'utc': '8', 'dst': '8'},
	{'title': 'Asia/Magadan													UTC +11', 'tzn': 'Asia/Magadan', 'utc': '+11', 'dst': '+11'},
	{'title': 'Asia/Makassar												UTC +8', 'tzn': 'Asia/Makassar', 'utc': '8', 'dst': '8'},
	{'title': 'Asia/Manila													UTC +8', 'tzn': 'Asia/Manila', 'utc': '8', 'dst': '8'},
	{'title': 'Asia/Nicosia													UTC +2', 'tzn': 'Asia/Nicosia', 'utc': '2', 'dst': '3'},
	{'title': 'Asia/Novokuznetsk										UTC +7', 'tzn': 'Asia/Novokuznetsk', 'utc': '7', 'dst': '7'},
	{'title': 'Asia/Novosibirsk											UTC +7', 'tzn': 'Asia/Novosibirsk', 'utc': '7', 'dst': '7'},
	{'title': 'Asia/Omsk														UTC +6', 'tzn': 'Asia/Omsk', 'utc': '6', 'dst': '6'},
	{'title': 'Asia/Oral														UTC +5', 'tzn': 'Asia/Oral', 'utc': '5', 'dst': '5'},
	{'title': 'Asia/Pontianak												UTC +7', 'tzn': 'Asia/Pontianak', 'utc': '7', 'dst': '7'},
	{'title': 'Asia/Pyongyang												UTC +9', 'tzn': 'Asia/Pyongyang', 'utc': '9', 'dst': '9'},
	{'title': 'Asia/Qatar														UTC +3', 'tzn': 'Asia/Qatar', 'utc': '3', 'dst': '3'},
	{'title': 'Asia/Qostanay												UTC +6', 'tzn': 'Asia/Qostanay', 'utc': '6', 'dst': '6'},
	{'title': 'Asia/Qyzylorda												UTC +5', 'tzn': 'Asia/Qyzylorda', 'utc': '5', 'dst': '5'},
	{'title': 'Asia/Riyadh													UTC +3', 'tzn': 'Asia/Riyadh', 'utc': '3', 'dst': '3'},
	{'title': 'Asia/Sakhalin												UTC +11', 'tzn': 'Asia/Sakhalin', 'utc': '+11', 'dst': '+11'},
	{'title': 'Asia/Samarkand												UTC +5', 'tzn': 'Asia/Samarkand', 'utc': '5', 'dst': '5'},
	{'title': 'Asia/Seoul														UTC +9', 'tzn': 'Asia/Seoul', 'utc': '9', 'dst': '9'},
	{'title': 'Asia/Shanghai												UTC +8', 'tzn': 'Asia/Shanghai', 'utc': '8', 'dst': '8'},
	{'title': 'Asia/Singapore												UTC +8', 'tzn': 'Asia/Singapore', 'utc': '8', 'dst': '8'},
	{'title': 'Asia/Srednekolymsk										UTC +11', 'tzn': 'Asia/Srednekolymsk', 'utc': '+11', 'dst': '+11'},
	{'title': 'Asia/Taipei													UTC +8', 'tzn': 'Asia/Taipei', 'utc': '8', 'dst': '8'},
	{'title': 'Asia/Tashkent												UTC +5', 'tzn': 'Asia/Tashkent', 'utc': '5', 'dst': '5'},
	{'title': 'Asia/Tbilisi													UTC +4', 'tzn': 'Asia/Tbilisi', 'utc': '4', 'dst': '4'},
	{'title': 'Asia/Tehran													UTC +3.5', 'tzn': 'Asia/Tehran', 'utc': '3.5', 'dst': '4.5'},
	{'title': 'Asia/Thimphu													UTC +6', 'tzn': 'Asia/Thimphu', 'utc': '6', 'dst': '6'},
	{'title': 'Asia/Tokyo														UTC +9', 'tzn': 'Asia/Tokyo', 'utc': '9', 'dst': '9'},
	{'title': 'Asia/Tomsk														UTC +7', 'tzn': 'Asia/Tomsk', 'utc': '7', 'dst': '7'},
	{'title': 'Asia/Ulaanbaatar											UTC +8', 'tzn': 'Asia/Ulaanbaatar', 'utc': '8', 'dst': '8'},
	{'title': 'Asia/Urumqi													UTC +6', 'tzn': 'Asia/Urumqi', 'utc': '6', 'dst': '6'},
	{'title': 'Asia/Ust-Nera												UTC +10', 'tzn': 'Asia/Ust-Nera', 'utc': '10', 'dst': '10'},
	{'title': 'Asia/Vladivostok											UTC +10', 'tzn': 'Asia/Vladivostok', 'utc': '10', 'dst': '10'},
	{'title': 'Asia/Yakutsk													UTC +9', 'tzn': 'Asia/Yakutsk', 'utc': '9', 'dst': '9'},
	{'title': 'Asia/Yangon													UTC +6.5', 'tzn': 'Asia/Yangon', 'utc': '6.5', 'dst': '6.5'},
	{'title': 'Asia/Yekaterinburg										UTC +5', 'tzn': 'Asia/Yekaterinburg', 'utc': '5', 'dst': '5'},
	{'title': 'Asia/Yerevan													UTC +4', 'tzn': 'Asia/Yerevan', 'utc': '4', 'dst': '4'},
	{'title': 'Atlantic/Azores											UTC -1', 'tzn': 'Atlantic/Azores', 'utc': '-1', 'dst': '0'},
	{'title': 'Atlantic/Bermuda											UTC -4', 'tzn': 'Atlantic/Bermuda', 'utc': '-4', 'dst': '-3'},
	{'title': 'Atlantic/Canary											UTC +0', 'tzn': 'Atlantic/Canary', 'utc': '0', 'dst': '1'},
	{'title': 'Atlantic/Cape_Verde									UTC -1', 'tzn': 'Atlantic/Cape_Verde', 'utc': '-1', 'dst': '-1'},
	{'title': 'Atlantic/Faroe												UTC +0', 'tzn': 'Atlantic/Faroe', 'utc': '0', 'dst': '1'},
	{'title': 'Atlantic/Madeira											UTC +0', 'tzn': 'Atlantic/Madeira', 'utc': '0', 'dst': '1'},
	{'title': 'Atlantic/Reykjavik										UTC +0', 'tzn': 'Atlantic/Reykjavik', 'utc': '0', 'dst': '0'},
	{'title': 'Atlantic/South_Georgia								UTC -2', 'tzn': 'Atlantic/South_Georgia', 'utc': '-2', 'dst': '-2'},
	{'title': 'Atlantic/Stanley											UTC -3', 'tzn': 'Atlantic/Stanley', 'utc': '-3', 'dst': '-3'},
	{'title': 'Australia/Adelaide										UTC +9.5', 'tzn': 'Australia/Adelaide', 'utc': '9.5', 'dst': '10.5'},
	{'title': 'Australia/Brisbane										UTC +10', 'tzn': 'Australia/Brisbane', 'utc': '10', 'dst': '10'},
	{'title': 'Australia/Broken_Hill								UTC +9.5', 'tzn': 'Australia/Broken_Hill', 'utc': '9.5', 'dst': '10.5'},
	{'title': 'Australia/Darwin											UTC +9.5', 'tzn': 'Australia/Darwin', 'utc': '9.5', 'dst': '9.5'},
	{'title': 'Australia/Eucla											UTC +8.75', 'tzn': 'Australia/Eucla', 'utc': '8.75', 'dst': '8.75'},
	{'title': 'Australia/Hobart											UTC +10', 'tzn': 'Australia/Hobart', 'utc': '10', 'dst': '11'},
	{'title': 'Australia/Lindeman										UTC +10', 'tzn': 'Australia/Lindeman', 'utc': '10', 'dst': '10'},
	{'title': 'Australia/Lord_Howe									UTC +10.5', 'tzn': 'Australia/Lord_Howe', 'utc': '10.5', 'dst': '11'},
	{'title': 'Australia/Melbourne									UTC +10', 'tzn': 'Australia/Melbourne', 'utc': '10', 'dst': '11'},
	{'title': 'Australia/Perth											UTC +8', 'tzn': 'Australia/Perth', 'utc': '8', 'dst': '8'},
	{'title': 'Australia/Sydney											UTC +10', 'tzn': 'Australia/Sydney', 'utc': '10', 'dst': '11'},
	{'title': 'Etc/GMT															UTC +0', 'tzn': 'Etc/GMT', 'utc': '0', 'dst': '0'},
	{'title': 'Etc/GMT+1														UTC -1', 'tzn': 'Etc/GMT+1', 'utc': '-1', 'dst': '-1'},
	{'title': 'Etc/GMT+10														UTC -10', 'tzn': 'Etc/GMT+10', 'utc': '-10', 'dst': '-10'},
	{'title': 'Etc/GMT+11														UTC -11', 'tzn': 'Etc/GMT+11', 'utc': '-11', 'dst': '-11'},
	{'title': 'Etc/GMT+12														UTC -12', 'tzn': 'Etc/GMT+12', 'utc': '-12', 'dst': '-12'},
	{'title': 'Etc/GMT+2														UTC -2', 'tzn': 'Etc/GMT+2', 'utc': '-2', 'dst': '-2'},
	{'title': 'Etc/GMT+3														UTC -3', 'tzn': 'Etc/GMT+3', 'utc': '-3', 'dst': '-3'},
	{'title': 'Etc/GMT+4														UTC -4', 'tzn': 'Etc/GMT+4', 'utc': '-4', 'dst': '-4'},
	{'title': 'Etc/GMT+5														UTC -5', 'tzn': 'Etc/GMT+5', 'utc': '-5', 'dst': '-5'},
	{'title': 'Etc/GMT+6														UTC -6', 'tzn': 'Etc/GMT+6', 'utc': '-6', 'dst': '-6'},
	{'title': 'Etc/GMT+7														UTC -7', 'tzn': 'Etc/GMT+7', 'utc': '-7', 'dst': '-7'},
	{'title': 'Etc/GMT+8														UTC -8', 'tzn': 'Etc/GMT+8', 'utc': '-8', 'dst': '-8'},
	{'title': 'Etc/GMT+9														UTC -9', 'tzn': 'Etc/GMT+9', 'utc': '-9', 'dst': '-9'},
	{'title': 'Etc/GMT-1														UTC +1', 'tzn': 'Etc/GMT-1', 'utc': '1', 'dst': '1'},
	{'title': 'Etc/GMT-10														UTC +10', 'tzn': 'Etc/GMT-10', 'utc': '10', 'dst': '10'},
	{'title': 'Etc/GMT-11														UTC +11', 'tzn': 'Etc/GMT-11', 'utc': '11', 'dst': '11'},
	{'title': 'Etc/GMT-12														UTC +12', 'tzn': 'Etc/GMT-12', 'utc': '12', 'dst': '12'},
	{'title': 'Etc/GMT-13														UTC +13', 'tzn': 'Etc/GMT-13', 'utc': '13', 'dst': '13'},
	{'title': 'Etc/GMT-14														UTC +14', 'tzn': 'Etc/GMT-14', 'utc': '14', 'dst': '14'},
	{'title': 'Etc/GMT-2														UTC +2', 'tzn': 'Etc/GMT-2', 'utc': '2', 'dst': '2'},
	{'title': 'Etc/GMT-3														UTC +3', 'tzn': 'Etc/GMT-3', 'utc': '3', 'dst': '3'},
	{'title': 'Etc/GMT-4														UTC +4', 'tzn': 'Etc/GMT-4', 'utc': '4', 'dst': '4'},
	{'title': 'Etc/GMT-5														UTC +5', 'tzn': 'Etc/GMT-5', 'utc': '5', 'dst': '5'},
	{'title': 'Etc/GMT-6														UTC +6', 'tzn': 'Etc/GMT-6', 'utc': '6', 'dst': '6'},
	{'title': 'Etc/GMT-7														UTC +7', 'tzn': 'Etc/GMT-7', 'utc': '7', 'dst': '7'},
	{'title': 'Etc/GMT-8														UTC +8', 'tzn': 'Etc/GMT-8', 'utc': '8', 'dst': '8'},
	{'title': 'Etc/GMT-9														UTC +9', 'tzn': 'Etc/GMT-9', 'utc': '9', 'dst': '9'},
	{'title': 'Etc/UTC															UTC +0', 'tzn': 'Etc/UTC', 'utc': '0', 'dst': '0'},
	{'title': 'Europe/Amsterdam											UTC +1', 'tzn': 'Europe/Amsterdam', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Andorra												UTC +1', 'tzn': 'Europe/Andorra', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Astrakhan											UTC +4', 'tzn': 'Europe/Astrakhan', 'utc': '4', 'dst': '4'},
	{'title': 'Europe/Athens												UTC +2', 'tzn': 'Europe/Athens', 'utc': '2', 'dst': '3'},
	{'title': 'Europe/Belgrade											UTC +1', 'tzn': 'Europe/Belgrade', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Berlin												UTC +1', 'tzn': 'Europe/Berlin', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Brussels											UTC +1', 'tzn': 'Europe/Brussels', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Bucharest											UTC +2', 'tzn': 'Europe/Bucharest', 'utc': '2', 'dst': '3'},
	{'title': 'Europe/Budapest											UTC +1', 'tzn': 'Europe/Budapest', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Chisinau											UTC +2', 'tzn': 'Europe/Chisinau', 'utc': '2', 'dst': '3'},
	{'title': 'Europe/Copenhagen										UTC +1', 'tzn': 'Europe/Copenhagen', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Dublin												UTC +1', 'tzn': 'Europe/Dublin', 'utc': '1', 'dst': '0'},
	{'title': 'Europe/Gibraltar											UTC +1', 'tzn': 'Europe/Gibraltar', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Helsinki											UTC +2', 'tzn': 'Europe/Helsinki', 'utc': '2', 'dst': '3'},
	{'title': 'Europe/Istanbul											UTC +3', 'tzn': 'Europe/Istanbul', 'utc': '3', 'dst': '3'},
	{'title': 'Europe/Kaliningrad										UTC +2', 'tzn': 'Europe/Kaliningrad', 'utc': '2', 'dst': '2'},
	{'title': 'Europe/Kiev													UTC +2', 'tzn': 'Europe/Kiev', 'utc': '2', 'dst': '3'},
	{'title': 'Europe/Kirov													UTC +3', 'tzn': 'Europe/Kirov', 'utc': '3', 'dst': '3'},
	{'title': 'Europe/Lisbon												UTC +0', 'tzn': 'Europe/Lisbon', 'utc': '0', 'dst': '1'},
	{'title': 'Europe/London												UTC +0', 'tzn': 'Europe/London', 'utc': '0', 'dst': '1'},
	{'title': 'Europe/Luxembourg										UTC +1', 'tzn': 'Europe/Luxembourg', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Madrid												UTC +1', 'tzn': 'Europe/Madrid', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Malta													UTC +1', 'tzn': 'Europe/Malta', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Minsk													UTC +3', 'tzn': 'Europe/Minsk', 'utc': '3', 'dst': '3'},
	{'title': 'Europe/Monaco												UTC +1', 'tzn': 'Europe/Monaco', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Moscow												UTC +3', 'tzn': 'Europe/Moscow', 'utc': '3', 'dst': '3'},
	{'title': 'Europe/Oslo													UTC +1', 'tzn': 'Europe/Oslo', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Paris													UTC +1', 'tzn': 'Europe/Paris', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Prague												UTC +1', 'tzn': 'Europe/Prague', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Riga													UTC +2', 'tzn': 'Europe/Riga', 'utc': '2', 'dst': '3'},
	{'title': 'Europe/Rome													UTC +1', 'tzn': 'Europe/Rome', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Samara												UTC +4', 'tzn': 'Europe/Samara', 'utc': '4', 'dst': '4'},
	{'title': 'Europe/Saratov												UTC +4', 'tzn': 'Europe/Saratov', 'utc': '4', 'dst': '4'},
	{'title': 'Europe/Simferopol										UTC +3', 'tzn': 'Europe/Simferopol', 'utc': '3', 'dst': '3'},
	{'title': 'Europe/Sofia													UTC +2', 'tzn': 'Europe/Sofia', 'utc': '2', 'dst': '3'},
	{'title': 'Europe/Stockholm											UTC +1', 'tzn': 'Europe/Stockholm', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Tallinn												UTC +2', 'tzn': 'Europe/Tallinn', 'utc': '2', 'dst': '3'},
	{'title': 'Europe/Tirane												UTC +1', 'tzn': 'Europe/Tirane', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Ulyanovsk											UTC +4', 'tzn': 'Europe/Ulyanovsk', 'utc': '4', 'dst': '4'},
	{'title': 'Europe/Uzhgorod											UTC +2', 'tzn': 'Europe/Uzhgorod', 'utc': '2', 'dst': '3'},
	{'title': 'Europe/Vienna												UTC +1', 'tzn': 'Europe/Vienna', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Vilnius												UTC +2', 'tzn': 'Europe/Vilnius', 'utc': '2', 'dst': '3'},
	{'title': 'Europe/Volgograd											UTC +3', 'tzn': 'Europe/Volgograd', 'utc': '3', 'dst': '3'},
	{'title': 'Europe/Warsaw												UTC +1', 'tzn': 'Europe/Warsaw', 'utc': '1', 'dst': '2'},
	{'title': 'Europe/Zaporozhye										UTC +2', 'tzn': 'Europe/Zaporozhye', 'utc': '2', 'dst': '3'},
	{'title': 'Europe/Zurich												UTC +1', 'tzn': 'Europe/Zurich', 'utc': '1', 'dst': '2'},
	{'title': 'Factory															UTC +0', 'tzn': 'Factory', 'utc': '0', 'dst': '0'},
	{'title': 'Indian/Chagos												UTC +6', 'tzn': 'Indian/Chagos', 'utc': '6', 'dst': '6'},
	{'title': 'Indian/Christmas											UTC +7', 'tzn': 'Indian/Christmas', 'utc': '7', 'dst': '7'},
	{'title': 'Indian/Cocos													UTC 6.5', 'tzn': 'Indian/Cocos', 'utc': '6.5', 'dst': '6.5'},
	{'title': 'Indian/Kerguelen											UTC +5', 'tzn': 'Indian/Kerguelen', 'utc': '5', 'dst': '5'},
	{'title': 'Indian/Mahe													UTC +4', 'tzn': 'Indian/Mahe', 'utc': '4', 'dst': '4'},
	{'title': 'Indian/Maldives											UTC +5', 'tzn': 'Indian/Maldives', 'utc': '5', 'dst': '5'},
	{'title': 'Indian/Mauritius											UTC +4', 'tzn': 'Indian/Mauritius', 'utc': '4', 'dst': '4'},
	{'title': 'Indian/Reunion												UTC +4', 'tzn': 'Indian/Reunion', 'utc': '4', 'dst': '4'},
	{'title': 'Pacific/Apia													UTC +13', 'tzn': 'Pacific/Apia', 'utc': '13', 'dst': '14'},
	{'title': 'Pacific/Auckland											UTC +12', 'tzn': 'Pacific/Auckland', 'utc': '12', 'dst': '13'},
	{'title': 'Pacific/Bougainville									UTC +11', 'tzn': 'Pacific/Bougainville', 'utc': '11', 'dst': '11'},
	{'title': 'Pacific/Chatham											UTC +12.75', 'tzn': 'Pacific/Chatham', 'utc': '12.75', 'dst': '13.75'},
	{'title': 'Pacific/Chuuk												UTC +10', 'tzn': 'Pacific/Chuuk', 'utc': '10', 'dst': '10'},
	{'title': 'Pacific/Easter												UTC -6', 'tzn': 'Pacific/Easter', 'utc': '-6', 'dst': '-5'},
	{'title': 'Pacific/Efate												UTC +11', 'tzn': 'Pacific/Efate', 'utc': '11', 'dst': '11'},
	{'title': 'Pacific/Enderbury										UTC +13', 'tzn': 'Pacific/Enderbury', 'utc': '13', 'dst': '13'},
	{'title': 'Pacific/Fakaofo											UTC +13', 'tzn': 'Pacific/Fakaofo', 'utc': '13', 'dst': '13'},
	{'title': 'Pacific/Fiji													UTC +12', 'tzn': 'Pacific/Fiji', 'utc': '12', 'dst': '13'},
	{'title': 'Pacific/Funafuti											UTC +12', 'tzn': 'Pacific/Funafuti', 'utc': '12', 'dst': '12'},
	{'title': 'Pacific/Galapagos										UTC -6', 'tzn': 'Pacific/Galapagos', 'utc': '-6', 'dst': '-6'},
	{'title': 'Pacific/Gambier											UTC -9', 'tzn': 'Pacific/Gambier', 'utc': '-9', 'dst': '-9'},
	{'title': 'Pacific/Guadalcanal									UTC +11', 'tzn': 'Pacific/Guadalcanal', 'utc': '11', 'dst': '11'},
	{'title': 'Pacific/Guam													UTC +10', 'tzn': 'Pacific/Guam', 'utc': '10', 'dst': '10'},
	{'title': 'Pacific/Honolulu											UTC -10', 'tzn': 'Pacific/Honolulu', 'utc': '-10', 'dst': '-10'},
	{'title': 'Pacific/Kiritimati										UTC +14', 'tzn': 'Pacific/Kiritimati', 'utc': '14', 'dst': '14'},
	{'title': 'Pacific/Kosrae												UTC +11', 'tzn': 'Pacific/Kosrae', 'utc': '11', 'dst': '11'},
	{'title': 'Pacific/Kwajalein										UTC +12', 'tzn': 'Pacific/Kwajalein', 'utc': '12', 'dst': '12'},
	{'title': 'Pacific/Majuro												UTC +12', 'tzn': 'Pacific/Majuro', 'utc': '12', 'dst': '12'},
	{'title': 'Pacific/Marquesas										UTC -9.5', 'tzn': 'Pacific/Marquesas', 'utc': '-9.5', 'dst': '-9.5'},
	{'title': 'Pacific/Nauru												UTC +12', 'tzn': 'Pacific/Nauru', 'utc': '12', 'dst': '12'},
	{'title': 'Pacific/Niue													UTC -11', 'tzn': 'Pacific/Niue', 'utc': '-11', 'dst': '-11'},
	{'title': 'Pacific/Norfolk											UTC +11', 'tzn': 'Pacific/Norfolk', 'utc': '11', 'dst': '12'},
	{'title': 'Pacific/Noumea												UTC +11', 'tzn': 'Pacific/Noumea', 'utc': '11', 'dst': '11'},
	{'title': 'Pacific/Pago_Pago										UTC -11', 'tzn': 'Pacific/Pago_Pago', 'utc': '-11', 'dst': '-11'},
	{'title': 'Pacific/Palau												UTC +9', 'tzn': 'Pacific/Palau', 'utc': '9', 'dst': '9'},
	{'title': 'Pacific/Pitcairn											UTC -8', 'tzn': 'Pacific/Pitcairn', 'utc': '-8', 'dst': '-8'},
	{'title': 'Pacific/Pohnpei											UTC +11', 'tzn': 'Pacific/Pohnpei', 'utc': '11', 'dst': '11'},
	{'title': 'Pacific/Port_Moresby									UTC +10', 'tzn': 'Pacific/Port_Moresby', 'utc': '10', 'dst': '10'},
	{'title': 'Pacific/Rarotonga										UTC -10', 'tzn': 'Pacific/Rarotonga', 'utc': '-10', 'dst': '-10'},
	{'title': 'Pacific/Tahiti												UTC -10', 'tzn': 'Pacific/Tahiti', 'utc': '-10', 'dst': '-10'},
	{'title': 'Pacific/Tarawa												UTC +12', 'tzn': 'Pacific/Tarawa', 'utc': '12', 'dst': '12'},
	{'title': 'Pacific/Tongatapu										UTC +13', 'tzn': 'Pacific/Tongatapu', 'utc': '13', 'dst': '13'},
	{'title': 'Pacific/Wake													UTC +12', 'tzn': 'Pacific/Wake', 'utc': '12', 'dst': '12'},
	{'title': 'Pacific/Wallis												UTC +12', 'tzn': 'Pacific/Wallis', 'utc': '12', 'dst': '12'}

]

tzalias = [

{'title': 'Africa/Addis_Ababa', 'utc': '3', 'dst': '3'},
{'title': 'Africa/Asmara', 'utc': '3', 'dst': '3'},
{'title': 'Africa/Bamako', 'utc': '0', 'dst': '0'},
{'title': 'Africa/Bangui', 'utc': '1', 'dst': '1'},
{'title': 'Africa/Banjul', 'utc': '0', 'dst': '0'},
{'title': 'Africa/Blantyre', 'utc': '2', 'dst': '2'},
{'title': 'Africa/Brazzaville', 'utc': '1', 'dst': '1'},
{'title': 'Africa/Bujumbura', 'utc': '2', 'dst': '2'},
{'title': 'Africa/Conakry', 'utc': '0', 'dst': '0'},
{'title': 'Africa/Dakar', 'utc': '0', 'dst': '0'},
{'title': 'Africa/Dar_es_Salaam', 'utc': '3', 'dst': '3'},
{'title': 'Africa/Djibouti', 'utc': '3', 'dst': '3'},
{'title': 'Africa/Freetown', 'utc': '0', 'dst': '0'},
{'title': 'Africa/Gaborone', 'utc': '2', 'dst': '2'},
{'title': 'Africa/Harare', 'utc': '2', 'dst': '2'},
{'title': 'Africa/Kampala', 'utc': '3', 'dst': '3'},
{'title': 'Africa/Kigali', 'utc': '2', 'dst': '2'},
{'title': 'Africa/Kinshasa', 'utc': '1', 'dst': '1'},
{'title': 'Africa/Libreville', 'utc': '1', 'dst': '1'},
{'title': 'Africa/Lome', 'utc': '0', 'dst': '0'},
{'title': 'Africa/Luanda', 'utc': '1', 'dst': '1'},
{'title': 'Africa/Lubumbashi', 'utc': '2', 'dst': '2'},
{'title': 'Africa/Lusaka', 'utc': '2', 'dst': '2'},
{'title': 'Africa/Malabo', 'utc': '1', 'dst': '1'},
{'title': 'Africa/Maseru', 'utc': '2', 'dst': '2'},
{'title': 'Africa/Mbabane', 'utc': '2', 'dst': '2'},
{'title': 'Africa/Mogadishu', 'utc': '3', 'dst': '3'},
{'title': 'Africa/Niamey', 'utc': '1', 'dst': '1'},
{'title': 'Africa/Nouakchott', 'utc': '0', 'dst': '0'},
{'title': 'Africa/Ouagadougou', 'utc': '0', 'dst': '0'},
{'title': 'Africa/Porto-Novo', 'utc': '1', 'dst': '1'},
{'title': 'America/Anguilla', 'utc': '-4', 'dst': '-4'},
{'title': 'America/Antigua', 'utc': '-4', 'dst': '-4'},
{'title': 'America/Aruba', 'utc': '-4', 'dst': '-4'},
{'title': 'America/Cayman', 'utc': '-5', 'dst': '-5'},
{'title': 'America/Dominica', 'utc': '-4', 'dst': '-4'},
{'title': 'America/Grenada', 'utc': '-4', 'dst': '-4'},
{'title': 'America/Guadeloupe', 'utc': '-4', 'dst': '-4'},
{'title': 'America/Kralendijk', 'utc': '-4', 'dst': '-4'},
{'title': 'America/Lower_Princes', 'utc': '-4', 'dst': '-4'},
{'title': 'America/Marigot', 'utc': '-4', 'dst': '-4'},
{'title': 'America/Montserrat', 'utc': '-4', 'dst': '-4'},
{'title': 'America/St_Barthelemy', 'utc': '-4', 'dst': '-4'},
{'title': 'America/St_Kitts', 'utc': '-4', 'dst': '-4'},
{'title': 'America/St_Lucia', 'utc': '-4', 'dst': '-4'},
{'title': 'America/St_Thomas', 'utc': '-4', 'dst': '-4'},
{'title': 'America/St_Vincent', 'utc': '-4', 'dst': '-4'},
{'title': 'America/Tortola', 'utc': '-4', 'dst': '-4'},
{'title': 'Antarctica/McMurdo', 'utc': '12', 'dst': '13'},
{'title': 'Arctic/Longyearbyen', 'utc': '1', 'dst': '2'},
{'title': 'Asia/Aden', 'utc': '3', 'dst': '3'},
{'title': 'Asia/Bahrain', 'utc': '3', 'dst': '3'},
{'title': 'Asia/Istanbul', 'utc': '3', 'dst': '3'},
{'title': 'Asia/Kuwait', 'utc': '3', 'dst': '3'},
{'title': 'Asia/Muscat', 'utc': '4', 'dst': '4'},
{'title': 'Asia/Phnom_Penh', 'utc': '7', 'dst': '7'},
{'title': 'Asia/Vientiane', 'utc': '7', 'dst': '7'},
{'title': 'Atlantic/St_Helena', 'utc': '0', 'dst': '0'},
{'title': 'Etc/GMT+0', 'utc': '0', 'dst': '0'},
{'title': 'Etc/GMT-0', 'utc': '0', 'dst': '0'},
{'title': 'Etc/GMT0', 'utc': '0', 'dst': '0'},
{'title': 'Europe/Bratislava', 'utc': '1', 'dst': '2'},
{'title': 'Europe/Busingen', 'utc': '1', 'dst': '2'},
{'title': 'Europe/Guernsey', 'utc': '0', 'dst': '1'},
{'title': 'Europe/Isle_of_Man', 'utc': '0', 'dst': '1'},
{'title': 'Europe/Jersey', 'utc': '0', 'dst': '1'},
{'title': 'Europe/Ljubljana', 'utc': '1', 'dst': '2'},
{'title': 'Europe/Mariehamn', 'utc': '2', 'dst': '3'},
{'title': 'Europe/Nicosia', 'utc': '2', 'dst': '3'},
{'title': 'Europe/Podgorica', 'utc': '1', 'dst': '2'},
{'title': 'Europe/San_Marino', 'utc': '1', 'dst': '2'},
{'title': 'Europe/Sarajevo', 'utc': '1', 'dst': '2'},
{'title': 'Europe/Skopje', 'utc': '1', 'dst': '2'},
{'title': 'Europe/Vaduz', 'utc': '1', 'dst': '2'},
{'title': 'Europe/Vatican', 'utc': '1', 'dst': '2'},
{'title': 'Europe/Zagreb', 'utc': '1', 'dst': '2'},
{'title': 'GMT', 'utc': '0', 'dst': '0'},
{'title': 'Indian/Antananarivo', 'utc': '3', 'dst': '3'},
{'title': 'Indian/Comoro', 'utc': '3', 'dst': '3'},
{'title': 'Indian/Mayotte', 'utc': '3', 'dst': '3'},
{'title': 'Pacific/Midway', 'utc': '-11', 'dst': '-11'},
{'title': 'Pacific/Saipan', 'utc': '10', 'dst': '10'},
{'title': 'UTC', 'utc': '0', 'dst': '0'}

]

wochentage_kuerzel = ["Su.", "Mo.", "Tu.", "We.", "Th.", "Fr.", "Sa.", "Su."]

#textfield_did_change Alternative einbauen

class MyTextFieldDelegate (object):
	
	def textfield_did_change(self, textfield):
		global filter_is_set
		global filter
		filter_is_set = 1
	
		txt = view['textfield1'].text
		#print(txt)
		filter = []				
		filter = [items for items in items
		if txt.lower() in items.lower()]
		#print(filter)	
		data_source.items = filter
		view.name = 'Choose Location' + ' (' + str(len(filter)) + ')'

class ReportDelegate (object):

	def textfield_did_end_editing(self, textfield):
		global sathoehe
			
		if float(vsettings['sathoehe'].text) < 250.0:
			vsettings['sathoehe'].text = '250.0'
			dialogs.hud_alert('Minimum map size reset to 250 m².', 'error', 1.8)			
		
		sathoehe = float(vsettings['sathoehe'].text)

def switch_did_change(sender):
	global printmoonstats
	
	if vsettings['switch1'].value is True:
		printmoonstats = 0
	else:
		printmoonstats = 1

def resize(file, scale):
	basewidth = scale
	img = Image.open(file)
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), Image.ANTIALIAS)
	img.save(file)
	
def filter(sender):
	global filter_is_set
	filter_is_set = 1
	
	v = sender.superview
	txt = v['textfield1'].text
	#print(txt)
	filter = []				
	filter = [items for items in items
	if txt.lower() in items.lower()]
	#print(filter)	
	data_source.items = filter
	
def toTZ(d):
    #return tz.normalize(tz.localize(d)).astimezone(pytz.utc)
    return tzstatus.normalize(tzstatus.localize(d)).astimezone(tz2)

def getzeitwert(selected_year):
	fmt_long='%Y-%m-%d %H:%M:%S '
	fmt_timestamp="%s"
	zeitwert = []
	for d in utt:
		tstamp = d.strftime(fmt_timestamp)
		dstr = d.strftime(fmt_long)
		if d.year == selected_year :
			#print(tstamp + "\t# " + dstr + "UTC")
			dyear = int(d.strftime('%Y'))
			dmonth = int(d.strftime('%m'))
			dday = int(d.strftime('%d'))
			dhour = int(d.strftime('%H'))
			dminute = int(d.strftime('%M'))
			dsecond = int(d.strftime('%S'))
			test = datetime.datetime(dyear,dmonth,dday,dhour,dminute,dsecond)
			test = toTZ(test)
			zeitwert.append(test)  
	return(zeitwert)
			
def do_wcount(wdate,wyear,wmonth,wday,vergleichswert):
	wcount = 0	
	wdaylocal = 1
	for i in range(1, wday+1):
		if wdate.weekday() == vergleichswert:
			wcount += 1
		wdaylocal += 1
		try:
			wdate = datetime.datetime(wyear,wmonth,wdaylocal)
		except:
			pass
			
	if wcount == 4:
		wcount += 1
		
	return wcount
	
def do_wday(wdate, wcountexternal, vergleichswert, tagbasis, monat):
	finalwday = 0
	wcountlocal = 0	
	wday = 1
	
	for i in range(1, tagbasis+1):
		if wdate.weekday() == vergleichswert:
			wcountlocal += 1
			
		if wcountlocal == wcountexternal:
			finalwday = wday
			break
				
		wday += 1

		try:
			wdate = datetime.datetime(selected_year,monat,wday)
		except:
			pass
	
	return finalwday
	
def checkdststatus():		
	global tzstatus, tz2, utt, selected_year
	tzstatus = pytz.timezone('UTC')
	tf = TimezoneFinder()
	tzchoice = tf.timezone_at(lng=b4, lat=b3) # returns 'Europe/Berlin'
	print('Timezone:					' + tzchoice)
	tz2 = pytz.timezone(tzchoice)
	#tz2 = pytz.timezone('Europe/Berlin')
	try:
		utt = tz2._utc_transition_times
	except:
		print()
		print('No timezone information available.')
		return
	
	#print("Test: ", datetime.datetime(2011,1,15,15,30), " = ", toTZ(datetime.datetime(2011,1,15,15,30)))
	#print("Test: ", datetime.datetime.utcnow(), " = ", toUTC(datetime.datetime.now()))
	#date.weekday() Monat 0 Sonntag 6

	#selected_year = int(input('Jahr: '))
	selected_year = a3
	zeitwert = getzeitwert(selected_year)

	if len(zeitwert) < 2:
		zeitwert = getzeitwert(2020)
		
		try:
			d0 = (zeitwert[0].weekday())
		except:
			print('\nStandard time is used throughout whole year.\n')
			return
			
		d1 = (zeitwert[1].weekday())
	
		wyear0 = int(zeitwert[0].strftime('%Y'))
		wyear1 = int(zeitwert[1].strftime('%Y'))
		wmonth0 = int(zeitwert[0].strftime('%m'))
		wmonth1 = int(zeitwert[1].strftime('%m'))
		wday0 = int(zeitwert[0].strftime('%d'))
		wday1 = int(zeitwert[1].strftime('%d'))
	
		days0 = monthrange(wyear0, wmonth0)[1]
		days1 = monthrange(wyear1, wmonth1)[1]
	
		#--------
	
		wdate = datetime.datetime(wyear0,wmonth0,1)
		wcount0 = do_wcount(wdate,wyear0,wmonth0,wday0,d0)
	
		#wcount0 ist der xte Wochentag im Referenzjahr 2020
		#print(wcount0)
	
		#finde den xten Wochentag auch im gewählten Jahr
		wdate = datetime.datetime(selected_year,wmonth0,1)
		wday0 = do_wday(wdate, wcount0, d0, days0, wmonth0)
		#print(wday0)
	
		# wenn es keine 5 gibt nimm 4
	
		if wday0 == 0:
			wcount0 -= 1
		
			wdate = datetime.datetime(selected_year,wmonth0,1)
			wday0 = do_wday(wdate, wcount0, d0, days0, wmonth0)
	
		springdate = zeitwert[0]
		springdate = springdate.replace(day=wday0)
		springdate = springdate.replace(year=selected_year)
		springdate = springdate.replace(month=wmonth0)
		
		wochentag_nr = springdate.isoweekday()
		wochentag_s = wochentage_kuerzel[wochentag_nr]
		#print(springdate)
		print('DST Start Date:			' + wochentag_s + ', ' + str(springdate))
		#print(wday0, wmonth0, selected_year)
	
		#--------
	
		wdate = datetime.datetime(wyear1,wmonth1,1)
		wcount1 = do_wcount(wdate,wyear1,wmonth1,wday1,d1)
	
		#wcount0 ist der xte Wochentag im Referenzjahr 2020
		#print(wcount0)
	
		#finde den xten Wochentag auch im gewählten Jahr
		wdate = datetime.datetime(selected_year,wmonth1,1)
		wday1 = do_wday(wdate, wcount1, d1, days1, wmonth1)
		#print(wday0)
	
		# wenn es keine 5 gibt nimm 4
	
		if wday1 == 0:
			wcount1 -= 1
		
			wdate = datetime.datetime(selected_year,wmonth1,1)
			wday1 = do_wday(wdate, wcount1, d1, days1, wmonth1)
	
		autumndate = zeitwert[1]
		autumndate = autumndate.replace(day=wday1)
		autumndate = autumndate.replace(year=selected_year)
		autumndate = autumndate.replace(month=wmonth1)
		
		wochentag_nr = autumndate.isoweekday()
		wochentag_a = wochentage_kuerzel[wochentag_nr]
	
		#print(autumndate)
		print('Std. Time Start Date:	' + wochentag_a + ', ' + str(autumndate))
		#print(wday1, wmonth1, selected_year)
		
		zeitwertcomp = autumndate
		zeitwertcomp = zeitwertcomp.replace(year=a3)
		
		try:
			zeitwertcomp = zeitwertcomp.replace(month=a2)
		except:
			zeitwertcomp = springdate
			zeitwertcomp = zeitwertcomp.replace(year=a3)
			zeitwertcomp = zeitwertcomp.replace(month=a2)
			
		zeitwertcomp = zeitwertcomp.replace(day=a1)
		
		smonth = str(a2)
		if len(smonth) == 1:
			smonth = '0' + smonth
			
		sday = str(a1)
		if len(sday) == 1:
			sday = '0' + sday
		
		print('Chosen Date:				' + wotag + ', ' + str(a3) + '-' + smonth + '-' + sday)
		print()
		if zeitwertcomp < springdate or zeitwertcomp >= autumndate:
			print('Chosen time is Standard Time.')
		if zeitwertcomp >= springdate and zeitwertcomp < autumndate:
			print('Chosen time is Daylight Saving Time.')
		print ('(Theoretical assumption. There is no valid switch time for the chosen date.)')
		print()
	
	else:
		wochentag_nr = zeitwert[0].isoweekday()
		wochentag_0 = wochentage_kuerzel[wochentag_nr]
		
		wochentag_nr = zeitwert[1].isoweekday()
		wochentag_1 = wochentage_kuerzel[wochentag_nr]
		
		print('DST Start Date:			' + wochentag_0 + ', ' + str(zeitwert[0]))
		print('Std. Time Start Date:	' + wochentag_1 + ', ' + str(zeitwert[1]))
		#print(type(zeitwert[0]))
		
		zeitwertcomp = zeitwert[0]
		zeitwertcomp = zeitwertcomp.replace(year=a3)
		zeitwertcomp = zeitwertcomp.replace(month=a2)
		zeitwertcomp = zeitwertcomp.replace(day=a1)
		
		smonth = str(a2)
		if len(smonth) == 1:
			smonth = '0' + smonth
			
		sday = str(a1)
		if len(sday) == 1:
			sday = '0' + sday
				
		print('Chosen Date:				' + wotag + ', ' + str(a3) + '-' + smonth + '-' + sday)
		print()
		if zeitwertcomp < zeitwert[0] or zeitwertcomp >= zeitwert[1]:
			print('Chosen time is Standard Time.')
		if zeitwertcomp >= zeitwert[0] and zeitwertcomp < zeitwert[1]:
			print('Chosen time is Daylight Saving Time.')
		print()
		
def mondstats():
	
	global mjahr, mmonat, mtag, mutc
	
	norise = 0
	noset= 0
	
	mjahr = str(a3)
	mmonat = str(a2)
	mtag = str(a1)
	utch = str(int(timezone))
	utcm = str(int((timezone - int(timezone)) * 60))

	if len(mmonat) == 1:
		mmonat = '0' + mmonat
	mtag = str(mtag)
	if len(mtag) == 1:
		mtag = '0' + mtag
	if float(utch) >= 0:
		if len(utch) == 1:
			utch = '0' + utch
		utch = '+' + utch
	else:
		if len(utch) == 2:
			utch = utch[1:]
			utch = '0' + utch
		utch= '-' + utch
	if len(utcm) == 1:
		utcm = '0' + utcm
	
	mutc = utch + ':' + utcm
	
	if len(mutc) == 7:
		mutc = mutc[1:]

	anforderung = "https://api.met.no/weatherapi/sunrise/2.0/.json?lat=b3&lon=b4&date=mjahr-mmonat-mtag&offset=mutc"
	
	#print(mjahr,mmonat,mtag,mutc)

	anforderung = anforderung.replace('mjahr',mjahr)
	anforderung = anforderung.replace('mmonat',mmonat)
	anforderung = anforderung.replace('mtag',mtag)
	anforderung = anforderung.replace('mutc',mutc)
	anforderung = anforderung.replace('b3',str(b3))
	anforderung = anforderung.replace('b4',str(b4))
	
	#print(anforderung)
	try:
		r = requests.get(anforderung)
	except:
		print ()
		print ('No moon data available.')
		return
		
	data = r.json() # data contains the parsed JSON string
	r.close()

	try:
		mrisetime = data['location']['time'][0]['moonrise']['time']
	except KeyError:
		mrisetime = '-'
		norise = 1

	if norise == 0:
		mrisetime = mrisetime[11:19]

	try:
		msettime = data['location']['time'][0]['moonset']['time']
	except KeyError:
		msettime = '-'
		noset = 1
	
	if noset == 0:
		msettime = msettime[11:19]
	
	try:
		mondphasenwert = float(data['location']['time'][0]['moonphase']['value'])
		#print(data['location']['time'][0]['moonphase'])
	except:
		print ()
		print ('No moon data available.')
		return
	
	#nullutc = '00:00'	
	#anforderung = anforderung.replace(mutc,nullutc)
	#r = requests.get(anforderung)	
	#data2 = r.json() # data contains the parsed JSON string
	#r.close()
	
	#mondphasenull = float(data2['location']['time'][0]['moonphase']['value'])

	mphase = mondphasenwert/100

	if mphase <= 0.125:
		mphasestatus = '🌒 Wax. Crescent'
		mpic = '01.JPG'
	
	if mphase > 0.125 and mphase <= 0.25:
		mphasestatus = '🌓 1. Quarter'
		mpic = '02.JPG'
	
	if mphase > 0.25 and mphase <= 0.375:
		mphasestatus = '🌔 Wax. ¾-Moon'
		mpic = '03.JPG'
	
	if mphase > 0.375 and mphase <= 0.5:
		mphasestatus = '🌕 Full Moon'
		mpic = '04.JPG'

	if mphase > 0.5 and mphase <= 0.625:
		mphasestatus = '🌖 Wan. ¾-Moon'
		mpic = '05.JPG'
	
	if mphase > 0.625 and mphase <= 0.75:
		mphasestatus = '🌗 3. Quarter'
		mpic = '06.JPG'
		
	if mphase > 0.75 and mphase <= 0.875:
		mphasestatus = '🌘 Wan. Crescent'
		mpic = '07.JPG'
	
	if mphase > 0.875 and mphase < 1:
		mphasestatus = '🌑 New Moon'
		mpic = '00.jpg'

	syn_moon_month = 29.530589 # gemittelte Lunation von Neumond zu Neumond
	#syn_moon_month = 29.45972222222222 # für 15.8.21
	
	mondalter = round(syn_moon_month * mphase,1)
	#mondalternull = round(syn_moon_month * mondphasenull/100,1)	
	beleuchtungsgrad = illumination(mphase)	

	naeneumond = round(syn_moon_month - mondalter)

	if mphase > 0.5:
		naevollmond = naeneumond + syn_moon_month*0.5
		naevollmond = round(naevollmond)
	else:
		naevollmond = syn_moon_month*0.5-mondalter
		naevollmond = round(naevollmond)
		
	#---------
	
	gewaehltes_datum = datetime.datetime(int(mjahr), int(mmonat), int(mtag))
			
	#---------
	
	vollmond_plus0 = gewaehltes_datum + datetime.timedelta(days=naevollmond)
	vollmond_min1 = gewaehltes_datum + datetime.timedelta(days=naevollmond-1)	
	vollmond_min2 = gewaehltes_datum + datetime.timedelta(days=naevollmond-2)
	vollmond_min3 = gewaehltes_datum + datetime.timedelta(days=naevollmond-3)	
	
	vjahr = vollmond_plus0.strftime("%Y")
	vmonat = vollmond_plus0.strftime("%m")
	vtag = vollmond_plus0.strftime("%d")
		
	phase_vollmond_plus0 = comparedates(vjahr, vmonat, vtag)
	
	vjahr = vollmond_min1.strftime("%Y")
	vmonat = vollmond_min1.strftime("%m")
	vtag = vollmond_min1.strftime("%d")
		
	phase_vollmond_min1 = comparedates(vjahr, vmonat, vtag)
	
	vjahr = vollmond_min2.strftime("%Y")
	vmonat = vollmond_min2.strftime("%m")
	vtag = vollmond_min2.strftime("%d")
		
	phase_vollmond_min2 = comparedates(vjahr, vmonat, vtag)
	
	vjahr = vollmond_min3.strftime("%Y")
	vmonat = vollmond_min3.strftime("%m")
	vtag = vollmond_min3.strftime("%d")
		
	phase_vollmond_min3 = comparedates(vjahr, vmonat, vtag)
		
	#liste = [phase_vollmond_min1, phase_vollmond_plus0, phase_vollmond_plus1]
	#print(liste)
	
	vg0 = 0.5 - phase_vollmond_min1
	if vg0 < 0:
		vg0 = 1
	vg1 = 0.5 - phase_vollmond_plus0
	if vg1 < 0:
		vg1 = 1		
	vg3 = 0.5 - phase_vollmond_min2
	if vg3 < 0:
		vg3 = 1
	vg4 = 0.5 - phase_vollmond_min3
	if vg4 < 0:
		vg4 = 1
		
	vgwert = min(vg0, vg1, vg3, vg4)
		
	if vgwert == vg0:
		naevollmond -= 1
		
	if vgwert == vg3:
		naevollmond -= 2
		
	if vgwert == vg4:
		naevollmond -= 3
		
	#---------
	
	neumond_plus0 = gewaehltes_datum + datetime.timedelta(days=naeneumond)
	neumond_min1 = gewaehltes_datum + datetime.timedelta(days=naeneumond-1)
	neumond_plus1 = gewaehltes_datum + datetime.timedelta(days=naeneumond+1)
	
	vjahr = neumond_plus0.strftime("%Y")
	vmonat = neumond_plus0.strftime("%m")
	vtag = neumond_plus0.strftime("%d")
		
	phase_neumond_plus0 = comparedates(vjahr, vmonat, vtag)
	
	vjahr = neumond_min1.strftime("%Y")
	vmonat = neumond_min1.strftime("%m")
	vtag = neumond_min1.strftime("%d")
		
	phase_neumond_min1 = comparedates(vjahr, vmonat, vtag)
	
	vjahr = neumond_plus1.strftime("%Y")
	vmonat = neumond_plus1.strftime("%m")
	vtag = neumond_plus1.strftime("%d")
		
	phase_neumond_plus1 = comparedates(vjahr, vmonat, vtag)
	
	#print(phase_neumond_min1, phase_neumond_plus0, phase_neumond_plus1)
	
	vg0 = 1 - phase_neumond_min1
	if vg0 > 0.5:
		vg0 = 1
	vg1 = 0.5 - phase_neumond_plus0
	if vg1 > 0.5:
		vg1 = 1
	vg2 = 0.5 - phase_neumond_plus1
	if vg2 > 0.5:
		vg2 = 1
	
	vgwert = min(vg0, vg1, vg2)
	
	if vgwert == vg0:
		naeneumond -= 1
		
	if vgwert == vg2:
		naeneumond += 1
		
	naevollmond_datum = gewaehltes_datum + datetime.timedelta(days=naevollmond)
	naeneumond_datum = gewaehltes_datum + datetime.timedelta(days=naeneumond)
	
	vjahr = naevollmond_datum.strftime("%Y")
	vmonat = naevollmond_datum.strftime("%m")
	vtag = naevollmond_datum.strftime("%d")
	
	aktuellesDatum = datetime.date(int(vjahr), int(vmonat), int(vtag))
	wochentag_nr = aktuellesDatum.isoweekday()
	vwotag = wochentage_kuerzel[wochentag_nr]
	
	njahr = naeneumond_datum.strftime("%Y")
	nmonat = naeneumond_datum.strftime("%m")
	ntag = naeneumond_datum.strftime("%d")
	
	aktuellesDatum = datetime.date(int(njahr), int(nmonat), int(ntag))
	wochentag_nr = aktuellesDatum.isoweekday()
	nwotag = wochentage_kuerzel[wochentag_nr]
		
	#---------

	print()
	print('Moon Data at 0h Local Time')
	print()
	
	#print('Datum:							' + mjahr + '-' + mmonat + '-' + mtag)
		
	print('Moonrise:				' + mrisetime)
	print('Moonset:				' + msettime)
	print('Moon age:				' + str(mondalter) + ' days')					
	print('Moon phase:			', end = '')
	print(mphasestatus)
	print('Illumination:			' + str(beleuchtungsgrad) + '%')
	print('Next full moon:		' + vwotag + ', ' + vjahr + '-' + vmonat + '-' + vtag)
	print('Next new moon:		' + nwotag + ', ' + njahr + '-' + nmonat + '-' + ntag)	
	print()
	
	from PIL import Image, ImageDraw, ImageFont

	width = 512
	height = 512

	img  = Image.new( mode = "RGB", size = (width, height), color = (255, 255, 255) )
	#img.show()
	draw = ImageDraw.Draw(img)
	fnt = ImageFont.truetype("FreeMono.txt", 20)
	d = ImageDraw.Draw(img)
	
	mphaseersatz = mphasestatus[2:]
	
	d.multiline_text((100,0), "Moon data at 0h local time", font = fnt, fill=(0, 0, 0))
	d.multiline_text((10,370), "     Moonrise:       " + mrisetime, font = fnt, fill=(0, 0, 0))
	d.multiline_text((10,390), "     Moonset:        " + msettime, font = fnt, fill=(0, 0, 0))
	d.multiline_text((10,410), "     Moon age:       " + str(mondalter) + ' Tage', font = fnt, fill=(0, 0, 0))
	d.multiline_text((10,430), "     Moon phase:     " + mphaseersatz, font = fnt, fill=(0, 0, 0))
	d.multiline_text((10,450), "     Illumination:   " + str(beleuchtungsgrad) + '%', font = fnt, fill=(0, 0, 0))
	d.multiline_text((10,470), "     Next full moon: " + vwotag + ', ' + vjahr + '-' + vmonat + '-' + vtag, font = fnt, fill=(0, 0, 0))
	d.multiline_text((10,490), "     Next new moon:  " + nwotag + ', ' + njahr + '-' + nmonat + '-' + ntag, font = fnt, fill=(0, 0, 0))
	
	img.save('.mond.png')	
	
	im1 = Image.open('.mond.png')
	im2 = Image.open(mpic)

	back_im = im1.copy()
	back_im.paste(im2, (96, 30))
	back_im.save('.mond.png')

# Folgeermittlung mit Phase und Synodischer Periodendauer als Basis:

# Beleuchtungsgrad
# Alter des Mondes
# Vorhersage nächster Vollmond

# Mond Azimut und Elevation geht nur aus API zu 0 Uhr
# Aus API geht Entfernung zu 0 Uhr in km
# Mond in Tierkreiszeichen geht nicht

def comparedates(vergleichsjahr,vergleichsmonat,vergleichstag):

	mjahr = vergleichsjahr
	mmonat = vergleichsmonat
	mtag = vergleichstag	
		
	anforderung = "https://api.met.no/weatherapi/sunrise/2.0/.json?lat=b3&lon=b4&date=mjahr-mmonat-mtag&offset=mutc"

	anforderung = anforderung.replace('mjahr',mjahr)
	anforderung = anforderung.replace('mmonat',mmonat)
	anforderung = anforderung.replace('mtag',mtag)
	anforderung = anforderung.replace('mutc',mutc)
	anforderung = anforderung.replace('b3',str(b3))
	anforderung = anforderung.replace('b4',str(b4))
	
	time.sleep(0.1)

	#r = requests.get(anforderung, timeout=120)
	r = requests.get(anforderung)
	data3 = r.json() # data contains the parsed JSON string
	#print(data3)
	r.close()
	
	mondphasenwert = float(data3['location']['time'][0]['moonphase']['value'])
	mphase = mondphasenwert/100
	#beleuchtungsgrad = illumination(mphase)
	return mphase

def illumination(phase):
    #constants
    hmoonA = float(pi/2)                            # area of unit circle/2
 
    # calculate percentage of moon illuminated
    if phase < 0.5:
            s = cos(phase * pi * 2)
            ellipse = s * 1 * pi                    # Ellipsenfäche = Produkt der beiden Halbachsen * Pi 
            hEllA = ellipse / 2                     # Ellipse Area/2 (major half axis * minor half axis * pi)/2
            illA = hmoonA + hEllA                   # illuminated area of moon = Half moon area plus half Ellipse
    else:
            s = -cos(phase * pi *2)                 # minor half axis of ellipse
            ellipse = s * 1 * pi
            hEllA = ellipse / 2                     # Ellipse Area/2 (major half axis * minor half axis)/2
            illA = hmoonA - hEllA                   # illuminated area = Half moon area minus half Ellipse Area
 
    illumperc =  100 - (illA / pi * 100)                    # illuminated area relative to full moon area (based on unit circle r=1)
    #illumperc =  (illA / pi * 100)     
    illumperc = round(illumperc,1)
        
    return illumperc

def mondheute():
	url = "https://www.der-mond.de/feature/luna.php?version=5&txue=Mond+aktuell&zeko=1&rand=1&trans=0&julia=0&daem=3&zefu=1&grmo=1&grmoueber=1&txph=1&txmoal=1&txmoph=1&txmobe=1&txmophti=1&txmost=1&txmostau=0&txze=1&zezo=timezone&zeso=0&format=1&schgr=11&schriftart=Standard&schriftschnitt=0&grafikausdehnung=0&grafikpx=300&faan=1&scro=0&scgr=0&scbl=0&hiro=240&higr=240&hibl=240&grsoho=0&grsohoueber=0&soep=0&txsost=0&txsostau=0&geolagr=b4&geolami=geolaminute&geolase=geolasekunde&geola=o&geobrgr=b3&geobrmi=geobrminute&geobrse=geobrsekunde&geobr=n&lang=de"
	
	#geolagr=b4
	#geolami=0
	#geolase=0
	#geola=w
	#geobrgr=b3
	#geobrmi=0
	#geobrse=0
	#geobr=s
	
	laenge = abs(b4)	
	breite = abs(b3)
		
	url = url.replace('b3',str(int(breite)))
	url = url.replace('b4',str(int(laenge)))
	
	inGradUhrzeit(laenge)
	
	url = url.replace('geolaminute',str(minuten))
	url = url.replace('geolasekunde',str(sekunden))
	
	inGradUhrzeit(breite)
	
	url = url.replace('geobrminute',str(minuten))
	url = url.replace('geobrsekunde',str(sekunden))
	
	if b4 < 0:
		url = url.replace('geola=o','geola=w')
		
	if b3 < 0:
		url = url.replace('geobr=n','geobr=s')
		
	url = url.replace('timezone',str(timezone))
	
	#print(url)
	
	try:
		img = Image.open(BytesIO(urllib.request.urlopen(url, timeout=10).read()))
	except:
		print('No moon data available.')
		
	try:
		img.show()
	except:
		pass
		
	url = url.replace('trans=0','trans=1')
	url = url.replace('format=1','format=0')
	
	try:
		img = Image.open(BytesIO(urllib.request.urlopen(url).read()))
	except:
		pass
		
	try:
		img.save('.mond.png')
	except:
		pass	

def inGradUhrzeit(gr):
    global grad, minuten, sekunden, dezimalgrad
    dezimalgrad = gr
    grad = int(dezimalgrad)  
    minuten = int( (dezimalgrad - grad) * 60 )
    sekunden = abs( ( minuten -  ( (dezimalgrad - grad) * 60 ) ) * 60 )
    sekunden = round(sekunden,2)

def button3_tapped(sender):
	s = dialogs.alert('App-Info "Sun Calculator"', '\nAuthor: Vincent Truppe\nVersion: November 2021\n\nUsed Algorithms:\n\nhttps://en.wikipedia.org/wiki/Sunrise_equation\n\nhttps://de.wikipedia.org/wiki/Sonnenstand', 'OK', hide_cancel_button=True)

def findMiddle(input_list):
    #gibt den Wert in der Mitte einer Liste zurück
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])

def wochentag():
	from datetime import date
	aktuellesDatum = date(a3, a2, a1)
	wochentag_nr = aktuellesDatum.isoweekday()
	#print(wochentag_nr)
	return(wochentage_kuerzel[wochentag_nr])

def aequinox():
	#Die Tagundnachtgleichen fallen auf den 19., 20. oder 21. März und den 22., 23. oder 24. September
	#be = Rektaszension. Die muss beim Grühlingspunkt 0 sein und beim Herbstpunkt 180
	
	global a1, a2, springday, autumnday
	a2bak = a2
	a1bak = a1
	
	a2 = 3
	
	a1 = 19
	sonne(12,0)
	spring1 = abs(be - 0)
	#print(be)
	a1 = 20
	sonne(12,0)
	spring2 = abs(be - 0)
	#print(be)
	a1 = 21
	sonne(12,0)
	spring3 = abs(be - 0)
	#print(be)
	spring0 = min(spring1, spring2, spring3)
	
	if spring0 == spring1:
		springday = 19
	if spring0 == spring2:
		springday = 20
	if spring0 == spring3:
		springday = 21
		
	a2 = 9
	
	a1 = 22
	sonne(12,0)
	autumn1 = abs(be - 180)
	#print(be)
	a1 = 23
	sonne(12,0)
	autumn2 = abs(be - 180)
	#print(be)
	a1 = 24
	sonne(12,0)
	autumn3 = abs(be - 180)
	#print(be)
	autumn0 = min(autumn1, autumn2, autumn3)
	
	if autumn0 == autumn1:
		autumnday = 22
	if autumn0 == autumn2:
		autumnday = 23
	if autumn0 == autumn3:
		autumnday = 24
		
	a2 = a2bak
	a1 = a1bak

def wenden():
	#Die Tagundnachtgleichen fallen auf den 19., 20. oder 21. März und den 22., 23. oder 24. September
	#be = Rektaszension. Die muss beim Frühlingspunkt 0 sein und beim Herbstpunkt 180
	
	global a1, a2, summerday, winterday
	a2bak = a2
	a1bak = a1
	
	a2 = 6
	
	a1 = 20
	sonne(12,0)
	summer1 = abs(be - 90)
	#print(be)
	a1 = 21
	sonne(12,0)
	summer2 = abs(be - 90)
	#print(be)
	a1 = 22
	sonne(12,0)
	summer3 = abs(be - 90)
	#print(be)
	summer0 = min(summer1, summer2, summer3)
	
	if summer0 == summer1:
		summerday = 20
	if summer0 == summer2:
		summerday = 21
	if summer0 == summer3:
		summerday = 22
		
	global Hoehenverlauf_Sommersonnenwende_y, Hoehenverlauf_Sommersonnenwende_x 
	
	h = 28;
	Hoehenverlauf_Sommersonnenwende_x = [0 for x in range(h)]
	Hoehenverlauf_Sommersonnenwende_y = [0 for x in range(h)]

	for num in range(0, 12):
		# er hört bei 11 auf
		sonne(num, 0)
		Hoehenverlauf_Sommersonnenwende_y[num] = bt
		Hoehenverlauf_Sommersonnenwende_x[num] = num
				
	sonne(11,30)
	Hoehenverlauf_Sommersonnenwende_x[12] = 11.5
	Hoehenverlauf_Sommersonnenwende_y[12] = bt
	
	sonne(12,0)
	Hoehenverlauf_Sommersonnenwende_x[13] = 12
	Hoehenverlauf_Sommersonnenwende_y[13] = bt
	
	sonne(12,30)
	Hoehenverlauf_Sommersonnenwende_x[14] = 12.5
	Hoehenverlauf_Sommersonnenwende_y[14] = bt
	
	sonne(13,0)
	Hoehenverlauf_Sommersonnenwende_x[15] = 13
	Hoehenverlauf_Sommersonnenwende_y[15] = bt
	
	
	sonne(13,30)
	Hoehenverlauf_Sommersonnenwende_x[16] = 13.5
	Hoehenverlauf_Sommersonnenwende_y[16] = bt
	
	sonne(14,0)
	Hoehenverlauf_Sommersonnenwende_x[17] = 14
	Hoehenverlauf_Sommersonnenwende_y[17] = bt
	
	sonne(14,30)
	Hoehenverlauf_Sommersonnenwende_x[18] = 14.5
	Hoehenverlauf_Sommersonnenwende_y[18] = bt
	
	count = 19
	for num in range(15, 24):
		sonne(num, 0)
		Hoehenverlauf_Sommersonnenwende_y[count] = bt
		Hoehenverlauf_Sommersonnenwende_x[count] = num
		count += 1	
	
	a2 = 12
	
	a1 = 20
	sonne(12,0)
	if be < 0:
		winter1 = 360-270+be
	else:
		winter1 = abs(be - 270)
	#print(be)
	#print(winter1)
	a1 = 21
	sonne(12,0)
	if be < 0:
		winter2 = 360-270+be
	else:
		winter2 = abs(be - 270)
	#print(be)
	#print(winter2)
	a1 = 22
	sonne(12,0)
	if be < 0:
		winter3 = 360-270+be
	else:
		winter3 = abs(be - 270)
	#print(be)
	#print(winter3)
	winter0 = min(winter1, winter2, winter3)
	
	if winter0 == winter1:
		winterday = 20
	if winter0 == winter2:
		winterday = 21
	if winter0 == winter3:
		winterday = 22
		
	global Hoehenverlauf_Wintersonnenwende_x, Hoehenverlauf_Wintersonnenwende_y
	
	h = 28;
	Hoehenverlauf_Wintersonnenwende_x = [0 for x in range(h)]
	Hoehenverlauf_Wintersonnenwende_y = [0 for x in range(h)]	
	
	for num in range(0, 12):
		# er hört bei 11 auf
		sonne(num, 0)
		Hoehenverlauf_Wintersonnenwende_y[num] = bt
		Hoehenverlauf_Wintersonnenwende_x[num] = num
				
	sonne(11,30)
	Hoehenverlauf_Wintersonnenwende_x[12] = 11.5
	Hoehenverlauf_Wintersonnenwende_y[12] = bt
	
	sonne(12,0)
	Hoehenverlauf_Wintersonnenwende_x[13] = 12
	Hoehenverlauf_Wintersonnenwende_y[13] = bt
	
	sonne(12,30)
	Hoehenverlauf_Wintersonnenwende_x[14] = 12.5
	Hoehenverlauf_Wintersonnenwende_y[14] = bt
	
	sonne(13,0)
	Hoehenverlauf_Wintersonnenwende_x[15] = 13
	Hoehenverlauf_Wintersonnenwende_y[15] = bt
	
	
	sonne(13,30)
	Hoehenverlauf_Wintersonnenwende_x[16] = 13.5
	Hoehenverlauf_Wintersonnenwende_y[16] = bt
	
	sonne(14,0)
	Hoehenverlauf_Wintersonnenwende_x[17] = 14
	Hoehenverlauf_Wintersonnenwende_y[17] = bt
	
	sonne(14,30)
	Hoehenverlauf_Wintersonnenwende_x[18] = 14.5
	Hoehenverlauf_Wintersonnenwende_y[18] = bt
	
	count = 19
	for num in range(15, 24):
		sonne(num, 0)
		Hoehenverlauf_Wintersonnenwende_y[count] = bt
		Hoehenverlauf_Wintersonnenwende_x[count] = num
		count += 1			
	
	a1 = a1bak
	a2 = a2bak

def slider_action(sender):
	global shh,smm
	# Get the root view:
	v = sender.superview
	# Get the sliders:
	r = v['slider1'].value
	g = v['slider2'].value
	shh = int(r*23)
	smm = int(g*59)
	sonne(shh,smm)
	# Create the new color from the slider values:
	shour = str(int(r*23))
	smin = str(int(g*59))
	
	if int(shour) < 10:
		shour = '0' + shour
		
	if int(smin) < 10:
		smin = '0' + smin		
	
	v['label1'].text = shour + ':' + smin
	v['label6'].text = str(bq)
	v['label7'].text = str(bt)
	v['label10'].text = szeit
	v['label11'].text = s_ort
	
	#t = arange(0, 24, 1)
	t = Hoehenverlauf_x
	zerox = arange(0, 24, 1)
	zeroy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	]
	#s = Hoehenverlauf
	s = Hoehenverlauf_y
	plot(t, s, label = str(a1) + '.' + str(a2) + '.' + str(a3))
	mmc = smm/60
	hmc = shh + mmc
	#print(hmc,mmc,bt)	
	plot(hmc, bt, 'ro')
	plot(zerox, zeroy, 'k')
		
	b = BytesIO()
	savefig(b)
	img = ui.Image.from_data(b.getvalue())
	
	v['imageview2'].image=img
	
	clf() # Reset Plot Object - sonst schreibt ervallebKurven in dasselbe Objekt	
	

def copy_action(sender):
	std = str(shh)
	min = str(smm)
	if shh < 10:
		std = '0' + std
	if smm < 10:
		min = '0' + min
	clipboard.set(s_ort + ', ' + szeit + ', ' + std + ':' + min + ', ' + 'Direction: ' + sender.superview['label6'].text + ', ' + 'Height: ' + sender.superview['label7'].text)
	dialogs.hud_alert('Copied.')

def shuffle_action(sender):
	v = sender.superview
	s1 = v['slider1']
	s2 = v['slider2']
	s1.value = random()
	s2.value = random()
	slider_action(s1)

def savereport():
	s = dialogs.alert('Save report?', 'ODF+PDF are stored in Pythonista program folder.', 'ODT', 'ODT+PDF', 'Cancel', hide_cancel_button=True)
	
	if s == 1:
		# save the document
		textdoc.save(fname)
		dialogs.hud_alert('Sunreport.odt saved.')
		
	if s == 2:
		textdoc.save(fname)
		dialogs.hud_alert('Sunreport.odt saved.')
		dialogs.hud_alert('Generating PDF via Webservice..')
		createpdf()
	
		if pdfok == 0:
			dialogs.hud_alert('Sunreport.pdf saved.')
		else:
			dialogs.hud_alert('Could not create PDF. Check API-Key and online connection.', 'error', 3.0)

def savelocation():
	
	if flag != 1 and flag != 0:
		dialogs.hud_alert('Location already exists.', 'error', 1.8)
		return
		
	s = dialogs.alert('Save location?', 'Location will be stored in location list.', 'Yes', 'No', hide_cancel_button=True)
	if s == 1:
		# Ort speichern
		coords = str(b3) + ', ' + str(b4)
		if flag == 1:
			ort = gtitle
			ortcancel = 0
		else:
			ort = ''
			ortcancel = 0
			
		while True:
			try:
				ort = dialogs.input_alert('Name current location', 'Please enter name', ort, 'OK', hide_cancel_button=False)
			except KeyboardInterrupt:
				ortcancel = 1
				break
				
			if ort not in items and ort != '':
				break
			else:
				dialogs.hud_alert('Location already exists.', 'error', 1.8)
		
		if ortcancel == 0:			
			saveselection(ort,coords,str(tzoriginal),zone)
			items.append(ort)
			dialogs.hud_alert(ort + ' saved.')

def gettz(coords):
	tf = TimezoneFinder()
	mydict = {40:  None, 41: None}
	coords = coords.translate(mydict)
	try:
		coords = coords.split(",")
	except TypeError:
		pass
	try:
		b3 = float(coords[0])
	except ValueError:
		b3 = 0
		pass
	try:
		b4 = float(coords[1])
	except ValueError:
		b4 = 0
		pass	
	
	latitude, longitude = b3, b4
	tz = tf.timezone_at(lng=longitude, lat=latitude) # returns 'Europe/Berlin'
	return(tz)

def selectz():
	opt = dialogs.list_dialog('Please choose timezone', tznames)
	if opt is None:
		return
	else:
		#print('Auswahl: 	' + opt['title'] + '		' + opt['utc'])
		return(opt['tzn'], opt['utc'])

def newplace():
	form_list_of_sections = []

	sectionA_dicts = []
	sectionA_dicts.append(dict(type = 'text', title = 'Location title	',
	key = 'title', placeholder = 'Berlin, Brandenburg Gate'))

	sectionA_dicts.append(dict(type = 'text', title = 'Coordinates		',
	key = 'coords', placeholder = '52.516272, 13.377722')) 

	#sectionA_dicts.append(dict(type = 'text', title = 'UTC-Offset			',
	#key = 'utc', placeholder='1')) 

	#sectionA_dicts.append(dict(type = 'text', title = 'Zeitzone			',
	#key = 'tz', placeholder='Europe/Berlin'))
	
	sectionA_dicts.append(dict(type = 'check', title = 'Set timezone automatically', key = 'auto_tz', value = True))  

	form_list_of_sections.append(('Please enter data using required format', sectionA_dicts, 'Coordinate format: (Latitude, Longitude) as decimal number.\nNegative sign for western longitude, resp. southern latitude.'))

	diag = dialogs.form_dialog(title = 'Create new location', sections=form_list_of_sections)
	#print(diag['title'])
	#print(diag['coords'])
	#print(diag['utc'])
	#print(diag['tz'])
	return(diag)

def saveselection(ort,coords,utc,tz):
	try:
		add_json(ort, coords, utc, tz)
	except TypeError:
		pass			
	
	myobject = openjson()
	#print(myobject)

	length = len(myobject['locations'])
	#print(length)

	items = []

	for i in range (0, length):
		items.append(myobject['locations'][i]['title'])
	
	data_source.items = items
	view['textfield1'].text = ''
	view.name = 'Standort wählen' + ' (' + str(len(items)) + ')'

def editplace():
	form_list_of_sections = []

	sectionA_dicts = []
	sectionA_dicts.append(dict(type = 'text', title = 'Location title	',
	key = 'title', value = myobject['locations'][row]['title']))

	sectionA_dicts.append(dict(type = 'text', title = 'Coordinates		',
	key = 'coords', value = myobject['locations'][row]['coords'])) 

	#sectionA_dicts.append(dict(type = 'text', title = 'UTC-Offset			',
	#key = 'utc', value = myobject['locations'][row]['utc'])) 

	#sectionA_dicts.append(dict(type = 'text', title = 'Zeitzone			',
	#key = 'tz', value = myobject['locations'][row]['tz']))
	
	sectionA_dicts.append(dict(type = 'switch', title = 'Change timezone',
key = 'change_tz', value = False))

	sectionA_dicts.append(dict(type = 'check', title = 'Set timezone automatically', key = 'auto_tz', value = True))

	form_list_of_sections.append(('Please enter data using required format', sectionA_dicts, 'Current standard timezone:\n' + myobject['locations'][row]['tz'] + ', UTC: ' + myobject['locations'][row]['utc']))

	diag = dialogs.form_dialog(title = 'Change location', sections=form_list_of_sections)
	#print(diag['title'])
	#print(diag['coords'])
	#print(diag['utc'])
	#print(diag['tz'])
	return(diag)

def add_json(a,b,c,d):	
	new_data = {"title": a,
	"coords": b,
	"utc": c,
	"tz": d
	}
	
	if a not in items:
	
		filename = 'foo.json'
	
		with open(filename,'r+') as file:
			# First we load existing data into a dict.
			file_data = json.load(file)
			# Join new_data with file_data inside emp_details
			file_data["locations"].append(new_data)
			# Sets file's current position at offset.
			file.seek(0)
			# sort and convert back to json.		
			data_list = file_data['locations']
			file_data['locations'] = sorted(data_list, key=lambda k: k['title'])		
			json.dump(file_data, file, indent = 4, sort_keys = False)
			file.close()
			
	else:
		dialogs.hud_alert('Ort existiert schon.', 'error', 1.8)

def change_json(a,b,c,d):	
	new_data = {"title": a,
	"coords": b,
	"utc": c,
	"tz": d
	}
	
	filename = 'foo.json'
	
	with open(filename,'r+') as file:
		# First we load existing data into a dict.
		file_data = json.load(file)
		# Join new_data with file_data inside emp_details
		file_data["locations"].append(new_data)
		# Sets file's current position at offset.
		file.seek(0)
		# sort and convert back to json.		
		data_list = file_data['locations']
		file_data['locations'] = sorted(data_list, key=lambda k: k['title'])		
		json.dump(file_data, file, indent = 4, sort_keys = False)
		file.close()
				
def del_json(number, filename='foo.json'):
	#Zähler beginnt immer bei 0!
	with open(filename) as data_file:
		data = json.load(data_file)

	del data['locations'][number]

	with open('foo.json', 'w') as data_file:
		data = json.dump(data, data_file, indent = 4)

def showjson():
	with open("foo.json") as jsonFile:
		jsonObject = json.load(jsonFile)
		jsonFile.close()

	#a = jsonObject['a']
	#b = jsonObject['b']
	#c = jsonObject['c']

	#print(a)
	#print(b)
	#print(c)
	
	#print(jsonObject['article'][1]['id'])
	#print(jsonObject['article'][1])
	
	#print(jsonObject['article'][2]['id'])
	#print(jsonObject['article'][2])

	with open('foo.json','r+') as file:
		# First we load existing data into a dict.
		file_data = json.load(file)
		length = len(file_data['locations'])
		print(length)
		file.close()
	
	for i in range (0, length):
		print (file_data['locations'][i])

def openjson():
	with open("foo.json") as jsonFile:
		jsonObject = json.load(jsonFile)
		jsonFile.close()
		return(jsonObject)

def item_edited(sender):
    #global items
    global myobject
    global filter_is_set
    
    filter_is_set = 1
    
    if view['textfield1'].text == '':
    	filter_is_set = 0
    
    if filter_is_set == 0:
    	removed = [x for x in items if x not in sender.items]
    else:
    	removed = [x for x in filter if x not in sender.items]
    	
    #removed ist eine Liste mit dem einen der removed ist
    
    lenitems = len(items)
    #print(lenitems)
    itemcount = 0
    
    for i in range (0, lenitems):
        if removed[0] == items[i]:
            itemcount = i
    		
    #print(itemcount)
    #print(len(removed)) ist 70
    
    if len(removed) == 1 and removed[0] != ' My Location' and removed[0] != ' Choose new location':
        item = removed[0]
        #print('Item \'%s\' removed' % item)
        items.remove(item)
        data_source.items = items
        view['textfield1'].text = ''
        view.name = 'Choose location' + ' (' + str(len(items)) + ')'
        	
    #else:
        #print('Something\'s wrong, more than 1 removed item? With swipe to delete? Hmm ...')

        del_json(itemcount)
        myobject = openjson()
					
    else:
        dialogs.hud_alert('Location is protected from deletion.', 'error', 1.8)
        data_source.items = items
        view['textfield1'].text = ''
        view.name = 'Choose location' + ' (' + str(len(items)) + ')'

def item_selected(sender):
	global row, old_time
	row = sender.selected_row
	
	if row != -1:
		tapchoice = 1
		
	if filter_is_set == 1:
		rowtitle = sender.items[row]
		#print(rowtitle)
	
		for i in range(0, len(items)):
			if myobject['locations'][i]['title'] == rowtitle:
				row = int(i)
	
	button2_tapped(None)

def button4_tapped(sender):
	global printmoonstats, sathoehe, vsettings
	#vsettings = ui.load_view('reportsettings')

	try:
		vsettings = ui.load_view('reportsettings')
	except FileNotFoundError:
		vsettings = ui.load_view('reportsettings.json')		
					
	vsettings['sathoehe'].delegate = ReportDelegate()
	
	if 'sathoehe' not in globals():
		sathoehe = 250.0
	
	if sathoehe != 250.0:
		vsettings['sathoehe'].text = str(sathoehe)
	else:
		vsettings['sathoehe'].text = '250.0'	
	
	vsettings.present('sheet')
	
	if printmoonstats == 1:
		vsettings['switch1'].value = False
	
	#print(printmoonstats)

def closevsettings(sender):
	sender.superview.close()

def button2_tapped(sender):
	global tapchoice	
	if 'row' in globals():	
		tapchoice = 1
		view.close()
	else:
		dialogs.hud_alert('Please tap a location first.', 'error', 1.8)
	
def button1_tapped(sender):
	global items, myobject, data_source
	
	if 'row' in globals():
		
		if myobject['locations'][row]['title'] != ' My Location' and myobject['locations'][row]['title'] != ' Choose new location':
	
			diag = editplace()
			
			if diag is not None:
				
				mydict = {40:  None, 41: None}
				coords = diag['coords'].translate(mydict)
				try:
					coords = coords.split(",")
				except TypeError:
					dialogs.hud_alert('Coordinates invalid.', 'error', 1.8)
					return
				try:
					b3 = float(coords[0])
				except ValueError:
					dialogs.hud_alert('Coordinates invalid.', 'error', 1.8)
					return
				
				try:
					b4 = float(coords[1])
				except:
					dialogs.hud_alert('Coordinates invalid.', 'error', 1.8)
					return
					
				if b3 > 90 or b3 < -90 or b4 > 180 or b4 < -180:
					dialogs.hud_alert('Coordinates invalid.', 'error', 1.8)
					return
				
				if diag['title'] == '':
					dialogs.hud_alert('Location title is missing.', 'error', 1.8)
					
				else:				
				
					if diag['auto_tz'] is False and diag['change_tz'] is True:
						tzchoice = selectz()
				
					if diag['auto_tz'] is True and diag['change_tz'] is True:
						tmptz = gettz(diag['coords'])
						tzindex = 0
						comp = ''
					
						for i in range (0, len(tznames)):
							comp = (tznames[i]['tzn'])
							if comp == tmptz:
								tzindex = i
					
						tmputc = tznames[tzindex]['utc']
						
						tzchoice = ['','']
						tzchoice[0] = tmptz
						tzchoice[1] = tmputc
																		
					if diag['change_tz'] is False:						
						tzchoice = ['','']
						tzchoice[0] = myobject['locations'][row]['tz']
						tzchoice[1] = myobject['locations'][row]['utc']
		
					try:
						del_json(row)
						change_json(diag['title'], diag['coords'], tzchoice[1], tzchoice[0])
					except TypeError:
						tzchoice = ['','']
						tzchoice[0] = myobject['locations'][row]['tz']
						tzchoice[1] = myobject['locations'][row]['utc']
						change_json(diag['title'], diag['coords'], tzchoice[1], tzchoice[0])
						pass
	
					myobject = openjson()
					#print(myobject)

					length = len(myobject['locations'])
					#print(length)

					items = []

					for i in range (0, length):
						items.append(myobject['locations'][i]['title'])
	
					data_source.items = items
					view['textfield1'].text = ''
					view.name = 'Choose location' + ' (' + str(len(items)) + ')'
					
		else:
			dialogs.hud_alert('Location not editable.', 'error', 1.8)
			
	else:
		dialogs.hud_alert('Please tap a location first.', 'error', 1.8)
			
def button_tapped(sender):
	global items, myobject, data_source
	diag = newplace()

	if diag is not None:
		
		mydict = {40:  None, 41: None}
		coords = diag['coords'].translate(mydict)
		try:
			coords = coords.split(",")
		except TypeError:
			dialogs.hud_alert('Coordinates invalid.', 'error', 1.8)
			return
		try:
			b3 = float(coords[0])
		except ValueError:
			dialogs.hud_alert('Coordinates invalid.', 'error', 1.8)
			return
				
		try:
			b4 = float(coords[1])
		except:
			dialogs.hud_alert('Coordinates invalid.', 'error', 1.8)
			return
			
		if b3 > 90 or b3 < -90 or b4 > 180 or b4 < -180:
			dialogs.hud_alert('Coordinates invalid.', 'error', 1.8)
			return
	
		if diag['title'] == '':
			dialogs.hud_alert('Location title is missing.', 'error', 1.8)
		
		else:
			if diag is not None:
				
				if diag['auto_tz'] is False:
					tzchoice = selectz()
					
					try:
						add_json(diag['title'], diag['coords'], tzchoice[1], tzchoice[0])
					except TypeError:
						pass
				
				else:
					tmptz = gettz(diag['coords'])
					tzindex = 0
					comp = ''
					
					for i in range (0, len(tznames)):
						comp = (tznames[i]['tzn'])
						if comp == tmptz:
							tzindex = i
					
					tmputc = tznames[tzindex]['utc']
					
					try:
						add_json(diag['title'], diag['coords'], tmputc, tmptz)
					except TypeError:
						pass			
	
			myobject = openjson()
			#print(myobject)

			length = len(myobject['locations'])
			#print(length)

			items = []

			for i in range (0, length):
				items.append(myobject['locations'][i]['title'])
	
			data_source.items = items
			view['textfield1'].text = ''
			view.name = 'Choose location' + ' (' + str(len(items)) + ')'

def showlist():
	global myobject, items, data_source, view
	myobject = openjson()
	#print(myobject)

	length = len(myobject['locations'])
	#print(length)

	items = []

	for i in range (0, length):
		items.append(myobject['locations'][i]['title'])

	data_source = ui.ListDataSource(items)
	data_source.delete_enabled = True
	data_source.edit_action = item_edited
	data_source.action = item_selected

	#view = ui.load_view()
	
	try:
		view = ui.load_view()
	except FileNotFoundError:
		view = ui.load_view('suncalc.json')
	
	view['tableview1'].data_source = data_source
	view['tableview1'].delegate = data_source
	view['textfield1'].delegate = MyTextFieldDelegate()
	view.name = 'Choose location' + ' (' + str(len(items)) + ')'
	view.present('fullscreen')

# Hauptprogramm
#showlist()

def createpdf():
	global pdfok
	pdfok = 0
	apikey = ''
	#import time
	import cloudmersive_convert_api_client
	from cloudmersive_convert_api_client.rest import ApiException

	#from pprint import pprint
	# Configure API key authorization: Apikey
	
	keyfile = open('cloudmersive-apikey.txt')
	apikey = keyfile.read(36)
	keyfile.close()
	
	configuration = cloudmersive_convert_api_client.Configuration()
	configuration.api_key['Apikey'] = apikey
	# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
	# configuration.api_key_prefix['Apikey'] = 'Bearer'
	# create an instance of the API class
	
	api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
	input_file = 'Sunreport.odt' # file | Input file to perform the operation on.
	try:
	# Convert Office Open Document ODT to PDF
		api_response = api_instance.convert_document_odt_to_pdf(input_file)
	except:
		pdfok = 1
		return
		#pprint(api_response)
	file = open("Sunreport.pdf", "wb")
	file.write(api_response)
	file.close()
	#except ApiException as e:
		#print("Exception when calling ConvertDocumentApi->convert_document_odt_to_pdf: %s\n" % e)	

def printtabp(aktp):
	global tabp
	
	#newtext = "Testing\tTabstops"
	
	tabp = P(stylename=tabparagraphstyle)
	teletype.addTextToElement(tabp, aktp)
	textdoc.text.addElement(tabp)
	#tabp.addElement(LineBreak())
	
def mancoords():
	global b3, b4, reset
	b3 = 1000
	b4 = 1000
	no = 1
	
	while no == 1:
		if noclip == 1:
			try:
				a4 = dialogs.input_alert('No location in clipboard', 'Please enter coords manually (latitude, longitude)', '', 'OK', hide_cancel_button=False)
			except KeyboardInterrupt:
				console.clear()
				reset = 1
				return		
				#print('Programmabbruch.')
				#exit()
		else:
			try:
				a4 = dialogs.input_alert('You are offline', 'Please enter coords manually (latitude, longitude)', '', 'OK', hide_cancel_button=False)
			except KeyboardInterrupt:
				console.clear()
				reset = 1
				return		
				#print('Programmabbruch.')
				#exit()
					
		mydict = {40:  None, 41: None}
		a4 = a4.translate(mydict)
		try:
			coords = a4.split(",")
		except TypeError:
			pass
		try:
			no = 0
			b4 = float(coords[1])
		except:
			no = 1
			pass
		try:
			b3 = float(coords[0])
		except:
			no = 1
			pass
		
		if b3 > 90 or b3 < -90 or b4 > 180 or b4 < -180:
			no = 1	
		
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

def is_dst(dt=None, timezone="UTC"):
	delta = datetime.timedelta(hours = 12)
	dt = dt + delta
	if dt is None:
		dt = datetime.utcnow()
	timezone = pytz.timezone(timezone)
	timezone_aware_date = timezone.localize(dt, is_dst=None)
	return timezone_aware_date.tzinfo._dst.seconds != 0

def currenttz():
	if time.daylight:
		return 1
	else:
		return 0

def get_location():
	global latitude, longitude, loc
	location.start_updates()
	time.sleep(1)
	loc = location.get_location()
	location.stop_updates()
	try:
		latitude = loc['latitude']
	except TypeError:
		print('No GPS available.')
		exit()
	longitude = loc['longitude']

def date_to_jd(year,month,day):
    # Convert a date to Julian Day.
    # Algorithm from 'Practical Astronomy with your Calculator or Spreadsheet', 
    # 4th ed., Duffet-Smith and Zwart, 2011.
    # This function extracted from https://gist.github.com/jiffyclub/1294443
    if month == 1 or month == 2:
        yearp = year - 1
        monthp = month + 12
    else:
        yearp = year
        monthp = month
    # this checks where we are in relation to October 15, 1582, the beginning
    # of the Gregorian calendar.
    if ((year < 1582) or
        (year == 1582 and month < 10) or
        (year == 1582 and month == 10 and day < 15)):
        # before start of Gregorian calendar
        B = 0
    else:
        # after start of Gregorian calendar
        A = math.trunc(yearp / 100.)
        B = 2 - A + math.trunc(A / 4.)

    if yearp < 0:
        C = math.trunc((365.25 * yearp) - 0.75)
    else:
        C = math.trunc(365.25 * yearp)
    D = math.trunc(30.6001 * (monthp + 1))
    jd = B + C + D + day + 1720994.5
    return jd    
# end of date_to_jd    

def modulo(z,n):
    m=z-int(int(z)/int(n))*int(n)
    return m
      
def sonne(hh,mm):
    global bq, bt, be
    
    mm = mm/60
    b1 = hh+mm
    rd = pi/180

    b2 = (b1+a4)/24
    b5 = int(a3/100)
    b6 = 2-b5+int(b5/4)
    b7 = int(365.25*(a3+4716))+int(30.6001*(a2+1))+a1+b2+b6-1524.5
    b8 = b7-2451545 # n = Julianische Tageszahl
    b9 = 280.46+0.9856474*b8 # Mittlere ekliptikale Laenge L
    g0 = 357.528+0.9856003*b8 # Mittlere Anomalie g
    bb = b9+1.915*sin(g0*rd)+0.01997*sin(2*g0*rd) # Ekliptikale Laenge A der Sonne - mutmasslich richtige Formel
    bc = 23.439-0.0000004*b8 # Schiefe der Ekliptik e
    bd = cos((bb*rd))

    if bd < 0:
        be = ((atan(cos(bc*rd)*tan(bb*rd))) + 4*atan(1))/rd # rektaszension a

    else:
        be = (atan(cos(bc*rd)*tan(bb*rd)))/rd # rektaszension a

    x = sin((bc*rd)*sin(bb*rd))
    x = atan(x/sqrt(1-x*x))

    bf = x/rd                    # deklidation d

    bg = int(365.25*(a3+4716))+int(30.6001*(a2+1))+a1+(0/24)+b6-1524.5   # julianische tageszahl jd0
    # print "bg",bg
    bh = (bg-2451545)/36525  # t0 in julianischen Jahrhunderten
    # print "bh",bh
    z = 6.697376+2400.05134*bh+1.002738*(b1+a4) # mittlere Sternzeit 0g zum Zeitpunkt T
    n = 24
    bi = modulo(z,n) # # mittlere Sternzeit 0g zum Zeitpunkt T bereinigt um Vielfache von 24

    bj = bi*15+b4
    bk = bj-be       # Stundenwinkel r der Sonne fuer den Ort des Beobachters

    x = atan(sin(bk*rd)/(cos(bk*rd)*sin(b3*rd)-tan(bf*rd)*cos(b3*rd))) # azimut

    if bd < 0:
        bl=(x/rd)+180
    else:
        bl=x/rd

    x=(cos(bk*rd)*sin(b3*rd)-tan(bf*rd)*cos(b3*rd))/rd # vermutlich trick fuer glatten werteverlauf des azimut ueber quadranten

    if x < 0:
        bm = bl+180
    else:
        bm = bl

    if bm > 360:
        bn = bm-360
    else:
        bn = bm

    if bn < 0:
        bo = bn+360
    else:
        bo = bn

    if bd > 0:
        bp = bo+180
    else:
        bp = bo

    if bp > 360:
        bq = bp-360
    else:
        bq = bp         # azimut
    
    x = cos(bf*rd)*cos(bk*rd)*cos(b3*rd)+sin(bf*rd)*sin(b3*rd) # hoehe h vorbereitung

    x = atan(x/sqrt(1-x*x))  # hoehe h mit arcussinus

    br = x/rd                # hoehe in grad
    bs = 1.02/(tan(br*rd+(10.3/(br*rd+5.11)))) # mittlere Refraktion (Lichtbrechung Atmosphaere einbeziehen)

    bt = ((br*rd)+(bs/60))/rd # Refraktionsbereinigte Hoehe
    bt = br # option ohne refraktion

def zeiten(ort):
	pi=3.14159265359

	global ah, am, mh, mm, uh, um, ahx, mhx, uhx, norise, pxyz, szeit, s_ort, sonnea, sonnem, sonneu, mittagkorrektur, bq, bt, wotag
	
	norise = 0
	mittagkorrektur = 0

	latitude_radians = math.radians(latitude_deg)
	longitude__radians = math.radians(longitude_deg)

	jd2000 = 2451545 #the julian date for Jan 1 2000 at noon

	import datetime

	currentDT = datetime.datetime.now()
	current_year = a3
	current_month = a2
	current_day = a1

	jd_now = date_to_jd(current_year,current_month,current_day)
	#print("jd",jd_now)

	n = jd_now - jd2000 + 0.0008

	jstar = n - longitude_deg/360

	M_deg = (357.5291 + 0.98560028 * jstar)%360
	M = M_deg * pi/180

	C = 1.9148 * math.sin(M) + 0.0200 * math.sin(2*M) + 0.0003 * math.sin(3*M)

	lamda_deg = math.fmod(M_deg + C + 180 + 102.9372,360)

	lamda = lamda_deg * pi/180
	#print("ld",lamda)

	Jtransit = 2451545.5 + jstar + 0.0053 * math.sin(M) - 0.0069 * math.sin(2*lamda)

	earth_tilt_deg = 23.44
	earth_tilt_rad = math.radians(earth_tilt_deg)

	sin_delta = math.sin(lamda) * math.sin(earth_tilt_rad)
	angle_delta = math.asin(sin_delta)

	sun_disc_deg =  -0.83
	sun_disc_rad = math.radians(sun_disc_deg)

	cos_omega = (math.sin(sun_disc_rad) - math.sin(latitude_radians) * math.sin(angle_delta))/(math.cos(latitude_radians) * math.cos(angle_delta))
	
	try:
		omega_radians = math.acos(cos_omega)
	except ValueError:
		omega_degrees = 0
		norise = 1
		pass
		
	if norise == 0:
		omega_degrees = math.degrees(omega_radians)
		
#Output section
	wotag = wochentag()
	print('Chosen date:		' + wotag + ', ' + str(int(a3)) + '-' + str(int(a2)) + '-' + str(int(a1)))
	aktp = 'Chosen date:\t' + wotag + ', ' + str(int(a3)) + '-' + str(int(a2)) + '-' + str(int(a1))
	szeit = str(int(a3)) + '-' + str(int(a2)) + '-' + str(int(a1))
	printtabp(aktp)
		
	if flag == 0:		
		print('Chosen location: Current location')
		aktp = 'Chosen location:\tCurrent location'
		s_ort = 'Current location'
		printtabp(aktp)
		
	if flag == 1:
		print('Chosen location:	' + ort)
		aktp = 'Chosen location:\t' + ort[0:68]
		s_ort = ort[0:68]
		printtabp(aktp)		
		
	if flag == 2:
		ort = myobject['locations'][row]['title']
		print('Chosen location:	' + ort)
		aktp = 'Chosen location:\t' + ort[0:68]
		s_ort = ort[0:68]
		printtabp(aktp)
	
	print("------------------------------")
	aktp = "------------------------------"
	printtabp(aktp)
	#("%Y-%m-%d %H:%M")
	
	print("Latitude		=	" + str(latitude_deg))
	aktp = "Latitude\t= " + '\t' + str(latitude_deg)
	printtabp(aktp)
	
	print("Longitude		=	" + str(longitude_deg))
	aktp = "Longitude\t= " + '\t' + str(longitude_deg)
	printtabp(aktp)
	print("UTC  			=	" + str(timezone))
	aktp = "UTC\t\t= " + '\t' + str(timezone)
	printtabp(aktp)
	
	print("------------------------------")
	aktp = "------------------------------"
	printtabp(aktp)

	Jrise = Jtransit - omega_degrees/360
	numdays = Jrise - jd2000
	numdays =  numdays + 0.5 #offset because Julian dates start at noon
	numdays =  numdays + timezone/24 #offset for time zone
	#print(numdays)
	sunrise = datetime.datetime(2000, 1, 1) + datetime.timedelta(numdays)
	Jset = Jtransit + omega_degrees/360
	numdays = Jset - jd2000
	numdays =  numdays + 0.5 #offset because Julian dates start at noon
	numdays =  numdays + timezone/24 #offset for time zone
	#print(numdays)
	sunset = datetime.datetime(2000, 1, 1) + datetime.timedelta(numdays)
	
	midday = sunrise + (sunset - sunrise)/2
	tdauer = sunset - sunrise
	
	if norise == 1:
		sunset = datetime.datetime(2000,1,1)
		midday = datetime.datetime(2000,1,1)
		sunrise = datetime.datetime(2000,1,1)
	
	b = tdauer.seconds
	bstunden = int(b/3600)
	bsekunden = int((b - bstunden*3600)/60)
	print("Day length	=" + '	' + str(bstunden).zfill(2) + ':' + str(bsekunden).zfill(2))
	aktp = "Day length	=" + '\t' + str(bstunden).zfill(2) + ':' + str(bsekunden).zfill(2)
	printtabp(aktp)
	
	print("------------------------------")
	aktp = "------------------------------"
	printtabp(aktp)
	
	uh = sunset.strftime("%H")
	uh = float(uh)
	um = sunset.strftime("%M")
	um = float(um)
	
	ah = sunrise.strftime("%H")
	ah = float(ah)
	am = sunrise.strftime("%M")
	am = float(am)
	
	mh = midday.strftime("%H")
	mh = float(mh)
	mm = midday.strftime("%M")
	mm = float(mm)
	
	if norise == 0:
		
		print('Rise (Hour, Direction, Height)')
		aktp = 'Rise (Hour, Direction, Height)'
		printtabp(aktp)
		sonne(ah,am)
		sonnea = bq
		x = str(bq)
		y = str(bt)
		print(sunrise.strftime("%H:%M") + '		' + x[0:5] + '		' + y[0:5])
		aktp = sunrise.strftime("%H:%M") + '\t\t' + x[0:5] + '\t' + y[0:5]
		printtabp(aktp)
		ahx = round(ah + am/60,2)
		ah = bq
		am = bt
		print("------------------------------")
		aktp = "------------------------------"
		printtabp(aktp)
		print('Noon (Hour, Direction, Height)')
		aktp = 'Noon (Hour, Direction, Height)'
		printtabp(aktp)
		sonne(mh,mm)
		
		newhour = mh
		
		sonnem = bq
		sonnebtm = bt
		mittagkorrektur = 0
		
		sonne(mh,mm-1)
		sonnemmin1 = bq
		sonnebtmin1 = bt
		
		sonne(mh,mm+1)
		sonnemplus1 = bq
		sonnebtplus1 = bt
		
		if sonnem > 270 or sonnem < 10:
			
			if sonnem < 10:
				sonnem += 360
			if sonnemmin1 < 10:
				sonnemmin1 += 360
			if sonnemplus1 < 10:
				sonnemmplus1 += 360
						
			diff0 = abs(360-sonnem)
			diff1 = abs(360-sonnemmin1)
			diff2 = abs(360-sonnemplus1)
			
			diffres = min(diff0, diff1, diff2)
			
			if diffres == diff1:
				bq = sonnemmin1
				bt = sonnebtmin1
				mittagkorrektur = 1
			if diffres == diff2:
				bq = sonnemplus1
				bt = sonnebtplus1
				mittagkorrektur = 2
			if diffres == diff0:
				bq = sonnem
				bt = sonnebtm
				mittagkorrektur = 0		
			
		else:
			
			diff0 = abs(180-sonnem)
			diff1 = abs(180-sonnemmin1)
			diff2 = abs(180-sonnemplus1)
			
			diffres = min(diff0, diff1, diff2)
			
			if diffres == diff1:
				bq = sonnemmin1
				bt = sonnebtmin1
				mittagkorrektur = 1
			if diffres == diff2:
				bq = sonnemplus1
				bt = sonnebtplus1
				mittagkorrektur = 2
			if diffres == diff0:
				bq = sonnem
				bt = sonnebtm
				mittagkorrektur = 0
				
		if bq >= 360:
			bq -= 360
			
		sonnem = bq
	
		x = str(bq)		
		y = str(bt)
			
		if mittagkorrektur == 1:
			newmin = int(mm-1)
			if newmin == -1:
				newmin = 59
				newhour = int(mh-1)
				midday = midday.replace(hour = newhour)				
			midday = midday.replace(minute = newmin)
			mm = newmin
						
		if mittagkorrektur == 2:
			newmin = int(mm+1)
			if newmin == 60:
				newmin = 0
				newhour = int(mh+1)
				midday = midday.replace(hour = newhour)				
			midday = midday.replace(minute = newmin)
			mm = newmin
			
		print(midday.strftime("%H:%M") + '		' + x[0:5] + '		' + y[0:5])
		aktp = midday.strftime("%H:%M") + '\t\t' + x[0:5] + '\t' + y[0:5]
		printtabp(aktp)		
		mhx = round(newhour + (mm)/60,2)					
		
		mh = bq
		mm = bt
		
		print("------------------------------")
		aktp = "------------------------------"
		printtabp(aktp)
		print('Sunset (Hour, Direction, Height)')
		aktp = 'Sunset (Hour, Direction, Height)'
		printtabp(aktp)
		sonne(uh,um)
		sonneu = bq
		x = str(bq)
		y = str(bt)
		print(sunset.strftime("%H:%M") + '		' + x[0:5] + '		' + y[0:5])
		aktp = sunset.strftime("%H:%M") + '\t\t' + x[0:5] + '\t' + y[0:5]
		printtabp(aktp)
		uhx = round(uh + um/60,2)
		uh = bq
		um = bt
#		print("------------------------------")
	else:
		ahx = 0
		mhx = 0
		uhx = 0

def drucken():
	global Matrix, Hoehenverlauf_x, Hoehenverlauf_y, pflag
	
	Hoehenverlauf_x = []
	Hoehenverlauf_y = []
	
	w, h = 3, 28;
	Matrix = [[0 for x in range(w)] for y in range(h)]
	
	Hoehenverlauf_x = [0 for x in range(28)]
	Hoehenverlauf_y = [0 for x in range(28)]

	for num in range(0, 24):
   		sonne(num, 0)
   		Matrix[num][0] = num
   		Matrix[num][1] = bq
   		Matrix[num][2] = bt

	Matrix[25][0] = ahx
	Matrix[25][1] = ah
	Matrix[25][2] = am

	Matrix[26][0] = mhx
	Matrix[26][1] = mh
	Matrix[26][2] = mm	
		
	Matrix[27][0] = uhx
	Matrix[27][1] = uh
	Matrix[27][2] = um
	
	Matrix.sort()
	
	for num in range(0, 28):	
		Hoehenverlauf_x[num] = Matrix[num][0]
		Hoehenverlauf_y[num] = Matrix[num][2]
	
	if norise == 1:
		pflag = 0
		for i in range(1,28):
			if Matrix[i][2] > 0:
				pflag = 1
			else:
				pflag = 0
		
		if pflag == 0:
			print('Sun does not rise.')
			aktp = 'Sun does not rise.'
			printtabp(aktp)
		else:
			print('Sun does not set.')
			aktp = 'Sun does not set.'
			printtabp(aktp)
	
	print("------------------------------")	
	aktp = "------------------------------"
	printtabp(aktp)
	print('Sun Table (Hours, Direction, Height)')
	aktp = 'Sun Table (Hours, Direction, Height)'
	printtabp(aktp)
	#print()
	#aktp = ''
	#printtabp(aktp)
	
	for num in range(1, 28):
		Matrix[num][0] = str(Matrix[num][0])
		Matrix[num][1] = str(Matrix[num][1])
		Matrix[num][1] = Matrix[num][1][0:5]
		Matrix[num][2] = str(Matrix[num][2])
		Matrix[num][2] = Matrix[num][2][0:5]
		
#	Matrix.sort()
# Ich kann hier kein String Array sortieren obwohl man String-Listen grundsätzlich sortieren kann: TypeError: '<' not supported between instances of 'str' and 'int'
# Ich vermute dass [num] int ist und [0] - [2] String. Ich brauche [num] aber als Zahlenindex für die For-Schleife. Ein so gemischtes Array kann ich nicht sortieren.
		
	ahx2 = (ahx - int(ahx))*60
	ahx2 = round(ahx2,0)
	mhx2 = (mhx - int(mhx))*60
	mhx2 = round(mhx2,0)
	uhx2 = (uhx - int(uhx))*60
	uhx2 = round(uhx2,0)
		
	for num in range(1, 28):
		if Matrix[num][0] == str(ahx):
			if ahx2 < 10 and ahx > 9:
				Matrix[num][0] = str(int(ahx)) + ':' + '0' + str(int(ahx2)) + ' R'
			if ahx2 < 10 and ahx < 10:
				Matrix[num][0] = '0' + str(int(ahx)) + ':' + '0' + str(int(ahx2)) + ' R'
			if ahx2 > 9 and ahx > 9:
				Matrix[num][0] = str(int(ahx)) + ':' + str(int(ahx2)) + ' R'
			if ahx2 > 9 and ahx < 10:
				Matrix[num][0] = '0' + str(int(ahx)) + ':' + str(int(ahx2)) + ' R'
				
		if Matrix[num][0] == str(mhx):
			Matrix[num][0] = str(int(mhx)) + ':' + str(int(mhx2)) + ' N'
			if mhx2 < 10:
				Matrix[num][0] = str(int(mhx)) + ':' + '0' + str(int(mhx2)) + ' N'
				
		if Matrix[num][0] == str(uhx):
			Matrix[num][0] = str(int(uhx)) + ':' + str(int(uhx2)) + ' S'
			if uhx2 < 10:
				Matrix[num][0] = str(int(uhx)) + ':' + '0' + str(int(uhx2)) + ' S'
				
		for num in range(1, 28):
			if len(Matrix[num][0]) == 1:
				Matrix[num][0] = '0' + Matrix[num][0]
				
			for num in range(1, 28):
				if len(Matrix[num][0]) == 2:
					Matrix[num][0] = Matrix[num][0] + ':00' + '	'
				
# Länge des größen Eintrags.
	m = max(len(i) for i in Matrix)
	m = m+5

# Listen formatiert ausgeben

	Matrix.pop(0)
	
# er rutscht auf, also 3x dasselbe Element löschen um sortierte Null-Einträge zu löschen
	
	if norise == 1:
		del Matrix[0]
		del Matrix[0]
		del Matrix[0]
		
#	for l in (Matrix):
#    		print ("	".join("{0:{1}}".format(i, m) for i in l))

	m = len(Matrix)

	for l in range(0,m):
		print(Matrix[l][0] + '	' + Matrix[l][1] + '		' + Matrix[l][2])
		aktp = Matrix[l][0] + '\t' + Matrix[l][1] + '\t' + Matrix[l][2]
		printtabp(aktp)

def datepick():
	dateerror = 1
	
	while dateerror == 1:
		pick = dialogs.date_dialog()
	
		try:
			dateerror = 0
			py = pick.strftime("%Y")
		except AttributeError:
			dialogs.hud_alert('Please confirm date with "Done".', 'error', 1.8)
			dateerror = 1
			pass		
		
	pm = pick.strftime("%m")
	pd = pick.strftime("%d")
	return py,pm,pd

###
		
def bestimmeStunden(tag, monat):
	global stunden, mcount
	monate =[ 0,31,28,31,30,31,30,31,31,30,31,30,31 ]
	
	# Jan 31 für Eintrag 0
	
	mcount = 0
	
	for i in range (0, monat):
		mcount = mcount + monate[i]
		
	mcount += tag-1
	
	if mcount >= 79:
		mcount -= 79
		
	else:
		mcount += 286
	
	#print(mcount)
	#print(monat)
	stunden = mcount * 24
	#print(stunden)
	
def bestimmeAlpha(stunden):
	global alpha
	
	b = 107226 * stunden
	alpha = (360 * b) / 939951138.7693618
	alpha = round(alpha,2) * (-1)

def bestimmeSonnenplatz(stunden):
	global radius, linie
	
	strecke = stunden * 107226
	streckenanteil = strecke / 939951138.769361
	
	#Fall a <= 21.6. und >= 21.3.
	if stunden <= 2208:
		radius = streckenanteil * gesamtmass + viertelmass
		linie = 'a'
		
	if stunden > 2208 and stunden <= 6600:
		radius = streckenanteil * gesamtmass - viertelmass
		linie = 'b'
		
	if stunden > 6600:
		radius = streckenanteil * gesamtmass - 3 * viertelmass
		linie = 'a'
		
	radius = round(radius,2)


	#Auf Linie a links unten ansetzen, 23,5 Grad einstellen mit Radius 0,429242342880689 cm und Kreis zeichnen 

def erzeugeBilder():
	
	global tage
	
	from PIL import Image, ImageDraw, ImageFont
	import numpy as np
	
	xbak = 0
	ybak = 0
	
	img = Image.new('RGB', (1024, 1824), color = (0, 0, 0))
	img.save('erdesonne.png')
	
	im = Image.open("erdesonne.png")
	pixels = im.load()

	p = pi/180

	for i in np.arange(1,360,0.5):
		pixels[512+400*cos(i*p), 512+400*sin(i*p)] = (255, 255, 255)	
		
	for i in np.arange(1,360,0.5):
		pixels[512+100*cos(i*p), 512+100*sin(i*p)] = (255, 255, 0)
		
	startx = 512+cos(alpha*p)*400
	starty = 512+sin(alpha*p)*400
		
	for i in np.arange(1,360,0.5):
		pixels[startx+25*cos(i*p), starty+25*sin(i*p)] = (127, 255, 212)	
		
	draw = ImageDraw.Draw(im)
	
	# Marker 1 Kreis
	
	x1 = 512+400
	y1 = 512
	x2 = x1+25
	y2 = y1
	draw.line((x1,y1,x2,y2), fill = (255,255,255))
	
	# Marker 2 Kreis
	
	x1 = 468
	y1 = 1000
	x2 = 556
	y2 = y1
	draw.line((x1,y1,x2,y2), fill = (255,255,255))
	
	x1 = 556
	y1 = 1000
	x2 = x1+20*cos(150*p)
	y2 = y1+20*sin(150*p)
	draw.line((x1,y1,x2,y2), fill = (255,255,255))
	
	x1 = 556
	y1 = 1000
	x2 = x1+20*cos(210*p)
	y2 = y1+20*sin(210*p)
	draw.line((x1,y1,x2,y2), fill = (255,255,255))
	
	# draw multiline text
	fnt = ImageFont.truetype("FreeMono.txt", 40)
	d = ImageDraw.Draw(im)
	
	date = str(tag) + '.' + str(monat) + '.'
	
	d.multiline_text((startx-10,starty+40), date, font = fnt, fill=(255, 255, 255))
	
	# Marker Linie a
		
	# Erde Linie a
	
	if stunden <= 2208:
			
		tage = mcount
		winkelt = (23.5 / 90) * tage	
		
	if stunden > 2208 and stunden <= 4464:
		
		tage = mcount - 186
		winkelt = (23.5 / 90) * tage * (-1)
		
	if stunden > 4464 and stunden <= 6600:
			
		tage = mcount - 186
		winkelt = (23.5 / 90) * tage * (-1)
		
	if stunden > 6600:
			
		tage = 365 - mcount
		winkelt = (23.5 / 90) * tage * (-1)
	
	startx = 50+cos(336.5*p)*viertelmass
	starty = 1650+sin(336.5*p)*viertelmass
	
	for i in np.arange(1,360,0.5):
		pixels[startx+100*cos(i*p), starty+100*sin(i*p)] = (127, 255, 212)	
		
	x1 = startx
	y1 = starty-100
	x2 = startx
	y2 = starty+100
	draw.line((x1,y1,x2,y2), fill = (255,0,0))	
		
	x1 = startx+cos((270 - winkelt)*p)*100	
	y1 = starty+sin((270 - winkelt)*p)*100	
	x2 = startx+cos((90 - winkelt)*p)*100
	y2 = starty+sin((90 - winkelt)*p)*100
	draw.line((x1,y1,x2,y2), fill = (255,255,0))
			
	x1 = startx+cos(-latitude_deg*p)*100
	y1 = starty+sin(-latitude_deg*p)*100	
	x2 = startx+cos((90 - winkelt)*p)*(y1-starty)
	y2 = y1		
	draw.line((x1,y1,x2,y2), fill = (255,255,0))		
		
	x1 = startx
	y1 = starty
	x2 = startx+viertelmass*cos(-winkelt*p)
	y2 = starty+viertelmass*sin(-winkelt*p)
	draw.line((x1,y1,x2,y2), fill = (255,255,0))
		
	# Sonne Linie a
	
	startx = x2
	starty = y2
		
	for i in np.arange(1,360,0.5):
		pixels[startx+3*cos(i*p), starty+3*sin(i*p)] = (255, 0, 0)	
	
	for i in np.arange(1,360,0.5):
		pixels[startx+25*cos(i*p), starty+25*sin(i*p)] = (255, 255, 0)	
		
	d.multiline_text((startx-50,starty+60), date, font = fnt, fill=(255, 255, 255))
		
	heightstring = ''
	for i in range (0, 30):
		heightstring += '█'
		
	d.multiline_text((10, 1124), heightstring, font = fnt, fill=(255, 255, 255))
	
	d.multiline_text((10, 1124), "Geo-centric sun pos. sidewise:", font = fnt, fill=(255, 0, 0))	
	
	heightstring = ''
	for i in range (0, 22):
		heightstring += '█'
		
	d.multiline_text((10,10), heightstring, font = fnt, fill=(255, 255, 255))
	
	d.multiline_text((10,10), "Earth path from above:", font = fnt, fill=(255, 0, 0))
			
	im.save("erdesonne.png")
	im.show()		
	
###	

def mainprogram():
	global fname, textdoc, gtitle, coords, tapchoice, flag, a1, a2, a3, a4, b3, b4, timezone, latitude_deg, longitude_deg, tabparagraphstyle, tzoriginal, zone, noclip, aktuellesdatum, reset, strfloat, filter_is_set, old_time
	
	aktuellesdatum = 0
	reset = 0
	filter_is_set = 0
	old_time = 0
	
	# Programmtitel

	console.clear()

	my_file = Path(".sat.png")
	if my_file.is_file():
		os.remove('.sat.png')

	my_file = Path(".map.png")
	if my_file.is_file():
		os.remove('.map.png')
		
	my_file = Path(".mond.png")
	if my_file.is_file():
		os.remove('.mond.png')

	#------------------------- Starte Report Anlage

	# fname is the path for the output file
	fname = r'Sunreport.odt';
	#fname='D:\Document\PersonalInfoRemixBook\examples\ch17\odfpy_gen_example.odt'

	# instantiate an ODF text document (odt)
	textdoc = OpenDocumentText()

	# We must describe the dimensions of the page
	#pagelayout = odfstyle.PageLayout(name="MyLayout")
	#textdoc.automaticstyles.addElement(pagelayout)
	#pagelayout.addElement(odfstyle.PageLayoutProperties(margin="0cm", #pagewidth="29.7cm", pageheight="21cm", printorientation="portrait"))

	s = textdoc.styles

	#textsammlung = "The following sections illustrate various possibilities in ODF Text"

	StandardStyle = Style(name="Standard", family="paragraph")
	##StandardStyle.addAttribute('class','text')
	s.addElement(StandardStyle)

	TextBodyStyle = Style(name="Text_20_body",family="paragraph", parentstylename='Standard', displayname="Text body")
	##TextBodyStyle.addAttribute('class','text')
	TextBodyStyle.addElement(ParagraphProperties(margintop="0in", marginbottom="0.0835in"))
	s.addElement(TextBodyStyle)

	# Creating a tabstop at 1cm
	tabstops_style = TabStops()
	tabstop_style = TabStop(position="1cm")
	tabstops_style.addElement(tabstop_style)
	tabstoppar = ParagraphProperties()
	tabstoppar.addElement(tabstops_style)
	tabparagraphstyle = Style(name="Question", family="paragraph")
	tabparagraphstyle.addElement(tabstoppar)
	s.addElement(tabparagraphstyle)

	frstyle = Style(name = 'frstyle', parentstylename="Graphics", family="graphic")
	frstyle.addElement(GraphicProperties(verticalpos="from-top", verticalrel="page", horizontalpos="from-left", horizontalrel="page", wrap = "parallel"))
	textdoc.automaticstyles.addElement(frstyle)

	h=H(outlinelevel=3, text='Sun Calculator')
	textdoc.text.addElement(h)

	#-------------------------

	flag = 0
	tapchoice = 0
	gtitle = ''
	showlist()
	view.wait_modal()

	if tapchoice != 0:
	
		coords = myobject['locations'][row]['coords'].split(",")
	
		if coords[0] == '2000' and coords[1] == '2000':
			get_location()
			b3 = latitude
			b4 = longitude
			flag = 0
		if coords[0] == '1000' and coords[1] == '1000':
			flag = 1
		if coords[0] != '2000' and coords[0] != '2000' and coords[0] != '1000' and coords[1] != '1000' :
			loc = coords
			a4 = float(myobject['locations'][row]['utc'])
			a4 = (-1) * a4
			timezone = a4*(-1)
			flag = 2

	else:
		exit()

	print()
	print('Sun Calculator')
	print()

	if flag == 0:
		dialogs.hud_alert('Current location set.')

	if flag == 1:
	
		clipboard.set('')
		k=connect()
	
		if k == True:	
			url = 'http://maps.google.com'
			webview = ui.WebView(title='Open Street Maps')
			webview.load_url(url)
			webview.present('fullscreen')
			#webview.close()
			dialogs.hud_alert('1. Long-tap place - 2. Press Share  - 3. Close', 'success', 5)
			webview.wait_modal()
			
			clip = clipboard.get()
		
			if clip.find("@") > 0:
				ltitle = clip
				num = clip.find("@")
				clip = clip[num+1:num+21]
		
				coords = clip.split(",")
				b3 = float(coords[0])
				b4 = float(coords[1])
			
				ltitle = ltitle[34:len(ltitle)]
				num = ltitle.find("/")
				ltitle = ltitle[0:num]
				ltitle = ltitle.replace('+',' ')
			
				ltitle = urllib.parse.unquote(ltitle)
			
			else:
				noclip = 1
				ltitle = 'Manual Input'
				mancoords()
				if reset == 1:
					return
			
		else:
			noclip = 0
			ltitle = 'Manual Input'
			mancoords()
			if reset == 1:
				return
		
		gtitle = ltitle					
																		
	if flag == 2:
		b3 = float(loc[0])
		b4 = float(loc[1])
	
		dialogs.hud_alert(myobject['locations'][row]['title'] + ' set.')

	latitude_deg = b3
	longitude_deg = b4

	if flag != 2:
	
		tf = TimezoneFinder()
		zone = tf.timezone_at(lng=b4, lat=b3) # returns 'Europe/Berlin'

		utctype = 'Calculated '

	else:
		utctype = 'Saved '	
	
	#utc = str(a4*(-1))
	current = 0

	s = dialogs.alert('Choose date', 'Please choose date', 'Current date', 'Choose custom date', hide_cancel_button=True)
	if s == 1:
		
		import datetime
		
		currentDT = datetime.datetime.now()
		current = 1
		a3 = currentDT.year
		a2 = currentDT.month
		a1 = currentDT.day
		dialogs.hud_alert('Current date is used.')
		
		aktuellesdatum = 1
		
	if s == 2:
		pdate = datepick()
		a1 = int(pdate[2])
		a2 = int(pdate[1])
		a3 = int(pdate[0])

	if flag == 2:
		tz = myobject['locations'][row]['tz']
		
		now = arrow.get(a3,a2,a1)
		now = now.shift(hours=+12)
		now = now.to(tz)
 
		now_dst = now.dst() 
		strnow = str(now_dst)
		strnow = strnow[0:1]
		strfloat = float(strnow)
		a4 = a4 + strfloat*(-1)
		timezone = timezone + strfloat
	
		if strfloat == 1:
			dialogs.hud_alert('Summertime is used.')
		else:
			dialogs.hud_alert('Standard time is used.')

	if flag == 0:
	
		for i in range (0, len(tznames)):
			comp = (tznames[i]['tzn'])
			if comp == zone:
				tzindex = i
			
		a4 = float(tznames[tzindex]['utc'])*(-1)
		timezone = a4*(-1)
		tzoriginal = timezone
						
		if current == 0:	
			zone = time.tzname[0]

			from datetime import datetime

			if (is_dst(datetime(a3, a2, a1), timezone = zone)) == True:
				a4 = a4 + 1*(-1)
				timezone = timezone + 1
				dialogs.hud_alert('Summertime is used.')
				strfloat = 1
			else:
				dialogs.hud_alert('Standard time is used.')
				strfloat = 0
		
		else:	
			now = arrow.get(a3,a2,a1)
			now = now.shift(hours=+12)
			now = now.to(zone) 
 
			now_dst = now.dst() 
			strnow = str(now_dst)
			strnow = strnow[0:1]
			strfloat = float(strnow)
			a4 = a4 + strfloat*(-1)
			timezone = timezone + strfloat
	
			if strfloat == 1:
				dialogs.hud_alert('Summertime is used.')
			else:
				dialogs.hud_alert('Standard time is used.')

	if flag == 1:
	
		zonematch = 0
	
		for i in range (0, len(tznames)):
			comp = (tznames[i]['tzn'])
			if comp == zone:
				zonematch = 1
				tzindex = i
			
				a4 = float(tznames[tzindex]['utc'])*(-1)			
				timezone = a4*(-1)
				tzoriginal = timezone
			
		if zonematch == 0:
				
			for i in range (0, len(tzalias)):
				comp = (tzalias[i]['title'])
				if comp == zone:
					zonematch = 1
					tzindex = i
				
					a4 = float(tzalias[tzindex]['utc'])*(-1)
					timezone = a4*(-1)
					tzoriginal = timezone
	
		# wenn auch hier keine UTC gefunden wurde gibt es keine Absicherung.
	
		now = arrow.get(a3,a2,a1)
		now = now.shift(hours=+12)
		now = now.to(zone) 
 
		now_dst = now.dst() 
		strnow = str(now_dst)
		strnow = strnow[0:1]
		strfloat = float(strnow)
		a4 = a4 + strfloat*(-1)
		timezone = timezone + strfloat
	
		if strfloat == 1:
			dialogs.hud_alert('Summertime is used.')
		else:
			dialogs.hud_alert('Standard time is used.')

	zeiten(gtitle)
	drucken()
	
	mondstats()

	#t = arange(0, 24, 1)
	t = Hoehenverlauf_x
	zerox = arange(0, 24, 1)
	zeroy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	]
	#s = Hoehenverlauf
	s = Hoehenverlauf_y
	plot(t, s, label = str(a1) + '.' + str(a2) + '.' + str(a3))
	legend(loc='upper right')	
	
	plot(zerox, zeroy, 'k')
	
	#turningpointresults()
	wenden()
	
	t = Hoehenverlauf_Sommersonnenwende_x
	s = Hoehenverlauf_Sommersonnenwende_y
	plot(t, s, label = str(summerday) + '.6.' + str(a3))
	legend(loc='upper right')
	
	t = Hoehenverlauf_Wintersonnenwende_x
	s = Hoehenverlauf_Wintersonnenwende_y
	plot(t, s, label = str(winterday) + '.12.' + str(a3))
	legend(loc='upper right')
	
	xlabel('Hours')
	ylabel('Height in Deg')
	title('Sun Diagram')
	#grid(color='r', linestyle='-', linewidth=2)
	grid(True)
	show()
	savefig('.plot.png')
	
	clf() # Reset Plot Object - sonst schreibt ervallebKurven in dasselbe Objekt
	
	#t = arange(0, 24, 1)
	#s = Hoehenverlauf
	#plot(t, s, label = str(a1) + '.' + str(a2) + '.' + str(a3))
	#hh = 11
	#mm = 29
	#mmc = mm/60
	#hmc = hh + mmc
	#sonne(hh,mm)
	#plot(hmc, bt, 'ro')	
	#savefig('.plot2.png')
	
	#clf() # Reset Plot Object - sonst schreibt ervallebKurven in dasselbe Objekt
	
	#if aktuellesdatum == 1:
		#mondheute()
	#mondheute()

###
		
	global viertelmass, gesamtmass, halbmass, tag, monat

	gesamtmass = 1880 # pixel
	halbmass = gesamtmass / 2
	viertelmass = gesamtmass / 4

	#469,9755693846805 = Line halbe Umrundungsdistanz Verkleinerung 1:1.000.000

	tag = a1
	monat = a2
	
	bestimmeStunden(tag,monat)
	#print('Stunden: ' + str(stunden))

	bestimmeAlpha(stunden)
	#print('Alpha: ' + str(alpha))

	bestimmeSonnenplatz(stunden)
	#print('Radius: ' + str(radius))
	#print('Linie: ' + linie)

	erzeugeBilder()

###	
	
	if 'sathoehe' not in globals():
		global sathoehe
		sathoehe = 250
										
	w, h = 1024, 1024 # Size of the image (points)
	map_w, map_h = sathoehe, sathoehe # Size of the map (meters)
	img = location.render_map_snapshot(b3, b4, width=map_w, height=map_h, img_width=w, img_height=h, map_type='satellite')

	try:
		jpeg_data = img.to_jpeg()
		with open('.sat.png', 'wb') as f:
			f.write(jpeg_data)
	except AttributeError:
		pass

	nosat = 0

	my_file = Path(".sat.png")
	if my_file.is_file():
		pass
	else:
		nosat = 1
		print()
		print()
		print("Satellite Service does not react.")
		print()
		
	if nosat == 0:
		
		from PIL import Image, ImageDraw, ImageFont
		
		resize('.sat.png', 2048)
			
		img = Image.open(".sat.png")
		draw = ImageDraw.Draw(img)
		fnt = ImageFont.truetype("FreeMono.txt", 40)
		d = ImageDraw.Draw(img)
	
		heightstring = ''
		lensathoehe = len(str(sathoehe))
		for i in range (0, lensathoehe + 13):
			heightstring += '█'
		
		d.multiline_text((10,10), heightstring, font = fnt, fill=(255, 255, 255))
		
		d.multiline_text((10,10), 'Map size: ' + str(sathoehe) + ' m²', font = fnt, fill=(255, 0, 0))
	
		img.save(".sat.png")		
		img.show()

		if b3 >= 0:
			if b3 < 67:
				mapwidth = 10000000
				mapheight = 10000000
			elif b3 < 81:
				mapwidth = 1500000
				mapheight = 1500000
			else:
				mapwidth = 100000
				mapheight = 100000
		else:
			if b3 > -67:
				mapwidth = 10000000
				mapheight = 10000000
			elif b3 > -81:
				mapwidth = 1500000
				mapheight = 1500000
			else:
				mapwidth = 100000
				mapheight = 100000

		img=location.render_map_snapshot(b3, b4, width=mapwidth, height=mapheight, map_type='standard', img_width=512, img_height=512, img_scale=0)

		#img.show()
	
		try:
			jpeg_data = img.to_jpeg()
			with open('.temp.jpg', 'wb') as f:
				f.write(jpeg_data)
		except:
			pass
	
		#photos.create_image_asset('.temp.jpg')

		#im = Image.open("grid.png")
	
		#from PIL import Image, ImageDraw, ImageFont
		
		resize('.temp.jpg', 1024)
	
		im = Image.open(".temp.jpg")
		pixels = im.load()

		for i in range(412, 612): 
			pixels[i, 512] = (255, 150, 0)
		for i in range(412, 612): 
			pixels[i, 511] = (255, 150, 0)
		for i in range(412, 612): 
			pixels[i, 513] = (255, 150, 0)
    
    
		for i in range(412, 612): 
			pixels[512, i] = (255, 150, 0)
		for i in range(412, 612): 
			pixels[512, i] = (255, 150, 0)
		for i in range(412, 612): 
			pixels[513, i] = (255, 150, 0)
		#pixels[768, 768] = (255, 0, 0)

		p = pi/180

		for i in np.arange(1,360,0.5):
			pixels[512+50*cos(i*p), 512+50*sin(i*p)] = (255, 150, 0)	
		
		# draw multiline text
		draw = ImageDraw.Draw(im)
		fnt = ImageFont.truetype("FreeMono.txt", 20)
		d = ImageDraw.Draw(im)
    
		heightstring = ''
		for i in range (0, 40):
			heightstring += '█'
		
		d.multiline_text((10,10), heightstring, font = fnt, fill=(255, 255, 255))
	
		d.multiline_text((10,10), "Overview picture: Sun path and position.", font = fnt, fill=(255, 0, 0))

		if norise == 0:

			x1 = 512
			y1 = 512
			x2 = 512+100*cos(sonnea*p - p*90)
			y2 = 512+100*sin(sonnea*p - p*90)
			draw.line((x1,y1,x2,y2), fill = (255,0,0))
	
			x1 = 512
			y1 = 512
			x2 = 512+100*cos(sonnem*p - p*90)
			y2 = 512+100*sin(sonnem*p - p*90)
			draw.line((x1,y1,x2,y2), fill = (255,0,0))
	
			x1 = 512
			y1 = 512
			x2 = 512+100*cos(sonneu*p - p*90)
			y2 = 512+100*sin(sonneu*p - p*90)
			draw.line((x1,y1,x2,y2), fill = (255,0,0))
		
			if sonnem < 270 and sonnem > 5:
	
				for i in np.arange(sonnea-90,sonneu-90,0.5):
					pixels[512+100*cos(i*p), 512+100*sin(i*p)] = (255,0,0)	
				
				x2 = 512+100*cos(sonnea*p - p*90)
				y2 = 512+100*sin(sonnea*p - p*90)
				d.multiline_text((x2,y2-20), "R", font = fnt, fill=(255, 0, 0))
	
				x2 = 512+100*cos(sonnem*p - p*90)
				y2 = 512+100*sin(sonnem*p - p*90)
				d.multiline_text((x2-5,y2), "N", font = fnt, fill=(255, 0, 0))	
	
				x2 = 512+100*cos(sonneu*p - p*90)
				y2 = 512+100*sin(sonneu*p - p*90)
				d.multiline_text((x2-10,y2-20), "S", font = fnt, fill=(255, 0, 0))	
		
			else:
				for i in np.arange(sonneu-90,360+sonnea-90,0.5):
					pixels[512+100*cos(i*p), 512+100*sin(i*p)] = (255,0,0)
				
				x2 = 512+100*cos(sonnea*p - p*90)
				y2 = 512+100*sin(sonnea*p - p*90)
				d.multiline_text((x2,y2), "R", font = fnt, fill=(255, 0, 0))
	
				x2 = 512+100*cos(sonnem*p - p*90)
				y2 = 512+100*sin(sonnem*p - p*90)
				d.multiline_text((x2-5,y2-20), "N", font = fnt, fill=(255, 0, 0))	
	
				x2 = 512+100*cos(sonneu*p - p*90)
				y2 = 512+100*sin(sonneu*p - p*90)
				d.multiline_text((x2-10,y2), "S", font = fnt, fill=(255, 0, 0))			
		
		else:
		
			if pflag == 0:
				d.multiline_text((10,30), "Sun does not rise.", font = fnt, fill=(255, 0, 0))
			else:
				d.multiline_text((10,30), "Sun does not set.", font = fnt, fill=(255, 0, 0))
		
		try:
			im.show()
		except AttributeError:
			pass

		im.save(".map.png")

	textdoc.text.addElement(tabp)

	# add the image
	# img_path is the local path of the image to include
	img_path = '.plot.png';
	#img_path = 'D:\Document\PersonalInfoRemixBook\examples\ch17\campanile_fog.jpg'

	from odf.draw import Frame, Image

	href = textdoc.addPicture(img_path)
	f = Frame(name="graphics1", anchortype="page", width="9.04cm", height="6.93cm", x="10.84cm", y="2.04cm", stylename=frstyle, zindex="0")
	tabp.addElement(f)
	img = Image(href=href, type="simple", show="embed", actuate="onLoad")
	f.addElement(img)

	if nosat == 0:
		img_path = '.sat.png';
		basewidth = 600
		from PIL import Image
		img = Image.open('.sat.png')
		wpercent = (basewidth / float(img.size[0]))
		hsize = int((float(img.size[1]) * float(wpercent)))
		img = img.resize((basewidth, hsize), Image.ANTIALIAS)
		img.save('.sat.png')
	else:
		img_path = 'nosat.jpg';

	from odf.draw import Frame, Image

	#if aktuellesdatum == 0:
	if printmoonstats == 0:

		href = textdoc.addPicture(img_path)
		f = Frame(name="graphics1", anchortype="page", width="8.00cm", height="8.00cm", x="10.97cm", y="9.934cm", stylename=frstyle, zindex="0")
		tabp.addElement(f)
		img = Image(href=href, type="simple", show="embed", actuate="onLoad")
		f.addElement(img)
		
	#if aktuellesdatum == 1 and nosat == 0:
	if printmoonstats == 1 and nosat == 0:
				
		img_path = '.mond.png'
		href = textdoc.addPicture(img_path)
		f = Frame(name="graphics1", anchortype="page", width="8.00cm", height="8.00cm", x="10.97cm", y="9.934cm", stylename=frstyle, zindex="0")
		tabp.addElement(f)
		img = Image(href=href, type="simple", show="embed", actuate="onLoad")
		f.addElement(img)
		
	#if aktuellesdatum == 1 and nosat == 1:
	if printmoonstats == 1 and nosat == 1:
				
		img_path = 'nosat.jpg'
		href = textdoc.addPicture(img_path)
		f = Frame(name="graphics1", anchortype="page", width="8.00cm", height="8.00cm", x="10.97cm", y="9.934cm", stylename=frstyle, zindex="0")
		tabp.addElement(f)
		img = Image(href=href, type="simple", show="embed", actuate="onLoad")
		f.addElement(img)

	if nosat == 1:
		img_path = 'nosat.jpg';
	else:
		img_path = '.map.png';

	href = textdoc.addPicture(img_path)
	f = Frame(name="graphics1", anchortype="page", width="8.00cm", height="8.00cm", x="11.01cm", y="19.70cm", stylename=frstyle, zindex="0")
	tabp.addElement(f)
	img = Image(href=href, type="simple", show="embed", actuate="onLoad")
	f.addElement(img)	
	
	print('PLEASE INPUT ON KEYBOARD:\n\n1.	Save report\n2.	Open recent report PDF\n3.	Save location\n4.	Edit saved location\n5.	Select new location\n6.	Sun hour calculator\n7.	Seasons and DST switch time\n8.	About this app\n9.	Quit\n\n ')
			
# ---------------------- # Hauptprogramm # -----------------------

UIDevice = objc_util.ObjCClass('UIDevice')
device = UIDevice.currentDevice()
devtype = str(device.localizedModel())

if devtype == 'iPad':
	dialogs.hud_alert('This app is for iPhones only.', 'error', 1.8)	
	exit()
	
global printmoonstats
printmoonstats = 0

mainprogram()

while reset == 1:
	mainprogram()

while 1 == 1:
	
	while reset == 1:
		mainprogram()
	
	choice = input('')
	
	while choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6' and choice != '7' and choice != '8' and choice != '9':
		print()
		print('Invalid input.')
		print()
		choice = input('')
		
	if choice  == '1':
		print()
		print('Saving report..')
		savereport()	
		print()
		
	if choice == '2':
		print()
		print('Display recent PDF..')
		my_file = Path("Sunreport.pdf")
		if my_file.is_file():
			f = 'Sunreport.pdf'
			outfile_path = os.path.abspath(f)
			console.quicklook(outfile_path)
		else:
			dialogs.hud_alert('No PDF available.', 'error', 1.8)
		print()
		
	if choice  == '3':
		print()
		print('Saving location..')
		savelocation()		
		print()
		
	if choice == '4':
		print()
		print('Editing saved location..')
		print()
		button1_tapped(None)
		
	if choice  == '5':
		mainprogram()
		
	#if choice  == '7':	
	#	button4_tapped('sathoehe')
		
	if choice  == '6':
		print()
		print('Starting sun hour calculator..')
		
		#v = ui.load_view('slidertest')
		
		try:
			v = ui.load_view('slidertest')
		except FileNotFoundError:
			v = ui.load_view('slidertest.json')
		
		slider_action(v['slider1'])
		v.present('sheet')
		v.wait_modal()
		
		#std = float(input('Stunde: '))
		#min = float(input('Minute: '))
		#sonne(std,min)
		#print()
		#print ('Richtung:' + '	' + str(bq))
		#print ('HÃ¶he:' + '		' + str(bt))		
		print()

	if choice  == '7':
		print()
		print('Starting seasons and DST time overview..')
		aequinox()
		
		a1bak = a1
		a2bak = a2
		
		a1 = springday
		a2 = 3
		springwotag = wochentag()
		
		a1 = summerday
		a2 = 6
		summerwotag = wochentag()
		
		a1 = autumnday
		a2 = 9
		autumnwotag = wochentag()
		
		a1 = winterday
		a2 = 12
		winterwotag = wochentag()
		
		a1 = a1bak
		a2 = a2bak
		
		print()
		print('Seasons:')
		print('--------')
		print(f'Beginning of spring:	{springwotag}, {a3}-03-{springday}')
		print(f'Beginning of summer: 	{summerwotag}, {a3}-06-{summerday}')
		print(f'Beginning of autumn:	{autumnwotag}, {a3}-09-{autumnday}')
		print(f'Beginning of winter:	{winterwotag}, {a3}-12-{winterday}\n')
		
		print('DST Switch Time:')
		print('----------------')
		checkdststatus()
		print()
	
	if choice == '8':
		print()
		print('Starting app info..')
		button3_tapped(None)
		print()	
		
	if choice  == '9':
		print()
		print('Quit')
		exit()
    
