import random
import requests
from telethon import TelegramClient, events, Button
import sqlite3
import os

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

kimya = {
  'kimya':{'Hansı metal bakterisid xassəsinə malikdir?':'Gümüş','Müxtlif maddələrin qarışığından ibarət olan substansiya necə adlanır?':'Qarışıq','Kimyəvi reaksiyanın istilik effekti göstərilən kimyəvi reaksiya tənliyi necə adlanır?':'Termokimyəvi','Maddənin həll olmasının temperaturdan asılılıq qrafiki necə adlanır?':'Həllolma əyrisi','Dəmir, alüminium və natrium metallarından hansı dəyişgən valentlidir?':'Dəmir','Gümüş əşyaların qaralması hansı hadısələrə aiddir?':'Kimyəvi hadisələrə','Separatorlarda yağ südün qalan hissəsindən hansı üsul ilə ayrılır?':'Sentrifuqa üsulu ilə','Daimi komponentlərindən biri azot olan təbii qarışığı göstərin?':'Hava','Havanın tərkibindəki qazlardan hansı birinci kəşv olunub?':'Oksigen','Təbaşirin, mərmərin, əhəng daşının əsasını hansı maddə təşkil edir?':'Kalsium karbonat','Yer qabığında hansı metallar daha geniş yayılmışdır?':'Alüminium və dəmir','Tərkibində 2%-dən çox karbon, silisiumun, manqanın, fosforun və kükürdün əlavələri olan dəmir ərintisi neçə adlanır?':'Çuqun','Hansı turşu bütün canlıların əsası olan elementə malikdir?':'Karbonat turşusu','Aşağıdakı qazlardan hansı təbii birləşmə deyil: metan, dəm qazı, karbon qazı?':'Dəm qazı','Ağır maye metalı adlandırın ?':'Civə','Birinci dünya müharibəsində hansı qaz kimyəvi silah kimi istifadə olunmuşdur?':'Xlor','Dəniz kələmi hansı elemetn ilə zəngindir və onun insan organizimində çatışmazlığı qalxanabənzər vəzin xəstəliyinə səbəb olur?':'Yod','Sümük qırıldıqda sarğı qoymaq üçün tibbdə istifadə olunan kimyəvi maddənin adı nədir?':'Gips','Veneranın atmosferinin əsasını hansı qaz təşkil edir və Yerdə meyvə şirəsi almaq üçün istifadə olunur?':'Karbon qazı','Kimyəvi elementlərin simvollarını yazın: Oksigen, Nitrogen, Hidrogen, Qızıl, Gümüş':'O, N, H, Au, Ag','Birinci qrup elementlərində valent elektronları sayı hansıdır?':'1','Kimyəvi elementlərin simvollarını yazın: Kalsium, Barium, Kripton, Bor, radium':'Ca, Ba, Kr, B, Ra','Azotun simvolu hansıdır?':'N','Bir elementin atom nömrəsi 17-dir. Bu elementin kimyəvi simvolu nədir? ':'Cl','Bir elementin atom nömrəsi nədir?':'Protonların sayı','Bir elementin atom nömrəsi 11-dir. Bu elementin kimyəvi simvolu nədir?':'Na','Bir elementin atom nömrəsi 26-dir. Bu elementinnədir?':'Ca','Bir elementin atom nömrəsi 30-dur. Bu elementin kimyəvi simvolu nədir?':'Zn','Bir elementin atom nömrəsi 29-dur. Bu elementin kimyəvi simvolu nədir?':'Cu','Hansı kimyəvi element həm metal, həm də amfoterdir?':'Alüminium'
}
}

