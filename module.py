import custommodule as mod

mod.ex_method()

from custommodule import ex_method #sadece ex_methodu kullanabiliyon

ex_method()
#pythonda paket yöneticileri conda(jüpiter notbooke özel) ve pip dir.
#pythonda paket deposu pypi dir.


from AnimalPackage.cat import cat

c = cat.Cat("pisi", "tekir", 15)
c.info()