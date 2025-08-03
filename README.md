
## 👥 Takım İsmi
AI209

## 👩‍💻 Takım Rolleri

| Sahibi         | Roller                              | Sosyal Medya                           |
|----------------|-----------------------------------|--------------------------------------|
| İrem Uslu | Scrum Master, Developer, Product Owner | [LinkedIn](https://linkedin.com/in/irem-uslu) |


## 🧠 Ürün İsmi
<p align="center">
  <img src="https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/logoAI.png" alt="Emotery Logo" width="300"/>
  <br><em>Gelişmiş Yapay Zeka Destekli Mental Sağlık Günlüğü Uygulaması</em>
</p>

---


## 📝 Ürün Açıklaması
Emotery, kullanıcının günlük ruh hali ve duygusal durumunu yazılı veya sesli olarak kaydetmesine olanak tanıyan, gelişmiş yapay zeka destekli bir mental sağlık günlüğü uygulamasıdır. Uygulama, doğal dil işleme (NLP) teknikleriyle duygu analizini gerçekleştirir ve kullanıcının hissettiklerini derinlemesine anlamaya çalışır. Toplanan veriler ışığında, kullanıcıya kişiselleştirilmiş öneriler ve destekleyici içerikler sunar.

Emotery’nin güçlü hafıza sistemi sayesinde, kullanıcıların duygu durumları zaman içinde takip edilir ve gelişim grafikleriyle görselleştirilir. Bu sayede, stres yönetimi, kaygı azaltma ve genel ruh sağlığının iyileştirilmesi için somut geri bildirimler sağlanır. Ayrıca, kullanıcı dostu web arayüzü üzerinden kolay erişim ve güvenli veri saklama özellikleri sunar. Emotery, ruh sağlığına önem veren herkes için güvenilir bir dijital dost olarak tasarlanmıştır.

---

## ⚙️ Ürün Özellikleri
- Yazılı ve sesli duygu girişini kabul etme
- Duygu analizi (pozitif, negatif, nötr, detaylı duygular)
- Günlük öneri ve tavsiye sistemi
- Kişiye özel ruh hali geçmişi ve grafik gösterimleri
- Hafıza sistemi ile uzun vadeli duygu takibi
- Web tabanlı kullanıcı arayüzü
- Güvenli veri saklama ve gizlilik önlemleri

---

## 🎯 Hedef Kitle
- 18-65 yaş arası (özellikle genç yetişkinler ve orta yaşlı bireyler ön planda olabilir).
- İş ve günlük yaşam stresiyle başa çıkmaya çalışan, duygusal iniş çıkışlar yaşayan profesyoneller
- Ruh sağlığına önem veren, duygusal gelişim ve kişisel iyileşme alanında aktif olan gençler ve öğrenciler
- Kendini geliştirmeye, duygusal farkındalık ve iyileşmeye ilgi duyan bireyler.
- Depresyon, anksiyete, stres, yalnızlık gibi duygusal zorluklarla mücadele eden bireyler.

---

## 📋 Product Backlog — Emotery

| Görev / Özellik                                      | Açıklama                                                      | Öncelik | Tahmini Puan (Story Points) |
|-----------------------------------------------------|---------------------------------------------------------------|---------|-----------------------------|
| Kullanıcı kayıt ve giriş sistemi                     | Kullanıcıların hesap oluşturması ve giriş yapabilmesi          | Yüksek  | 5                           |
| Günlük ruh hali giriş formu                          | Kullanıcının yazılı veya sesli günlük girişi yapabilmesi       | Yüksek  | 5                           |
| Duygu analizi modülü (NLP tabanlı)                   | Kullanıcının girdilerini duygu analiziyle değerlendirme        | Yüksek  | 8                           |
| Tavsiye ve öneri sistemi                             | Duygu durumuna göre kişiye özel öneri ve tavsiyeler sunma      | Orta    | 5                           |
| Duygu durumu geçmişi ve grafik gösterimleri          | Kullanıcının ruh hali değişimlerini zaman içinde görselleştirme| Orta    | 5                           |
| Sesli duygu girişi desteği                           | Ses kaydını metne çevirme ve analiz etme                        | Orta    | 6                           |
| Hafıza sistemi ve veri saklama                       | Kullanıcı verilerinin güvenli ve uzun vadeli saklanması        | Yüksek  | 7                           |
| Web tabanlı kullanıcı arayüzü                        | Kullanıcı dostu, responsive ve erişilebilir arayüz tasarımı    | Yüksek  | 6                           |
| Güvenlik ve gizlilik önlemleri                       | Veri şifreleme, kullanıcı gizliliği, GDPR uyumluluğu           | Yüksek  | 6                           |
| Bildirim ve hatırlatma sistemi                       | Kullanıcıyı günlük giriş yapması için hatırlatma bildirimleri  | Orta    | 4                           |
| Chatbot entegrasyonu (opsiyonel)                     | Kullanıcının sohbet yoluyla destek alabilmesi                   | Düşük   | 4                           |

---


## 📂 Proje Dizini Yapısı
  
```plaintext
  app/         -> Ana uygulama dosyaları
  routers/     -> API endpointleri
  static/      -> CSS, JS, resimler
  templates/   -> HTML şablonları
  utils/       -> Yardımcı fonksiyonlar
  main.py      -> FastAPI giriş noktası
  database.py  -> Veritabanı bağlantısı
  models.py    -> Veritabanı modelleri
  emoteryai.db -> SQLite veritabanı
  requirements.txt -> Gerekli bağımlılıklar
```

## ⚙️ Projeyi Çalıştırma

<details>
<summary>Projeyi çalıştırmak için</summary>  
  
### 1. Gereksinimler
  - **Python 3.9+**
  - **pip** (Python paket yöneticisi)
  - Veritabanı: **PostgreSQL** veya **SQLite** (varsayılan: SQLite)
  -   `.env` dosyasında gerekli ortam değişkenleri

---

### 2. Kurulum Adımları
1. **Depoyu klonla**
   ```bash
   git clone https://github.com/iremuslu/Bootcamp-AI209
   cd Bootcamp-AI209

2. **Sanal Ortam Oluştur**
   ```bash
   python -m venv venv
   
   Windows:
   venv\Scripts\activate
   
   Mac/Linux:
   source venv/bin/activate
 3. **Bağımlılıkları Yükle**
    ```bash
     pip install -r requirements.txt

### 3. Çalıştırma
#### 1️⃣ `.env` Dosyası Oluştur
`.env` dosyası proje kök dizininde olmalı.

Örnek `.env` içeriği:
- GOOGLE_API_KEY=your_google_api_key
- SECRET_KEY=your_secret_key
- ACCESS_TOKEN_EXPIRE_MINUTES=30
- ALGORITHM=HS256

#### 2️⃣ Uygulamayı Başlat
  ```bash
  uvicorn main:app --reload  
 ```
</details>



### 📆 Sprint Raporları
<details>
<summary>🔹 Sprint 1</summary>

### 📝 Sprint Notları
Sprint sürecine başlamadan önce, Trello üzerinde oluşturulan **Product Backlog**, üç sprintlik iş yükünü kapsayacak şekilde planlanmıştır. Bu planlama, projenin genel yol haritasını netleştirerek uzun vadeli hedeflere daha stratejik bir şekilde yaklaşmamı sağlamıştır.

İlk sprintin temel amacı; günlük girişi, duygu analizi ve öneri sisteminin temel işlevlerini kurmaktır. Kullanıcı yazılı bir günlük girdisi oluşturduktan sonra bu içerik analiz edilir ve duygusal durumuna göre yorumlar ve kişiselleştirilmiş öneriler sunulur.

---

### 🎯 Sprint İçinde Tamamlanması Tahmin Edilen Puan
Toplam **61 story points** üzerinden 3 sprint’e bölünmüştür.

---

### 🧠 Puan Dağılımı ve Tahmin Mantığı

Proje kapsamında toplam **61 story points** puanlık iş yükü öngörülmüştür. Bu yük 3 sprint arasında eşit şekilde dağıtılmıştır. Sprint 1 için hedeflenen 23 puan başarıyla tamamlanmıştır.

## Sprint 1 — ~23 puan
| Görev / Özellik                  | Story Points |
|---------------------------------|--------------|
| Kullanıcı kayıt ve giriş sistemi | 5            |
| Günlük ruh hali giriş formu      | 5            |
| Duygu analizi modülü (NLP)       | 8            |
| Tavsiye ve öneri sistemi          | 5            |
---

### 📅 Daily Scrum Süreci
Tek başıma geliştirdiğim bu projede, ilerlememi takip etmek ve hedeflerimi kontrol etmek için günlük bireysel planlama oturumları gerçekleştirdim. Her gün Trello üzerinde yapılacaklarımı listeleyerek ilerlememi ölçtüm.

---

### 🔄 Sprint Board Güncellemeleri
Sprint süresince tüm görevler Trello panosunda aşağıdaki başlıklar altında yönetildi:

- **Rejected**: İlerleyen süreçte hedefler veya gereksinimler doğrultusunda iptal edilen, gözden geçirilen veya geçici olarak askıya alınan görevler
- **Backlog**: Projenin genel ihtiyaçları
- **To Do**: Sprint 1’e dahil ettiğim görevler
- **In Progress**: Üzerinde çalıştığım anlık görevler
- **Done**: Tamamlananlar

### 🖼️ Görsel: Trello Sprint Board 

<img src="https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/backlogTrello.png" width="1000"/>


---

### ✅ Sprint Review

Sprint sonunda hedeflenen tüm modüller başarıyla tamamlandı:
- Kullanıcıdan alınan günlük metni duygu analizine tabi tutuluyor
- Arayüz kullanıcı dostu ve modern bir yapı sunuyor
- Sistem öneri ve yorum üretiminde anlamlı geri bildirim sağlıyor

---

### 🔁 Sprint Retrospective

#### Güçlü Yönler
- Sprint planına sadık kalındı ve zamanında tamamlandı  
- UI/UX tasarımı sade ve etkili oldu 
- NLP entegrasyonu başarılı bir şekilde gerçekleştirildi

#### Geliştirilmesi Gereken Yönler
- Zaman yönetimi daha da disiplinli hale getirilebilir
- Test süreçleri sprintin daha erken safhalarında başlatılmalı
- Gelecek sprintlerde kullanıcı geçmişi ve grafiklerle görselleştirme eklenmeli
- Duygu analizi modülündeki prompt bazen öneri vermeyebiliyor, iyileştirmeler yapılabilir
- Frontend kısmı temel işlevleri sağlıyor ancak kullanıcı deneyimi ve tasarım açısından daha fazla geliştirme yapılabilir

<details>
<summary><strong>📎 Belgeler ve Ekler</strong></summary>

#### 📸 Uygulama Arayüzü

##### 🔹 Giriş Ekranı  
<img src="https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/login.png" alt="Emotery Logo" width="500" style="display: block; margin: 0;" />

**Açıklama:**  
- Giriş ekranı, kullanıcının mevcut hesabına giriş yapabilmesini sağlar. Kullanıcı adı ve şifre girişi yapıldıktan sonra, sistem kullanıcıyı **dashboard** sayfasına yönlendirir. 
- Bu ekran, kullanıcının güvenli bir şekilde sisteme giriş yapmasını sağlayacak basit ve kullanıcı dostu bir tasarıma sahiptir.

##### 🔹 Kayıt Ekranı  
<img src="https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/register.png" alt="Emotery Logo" width="500" style="display: block; margin: 0;" />

**Açıklama:**  
- Kayıt ekranı, yeni kullanıcıların hesap oluşturabilmesi için gerekli bilgileri (kullanıcı adı, şifre) girerek sisteme kaydolmalarını sağlar. 
- Kayıt işlemi tamamlandığında, kullanıcıya giriş ekranına yönlendirilir.  
- Bu ekran, güvenli kayıt işlemi için gerekli tüm doğrulama alanlarına sahiptir.

##### 🔹 Duygu Analizi  
<img src="https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/dashboard2.png" alt="Emotery Logo" width="500" style="display: block; margin: 0;" />

**Açıklama:**  
- Duygu analizi ekranı, kullanıcının ruh halini yazılı olarak girmesini sağlar.
- Kullanıcı, ruh hali girişini tamamladıktan sonra sistem, **NLP (Doğal Dil İşleme)** teknolojisini kullanarak duygu analizini yapar.  
- Ekran, kullanıcının duygusal durumunu açıklayan kişiselleştirilmiş öneriler sunar.
</details>

---

</details>

<details>
<summary>🔹 Sprint 2</summary>

### 📝 Sprint Hedefi
Bu sprintin amacı,duygu grafiğiyle ruh halindeki değişimi görebilmesi ve emojiler yardımıyla daha ilgi çekilebilir yapılması, kullanıcı profil ekranını görüntüleyebilmesi,sesli duygu giriş desteği ile günlüğünü kaydedebilmesi ve arayüzün daha gelişmiş bir kullanıcı deneyimi sunacak şekilde modernleştirilmesidir.

---

### 🎯 Sprint 2 Planlanan Puanlar
Toplam hedef: **29 story points**
Ekstradan kullanıcı profil sayfası **5 story points** olarak eklendi.

## Sprint 2 — ~29 puan
| Görev / Özellik                              | Story Points | Açıklama |
|---------------------------------------------|--------------|----------|
| Duygu durumu geçmişi ve grafik gösterimleri | 5            | Kullanıcının ruh halini zamansal olarak görüntüleyebilmesi |
| Sesli duygu girişi desteği                  | 6            | Kullanıcının mikrofona konuşarak günlük yazması |
| Hafıza sistemi ve veri saklama              | 7            | Günlüklerin veritabanında düzenli ve güvenli şekilde tutulması |
| Web tabanlı kullanıcı arayüzü geliştirme    | 6            | Dashboard ve diğer ekranların modernize edilmesi |
| Kullanıcı profil sayfası                    | 5            | Kullanıcının kendi bilgilerini ve önerilerini görebileceği detaylı ekran |

---

### 📅 Daily Scrum Süreci
Bu sprintte de bireysel geliştirme sürecine devam ettim. Her gün kodlamaya başlamadan önce Trello üzerindeki görevlerimi gözden geçirerek bir günlük plan oluşturdum. Ayrıca görevleri gün sonunda In Progress → Done şeklinde ilerlettim.Öncelikle kodlamaya başlamadan önce o günün temel işlevlerini belirledim.Daha sonra bir önceki yazdığım modülleri tekrardan test ettim.Frontend ve backend arasında olan gerekli API bağlantılarını entegre ettim.Tamamlanan görevleri gün sonunda Trello'da "Done" kartına çektim.

---

### 🔄 Sprint Board Güncellemeleri
Trello sprint 2 panosu aşağıdaki başlıklarla oluşturulmuştur:

- **Backlog**: Sprint 2 kapsamına alınan ve daha başlanmamış görevler
- **To Do**: Sprint 2 içinde o gün başlamayı planladığım işler
- **In Progress**: Aktif olarak üzerinde çalıştığım görevler
- **Done**: Tamamladığım işlevler (koda entegre edildi ve çalışıyor)

📌 Örnek **Sprint 2 Done User Stories**:
- Kullanıcı, önceki ruh hali girişlerini grafikle görüntüleyebiliyor
- Kullanıcı, mikrofona bastığında sesli giriş yapabiliyor
- Sistem, kullanıcı verilerini sqlite veritabanında güvenli şekilde saklıyor
- Kullanıcı, profil ekranında geçmiş girdilerini görebiliyor

### 🖼️ Görsel: Trello Sprint Board 

<img src= "https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/Sprint2/sprint2.png" width="1000"/>

---

### ✅ Sprint Review
Sprint sonunda hedeflenen tüm modüller başarıyla tamamlandı:
- Kullanıcıyı karşılayan ilk sayfa(giriş yap,kayıt ol,özellikler vb.) modern ve responsive bir şekilde tasarlandı.
- Kullanıcı artık önceki ruh hali girişlerini grafik yardımı ile görebiliyor
- Sesli günlük giriş butonu eklendi, temel mikrofon entegrasyonu test edildi.
- Kullanıcı profil sayfası oluşturularak kullanıcı bilgileri gösterildi

---

### 🔁 Sprint Retrospective

#### Güçlü Yönler
- Kullanıcı deneyimi tasarımı ciddi ölçüde iyileştirildi
- Sesli giriş desteğiyle kullanıcı etkileşimi artırıldı
- Veritabanı yapısı daha sürdürülebilir hale getirildi
- Kullanıcı profili ile kişisel veriler ve geçmiş öneriler erişilebilir kılındı.
- Günlük metin girişleri artık veritabanına güvenli biçimde kaydediliyor ve daha sonra analiz edilebiliyor

#### Geliştirilmesi Gerekenler
- Tek geliştirici olarak tüm süreçleri yürütmek, bazı görevlerin zamanında tamamlanmasını zorlaştırabiliyor.Bu yüzden zaman yönetimi daha planlı yapılabilir.
- Sesli girişte bazı tarayıcılarda uyumsuzluklar gözlemlendi
- Prompt sistemi biraz daha geliştirilebilir.
- Kullanıcı profil ekranı görsel olarak yeterince kişiselleştirilmiş değil, detaylandırılabilir
- Gelecek sprintlerde bildirim sistemi ve gelişmiş kullanıcı takibi planlanmalı
- Veritabanı yapısı SQLite olarak kalmaya devam ediyor; canlı sistemler için daha güçlü altyapıya geçiş planlanmalı (örn. PostgreSQL)

<details>
<summary><strong>📎 Belgeler ve Ekler</strong></summary>

#### 📸 Uygulama Arayüzü

##### 🔹 Giriş Ekranı  
<img src="https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/Sprint2/dashboard.png" alt="Emotery Logo" width="500" style="display: block; margin: 0;" />

**Açıklama:**  
- Bu yeni giriş ekranı, kullanıcıyı uygulamaya sıcak bir şekilde karşılayan sezgisel bir yapıya sahiptir.
- "Bugün nasıl hissediyorsun?" sorusu ile duygusal farkındalık artırılarak kullanıcı günlük girişine teşvik edilir.
- Bu ekran, kullanıcının güvenli bir şekilde sisteme giriş yapmasını sağlayacak basit ve kullanıcı dostu bir tasarıma sahiptir.
- Alt kısımda Sesli Günlük, Ruh Hali Analizi ve Kişisel Öneriler gibi temel özellikler ikonlarla sade biçimde tanıtılmıştır.
- Gelişmiş kullanıcı deneyimi için responsive tasarım uygulanmıştır


##### 🔹 Kayıt Ekranı  
<img src="https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/Sprint2/register.png" alt="Emotery Logo" width="500" style="display: block; margin: 0;" />

**Açıklama:**  
- Yeni kayıt ekranı kullanıcıdan artık Ad Soyad, E-posta, Kullanıcı Adı ve Şifre bilgilerini alarak daha güvenli ve kişiselleştirilebilir bir kullanıcı profili oluşturulmasını sağlar.
- Form tasarımı sade ve okunabilir.
- Kayıt işlemi tamamlandığında, kullanıcıya giriş ekranına yönlendirilir.
- Daha fazla kullanıcı verisi alınması sayesinde kişiselleştirilmiş önerilerde daha doğru sonuçlar sunmak hedeflenmiştir.


##### 🔹 Ana Sayfa/Duygu Analizi
<img src="https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/Sprint2/mutlu1.png" alt="Emotery Logo" width="500" style="display: block; margin: 0;" />

**Açıklama:**  
- Günlük giriş alanına ek olarak artık profil ekranı, duygu grafiği görüntüleme butonu ve sesli günlük başlatma özelliği entegre edildi.
- Günlük gönderimi sonrası:
    - Duygu analizi yapılır
    - Yorum ve kişiselleştirilmiş öneriler otomatik olarak sunulur
- **Yeni Özellik:** Kullanıcılar isterlerse günlüğü **sesli olarak** da kaydedebilir. Mikrofon simgesi ile başlayan bu işlem, sesi metne dönüştürerek duygu analizi sürecine dahil eder.
- Sayfaya güncellemeler yapılabilir.

##### 🔹 Duygu Değişim Grafiği
<img src="https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/Sprint2/duygugrafi%C4%9Fi.png" alt="Emotery Logo" width="500" style="display: block; margin: 0;" />

**Açıklama:**  
- Bu ekran, kullanıcının geçmiş günlüklerine göre zaman içerisindeki **duygu durum değişimini görsel olarak analiz etmesini** sağlar.
- Grafikte her veri noktası, kullanıcının o günkü ruh halini ve tarih-saat bilgisini temsil eder.
- Kullanıcı, grafik üzerinden **hangi zaman aralığında hangi duyguyu hissettiğini** kolayca gözlemleyebilir.
- Bu ekran, kullanıcının kendini tanımasına ve zaman içindeki ruh hali dalgalanmalarını fark etmesine destek olur.

##### 🔹 Kullanıcı Profili 
<img src="https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/Sprint2/kullaniciprofili.png" alt="Emotery Logo" width="500" style="display: block; margin: 0;" />

**Açıklama:**  
- Bu ekran, kullanıcının kendisine ait istatistikleri ve günlük kullanım geçmişini görüntüleyebilmesini sağlar.
- **Kayıt Tarihi**, toplam günlük sayısı ve en sık hissedilen duygu gibi kişisel veriler özetlenmiştir.  
- "Günlük Takvimi" bölümü, ilerleyen sprintlerde entegre edilecek takvimsel geçmiş özelliği için ayrılmıştır.(opsiyonel)
- Bu ekran, kullanıcıya duygusal farkındalık kazandırmak ve uzun vadeli gelişimini takip etmesine yardımcı olmak amacıyla tasarlanmıştır.
- Bu sayfa daha fazla geliştirilcek.

</details>
</details>

<details>
<summary>🔹 Sprint 3 </summary>

### 📝 Sprint Hedefi
Bu sprintin amacı, kullanıcıların geçmiş günlüklerini detaylı şekilde görüntüleyebilmesi, takvim üzerinden hangi günlerde hangi duyguların girildiğini takip edebilmesi, motivasyon sözleri ile kullanıcı etkileşimini artırmak, gelişmiş duygu rehberi ile duyguların anlamlarını öğrenebilmesi ve profil ekranındaki istatistiklerin geliştirilmesi ile kullanıcıya daha kapsamlı bir deneyim sunmaktır. Ayrıca arayüz karanlık tema ile modernize edilmiştir.

---

### 🎯 Sprint 3 Planlanan Puanlar
Toplam hedef: **28 story points**

## Sprint 3 — ~28 puan
| Görev / Özellik                         | Story Points | Açıklama                                                                                  |
|------------------------------------------|--------------|------------------------------------------------------------------------------------------|
| Günlük detay görüntüleme ve düzenleme    | 5            | Kullanıcıların geçmiş günlüklerini detaylı görmesi ve düzenleyebilmesi                    |
| Duygu takvimi entegrasyonu               | 5            | Takvim üzerinden hangi günlerde hangi duygu girildiğinin görüntülenmesi                   |
| Motivasyon sözleri modülü                | 4            | Kullanıcıya her gün farklı motivasyon sözleri gösterilmesi                                |
| Gelişmiş duygu rehberi                    | 4            | Duyguların anlamlarının ve etkilerinin kullanıcıya gösterilmesi                           |
| Profil ekranı istatistik geliştirmeleri  | 5            | Ortalama ruh hali, en sık hissedilen duygu, toplam günlük sayısı                         |
| Arayüz iyileştirmeleri ve karanlık tema | 5            | Profil sayfası ve takvim kısmı için UI düzenlemeleri                                     |

---

### 📅 Daily Scrum Süreci
Bu sprintte yine bireysel geliştirme süreci takip edildi.  
Her sabah Trello’daki **To Do** görevleri gözden geçirilerek günlük plan yapıldı.  
Frontend tarafında arayüz iyileştirmeleri tamamlandıktan sonra backend API entegrasyonları yapıldı.  
Tamamlanan görevler her gün **In Progress → Done** olarak güncellendi.

---

### 🔄 Sprint Board Güncellemeleri
Trello sprint 3 panosu aşağıdaki başlıklarla oluşturulmuştur:

- **Rejected**:Sprint 3'te tamamlamaktan vazgeçilen görevler
- **Backlog**: Sprint 3’te planlanan yeni görevler    
- **Done**: Tamamlanan işlevler (koda entegre edildi ve test edildi)  

📌 Örnek **Sprint 3 Done User Stories**:
- Kullanıcı geçmiş günlüklerini **detay modali** ile görüntüleyebiliyor
- Günlükler **düzenlenip silinebiliyor**
- Takvim üzerinden hangi günlerde hangi duygular girildiği görülebiliyor
- Motivasyon sözleri **her gün ana sayfada** gösteriliyor
- Profil ekranında **toplam günlük sayısı, ortalama ruh hali, en sık duygu bilgisi** görüntüleniyor
- Arayüz **karanlık tema desteğiyle** geliştirildi

---

### 🖼️ Görsel: Trello Sprint Board 

<img src="https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/Sprint3/Sprint3.png" width="1000"/>

---

### ✅ Sprint Review
Sprint sonunda hedeflenen tüm özellikler tamamlandı:
- Günlük detay görüntüleme ekranı eklendi (**modal yapı ile**)  
- Takvim üzerinden günlük geçmişi erişilebilir hale geldi  
- Motivasyon sözleri modülü eklendi  
- Profil ekranına **istatistik ve ortalama ruh hali** bilgileri eklendi  
- Duygu rehberi ile tüm duyguların anlamları kullanıcıya sunuldu  
- UI **karanlık tema ile modernize** edildi  

---

### 🔁 Sprint Retrospective

#### Güçlü Yönler
- Kullanıcı deneyimi tasarımı ciddi ölçüde iyileştirildi
- Takvim ve günlük detay entegrasyonu kullanıcı deneyimini güçlendirdi
- Motivasyon sözleri kullanıcı etkileşimini artırdı
- Profil ekranındaki istatistikler kullanıcıya kendi gelişimini takip etme fırsatı verdi
- Sesli giriş desteğiyle kullanıcı etkileşimi artırıldı
- Veritabanı yapısı daha sürdürülebilir hale getirildi
- Kullanıcı profili ile kişisel veriler ve geçmiş öneriler erişilebilir kılındı
- Günlük metin girişleri artık veritabanına güvenli biçimde kaydediliyor ve daha sonra analiz edilebiliyor

#### Geliştirilmesi Gerekenler
- Tek geliştirici olarak tüm süreçleri yürütmek, bazı görevlerin zamanında tamamlanmasını zorlaştırabiliyor → Zaman yönetimi daha planlı yapılabilir
- Sesli girişte bazı tarayıcılarda uyumsuzluklar gözlemlendi
- Kullanıcı profil ekranı görsel olarak yeterince kişiselleştirilmiş değil, detaylandırılabilir
- Motivasyon sözleri veri seti genişletilebilir
- Takvimde filtreleme özellikleri (belirli duyguya göre arama) eklenebilir
- Duygu rehberi daha interaktif hale getirilebilir
- Gelecek sprintlerde bildirim sistemi ve gelişmiş kullanıcı takibi planlanmalı
- Veritabanı yapısı SQLite olarak kalmaya devam ediyor → Canlı sistemler için PostgreSQL geçişi planlanmalı
- Chatbot entegrasyonu ilerleyen aşamalara bırakıldı
- Gelişmiş öneri sistemi ileriki versiyonlarda ele alınmalı

---

### 📌 Genel Kapanış & Sonuç
3 sprint sonunda **Emotery uygulaması** şu duruma gelmiştir:

**Temel İşlevler**  
✅ Günlük ekleme, düzenleme, duygu analizi  
✅ Grafik ile ruh hali takibi  
✅ Takvim entegrasyonu  
✅ Profil istatistikleri  
✅ Motivasyon sözleri modülü  

**UI/UX**  
🎨 Modern ve responsive arayüz  
🌙 Karanlık tema desteği eklendi  

**Teknik Altyapı**  
🗄️ SQLite üzerinde çalışıyor  
➡️ PostgreSQL geçişi yapılmalı 

**Eksikler / Sonraki Adımlar**  
⚠️ Bildirim sistemi  
⚠️ Chatbot entegrasyonu  
⚠️ Daha gelişmiş öneri sistemi  
➡️ Bu özellikler daha sonra geliştirilebilir.

<details>
<summary><strong>📎 Belgeler ve Ekler</strong></summary>

#### 📸 Uygulama Arayüzü

---

##### 🔹 Ana Sayfa (Günlük Ekleme + Motivasyon Sözleri)  
![Ana Sayfa](https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/Sprint3/sayfa1.png)  

**Açıklama:**  
- Ana sayfa artık günlük ekleme alanına ek olarak **günlük motivasyon sözlerini** de göstermektedir.  
- Motivasyon sözleri her gün yenilenir ve kullanıcıya olumlu bir başlangıç yapması için destek olur.  
- **Yeni günlük**, **grafik butonu** ve **profil bağlantısı** korunarak modern bir tasarım sunulmuştur.
  
---

##### 🔹 Profil Sayfası (İstatistikler + Duygu Rehberi + Takvim)  
![Profil Sayfası](https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/Sprint3/sayfa2.png)  

**Açıklama:**  
- Profil sayfası Sprint 3 ile **ortalama ruh hali**, **en sık hissedilen duygu** ve **toplam günlük sayısı** gibi istatistiklerle geliştirilmiştir.  
- **Takvim entegrasyonu** ile kullanıcı hangi gün hangi duyguyu girdiğini görebilir.  
- **Gelişmiş Duygu Rehberi** ile tüm duyguların anlamları ve etkileri kullanıcıya sunulmaktadır.  
- Arayüz, karanlık tema ile daha profesyonel bir görünüm kazanmıştır.  

---

##### 🔹 Tüm Günlükler (Detay Görüntüleme & Düzenleme)  
![Tüm Günlükler](https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/Sprint3/sayfa4.png)  

**Açıklama:**  
- Kullanıcı artık tüm günlüklerini liste halinde görebilir.  
- Her günlüğe tıklayarak **detay modalı** ile içeriğini inceleyebilir.  
- Günlükler **düzenlenebilir veya silinebilir** hale gelmiştir.  
- Düzenleme sonrası veritabanı otomatik güncellenir.  

---

##### 🔹 Motivasyon Sözleri Modülü  
![Motivasyon Sözleri](https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/Sprint3/sayfa5.png) 

**Açıklama:**  
- Her gün kullanıcıya rastgele seçilmiş bir motivasyon sözü gösterilir.  
- Bu sözler veri tabanındaki hazır motivasyon listesi üzerinden çekilir.  

---

##### 🔹 Günlük Detayı Modal (Takvim Entegrasyonu ile)  
![Günlük Detayı Modal](https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/Sprint3/sayfa6.png) 

**Açıklama:**  
- Takvimden seçilen bir güne tıklandığında o güne ait tüm günlükler modal pencerede görüntülenebilir.  
- Kullanıcı burada günlüğü **okuyabilir, düzenleyebilir veya silebilir**.  
- Modal yapısı kullanıcı deneyimini artırmak için sade bir şekilde tasarlanmıştır.  

</details>
</details>

## 🤖 Yapay Zeka Kullanımı

Emotery uygulaması, kullanıcıların duygularını anlamlandırmasına ve kişiselleştirilmiş öneriler almasına yardımcı olmak için yapay zeka tabanlı doğal dil işleme (NLP) tekniklerinden yararlanmaktadır.

### 📌 Kullanılan AI Bileşenleri

- **Google Gemini 2.5 Pro (LangChain ChatGoogleGenerativeAI ile)**
  - Kullanıcı günlük metinlerinden tek kelimelik **duygu etiketi** çıkarır.
  - Empatik bir **yorum** üretir.
  - Kullanıcıya uygun **3 kişiselleştirilmiş öneri** sunar.
  
- **SentenceTransformer (all-MiniLM-L6-v2)**
  - Günlük metinlerini **vektör embedding**’lerine dönüştürerek benzer ruh halleri arasındaki ilişkileri tespit eder.
  
- **ChromaDB**
  - AI tarafından üretilen embedding’ler **vektör veritabanında** saklanır.
  - Geçmiş duygu kayıtlarına hızlı erişim ve öneri sisteminin gelecekte gelişmesi için altyapı sağlar.

### 🔍 Çalışma Prensibi
1. Kullanıcı bir günlük girdisi yazar veya sesli olarak ekler.  
2. Metin **Gemini AI** ile analiz edilir:
   - Tek kelimelik bir **duygu etiketi** belirlenir.
   - Kısa bir **yorum** oluşturulur.
   - Kullanıcıya uygulanabilir **3 öneri** üretilir.
3. Bu bilgiler **profil, takvim ve istatistik ekranlarına** entegre edilir.

### 🎯 AI Kullanım Amacı
- Kullanıcıya **daha anlamlı geri bildirimler** sunmak.
- Uzun vadede **kişiselleştirilmiş öneri sistemi** geliştirmek.
- Duygu farkındalığını artırarak kullanıcı deneyimini güçlendirmek.

---

## 🎥 Proje Tanıtım Videosu

<div align="center">
  <a href="https://youtu.be/y9eVmjq9ohc" target="_blank">
    <img src="https://github.com/iremuslu/Bootcamp-AI209/blob/main/images/emoterykapak.png" alt="Emotery Tanıtım Videosu" style="width:100%; height:auto;">
  </a>
</div>

---

## 📝 Jüriye Not 

Proje sürecinde takım arkadaşlarımdan süreç boyunca geri dönüş alamadığım için **geliştirmeleri tek başıma yürüttüm**. Bu durum zaman yönetimini daha kritik hale getirdi ve öncelikleri doğru belirlemeyi gerektirdi.  

**Sprint 1**’de uygulamanın temel işlevleri (kullanıcı kayıt/girişi, günlük girişi, duygu analizi ve öneri sistemi) hayata geçirildi. Öneri sistemi temel haliyle çalışmakta ancak doğruluk oranı sonraki sprintlerde geliştirilmek üzere planlandı.  

**Sprint 2**’de kullanıcı deneyimini iyileştiren grafikler, sesli giriş ve profil sayfası eklendi. Veritabanı yapısı sürdürülebilir hale getirildi ancak canlı sistemler için PostgreSQL geçişi bir sonraki aşamaya bırakıldı.  

**Sprint 3** ile birlikte takvim entegrasyonu, gelişmiş profil istatistikleri, motivasyon sözleri, duygu rehberi ve karanlık tema gibi kullanıcı deneyimini artıran özellikler başarıyla tamamlandı.  

**Sonuç olarak** Emotery uygulaması;  
✅ **Temel işlevleri tam çalışan, modern arayüze sahip** bir duygu takibi ve farkındalık platformu haline gelmiştir.  
⚠️ **Geliştirme fırsatları**: Bildirim sistemi, chatbot entegrasyonu, gelişmiş öneri algoritmaları ve veri tabanı geçişi gibi alanlar ilerleyen sürümlerde ele alınacaktır.  

---


