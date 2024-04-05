import random

characters = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
language_options = {
    "en": {"num_passwords": "How many passwords do you want to generate? ", "password_length": "Enter your password length: ", "password": "Your password: "},
    "es": {"num_passwords": "¿Cuántas contraseñas desea generar? ", "password_length": "Ingrese la longitud de su contraseña: ", "password": "Su contraseña: "},
    "fr": {"num_passwords": "Combien de mots de passe souhaitez-vous générer? ", "password_length": "Entrez la longueur de votre mot de passe: ", "password": "Votre mot de passe: "},
    "tr": {"num_passwords": "Kaç adet şifre oluşturmak istiyorsunuz? ", "password_length": "Şifre uzunluğunu girin: ", "password": "Şifreniz: "},
    "jp": {"num_passwords": "何個のパスワードを生成しますか？ ", "password_length": "パスワードの長さを入力してください：", "password": "あなたのパスワード："},
    "zh": {"num_passwords": "您要生成多少个密码？ ", "password_length": "请输入您的密码长度：", "password": "您的密码："},
    "it": {"num_passwords": "Quante password vuoi generare? ", "password_length": "Inserisci la lunghezza della tua password: ", "password": "La tua password: "},
    "de": {"num_passwords": "Wie viele Passwörter möchten Sie generieren? ", "password_length": "Geben Sie die Länge Ihres Passworts ein: ", "password": "Ihr Passwort: "},
    "ru": {"num_passwords": "Сколько паролей вы хотите создать? ", "password_length": "Введите длину вашего пароля: ", "password": "Ваш пароль: "},
    "ko": {"num_passwords": "몇 개의 비밀번호를 생성 하시겠습니까? ", "password_length": "비밀번호 길이를 입력하세요: ", "password": "당신의 비밀번호: "},
    "ar": {"num_passwords": "كم عدد كلمات المرور التي تريد إنشاؤها؟ ", "password_length": "أدخل طول كلمة المرور الخاصة بك: ", "password": "كلمة المرور الخاصة بك: "},
    "pt": {"num_passwords": "Quantas senhas você deseja gerar? ", "password_length": "Digite o comprimento da sua senha: ", "password": "Sua senha: "},
    "nl": {"num_passwords": "Hoeveel wachtwoorden wilt u genereren? ", "password_length": "Voer de lengte van uw wachtwoord in: ", "password": "Uw wachtwoord: "},
    "sv": {"num_passwords": "Hur många lösenord vill du generera? ", "password_length": "Ange längden på ditt lösenord: ", "password": "Ditt lösenord: "},
    "fi": {"num_passwords": "Kuinka monta salasanaa haluat luoda? ", "password_length": "Syötä salasanasi pituus: ", "password": "Salasanasi: "},
    "no": {"num_passwords": "Hvor mange passord vil du generere? ", "password_length": "Skriv inn lengden på passordet ditt: ", "password": "Ditt passord: "},
    "hi": {"num_passwords": "आप कितने पासवर्ड उत्पन्न करना चाहते हैं? ", "password_length": "अपने पासवर्ड की लंबाई दर्ज करें: ", "password": "आपका पासवर्ड: "},
    "el": {"num_passwords": "Πόσους κωδικούς πρόσβασης θέλετε να δημιουργήσετε; ", "password_length": "Εισαγάγετε το μήκος του κωδικού πρόσβασής σας: ", "password": "Ο κωδικός πρόσβασής σας: "},
    "az": {"num_passwords": "Neçə şifrə yaratmaq istəyirsiniz? ", "password_length": "Şifrə uzunluğunu daxil edin: ", "password": "Sizin şifrəniz: "}
}

language = input("Choose your language (en/es/fr/tr/jp/zh/it/de/ru/ko/ar/pt/nl/sv/fi/no/hi/el/az ): ")


if language in language_options:
    num_passwords = int(input(language_options[language]["num_passwords"]))
    password_length = int(input(language_options[language]["password_length"]))

    for _ in range(num_passwords):
        password = ""
        for i in range(password_length):
            password += random.choice(characters)
        print(language_options[language]["password"], password)
else:
    print("Invalid language selection!")