fizika = {
  'fizika':{   
    'İki nöqtə arasındakı məsafənin kvadratı ilə aralarındakı qüvvənin nisbəti hansı fizika qanununu ifadə edir: ': 'Newtonun qravitasiya qanunu','Bir cismin sürəti 10 m/s dir. 5 saniyə sonra neçə metr uzaqlığa gedir?': '50','Mənzilindən atılan bir cisim yer sürəti 50 m/s olan bir reaktiv roket tərəfindən düzgün sürətdə cəlb edilir. Roketin sürəti 200 m/s olsa, cismin sürəti necədir?':'150','Bir avtomobil 20 m/s sürətlə hərəkət edir. 4 saniyə sonra avtomobilin aldığı yolun məsafəsi necədir?':'80','Bir cisim müəyyən müddət ərzində 50 m məsafəni 2 saniyədə qat edir. Bu zaman ərzində cismin sürəti necədir?':'25','kütləsi 500 g olan bir cism düzgün sürətlə 10 m/s sürətlə hərəkət edir. Cismin kinetik enerjisi necədir?':'25','İki cism tərəfindən tətbiq edilən çəki gücü F olan və kütlələri m1 və m2 olan iki cisim arasındakı qüvvənin mənşəyi necədir?':'F = G * m1 * m2 / r²','Bir nəfərin ağırlığı 600 N-dir. Bu nəfərin kütləsi necədir? (Yer çəkisində g = 9.8 m/s² qəbul edilir.)':'61.22','Bir optik lensin odaq məsafəsi 20 sm-dir. Lensə düşən bir şəffaflığın fokus məsafəsi necədir?':'-20','Bir elektrik motoru 20 A elektrik cərəyanı ilə işləyir. Bu motorun elektrik gücü 2400 W-dur. Motorun elektrik gərginliyi necədir?':'120','Bir atomun elektronları mövcudluğu olan orbitalda hərəkət edərkən, orbitalın məsafəsi və elektronların kinetik enerjisi arasında bir əlaqə var. Bu əlaqəni ifadə edən hansı fizika qanunu var?':'Heisenberg nəzəriyyəsi','Əgər bir cisim yer cazibəsi olmayan ortamda olsaydı, onun üzərindəki qüvvələrin cəmi hansı qiyməti verərdi?':'0','Bir nöqtənin hərəkəti bir ölçüdür. Bu ölçü nədir?':'Sürət','Əgər bir cismin həcminə görə şəklində dəyişiklik edilirsə, həmin prosesə nə ad verilir?':'Deformasiya','Hava təzyiqi hansı vahidlə ölçülür?':'Pasqal','Newton ikinci qanununun məzmunu nədir?':'F = ma','Elektronların mövcudluğunu kim təsdiq edib?':'Thomson','Atomları müxtəlif elementlərə ayırma prosesi nə adlanır?':'Fisil prosesi','Elektromaqnit dalğalar hansı dairə qanunu ilə yayılır?':'Faraday','Nəticəni hesablaya bilmədən öncə, bir qurğunun bütövlükdəki hər hissəsinin fərqli sürətlərlə hərəkət etməsi tədqiq edilməsi nədir?':'Difrensiyel hesablama','Işığın üç əsas rəngi hansılardır?':'Qırmızı, yasil və mavi.','Fizikada "g" hərfləri hansı qüvvəni ifadə edir?':'Qravitasiya','İki cism arasındakı uzaqlıq artdıqca gravitasiya qüvvəsi necə dəyişir?':'Azalır','Elektronların yükləri hansı işarədədir?':'-','Elektromaqnit spektrumunda növbəti dalğa uzunluğu ölçüsü hansıdır?':'Nanometr','Elektrikli arxaların köməyi ilə istifadə edilən bir cihazın adı nədir?':'Kvark növü','İlk optik mikroskop hansı ildə yaradılmışdır?':'1590','Bir optik dəqiqə məsafəsinin ölçüsü nədir?':'saniyə','Hər hansı cism hansı hallarda potensial enerjiyə malik olur?':'Yüksəklikdə'
  }
}

