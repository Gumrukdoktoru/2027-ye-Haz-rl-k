# Üretim Hafızası

Prompt 1 (Akıllı Test Soru Motoru) ile üretilen her soru buraya tek satır olarak eklenir.
Yeni set üretilmeden önce bu dosya okunur; aynı çekirdek tekrar üretilmez.

```
ID | KONU | MADDE | ÇEKİRDEK | TİP | ZORLUK | CEVAP | SET
KAR-001 | Karar | GK m.6/2 | Karar talebi: idare, başvurunun kendisine ulaştığı tarihten itibaren otuz gün içinde karar alır | SÜ | K | C | S1
KAR-002 | Karar | GK m.6/1, 6/2, 6/4; GY m.27/1 | Karar alınması talebinin yazılı olarak yapılması zorunludur | DĞ | O | A | S1
KAR-003 | Karar | GK m.6/2 (ikinci paragraf) | Süre aşımı: süre aşılabilir; süre dolmadan gerekçe ve gerekli ek süre başvuru sahibine bildirilir | ÇI | O | D | S1
KAR-004 | Karar | GK m.6/2, 6/3 | Ret ve aleyhe kararlar gerekçeli alınır, itiraz yolunun açık olduğu kararda belirtilir | UK | Z | D | S1
KAR-005 | Karar | GK m.7/1 | Lehe kararın zorunlu iptali: yanlış/eksik bilgi + başvuranın bilmesi/bilmesi gerekmesi + doğru bilgiyle verilememe, üçü bir arada | ÇI | Z | B | S1
KAR-006 | Karar | GK m.7/2-a | Karara esas koşulun gerçekleşmemesi/gerçekleşemez olması: lehe karar değiştirilir veya iptal edilebilir (ihtiyari) | DY | O | D | S1
KAR-007 | Karar | GK m.7/4 | Yürürlük: zorunlu iptal → iptal kararının verildiği tarih; değiştirme/iptal edilebilir hali → tebliğ tarihi | EŞ | ÇZ | C | S1
KAR-008 | Karar | GK m.7/4 (ikinci cümle) | İstisna: muhatabın yasal çıkarları gerektirirse yönetmelikle belirlenen koşullarda yürürlük tarihi ertelenebilir | DY | Z | C | S1
KAR-009 | Karar | GY m.27/3, 27/4 | Değiştirme/iptal, yürürlük tarihinde rejime tabi tutulmaya başlanmış eşyaya uygulanmaz; idare belirli dönemde GOİK isteyebilir | UK | Z | E | S1
KAR-010 | Karar | GY m.586/1 | İtirazlar otuz gün içinde karara bağlanıp tebliğ edilir; bu sürede karar alınamazsa GK m.6/2 (süre aşımı) uygulanır | SÜ | O | A | S1
KAR-011 | Karar | GY m.586/1 | İtiraz incelemesi: örnek alınamazsa eşyanın kendisi veya fotoğraf, katalog, prospektüs gibi fikir verecek belgeler incelenir | BD | Z | B | S1
KAR-012 | Karar | GY m.586/1 | İtiraz incelemesinde gerek duyulursa ilgili gümrük idaresinin mütalaası alınır | MK | O | E | S1
KAR-013 | Karar | GK m.6/3, 6/4, 7/3, 7/4; GY m.27/3 | Kararın iptali muhatabına tebliğ edilir (diğer kurallarla birlikte değerlendirme) | ÇI | ÇZ | B | S1
KAR-014 | Karar | GK m.6/1 | Karar talep eden kişi kararın verilebilmesi için gerekli bütün bilgi ve belgeleri ibraz etmek zorundadır | UK | Z | E | S1
KAR-015 | Karar | GK m.6/2, 6/4 | Karar başvuru sahibine yazılı tebliğ edilir ve gümrük idarelerince derhal uygulanır; ayrı bir onay ya da bekleme süresi yoktur | UU | ÇZ | A | S1
```

Toplam: 15 satır (Karar: 15)
