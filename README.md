# 🛡️ Gelişmiş Discord Guard (Koruma) Botu Altyapısı

Bu proje, Discord sunucularının güvenliğini en üst düzeye çıkarmak amacıyla geliştirilmiş, modern ve hızlı bir **Guard Bot** altyapısıdır. Sunucunuza yönelik yapılabilecek yetki suistimallerini ve raid (saldırı) girişimlerini anlık olarak engeller.

---

## ✨ Özellikler

*   ❌ **Rol Silme Koruması:** Sunucuda izinsiz rol silen yetkilinin tüm rolleri anında sıfırlanır.
*   🗑️ **Kanal Silme Koruması:** İzinsiz kanal silen kişi sunucudan banlanır ve silinen kanal otomatik olarak tüm ayarlarıyla geri açılır.
*   🔨 **Sağ Tık Ban Koruması:** Sunucudaki üyeleri izinsiz şekilde banlamaya çalışan yetkili banlanır ve banlanan üyenin banı otomatik açılır.
*   📊 **Bilgi Sistemi:** `!guard-bilgi` komutu ile sistemin aktifliği kontrol edilebilir.

---

## 🚀 Kurulum ve Çalıştırma

### 1. Gereksinimler
Bilgisayarınızda veya uzak sunucunuzda (VDS) **Python 3.8+** yüklü olmalıdır.

### 2. Bağımlılıkları Yükleyin
Proje klasöründe bir terminal açın ve gerekli kütüphaneleri yükleyin:
```bash
pip install discord.py python-dotenv