riyaziyyat = {
    'riyaziyyat':{
          '8 vur 7 nə qədərdir?': '56',
'Ədədlərin harmonik ortalaması necə tapılır?': 'Reciprok hissələrinin aritmetik ortalamasının reciprok hissəsi ilə hesablanır.',
'20, 30 və 40 ədədləri arasında hansı ədəd ən böyükdür?': '40',
'3x + 5y = 16 və 2x - 3y = 4 sistemində x və y necə tapılır?': 'x = 23/13, y = -38/39',
'30 üzərindən ədədlərin cəmi necə hesablanır?': '465',
'7 dərəcəlik köklü 128 necə hesablanır?': '2 dərəcəlik kök 2',
'Sinus funksiyası necə hesablanır?': 'Qarşıt cətanın qarşısındakı üçbucaq çevrilməsi üçün istifadə olunur.',
'Bir çoxbucağın ətrafındakı açıların cəmi necə hesablanır?': '(n-2) x 180 dərəcə, burada "n" çoxbucağın tərəflərinin sayısını təmsil edir.',
'Vurma əməliyyatının qaydası nədir?': 'İki ədədin hasilini tapmaq üçün istifadə olunur.',
'18 və 24 riyallıq məhsulların ortalaması necə hesablanır?': '21 riyal','2 vur 3 nə qədərdir?': '6', '8 vur 9 nə qədərdir?': '72', '15 vur 6 nə qədərdir?': '90', '36 bölü 6 nə qədərdir?': '6', '27 bölü 9 nə qədərdir?': '3', '12 bölü 4 nə qədərdir?': '3', '9 vur 7 nə qədərdir?': '63', '10 vur 5 nə qədərdir?': '50', '25 bölü 5 nə qədərdir?': '5', '4 vur 4 nə qədərdir?': '16', '7 vur 5 nə qədərdir?': '35', '11 vur 3 nə qədərdir?': '33', '18 bölü 6 nə qədərdir?': '3', '40 bölü 8 nə qədərdir?': '5', '14 vur 2 nə qədərdir?': '28','3 üstü 4 nə qədərdir?': '81', '25 bölü 5 nədir?': '5', '16 köklü 4 nədir?': '2', '4 dərəcə nədir?': '1/16', '2 vur 2 vur 2 nə qədərdir?': '8', '5! nə qədərdir?': '120', '1/2 vur 1/3 nədir?': '1/6', '5 dərəcəsinin kosinusu nədir?': '0.996', '2m + 3n = 7, m - n = 1, m+n = ?': '4', 'ax² + bx + c = 0, a=3, b=-5, c=2, x= ?': '1, 2/3', '7² + 24² = c², c = ?': '25', 'Lim (x -> 3) x² + 4x - 9, nədir?': '18', 'cos 60 dərəcə nədir?': '0.5', '9 üstü 0 nədir?': '1', '8 dərəcə kök 2 nədir?': '2³√2','Kənardan içəri dairənin diametri necə hesablanır?': '2 * radius', 'Bir üçbucağın sahəsi necə hesablanır?': '(üçbucağın hündürlüyü * üçbucağın tərəfi) / 2', 'Düyümlər necə metrəyə çevrilir?': 'düyüm * 0.0254', 'Yarımçıq fondu necə hesablanır?': 'hər iki tərəfdən toplanan ədəd / 2', 'Orta kvadrat necə tapılır?': 'ədədlərin cəmi / ədəd sayı', 'Açıların cəməti necə hesablanır?': '180 - mərkəz açı', 'Dik üçbucağın hypotenusa necə hesablanır?': '√(a^2 + b^2)', 'Üçbucağın eşkenar kütləri necə tapılır?': '(köklü 3 * sətirin kvadrati) / 4', 'Pifaqor teoremi nəyə deyilir?': 'a² + b² = c²', 'Silindrin həcminin formulü nədir?': 'π * r^2 * h', 'Funksiyanın dərəcəsinin təyini necə edilir?': 'f(x) = ax^n',
      
    }
  
}

