# BinaryBear's Forge - Yazı Ekleme ve Silme Rehberi

Bu rehber blogunuza yeni yazı eklemek veya var olanı silmek için adımları içerir.

---

## ➕ Yeni Yazı Ekleme

1.  **Klasöre Git:** Bilgisayarında proje klasörüne gir ve `_posts` klasörünü aç.
2.  **Dosya Oluştur:** Tıpkı `TASLAK_YAZI.md` gibi yeni bir `.md` dosyası oluştur.
3.  **İsimlendir:** Dosya ismini MUTLAKA şu formatta yap:
    *   `YIL-AY-GÜN-baslik.md`
    *   Örnek: `2026-03-25-tersine-muhendislik-nedir.md`
4.  **İçeriği Yaz:** Dosyanın en başına şu "Front Matter" kısmını yapıştır ve düzenle:

    ```yaml
    ---
    title: Yazının Başlığı Buraya
    date: 2026-03-25 14:00:00 +0300
    categories: [Ana Kategori]
    tags: [etiket1, etiket2]
    ---
    ```

5.  **Kaydet ve Yayınla:**
    Terminali açıp şu komutları sırasıyla gir:

    ```bash
    git add .
    git commit -m "Yeni yazı eklendi: Yazı Başlığı"
    git push
    ```

---

## ❌ Yazı Silme

1.  **Klasöre Git:** `_posts` klasörüne gir.
2.  **Dosyayı Sil:** Silmek istediğin `.md` dosyasını (örneğin: `2026-02-15-merhaba-dunya.md`) sil.
3.  **Değişikliği Yayınla:**
    Terminali açıp şu komutları gir:

    ```bash
    git add .
    git commit -m "Yazı silindi"
    git push
    ```

---

## 📝 İpuçları
- **Taslaklar:** Yazını hemen yayınlamak istemiyorsan, dosyanın en başına `published: false` ekleyebilirsin veya dosyayı `_drafts` klasörüne taşıyabilirsin.
- **Resim Ekleme:** Resimlerini `assets/img/` klasörüne atıp, yazında `![Resim Açıklaması](/assets/img/resimdosyasi.jpg)` şeklinde kullanabilirsin.
