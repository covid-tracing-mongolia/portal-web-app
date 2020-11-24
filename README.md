# COVID Tracing Mongolia - Портал вэб апп

Албан ёсны, эрх бүхий байгууллагууд (ЭМЯ, УОК) болон түүний ажилчид нь энэхүү портал вэб аппыг ашиглан _Нэг Удаагийн Код_ гарган авч, COVID шинжилгээгээр эерэг гарсан хүмүүст кодыг өгсөнөөр тухайн хүмүүс уг кодыг гар утасныхаа апп дотор хийснээр өөсдөдтэй нь өнгөрсөн 14 хоногт хавьтсан хүмүүсийн гар утсанд анхааруулга очих юм. Тиймээс энэхүү вэб апп нь зөвхөн батлагдсан тохиолдлуудад, албан ёсны эрхтэй эрх бүхий ажилчид ашиглан Нэг Удаагийн Код гаргаж авах чухал хэрэгслүүр болж таарч байгаа юм. 

COVID Tracing Mongolia нь [CovidShield]((https://www.covidshield.app/)) гэсэн нээлттэй эхийн (Apache 2.0 License) төсөл дээр үндэслэн хийсэн төсөл юм. CovidShield төслийг Канада-д төвтэй Shopify компанийн сайн дурын инженерүүд зохион бүтээж, хөгжүүлсэн байдаг. COVID Tracing Mongolia-г Цар Тахалтай тэмцэж байгаа өнөө үед технологийн салбарт олон жил ажилласаны хувьд улсдаа чадах зүйлээрээ хувь нэмрээ оруулах үүднээс сайн дурын, Монгол мэргэжилтнүүд хөгжүүлсэн юм.

Холбоо барих хүсэлтэй бол: amarbayar.amarsanaa@gmail.com гэсэн хаягаар холбогдоорой.

## Жишээ

<img src="/images/1.png" width="240"><img src="/images/2.png" width="240"><img src="/images/3.png" width="240"><img src="/images/4.png" width="240">

## Техникийн Үндэс

Энэхүү портал вэб апп нь `docker-compose up` аар эсвэл өөрөө бие даасан python процесс болон ажиллах боломжтой.

- Бие даасан байдлаар ажиллуулах хүсэлтэй бол [python3](https://www.python.org/downloads/) болон өгөгдлийн сан суулгасан байх шаардлагатай. (Connection string тохиргоондоо оруулж өгөөгүй бол автоматаар SQLite өгөгдлийн сан сууна гэдгийг анхаарна уу).
- `docker-compose` ашиглахын тулд урьдчилан [Docker](https://www.docker.com/get-started) суулгасан байх шаардлагатай.

## Бэлтгэл / Тохиргоо

### Virtualenv бэлэн болгох (Python процесс байдлаар дангаар нь ажиллуулах гэж байгаа тохиолдолд)

Эхлээд [`pipenv`](https://pypi.org/project/pipenv/) суулгана. Дараа нь:

```sh
# cd into project folder
pipenv --three  # create a new virtualenv
pipenv shell    # activate virtualenv
pipenv install  # install dependencies
```

### Environment variables (хувьсагчдын тохиргоо)

Python болон Django framework дээр үндэслэн ажиллуулж буй учир эдгээр технологийн хувьд хэрэглэгдэх environment variable уудыг тохируулж өгөх хэрэгтэй болно. Ингэснээр вэб портал нь өөрөө ямар тохиргоо, горимд ажиллах вэ гэдгээ мэдэж авах юм. Хувьсагчдын утгыг оноож өгөөгүй тохиолдолд үндсэн утга нь хоосон буюу `''` эсвэл `None` гэж тооцогдоно.

<details>
<summary>Environment variable болгоны дэлгэрэнгүй тайлбар</summary>
<div>

#### App тохиргоо

- `DJANGO_ENV` (default: `development`): Энэ тохиргоо нь [`DEBUG`](https://docs.djangoproject.com/en/3.0/ref/settings/#debug) горимыг идэвхжүүлдэг бөгөөд HTTPS протоколыг заавал шаардахгүй болгодог. Ингэснээр хөгжүүлэлтийн орчинд хөгжүүлэгчид ажиллах боломжтой болно.

- `DJANGO_SECRET_KEY`: Django framework-н `SECRET_KEY` гэсэн тохиргоо. Энэ нь мэдээллийг нууцлахад хэрэглэгдэх шифрлэлтийн алгоритмд хэрэгтэй нууц түлхүүр учир энэ хувьсагчийн утга нь тааж болшгүй байх хэрэгтэй. Энэ хувьсагчийн утгыг зааж өгөөгүй тохиолдолд Djangao ажиллахгүй гэдгийг анхаарна уу. [Дэлгэрэнгүй уншихыг хүсвэл.](https://docs.djangoproject.com/en/3.0/ref/settings/#secret-key).

- `DJANGO_ALLOWED_HOSTS`: Илүү аюулгүй байдлын үүднээс энэхүү вэб аппыг тодорхой IP хаяг эсвэл domain name үүд нь мэдэгдэж байгаа газраас л ажиллахыг зөвшөөрч өгөх боломжтой. Ийм тохиолдолд тэдгээр IP хаяг эсвэл domain name үүдийг энд array байдлаар зааж өгөх боломжтой. [Дэлгэрэнгүй уншихыг хүсвэл.](https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts).

- `DJANGO_ADMINS`: Вэб апп дээр гэнэтийн алдаа гарах боломжтой. Алдаа гараад эхэлвэл тодорхой хүмүүст мэдээллэх боломжтой. Тэдгээр хүмүүсийн нэр болон имэйлийг энд бүртгүүлэн оруулж болно. Тэгсэнээр вэб апп дээр ямар нэг асуудал гарвал мэдээлэл нь тэр хүмүүст очно гэсэн үг. Энэ тохиргоог ажиллуулахын тулд имэйл сервэр ажиллуулж байх хэрэгтэй бөгөөд, түүнийгээ тусад нь холбож өгөх хэрэгтэй гэдгийг анхаарна уу. [Дэлгэрэнгүй уншихыг хүсвэл.](https://docs.djangoproject.com/en/3.0/ref/settings/#admins).

- `SU_DEFAULT_PASSWORD`: Вэб апп анхны удаа ажиллаж эхлэхэд хамгийн эхний админ эрхтэй хэрэглэгчийг (`uok_admin`) үүсгэх хэрэгтэй болно. Тэр хэрэглэгчийн нууц үг нь юу байхыг энд зааж өгнө. 

##### Өгөгдлийн сангийн тохиргоо

- `DATABASE_URL`: Өгөгдлийн санд холбогдох тохиргооны мэдээлэл. (Scheme, host, username, password болон port). Энд оноож өгсөн мэдээллийг [`dj-django-url`](https://pypi.org/project/dj-database-url/)-р уншуулж авдаг.

##### Имэйл тохиргоо

- `EMAIL_BACKEND` (default: `django.core.mail.backends.console.EmailBackend`): Имэйл тохиргоо. Production орчинд энэ хувьсагчийг:  `django.core.mail.backends.smtp.EmailBackend` гэж тохируулах хэрэгтэй.. [Дэлгэрэнгүй уншихыг хүсвэл.](https://docs.djangoproject.com/en/3.0/ref/settings/#email-backend).

- `DEFAULT_FROM_EMAIL`: Имэйлийн эх үүсвэрийн хаягийг оруулж өгнө. (Имэйл хүлээж авсан  хүмүүс хаанаас ирсэн имэйл вэ гэж харахаар энэ хаяг харагдана гэсэн үг)

Доорх хувьсагчууд зөвхөн `smtp` тохиргоотой имэйл сервэрүүдэд хамааралтай:

- `EMAIL_HOST`: Имэйл явуулах сервэр. [Дэлгэрэнгүй уншихыг хүсвэл.](https://docs.djangoproject.com/en/3.0/ref/settings/#email-host).

- `EMAIL_PORT`: EMAIL_HOST д тааруулж өгсөн сервэр дээрх порт.
  [Дэлгэрэнгүй уншихыг хүсвэл.](https://docs.djangoproject.com/en/3.0/ref/settings/#email-port).

- `EMAIL_HOST_USER`: Username. [Дэлгэрэнгүй уншихыг хүсвэл.](https://docs.djangoproject.com/en/3.0/ref/settings/#email-host-user).

- `EMAIL_HOST_PASSWORD`: Password. [Дэлгэрэнгүй уншихыг хүсвэл.](https://docs.djangoproject.com/en/3.0/ref/settings/#email-host-password).

- `EMAIL_USE_TLS` (default: `False`): TLS (secure) ашиглах эсэх. [Дэлгэрэнгүй уншихыг хүсвэл.](https://docs.djangoproject.com/en/3.0/ref/settings/#email-use-tls).

#### Backend Server-д хандах API Тохиргоо

- `API_ENDPOINT`: _Нэг Удаагийн Код_ авах хүсэлтийг илгээх backend service-н хаяг. Хэрвээ энийг тохируулж өгөөгүй тохиолдолд _Нэг Удаагийн Код_ нь `0000 0000` гэж гарч ирнэ.

- `API_AUTHORIZATION`: _Нэг Удаагийн Код_ гаргаж авах backend server-т холбогдоход хэрэглэгдэх нууц үг. Энэ буруу байгаа тохиолдолд backend service ээс `401` гэсэн алдааны код буцаж ирнэ.

#### New Relic тохиргоо

Энэхүү прожект нь New Relic ашиглан сервэр талын алдаа болон аппын ажиллагааны талаарх мэдээллийг гаргаж авдаг байдлаар тохируулсан. (Client буюу browser талын мэдээллийг бол авдаггүй). 

- `NEW_RELIC_APP_NAME`: New Relic-т бүртгэлтэй апп-н нэр..

- `NEW_RELIC_LICENSE_KEY`: New Relic-т хандахад хэрэгтэй нууц үг / лиценз.

#### OTP (2-factor) тохиргоо

Вэв апп руу албан ёсны, эрх бүхий байгууллагын (ЭМЯ, УОК...) ажилчид имэйл, нууц үгээрээ нэвтрэн ороход OTP буюу нэг удаагийн нууц үгийг утасруу нь мэссэж илгээж болдог байхаар оруулсан байгаа. (Энэ нэг удаагийн нууц үг гэдэг нь оношилгооны сервисээс авдаг _Нэг Удаагийн Код_ оос өөр гэдгийг анхаарна уу). Энэ нь зөвхөн ваб апп руу нэвтрэхэд л хэрэг болдог, тухайн ажилчныг мөн гэдгийг бататгаж байгаа аюулгүй байдлын үүднээс авч буй арга хэмжээ юм.

- `OTP_NOTIFY_ENDPOINT`: Мэссэж илгээх ажиллагааг хариуцаж буй сервисийн хаяг.

- `OTP_NOTIFY_TEMPLATE_ID`: Мэссэжний ерөнхий бүтцийг зааж өгсөн template ID. Үүнийг Notify dashboard дээр үүсгэж өгсөн байна.

- `OTP_NOTIFY_API_KEY`: Notify сервисийг ажиллуулахад хэрэгтэй нууц түлхүүр.

- `OTP_NOTIFY_NO_DELIVERY`: Зөвхөн тестийн орчинд ашиглагдана. (Notify дуудахад жинхэнэ сервис рүү хандахын оронд console дотор мэдээллийг хэвлэж харуулна).

- `OTP_NOTIFY_TOKEN_VALIDITY`: Мэссэжээр илгээсэн код нь хэдий хугацаанд хүчинтэй байхыг тохируулж өгнө. Секундээр.

[Дэлгэрэнгүй уншихыг хүсвэл.](https://django-otp-notify.readthedocs.io/en/latest/)

#### Notify тохиргоо

Notify сервис нь OTP (one time passcode) мэссэж кодыг `dhango-otp-` гэсэн plugin аар дамжуулан явуулах  боломжтой бөгөөд мөн үүгээр имэйл явуулах боломж ч байдаг. 

- `PASSWORD_RESET_EMAIL_TEMPLATE_ID_EN` : Нууц үг сэргээх хүсэлтийн хариуд явуулах имэйл ийн формат. Англи хэл дээр. (Монгол хэл дээр яг үүнтэй төстэйгээр үүсгэх боломжтой)

- `INVITATION_EMAIL_TEMPLATE_ID_EN` : Шинээр хэрэглэгч  бүртгүүлсэн тохиолдолд тухайн хэрэглэгчид очих автомат имэйлийн формат. Англи хэл дээр. Үүнийг мөн Монгол хэл дээр гаргах боломжтой.

#### Холбоо Барих 

Вэб аппын хэрэглэгчид холбоо вэб апп хийсэн, туслах үйлчилгээ үзүүлдэг операторуудтай холбоо барих хүсэлтэй бол асуух асуулт нь Freshdesk рүү орохоор тохируулах боломжтой.

- `FRESHDESK_API_KEY`: FreshDesk систем-д API түвшинд хандах түлхүүр.

- `FRESHDESK_API_ENDPOINT`: FreshDesk систем-д API түвшинд хандах `/api/v2/`-аар төгссөн хаяг.

- `FRESHDESK_PRODUCT_ID`: Freshdesk дотор нэгээс олон бүтээгдэхүүн бүртгүүлсэн байдаг бол яг хэрэгтэй бүтээгдэхүүнийхээ ID-г энд оруулж өгнө.
</div>
</details>

<strong>[Жишээ `.env` файл](https://github.com/cds-snc/covid-healthcare-portal/blob/main/portal/.env.example)</strong>

### Вэб аппыг анхныхаа удаа ажиллуулахад

**Хурдан эхлэх:** virtual environment, аа идэвхжүүлсэний дараа доорх коммандуудыг ажиллуулна:

- `pipenv run css`
- `python manage.py collectstatic --noinput -i scss`
- `entrypoint.sh` скриптийг ажиллуулж өгөгдлийн сангийн migration-г хийнэ

Ингэсний дараа вэб апп маань: `http://127.0.0.1:3000/` or `http://localhost:3000` гэсэн хаяг дээр ажиллаж байна..

Өшөө дэлгэрэнгүй, нарийн тохиргоонуудын талаар мэдээлэл авах бол дараах мэдээлэлтэй танилцана уу:

`./portal/.env.example` гэсэн файлыг хуулбарлан `./portal/.env` гэсэн нэртэй файл үүсгэн, доторх тохиргоонуудыг хийж өгнө.

#### 1. Database migrations

Ямар нэг нэмэлт тохиргоогүйгээр Django бол өөрөө SQLite өгөгдлийн сан үүсгэдэг байгаа. Гэхдээ энэхүү вэб апп нь Postgres-г хэрэглэдэг. `DATABASE_URL` гэсэн хувьсагчийн утгыг оноож өгсөн бол түүний дагуу өгөгдлийн санд холбогдох мэдээллийг аваад тохируулна гэсэн үг.

##### Postgres [URL schema](https://github.com/jacobian/dj-database-url#url-schema)

| Django Backend                  | DATABASE_URL                              |
| ------------------------------- | ----------------------------------------- |
| `django.db.backends.postgresql` | `postgres://USER:PASSWORD@HOST:PORT/NAME` |

Өгөгдлийн сангийн scheme үүсгэхэд: `python manage.py makemigrations`.

Table үүдээ үүсгэхдээ: `python manage.py migrate`.

#### 2. SCSS файлуудыг CSS болгож хөрвүүлэх

SCSS файлуудыг compile хийж `profiles/static/css/styles.css` үүсгэх хэрэгтэй.. Ингэхийн тулд:

```
pipenv run css
```

Хөгжүүлэлтийн орчинд ажиллан, оруулсан өөрчлөлтөө шууд хардаг байхыг хүсвэл `--watch` гэсэн нэмэлт тохиргоог комманддаа дамжуулж өгөх боломжтой.

```
pipenv run csswatch
```

SCSS нь комманд терминалын орчинд шинэ цонх нээхийг шаарддаг. Тиймээс та жишээ нь iTerm ашиглаж байгаа тохиолдолд, шинэ цонх нэхийн оронд шинэ таб `Command + t` эсвэл `Command + d` гэж үүсгэх боломжтой. Шинэ таб үүсгэсний дараа прожектийнхоо фолдер дотор дахин `pipenv shell` болон `pipenv install` гэсэн коммандуудыг ажиллуулахаа мартав аа.

#### 3. Гар аргаар админ хэрэглэгч (super user) үүсгэх

Вэб апп-т бүртгэлтэй байгаа хэрэглэгчдийг удирдах хэрэгцээтэй бол админ хэрэглэгч байх хэрэгтэй болно. Админы хандах эрх нь `/admin` гэсэн хаягт байна.

`/admin` гэсэн хаягаар хандахын тулд эхлээд super user аккаунт үүсгэсэн байх шаардлагатай. (Хэрвээ та `docker-compose up` ажиллуулж байгаа бол энэ аккаунт нь аль хэдийний үүссэн байна). 

Хэрвээ гар аргаар админ үүсгэх шаардлагатай бол дараах коммандыг ажиллуулна уу: `python manage.py createsuperuser`

#### 4. Хөгжүүлэлтийн орчны сервэрийг ажиллуулах

 Вэб аппыг ажиллуулахын тулд ажиллуулах комманд: `python manage.py runserver`. Дараа нь: `http://127.0.0.1:3000/` гэж browser-т хандана.

### Docker Compose ашиглан вэб аппыг ажиллуулах

> [Compose](https://docs.docker.com/compose/) нь Docker суурьтай апп уудад зориулсан, нэг комманд ажиллуулахад л бүх хэрэтэй сервисүүд тусдаа өөрийн гэсэн орчин үүсэн ажиллах боломжтой болгодог технологи юм.

Энэ вэб аппын хувьд Docker Compose -г ашиглан Postgres өгөгдлийн сантай, вэб аппыг бүрэн ажиллуулах хялбар боломжтой. Ингэснээр таны хөгжүүлэлтийн орчинд байгаа файлуудыг Docker-н орчинд оруулан, PostgreSQL өгөгдлийн санг үүсгэж, CSS compilation хийж, өгөгдлийн сангийн migration-г хийж хэрэгцээтэй scheme болон table үүдийг үүсгэх гэсэн бүх зүйлсийг өөрөө хийчихдэг гэсэн үг. Вэб апп нь `3000` гэсэн порт дээр ажиллахаар тохируулагдсан байгаа бол өгөгдлийн сан нь `5432` гэсэн порт дээр ажиллахаар тохируулагдсан байгаа.

Өмнө нь [Django, Docker, and PostgreSQL Tutorial](https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial) оролцсон апп хөгжүүлэлт хийж байгаагүй бол энэ хичээлээс харах боломжтой. 

### Run

1. Апп ажиллуулах: `docker-compose up`
2. Аппыг унтраах: `Command + c` or `docker-compose down`

### Орчуулга

Эх хэл рүү хөрвүүлэх боломжийг Django технологийн стандард сангууд бий болгож өгч байгаа. Тэгэхээр бид үүнийг ашиглан Монгол хэл рүү хөрвүүлэх ажлыг хийхээр бэлдээд байна. (Энийг уншиж байх үед хэл нь орчуулагдсан байвал орчуулгын ажлаа хийсэн мөртлөө энэ баримтаа шинэчлээгүй байна гэсэн үг юм). 

Орчуулгын ажлыг хэрхэн хийх талаар товч зааварчилгаа:

`trans` гэсэн tag ашиглан орчуулгын текстээ templare рүү нэмж өгнө.

```
# profiles/templates/profiles/start.html

<h1>{% trans "Generate code for Exposure Notification app" %}</h1>
```

Дараа нь `python manage.py makemessages -l mn` ажиллуулж `/locale` дотор байрлаж буй `django.po` гэсэн орчуулгын файлыг шинэчлэнэ.

```
# locale/mn/LC_MESSAGES/django.po

#: profiles/templates/profiles/start.html:7
msgid "Generate code for Exposure Notification app"
msgstr "Exposure Notification апп-д зориулсан кодыг үүсгэх"
```

Үүний дараа: `python manage.py compilemessages` гэж ажиллуулсанаар Django нь шинэ орчуулга орж ирсэн байна гэдгийг мэдэж аван, ашиглаж эхлэнэ гэсэн үг юм.

Илүү дэлгэрэнгүй мэдээлэл:  [Django Translation](https://docs.djangoproject.com/en/3.0/topics/i18n/translation/#translation) docs.

## Хөгжүүлэх Процесс

### Frature нэмэх / өөрчлөлт, засвар хийх

Вэб апп-д нэмэлт feature хөгжүүлэх гэж байгаа тохиолдолд  [trunk-based development](https://trunkbaseddevelopment.com/) wпроцессыг дагана. `main` branch-д байнга хамгийн сүүлийн, production-ready код байрлана гэсэн үг. Шинээр хөгжүүлэлт хийх гэж буй тохиолдолд `main` branch аас салаалуулж, хөгжүүлэлтийн ажлаа хийгээд, code review, test давсаны дараа буцаад `main` branch рүү нийлүүлнэ. Орж ирэх PR-ууд нь [автоматжуулсан тестүүдийг](https://github.com/cds-snc/covid-alert-portal#automated-tests) (unit tests, linting, etc) давдаг байх хэхрэгтэй. 

### Аппын дугаарлалт

Үндсэн түвшинд аппын дугаарлалтыг [`VERSION` файл](https://github.com/cds-snc/covid-alert-portal/blob/main/VERSION)-д хадгалж явна. Орсон өөрчлөлтүүдийг [`CHANGELOG.md` файл](https://github.com/cds-snc/covid-alert-portal/blob/main/CHANGELOG.md)-д хадгалж явна. Бидний дугаарлалтыг дагах процесс нь: [semantic versioning conventions](https://semver.org/).

Бүх PR нь дугаарлалтыг өсгөх ёстой гэсэн үг биш. Шинэ өөрчлөлтүүд болон алдааны засварууд бол зайлшгүй Changelog файлд орсон байх  ёстой. Орохдоо "Unreleased" гэсэн хэсэг доор байрлана. Аппын дугаарлалтыг өсгөх үед энэ бүх "Unreleased" гэсэн өөрчлөлтүүдийг оруулж өгөх юм.

Production руу аппыг оруулж байгаа тохиолдолд бол дугаарлалтыг заавал өсгөх шаардлагатай гэдгийг анхаарна уу. 

### Автоматжуулсан тест

Эх үүсвэрийн прожектууд бол [GitHub Actions](https://github.com/features/actions)-г CI шийдэлдээ ашигласан байгаа. Энэ нь автоматжуулсан тестүүд болон deployment-уудыг ажуллуулах үүрэгтэй. Яг одоогийн байдлаар (2020-11-22) Монголд зориулан сайн дураараа хийж байгаа энэхүү төсөлд маань GitHub Actions ажиллаж эхлээгүй байгаа бөгөөд энэ нь хийгдэх ажлын жагсаалтуудад орсон байгаа.

Тестүүдэд:

- `pipenv run test`: unit test-үүдийг ажиллуулна (Python - 3.6, 3.7, 3.8)
- `pipenv run format --check`: code consistency
- `pipenv run lint`: uses `flake8` to ensure Python style guide compliance
- Snyk (SaaS): checks for vulnerable dependencies
- LGTM (SaaS): checks for code smells and insecure coding practices
- `terraform plan`: if the terraform config has been modified, `terraform plan` will return a diff of changes between the current infrastructure and the files in the PR.
- `terraform security-scan`: will flag any unsafe configuration changes

Code Coverage бас орсон байгаа бөгөөд 80% аас доош унасан тохиолдолд тестүүд fail хийж эхлэнэ гэсэн үг. Үүнд хэрэглэгдэж буй сан нь: [`coverage`](https://coverage.readthedocs.io/en/coverage-5.3/). `coverage`-н тохиргоо нь [`pyproject.toml`](https://github.com/cds-snc/covid-alert-portal/blob/main/pyproject.toml) файл дотор байна..

- `pipenv run coverage_test`: run the unit tests to generate the report
- `pipenv run coverage_report`: display the report

---