informatika= {
   'informatika':{
          'Vektor qrafikada əsas element nədir?': 'xətlər','Kriptoqrafiya nədi?': 'gizli yazı','Troyan nədir?': 'Virus','Virusun həyat yolu nə ilə başlayır?': 'Yoluxdurma və aktivləşmə','İnformasiyanın neçə kompleks mühafizə sistemi var?': '4','Daktiloskopiya nədir?': 'Barmaq izinə görə tanıma','HLML-də siyahılar neçə növə ayrılır?': '3','Nizamlanmış siyahılar hansı teqlə işarə olunur?': '<ol>','<u> teqi nə üçündür?': 'Veb- səhifədə mətni altxətlə yazmaq üçün','IP ünvanı neçə hissədən ibarətdir?': '4','İlk əməliyyat sistemi hansıdır?': 'MS DOS','Şəbəkə avadanlıqları neçə yerə bölünür? Və hansılardır?': '2','Neçə Şəbəkə topologiyası var? ': '3','LAN nədir?': 'Local Area Network','Python dilində funksiyanı hansı açar sözlə ifadə edirlər?': 'def','Altproqramlar neçə kateqoriyaya bölünür?': '2','Python dilində "While" nəyi bildirir?': 'Dövrü','Python dilində faiz (%) hansı hesab əməlini bildirir? ': 'Bölünmədən alınan qalıq','Alqoritmin növləri hansılardır?': 'Dövri, xətti, budaqlanan','Alqoritmdə şərti yoxlamaq üçün hansı fiqurdan istifadə olunur? ( Hansı fiqurun daxilinde şərt yoxlanılır?) ': 'Romb','Alqoritmin neçə xassəsi var? ': '4','Elektron blank nədir?': 'Form','Query language nədir?': 'Sorğu dili','Verilənlər bazasında ən çox istifadə olunan model hansıdır?': 'Relyasiya','EXCEL nədir?': ' Elektron cədvəl proqramı','Neçə növ istinad var? ': '3','Sənəddə seçilmiş mətn fraqmentini kəsmək üçün hansı düymədən istifadə olunur?': 'cut','Şərti olaraq hansı qovluqları tanıyırsınız?': 'adi və xüsusi','" .flv "nəyin uzantısıdır?': 'Video fayl','Utilitlər ...  proqramlarına aiddir.': 'Sistem','16-lıq say sistemində " D " neçədir?': '13','8-lik say sistemindən 2-lik say sisteminə keçid üçün hansı koddan istifadə olunur?': '421','Macromedia Freehand hansı proqramlara aiddir?': 'Qrafik','WinZIP hansı proqramlara aiddir?': 'Arxiv'
     
   }
  
}


client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

                                

@client.on(events.NewMessage(pattern='/ksual'))
async def send_question(event):

    kategori = random.choice(list(kimya.keys()))


    soru, cevap = random.choice(list(kimya[kategori].items()))


    await event.reply(f'{soru}')


    @client.on(events.NewMessage)
    async def check_answer(answer):
        if answer.raw_text == cevap:
            await answer.reply(f'**🏆 TƏBRIKLƏR {answer.sender.first_name},** -----------\n{soru}\n--------------**SUALINA DOĞRU CAVAB VERDINIZ🥳**')
            client.remove_event_handler(check_answer)  

@client.on(events.NewMessage(pattern='/fsual'))
async def send_question(event):
    
    kategori = random.choice(list(fizika.keys()))


    soru, cevap = random.choice(list(fizika[kategori].items()))

    await event.reply(f'{soru}')

    @client.on(events.NewMessage)
    async def check_answer(answer):
        if answer.raw_text == cevap:
            await answer.reply(f'**🏆 TƏBRIKLƏR {answer.sender.first_name},** -----------\n{soru}\n--------------**SUALINA DOĞRU CAVAB VERDINIZ🥳**')
            client.remove_event_handler(check_answer)  


