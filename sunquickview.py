import appex, ui
from math import *
from datetime import timedelta
from datetime import datetime
import location
from pylab import *
import arrow
from time import tzname
from console import clear
from PIL import Image, ImageDraw, ImageFont
from timezonefinder import TimezoneFinder
import objc_util

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
	{'title': 'Pacific/Niue													UTC -11', 'tzn': 'Pacific/Niue', 'utc': '−11', 'dst': '−11'},
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

global norise

def drawsunstatus(rise, noon, set, current):
	
	UIDevice = objc_util.ObjCClass('UIDevice')
	device = UIDevice.currentDevice()
	devtype = str(device.localizedModel())

	if devtype == 'iPad':
		width = 800
	else:
		width = 360
	
	rise -= 90
	noon -= 90
	set -= 90
	current -= 90
	im = Image.new('RGB', (width, 210), (0, 0, 0))
	draw = ImageDraw.Draw(im)

	draw.ellipse((30, 15, 200, 185), fill=(None), outline=(255, 255, 0))

	pi = 3.141592653589793
	centerx = 115
	centery = 100
	radius = 85

	targetangle = rise
	angleconv = targetangle * (pi/180)
	targetx = cos(angleconv) * radius + centerx
	targety = sin(angleconv) * radius + centery

	draw.line((centerx, centery, targetx, targety), fill=(255, 0, 0), width=1)
	
	targetangle = noon
	angleconv = targetangle * (pi/180)
	targetx = math.cos(angleconv) * radius + centerx
	targety = math.sin(angleconv) * radius + centery

	draw.line((centerx, centery, targetx, targety), fill=(255, 0, 0), width=1)
	
	targetangle = set
	angleconv = targetangle * (pi/180)
	targetx = math.cos(angleconv) * radius + centerx
	targety = math.sin(angleconv) * radius + centery

	draw.line((centerx, centery, targetx, targety), fill=(255, 0, 0), width=1)
	
	targetangle = current
	angleconv = targetangle * (pi/180)
	targetx = math.cos(angleconv) * radius + centerx
	targety = math.sin(angleconv) * radius + centery

	draw.line((centerx, centery, targetx, targety), fill=(0, 255, 0), width=1)
	
	draw.text((115, 0), '0°', fill = 'yellow', font = None)
	draw.text((0, 95), '270°', fill = 'yellow', font = None)
	draw.text((105, 190), '180°', fill = 'yellow', font = None)
	draw.text((205, 95), '90°', fill = 'yellow', font = None) 

	#im.save('data/dst/pillow_imagedraw.jpg', quality=95)

	im.show()

def get_location():
	global latitude, longitude, loc
	location.start_updates()
	loc = location.get_location()
	location.stop_updates()
	try:
		latitude = loc['latitude']
	except TypeError:
		print('Kein GPS.')
		exit()
	longitude = loc['longitude']

def date_to_jd(year,month,day):
    if month == 1 or month == 2:
        yearp = year - 1
        monthp = month + 12
    else:
        yearp = year
        monthp = month

    if ((year < 1582) or
        (year == 1582 and month < 10) or
        (year == 1582 and month == 10 and day < 15)):
        B = 0
    else:

        A = math.trunc(yearp / 100.)
        B = 2 - A + math.trunc(A / 4.)

    if yearp < 0:
        C = math.trunc((365.25 * yearp) - 0.75)
    else:
        C = math.trunc(365.25 * yearp)
    D = math.trunc(30.6001 * (monthp + 1))
    jd = B + C + D + day + 1720994.5
    return jd    

def modulo(z,n):
    m=z-int(int(z)/int(n))*int(n)
    return m
      
def sonne(hh,mm):
    global bq, bt
    
    mm = mm/60
    b1 = hh+mm
    rd = pi/180

    b2 = (b1+a4)/24
    b5 = int(a3/100)
    b6 = 2-b5+int(b5/4)
    b7 = int(365.25*(a3+4716))+int(30.6001*(a2+1))+a1+b2+b6-1524.5
    b8 = b7-2451545
    b9 = 280.46+0.9856474*b8
    g0 = 357.528+0.9856003*b8
    bb = b9+1.915*sin(g0*rd)+0.01997*sin(2*g0*rd)
    bc = 23.439-0.0000004*b8
    bd = cos((bb*rd))

    if bd < 0:
        be = ((atan(cos(bc*rd)*tan(bb*rd))) + 4*atan(1))/rd

    else:
        be = (atan(cos(bc*rd)*tan(bb*rd)))/rd
    x = sin((bc*rd)*sin(bb*rd))

    x = atan(x/sqrt(1-x*x))

    bf = x/rd
    bg = int(365.25*(a3+4716))+int(30.6001*(a2+1))+a1+(0/24)+b6-1524.5
    bh = (bg-2451545)/36525
    z = 6.697376+2400.05134*bh+1.002738*(b1+a4)
    n = 24
    bi = modulo(z,n)
    bj = bi*15+b4
    bk = bj-be
    x = atan(sin(bk*rd)/(cos(bk*rd)*sin(b3*rd)-tan(bf*rd)*cos(b3*rd))) 
    if bd < 0:
        bl=(x/rd)+180
    else:
        bl=x/rd
    x=(cos(bk*rd)*sin(b3*rd)-tan(bf*rd)*cos(b3*rd))/rd

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
        bq = bp

    x = cos(bf*rd)*cos(bk*rd)*cos(b3*rd)+sin(bf*rd)*sin(b3*rd)
    x = atan(x/sqrt(1-x*x))
    br = x/rd
    bs = 1.02/(tan(br*rd+(10.3/(br*rd+5.11))))
    bt = ((br*rd)+(bs/60))/rd

