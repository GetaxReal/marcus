import nextcord, json, datetime, string, random
from nextcord.ext import commands
from setting import tokens, roleadmin, genkeychannel, genkeylog, redeemlog, img, howtouselink, userhost, passhost, websitesellkey, sellerlog, apiddns, subdomain, tokenscf, nameshop

import requests
import os.path, os
from ftplib import FTP, error_perm
from os import system 





def create_dns(domainname):
    headers = {
        'X-Auth-Email': 'airrarae@gmail.com',
        'Authorization': f'Bearer {tokenscf}',
        'Content-Type': 'application/json',
    }
    json_data = {
        'type': 'A',
        'name': domainname,
        'content': '5.196.246.116',
        'ttl':  1,
        'proxied': True,
        'comment': 'This dns create by RESELL bot',
    }
    response = requests.post(
        'https://api.cloudflare.com/client/v4/zones/'+str(apiddns)+'/dns_records',
        headers=headers,
        json=json_data,
    )

def get_login():
    s = requests.Session()
    url = "https://5.196.246.116:2222/api/login"
    payload = json.dumps({
        "username": userhost,
        "password": passhost
    })
    headers = {
        'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78',
        'sec-ch-ua-platform': '"Windows"'
    }
    res = s.post(url, data=payload , headers=headers, verify=False)
    return res.cookies.get_dict() 

def create_subdomain(domainname,cookie):
    url = "https://5.196.246.116:2222/CMD_DOMAIN"

    payload='action=create&domain='+str(domainname)+f'{subdomain}&php=ON&ssl=ON&ubandwidth=unlimited&uquota=unlimited'
    headers = {
        'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Cookie': 'session='+str(cookie),
        'Referer' : 'https://5.196.246.116:2222/'
    }
    response = requests.request("POST", url, headers=headers, data=payload , verify=False)
    
def create_sql(domainname,cookie):
    
    url = "https://5.196.246.116:2222/CMD_DB"
    payload=f'action=create&create=Create&domain=jaonaish{subdomain}&fakepasswordremembered=&fakeusernameremembered=&name='+str(domainname)+'&passwd=@'+str(domainname)+f'_{userhost}&passwd2=@'+str(domainname)+f'_{userhost}&user='+str(domainname)+'&userlist=...'
    headers = {
        'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'https://5.196.246.116:2222/',
        'Cookie': 'session='+str(cookie)
    }
    response = requests.request("POST", url, headers=headers, data=payload,verify=False)
    
def upload_web(domainname , version):
    domain = domainname
    # clean up
    host = '5.196.246.116'
    port = 21
    ftp = FTP()
    ftp.connect(host,port)
    ftp.login(userhost,passhost)
    filenameCV = str(version)+"/"
    directory = '/domains/'+str(domain)+f'{subdomain}/public_html/'  

    # delete files in dir
    files = list(ftp.nlst(directory))
    for f in files:
        if f[-3:] == "/.." or f[-2:] == '/.': continue
        try:
            ftp.delete(f)   
        except:
            continue
    ftp.quit()
    if version == "web":
        php = '''
        <?php
            session_start();
            $host = "localhost";
            $db_user = "'''+str(userhost)+'''_'''+str(domain)+'''";
            $db_pass = "@'''+str(domain)+f'''_{userhost}";
            $db =  "'''+str(userhost)+'''_'''+str(domain)+'''";
            //connect to database
            $conn = new PDO("mysql:host=$host;dbname=$db",$db_user,$db_pass);
            $conn->exec("set names utf8mb4");
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            //end connect to database
            //function query
            function dd_q($str, $arr = []) {
                global $conn;
                try {
                    $exec = $conn->prepare($str);
                    $exec->execute($arr);
                } catch (PDOException $e) {
                    return false;
                }
                return $exec;
            }
            //end function query

            //function check login
            function check_login(){
                if(!isset($_SESSION['id'])){
                    return false;
                }else{
                    return true;
                }
            }
            function checknull($var = []){
                foreach ($var as $key => $value) {
                    if($value == "" || empty($value) || !isset($value)){
                        return false;
                    }
                }
                return true;
            }
            $conf['sitekey'] = "6LdmDFkkAAAAAEKni0zQPY4MEtv2nxLodGLEQvVO";
            $conf['secretkey'] = "6LdmDFkkAAAAAAFYBGr37VPuRl-L1hfwraFwO5pW";
            function base_url(){
                return "";
            }
        ?>
        '''
        f = open(str(version)+"/system/a_func.php", "w")
        f.write(php)
        f.close()
    host = '5.196.246.116'
    port = 21
    ftp = FTP()
    ftp.connect(host,port)
    ftp.login(userhost,passhost)
    filenameCV = str(version)+"/"
    ftp.cwd('/domains/'+str(domain)+f'{subdomain}/public_html')
    def placeFiles(ftp, path):
        for name in os.listdir(path):
            localpath = os.path.join(path, name)
            if os.path.isfile(localpath):
                print("STOR", name, localpath)
                ftp.storbinary('STOR ' + name, open(localpath,'rb'))
            elif os.path.isdir(localpath):
                print("MKD", name)
                try:
                    ftp.mkd(name)
                # ignore "directory already exists"
                except error_perm as e:
                    if not e.args[0].startswith('550'): 
                        raise

                print("CWD", name)
                ftp.cwd(name)
                placeFiles(ftp, localpath)           
                print("CWD", "..")
                ftp.cwd("..")
    placeFiles(ftp, filenameCV)
    ftp.quit()

