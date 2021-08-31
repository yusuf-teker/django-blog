#from .iletisim import iletisim
from .iletisim import IletisimFormView

from .anasayfa import anasayfa
#from .kategori import kategori
from .kategori import KategoriListView
from .yazilarim import yazilarim
#from .detay import detay
from .detay import DetayView #class-based view ile degistirdik


#from .yazi_ekle import yazi_ekle
from .yazi_ekle import YaziEkleCreateView

#from .yazi_guncelle import yazi_guncelle
from .yazi_guncelle import YaziGuncelleUpdateView
#from .yazi_sil import yazi_sil
from .yazi_sil import YaziSilDeleteView
from .yorum_sil import yorum_sil