def zeiten():
	pi=3.14159265359

	global ah, am, mh, mm, uh, um, ahx, mhx, uhx, norise, label, x1, x2, x3, x4
	
	norise = 0

	latitude_radians = math.radians(latitude_deg)
	longitude__radians = math.radians(longitude_deg)

	jd2000 = 2451545

	currentDT = datetime.datetime.now()
	current_year = a3
	current_month = a2
	current_day = a1

	jd_now = date_to_jd(current_year,current_month,current_day)
	n = jd_now - jd2000 + 0.0008
	jstar = n - longitude_deg/360
	M_deg = (357.5291 + 0.98560028 * jstar)%360
	M = M_deg * pi/180
	C = 1.9148 * math.sin(M) + 0.0200 * math.sin(2*M) + 0.0003 * math.sin(3*M)
	lamda_deg = math.fmod(M_deg + C + 180 + 102.9372,360)
	lamda = lamda_deg * pi/180
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
	
	label = ''

	label += 'Akt. Datum:		' + str(int(a3)) + '-' + str(int(a2)) + '-' + str(int(a1)) + '\n'
	label += 'Akt. Zeitzone:	' + zone + '\n'
	label += "------------------------------" + '\n'

	label += "Breite		=	" + str(latitude_deg) + '\n'
	label += "Länge		=	" + str(longitude_deg) + '\n'
	label += "UTC  		=	" + str(timezone) + '\n'
	label += "------------------------------" + '\n'

	Jrise = Jtransit - omega_degrees/360
	numdays = Jrise - jd2000
	numdays =  numdays + 0.5
	numdays =  numdays + timezone/24
	sunrise = datetime.datetime(2000, 1, 1) + datetime.timedelta(numdays)
	Jset = Jtransit + omega_degrees/360
	numdays = Jset - jd2000
	numdays =  numdays + 0.5
	numdays =  numdays + timezone/24
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
	label += "Taglänge	=" + '	' + str(bstunden).zfill(2) + ':' + str(bsekunden).zfill(2) + '\n'
	label += "------------------------------" + '\n'
	
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
	
	ch = currentDT.strftime("%H")
	ch = float(ch)
	cm = currentDT.strftime("%M")
	cm = float(cm)
	
	if norise == 0:
	
		label += 'Aufgang   (Std., Azimuth, Höhe)' + '\n'
		sonne(ah,am)
		x1 = str(bq)
		y = str(bt)
		label += sunrise.strftime("%H:%M") + '		' + x1[0:5] + '		' + y[0:5] + '\n'
		label += "------------------------------" + '\n'
		label += 'Mittag    (Std., Azimuth, Höhe)' + '\n'
		sonne(mh,mm)
		x2 = str(bq)
		y = str(bt)
		label += midday.strftime("%H:%M") + '		' + x2[0:5] + '		' + y[0:5] + '\n'
		label += "------------------------------" + '\n'
		label += 'Untergang (Std., Azimuth, Höhe)' + '\n'
		sonne(uh,um)
		x3 = str(bq)
		y = str(bt)
		label += sunset.strftime("%H:%M") + '		' + x3[0:5] + '		' + y[0:5] + '\n'
		label += "------------------------------" + '\n'
		label += 'Jetzt		(Std., Azimuth, Höhe)' + '\n'
		sonne(ch,cm)
		x4 = str(bq)
		y = str(bt)
		label += currentDT.strftime("%H:%M") + '		' + x4[0:5] + '		' + y[0:5] + '\n'
		label += "------------------------------" + '\n'
		
		if currentDT < sunset and currentDT > sunrise:
			rest = sunset - currentDT
			label += '▼ in ' + str(rest)
			
		if currentDT < sunrise:
			rest = sunrise - currentDT
			label += '▲ in ' + str(rest)
			
		if currentDT > sunset:
			rest = currentDT - sunset
			label += '▼ seit ' + str(rest)

	else:
		exit()
	
# Programmtitel

clear
get_location()
b3 = latitude
b4 = longitude
#b3 = 39.9576010
#b4 = 116.3351850

latitude_deg = b3
longitude_deg = b4

currentDT = datetime.datetime.now()
	
a3 = currentDT.year
a2 = currentDT.month
a1 = currentDT.day

tf = TimezoneFinder()
zone = tf.timezone_at(lng=b4, lat=b3) 

tzindex = 0

for i in range (0, len(tznames)):
	comp = (tznames[i]['tzn'])
	if comp == zone:
		tzindex = i
		
if tzindex == 0:
	for i in range (0, len(tzalias)):
		comp = (tzalias[i]['tzn'])
		if comp == zone:
			tzindex = i
			
if tzindex == 0:
	print('Zeitzone nicht ermittelbar.')
	exit()
				
a4 = float(tznames[tzindex]['utc'])*(-1)
timezone = a4*(-1)

now = arrow.get(a3,a2,a1)
now = now.shift(hours=+12)
now = now.to(zone) 
 
now_dst = now.dst() 
strnow = str(now_dst)
strnow = strnow[0:1]
strfloat = float(strnow)
a4 = a4 + strfloat*(-1)
timezone = timezone + strfloat

clear()				
zeiten()
print(label)
x1 = float(x1)
x2 = float(x2)
x3 = float(x3)
x4 = float(x4)
drawsunstatus(x1,x2,x3,x4)
exit()
#v = ui.View(frame=(0, 0, 320, 260))
#wlabel = ui.Label(frame=(8, 0, 320, 260), flex='wh')
#wlabel.name = 'text_label'
#wlabel.font = ('Menlo', 12)
#wlabel.number_of_lines = 0
#v.add_subview(wlabel)
#appex.set_widget_view(v)
#wlabel.text = label