def upload_sql(domainname ,version):
    url = "https://overdrivecloud.xyz/secret_api_ovdc_only/add_backend.php"
    payload=f'db_user={userhost}_'+str(domainname)+'&db_pass=@'+str(domainname)+'_'+str(userhost)+'&version='+str(version)+f'&db_name={userhost}_'+str(domainname)+'&auth=ovdc_expert_token_to_use_this_api'
    headers = {
        'User-Agent': 'ovdc_expert_token_to_use_this_api',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.request("POST", url, headers=headers, data=payload)

def set_admin(shopname , username):
    url = "https://overdrivecloud.xyz/secret_api_ovdc_only/add_admin.php"
    payload=f'db_user={userhost}_'+str(shopname)+'&db_pass=@'+str(shopname)+'_'+str(userhost)+f'&db_name={userhost}_'+str(shopname)+'&auth=ovdc_expert_token_to_use_this_api&user='+str(username)
    headers = {
        'User-Agent': 'ovdc_expert_token_to_use_this_api',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


bot = commands.Bot(command_prefix = "rs!", help_command = None, intents = nextcord.Intents.all())

class control_modal(nextcord.ui.Modal):

   def __init__(self):
        super().__init__("ทดสอบ")
        self.e = nextcord.ui.TextInput(
            label = "กรอก",
            placeholder = "กรอก",
            style = nextcord.TextInputStyle.short,
            required = True
        )
        self.add_item(self.e)


class main_modal(nextcord.ui.Modal):

   def __init__(self):
        super().__init__("โปรดกรอกข้อมูลให้ครบถ้วน")
        self.a = nextcord.ui.TextInput(
            label = "กรอกคีย์",
            placeholder = "ใส่คีย์ของคุณ",
            style = nextcord.TextInputStyle.short,
            required = True
        )
        self.add_item(self.a)

        self.b = nextcord.ui.TextInput(
            label = "กรอกชื่อเว็บไซต์",
            placeholder = "ใส่ชื่อเว็บไซต์ของคุณ ตัวอย่าง univezshop",
            style = nextcord.TextInputStyle.short,
            required = True
        )
        self.add_item(self.b)

        # self.c = nextcord.ui.TextInput(
        #  label = "ชื่อผู้ใช้",
        #  placeholder = "เอาไว้เข้าหลังบ้าน",
        #  style = nextcord.TextInputStyle.short,
        #  required = True
        # )
        # self.add_item(self.c)

        # self.d = nextcord.ui.TextInput(
        #     label = "รหัสผ่าน",
        #     placeholder = "เอาไว้เข้าหลังบ้าน",
        #     style = nextcord.TextInputStyle.short,
        #     required = True
        # )
        # self.add_item(self.d)

   async def callback(self, interaction: nextcord.Interaction):
      key = self.a.value.strip()
      r = json.load(open('./db/keys.json'))
      if key in r:
         if r[key]['redeem'] == False:
            r[key]['redeem'] = True
            r[key]['redeem-by'] = str(interaction.user.id)
            r[key]['redeem-time'] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            json.dump(r, open("./db/keys.json", "w"), indent = 4)
            await interaction.user.add_roles(nextcord.utils.get(interaction.user.guild.roles, id = int(r[key]['role'])))
            await interaction.response.send_message(embed = nextcord.Embed(title = 'สำเร็จ', description = 'รีดีมสำเร็จ หากคุณไม่ได้รับยศโปรดติดต่อแอดมิน', color = nextcord.Color.from_rgb(255,176,245), timestamp = datetime.datetime.now()), ephemeral = True)
            await bot.get_channel(redeemlog).send(embed = nextcord.Embed(title = 'redeem', description = f'Website : https://{self.b.value}{subdomain}/\nUser : <@{interaction.user.id}>\nRole : <@&{r[key]["role"]}>\nKey : {key}', color = nextcord.Color.from_rgb(255,176,245), timestamp = datetime.datetime.now()))
            link = "https://"+self.b.value+f"{subdomain}/"
            embedwait = nextcord.Embed(color=0x3151F7,description= "``🕐`` ``|``โปรดรอสักครู่กำลังสร้างเว็บไซต์")
            await interaction.send(embed=embedwait, ephemeral = True)
            cookie = get_login()
            create_dns(self.b.value)
            create_sql(self.b.value,cookie['session'])
            upload_sql(self.b.value,"x2winskywebv1")
            create_subdomain(self.b.value,cookie['session'])
            upload_web(self.b.value, "web")

            print("[LOG INFO] : CREATE WEB FOR "+str(link))
            embed = nextcord.Embed(title="RESELL OVERBOT | สร้างเว็บ", url=link, description="สร้างเว็บไซต์สำหรับ "+str(link)+" สำเร็จ", color=nextcord.Color.green())
            embed.set_thumbnail(url="https://media.nextcordapp.net/attachments/1035215878721122395/1066327239630798909/logo.png")
            await interaction.user.send(embed=embed)
         
            usersql = f"{userhost}_"+str(self.b.value)
            passsql = "@"+str(self.b.value)+f"_{userhost}"
            embed = nextcord.Embed(title="RESELL OVERBOT | สร้างเว็บ", url=link, description="สร้างเว็บไซต์สำหรับ "+str(link)+" สำเร็จ", color=nextcord.Color.green())
            embed.set_thumbnail(url="https://media.nextcordapp.net/attachments/1035215878721122395/1066327239630798909/logo.png")
            embed.add_field(name="DB_USER", value=usersql, inline=True)
            embed.add_field(name="DB_PASS", value=passsql, inline=True)
            embed.add_field(name="Website Link", value= link, inline=False)
            await bot.get_channel(sellerlog).send(embed=embed)
            

         else:
            await interaction.response.send_message(embed = nextcord.Embed(title = 'ไม่สำเร็จ', description = 'คีย์ถูกใช้ไปแล้ว', color = nextcord.Color.from_rgb(255,176,245), timestamp = datetime.datetime.now()), ephemeral = True)
      else:
         await interaction.response.send_message(embed = nextcord.Embed(title = 'ไม่สำเร็จ', description = 'ไม่พบคีย์ในระบบ', color = nextcord.Color.from_rgb(255,176,245), timestamp = datetime.datetime.now()), ephemeral = True)







class main_view(nextcord.ui.View):

    def __init__(self):
        super().__init__(timeout = None)
        self.add_item(nextcord.ui.Button(style = nextcord.ButtonStyle.link, url = howtouselink, label = "วิธีการใช้งาน"))
        @nextcord.ui.button(label = 'วิธีการใช้งาน', style = nextcord.ButtonStyle.link, custom_id = 'วิธีการใช้งาน', emoji = '📜')
        async def how_to_use(self, button: nextcord.Button, interaction: nextcord.Interaction):
            pass

        self.add_item(nextcord.ui.Button(style = nextcord.ButtonStyle.link, url = websitesellkey, label = "เว็บซื้อคีย์"))
        @nextcord.ui.button(label = 'เว็บซื้อคีย์', style = nextcord.ButtonStyle.link, custom_id = 'เว็บซื้อคีย์', emoji = '🌐')
        async def websitesell(self, button: nextcord.Button, interaction: nextcord.Interaction):
            pass

    @nextcord.ui.button(label = 'กรอกคีย์เปิดเว็บ', style = nextcord.ButtonStyle.green, custom_id = 'กรอกคีย์เปิดเว็บ', emoji = '💸')
    async def redeem(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await interaction.response.send_modal(main_modal())


system('cls')

@bot.event
async def on_ready():
   bot.add_view(main_view())
   print(f'''
   [LOGIN] : {bot.user}
   [SHOP] : {nameshop}
   [HOST] : {userhost} ''')
   await bot.change_presence(activity = nextcord.Game(name=f"{nameshop} | Class Univez"))

@bot.slash_command(name = 'setup', description = '(admin)')
async def setup(interaction: nextcord.Interaction):
   if nextcord.utils.get(interaction.user.guild.roles, id = roleadmin) in interaction.user.roles :
      await interaction.response.send_message(content = 'สำเร็จ', ephemeral = True)
      embed = nextcord.Embed(title = "🔑 สามารถ Redeem key ได้ที่นี่", description = f'{nameshop} บริการปล่อยเช่าเว็บราคาถูก', color = nextcord.Color.from_rgb(0,243,113))
      embed.set_image(url = img)
      await interaction.channel.send(embed = embed, view = main_view())
   else:
      await interaction.response.send_message(embed = nextcord.Embed(title = 'ไม่สำเร็จ', description = 'คุณไม่มียศ', color = nextcord.Color.from_rgb(0,243,113), timestamp = datetime.datetime.now()), ephemeral = True)

@bot.slash_command(name = 'control', description = '(admin)')
async def control(interaction: nextcord.Interaction):
    if nextcord.utils.get(interaction.user.guild.roles, id = roleadmin) in interaction.user.roles :
        await interaction.response.send_message(content = 'สำเร็จ', ephemeral = True)
        await interaction.channel.send(view = control_view())
    else:
        await interaction.response.send_message(embed = nextcord.Embed(title = 'ไม่สำเร็จ', description = 'คุณไม่มียศ', color = nextcord.Color.from_rgb(0,243,113), timestamp = datetime.datetime.now()), ephemeral = True)


@bot.slash_command(name = 'genkey', description = 'สร้างคีย์(admin)')
async def genkey(interaction: nextcord.Interaction, amount: int, role: nextcord.Role):
    if nextcord.utils.get(interaction.user.guild.roles, id = roleadmin) in interaction.user.roles :
        if interaction.channel.id == genkeychannel:
            message = await interaction.response.send_message(embed = nextcord.Embed(title = 'กำลังสร้างคีย์', description = '', color = nextcord.Color.from_rgb(0,243,113), timestamp = datetime.datetime.now()), ephemeral = True)
            all_key = ""
            for i in range(int(amount)):
                r = json.load(open('./db/keys.json'))
                key = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + "-" + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + "-" + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
                if not key in r:
                    all_key += key + "\n"
                    r[key] = {
                        "key": str(key),
                        "role": str(role.id),
                        "redeem": False,
                        "redeem-by": None,
                        "redeem-time": None,
                        "gen-by": str(interaction.user.id),
                        "gen-time": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                    }
                    json.dump(r, open("./db/keys.json", "w"), indent = 4)
                    await message.edit(embed = nextcord.Embed(title = 'กำลังสร้างคีย์', description = f'```{key}```', color = nextcord.Color.from_rgb(0,243,113), timestamp = datetime.datetime.now()))
            await message.edit(embed = nextcord.Embed(title = 'คีย์ทั้งหมด', description = f'```\n{all_key}\n```', color = nextcord.Color.from_rgb(0,243,113), timestamp = datetime.datetime.now()))
            await bot.get_channel(genkeylog).send(embed = nextcord.Embed(title = 'gen key', description = f'User : <@{interaction.user.id}>\nRole : <@&{role.id}>\n```\n{all_key}\n```', color = nextcord.Color.from_rgb(0,243,113), timestamp = datetime.datetime.now()))
        else:
            await interaction.response.send_message(embed = nextcord.Embed(title = 'ไม่สำเร็จ', description = 'ผิดห้อง', color = nextcord.Color.from_rgb(0,243,113), timestamp = datetime.datetime.now()), ephemeral = True)
    else:
        await interaction.response.send_message(embed = nextcord.Embed(title = 'ไม่สำเร็จ', description = 'คุณไม่มียศ', color = nextcord.Color.from_rgb(0,243,113), timestamp = datetime.datetime.now()), ephemeral = True)

@bot.slash_command(name = 'removekey', description = '(admin)')
async def removekey(interaction: nextcord.Interaction, key: str):
    if nextcord.utils.get(interaction.user.guild.roles, id = roleadmin) in interaction.user.roles :
        r = json.load(open('./db/keys.json'))
        if key.strip() in r:
            del r[key]
            json.dump(r, open("./db/keys.json", "w"), indent = 4)
            await interaction.response.send_message(embed = nextcord.Embed(title = 'สำเร็จ', description = f'ลบคีย์ ```{key.strip()}```', color = nextcord.Color.from_rgb(0,243,113), timestamp = datetime.datetime.now()), ephemeral = True)
        else:
            await interaction.response.send_message(embed = nextcord.Embed(title = 'ไม่สำเร็จ', description = 'ไม่พบคีย์', color = nextcord.Color.from_rgb(0,243,113), timestamp = datetime.datetime.now()), ephemeral = True)
    else:
      await interaction.response.send_message(embed = nextcord.Embed(title = 'ไม่สำเร็จ', description = 'คุณไม่มียศ', color = nextcord.Color.from_rgb(0,243,113), timestamp = datetime.datetime.now()), ephemeral = True)

@bot.slash_command(name = 'setadmin', description = '(admin)')
async def setadmin(interaction, shopname , username): # The name of the function is the name of the command
    print("[ LOG INFO ] : SETADMIN FOR SHOP["+str(shopname)+"] USER["+str(username)+"]")
    response = json.loads(set_admin(shopname, username))
    if nextcord.utils.get(interaction.user.guild.roles, id = roleadmin) in interaction.user.roles :
        if response['message'] == "add_admin_success":
            embed=nextcord.Embed(title="RESELL OVERBOT | ตั้งแอดมิน", url="https://"+str(shopname)+f"{subdomain}", description="ตั้งแอดมินสำเร็จ "+str(shopname)+str(f"{subdomain}"), color=nextcord.Color.green())
            embed.set_thumbnail(url="https://cms-assets.tutsplus.com/cdn-cgi/image/width=850/uploads/users/523/posts/32694/final_image/tutorial-preview-large.png")
            await interaction.send(embed=embed)
        else:
            if response['message'] == "user_not_found":
                embed=nextcord.Embed(title="RESELL OVERBOT | ตั้งแอดมิน", url="https://"+str(shopname)+f"{subdomain}", description="ตั้งแอดมินไม่สำเร็จ\nรายละเอียด: ไม่เจอ user ที่กรอกมา "+str(shopname)+str(f"{subdomain}"), color=nextcord.Color.red())
                embed.set_thumbnail(url="https://png.pngtree.com/png-vector/20190228/ourmid/pngtree-wrong-false-icon-design-template-vector-isolated-png-image_711430.jpg")
            elif response['message'] == "api_error":
                embed=nextcord.Embed(title="RESELL OVERBOT | ตั้งแอดมิน", url="https://"+str(shopname)+f"{subdomain}", description="ตั้งแอดมินไม่สำเร็จ\nรายละเอียด: คำสั่ง SQL ผิดพลาด"+str(shopname)+str(f"{subdomain}"), color=nextcord.Color.red())
                embed.set_thumbnail(url="https://png.pngtree.com/png-vector/20190228/ourmid/pngtree-wrong-false-icon-design-template-vector-isolated-png-image_711430.jpg")
            await interaction.send(embed=embed)
    else:
          await interaction.response.send_message(embed = nextcord.Embed(title = 'ไม่สำเร็จ', description = 'คุณไม่มียศ', color = nextcord.Color.from_rgb(0,243,113), timestamp = datetime.datetime.now()), ephemeral = True)

@bot.slash_command(name = 'delweb', description = '(admin)')
async def del_web(interaction, domain): # The name of the function is the name of the command
    if nextcord.utils.get(interaction.user.guild.roles, id = roleadmin) in interaction.user.roles :
        link = "https://"+domain+f"{subdomain}/"
        embed=nextcord.Embed(title="RESELL OVERBOT | กำลังระงับ", url=link, description="โปรดรอสักครู่กำลังระงับเว็บไซต์สำหรับ "+link, color=nextcord.Color.purple())
        await interaction.send(embed=embed)
        cookie = get_login()
        create_dns(domain)
        create_subdomain(domain,cookie['session'])
        upload_web(domain, "del")
        print("[LOG INFO] : CREATE WEB FOR "+str(link))
        embed=nextcord.Embed(title="RESELL OVERBOT | สร้างเว็บ", url=link, description="ระงับเว็บไซต์สำหรับ "+str(link)+" สำเร็จ", color=nextcord.Color.green())
        embed.set_thumbnail(url="https://cms-assets.tutsplus.com/cdn-cgi/image/width=850/uploads/users/523/posts/32694/final_image/tutorial-preview-large.png")
        embed.add_field(name="Website Link", value= link, inline=False)
        await interaction.send(embed=embed)
    else:
        await interaction.response.send_message(embed = nextcord.Embed(title = 'ไม่สำเร็จ', description = 'คุณไม่มียศ', color = nextcord.Color.from_rgb(0,243,113), timestamp = datetime.datetime.now()), ephemeral = True)

bot.run(tokens)