@client.on(events.NewMessage(pattern='/rsual'))
async def send_question(event):

    kategori = random.choice(list(riyaziyyat.keys()))

    soru, cevap = random.choice(list(riyaziyyat[kategori].items()))
    await event.reply(f'{soru}')

    @client.on(events.NewMessage)
    async def check_answer(answer):
        if answer.raw_text == cevap:
            await answer.reply(f'**🏆 TƏBRIKLƏR {answer.sender.first_name},** -----------\n{soru}\n--------------**SUALINA DOĞRU CAVAB VERDINIZ🥳**')
            client.remove_event_handler(check_answer)  

@client.on(events.NewMessage(pattern='/isual'))
async def send_question(event):

    kategori = random.choice(list(informatika.keys()))


    soru, cevap = random.choice(list(informatika[kategori].items()))


    await event.reply(f'{soru}')


    @client.on(events.NewMessage)
    async def check_answer(answer):
        if answer.raw_text == cevap:
            await answer.reply(f'**🏆 TƏBRIKLƏR {answer.sender.first_name},** -----------\n{soru}\n--------------**SUALINA DOĞRU CAVAB VERDINIZ🥳**')
            client.remove_event_handler(check_answer)  

@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):

    response = requests.get('https://media.istockphoto.com/id/980135076/tr/vekt%C3%B6r/mezun-%C3%B6%C4%9Frenci-simgesi.jpg?s=170667a&w=0&k=20&c=SpNrEaejDnbpNGZYyJzTB7mA1OluqWZCxhcHB1oll6o=')
    photo = await client.upload_file(response.content)
    buttons = [
        [Button.url('➕ 𝐌𝐄𝐍𝐈 𝐐𝐑𝐔𝐏𝐔𝐍𝐀 𝐄𝐋𝐀𝐕𝐄 𝐄𝐓 ➕', 'https://t.me/Enodersbot?startgroup=true')],
        [Button.url('📚 𝐍𝐞𝐜𝐞 𝐢𝐬𝐭𝐢𝐟𝐚𝐝𝐞 𝐞𝐭𝐦𝐞𝐥𝐢? 📚', 'https://t.me/Enobots/24')],
        [Button.url('🗣️ 𝐊𝐚𝐧𝐚𝐥', 'https://t.me/Enobots'), Button.url('🚀 𝐃𝐞𝐬𝐭𝐞𝐤', 'https://t.me/marsdabirgun')],
        [Button.url('🤵🏻‍♂️ 𝐒𝐚𝐡𝐢𝐛𝐢𝐦 🤵🏻‍♂️', 'http://t.me/ltfl_elvin')]
    ]
    button_message = 'ㅤ\n➸ 𝐀𝐁𝐈𝐓𝐔𝐑𝐈𝐘𝐄𝐍𝐓 botuna xoş gəldin!\n\n──────────────────\nMən  müxtəlif fənlərdən sual verən ve doğru cavabı yazdığında bunu bildirən ağıllı botam 🤓\n\n☞ /ksual - Kimya sualı \n☞ /fsual  - Fizika sualı \n☞ /rsual  - Riyaziyyat sualı \n☞ /isual  - Informatika sualı\n\n➻ Qruplarda daha əyləncəli olur.'
    message = await client.send_file(
        event.chat_id, 
        file=photo, 
        caption=button_message, 
        buttons=buttons, 
        link_preview=False  )

database_file = 'chats.db'

if not os.path.exists(database_file):
    conn = sqlite3.connect(database_file)
    conn.execute('''CREATE TABLE chats (chat_id INTEGER PRIMARY KEY)''')
    conn.commit()
    conn.close()

@client.on(events.NewMessage(pattern='/reyting'))
async def get_active_chats(event):
    if event.sender.username == 'ltfl_elvin':
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()
        cursor.execute('''SELECT COUNT(*) FROM chats''')
        total_chats = cursor.fetchone()[0]
        cursor.execute('''SELECT COUNT(*) FROM chats WHERE chat_id < 0''')
        total_groups = cursor.fetchone()[0]
        total_private_chats = total_chats - total_groups
        message = f"👤 Özəl Söhbətlər: {total_private_chats}\n👥 Qrup Söhbətlər: {total_groups}"
        await event.respond(message)
        conn.close()

