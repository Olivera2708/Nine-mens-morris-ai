"""
Modul sadrži implementaciju asocijativnog niza
"""


class MapElement(object):
    """
    Klasa modeluje element asocijativnog niza
    """
    __slots__ = '_key', '_value'

    def __init__(self, key, value):
        self._key = key
        self._value = value

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class Map(object):
    """
    Klasa modeluje asocijativni niz
    """
    def __init__(self):
        self._data = []

    def __getitem__(self, key):
        """
        Pristup elementu sa zadatim ključem

        Metoda vrši pristup elementu sa zadatim ključem. U slučaju
        da element postoji u mapi, metoda vraća njegovu vrednost, dok
        u suprotnom podiže odgovarajući izuzetak.

        Argument:
        - `key`: ključ elementa kome se pristupa
        """
        for item in self._data:
            if key == item.key:
                return item.value

        raise KeyError('Ne postoji element sa ključem %s' % str(key))

    def __setitem__(self, key, value):
        """
        Postavljanje vrednosti elementa sa zadatim ključem

        Metoda najpre pretražuje postojeće elemente po vrednosti ključa.
        Ukoliko traženi ključ već postoji, vrši se ažuriranje vrednosti
        postojećeg elementa. U suprotnom, kreira se novi element koji se
        dodaje u mapu.

        Argumenti:
        - `key`: ključ elementa koji se kreira ili ažurira
        - `value`: nova vrednost elementa
        """
        for item in self._data:
            if key == item.key:
                item.value = value
                return

        # element nije pronađen, zapiši ga u mapu
        self._data.append(MapElement(key, value))

    def __delitem__(self, key):
        """
        Brisanje elementa sa zadatim ključem

        Metoda pretražuje elemente po vrednosti ključa. Ukoliko element
        sa zadatim ključem postoji u mapi, vrši se njegovo brisanje. U
        suprotnom se podiže odgovarajući izuzetak.

        Argument:
        - `key`: ključ elementa za brisanje
        """
        length = len(self._data)
        for i in range(length):
            if key == self._data[i].key:
                self._data.pop(i)
                return

        raise KeyError('Ne postoji element sa ključem %s' % str(key))

    def __len__(self):
        return len(self._data)

    def __contains__(self, key):
        """
        Metoda vrši proveru postojanja ključa u mapi

        Argument:
        - `key`: ključ koji se traži
        """
        for item in self._data:
            if key == item.key:
                return True

        return False

    def __iter__(self):
        for item in self._data:
            yield item.key

    def items(self):
        for item in self._data:
            yield item.key, item.value

    def keys(self):
        """
        Metoda vraća sve ključeve u mapi
        """
        keys = []
        for key in self:
            keys.append(key)

        return keys

    def values(self):
        """
        Metoda vraća sve vrednosti u mapi
        """
        values = []
        for key in self:
            values.append(self[key])

        return values

    def clear(self):
        """
        Metoda uklanja sve elemente iz mape
        """
        self._data = []