@client.on(events.NewMessage())
async def save_chat_id(event):
    chat_id = event.chat_id
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute('''INSERT OR IGNORE INTO chats (chat_id) VALUES (?)''', (chat_id,))
    conn.commit()
    conn.close()

@client.on(events.ChatAction)
async def remove_chat_id(event):
    chat_id = event.chat_id
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM chats WHERE chat_id = ?''', (chat_id,))
    conn.commit()
    conn.close()

@client.on(events.NewMessage(pattern='/reklam'))
async def send_message_to_all_chats(event):
    if event.sender.username == 'ltfl_elvin':
        if event.is_reply and event.message.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            if reply_msg.media:
                message = reply_msg.message or ''
                conn = sqlite3.connect('chats.db')
                cursor = conn.cursor()
                cursor.execute('SELECT chat_id FROM chats')
                chat_ids = [row[0] for row in cursor.fetchall()]
                for chat_id in chat_ids:
                    try:
                        await client.send_file(chat_id, reply_msg.media, caption=message)
                    except Exception as e:
                        print(f'Error sending message to chat_id {chat_id}: {str(e)}')
                conn.close()
            elif reply_msg.text:
                message = reply_msg.text.strip()
                conn = sqlite3.connect('chats.db')
                cursor = conn.cursor()
                cursor.execute('SELECT chat_id FROM chats')
                chat_ids = [row[0] for row in cursor.fetchall()]
                for chat_id in chat_ids:
                    try:
                        await client.send_message(chat_id, message)
                    except Exception as e:
                        print(f'Error sending message to chat_id {chat_id}: {str(e)}')
                conn.close()
            else:
                print('The message cannot be empty unless a file is provided.')


@client.on(events.NewMessage(pattern='/help'))
async def help_handler(event):
    # Send a photo message
    response = requests.get('https://media.istockphoto.com/id/980135076/tr/vekt%C3%B6r/mezun-%C3%B6%C4%9Frenci-simgesi.jpg?s=170667a&w=0&k=20&c=SpNrEaejDnbpNGZYyJzTB7mA1OluqWZCxhcHB1oll6o=')
    photo = await client.upload_file(response.content)
    # Send 5 buttons
    buttons = [
        [Button.url('➕ 𝐌𝐄𝐍𝐈 𝐐𝐑𝐔𝐏𝐔𝐍𝐀 𝐄𝐋𝐀𝐕𝐄 𝐄𝐓 ➕', 'https://t.me/Enodersbot?startgroup=true')],
        [Button.url('📚 𝐍𝐞𝐜𝐞 𝐢𝐬𝐭𝐢𝐟𝐚𝐝𝐞 𝐞𝐭𝐦𝐞𝐥𝐢? 📚', 'https://t.me/Enobots/24')],
        [Button.url('🗣️ 𝐊𝐚𝐧𝐚𝐥', 'https://t.me/Enobots'), Button.url('🚀 𝐃𝐞𝐬𝐭𝐞𝐤', 'https://t.me/marsdabirgun')],
        [Button.url('🤵🏻‍♂️ 𝐒𝐚𝐡𝐢𝐛𝐢𝐦 🤵🏻‍♂️', 'http://t.me/ltfl_elvin')]
    ]
    button_message = 'ㅤ\n➸ Kömək menyusu\n\n──────────────────\nBotu qrupunuzda istifadə etmek üçün admin etməlisiniz\n\n☞ /ksual - Kimya sualı \n☞ /fsual  - Fizika sualı \n☞ /rsual  - Riyaziyyat sualı \n☞ /isual  - Informatika sualı\n\n➻ Şikayət və təkliflər üçün: @ltfl_elvin'
    message = await client.send_file(
        event.chat_id, 
        file=photo, 
        caption=button_message, 
        buttons=buttons, 
        link_preview=False  )
              
                          
    await client.run_until_disconnected()
client.start()
client.run_until_disconnected()
