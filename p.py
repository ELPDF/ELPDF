from pymino import *
from pymino.ext import *
import random as rd
from translate import Translator
#from googletrans import Translator as GTranslator
import datetime as dt
import qrcode
import os
import time as tm
import pyjokes
import openai
from httpx import get
import aminofix
from PIL import Image as igmage
import requests
from pydub import AudioSegment
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube
from youtubesearchpython import VideosSearch
from threading import Thread
from free_pygpt import ClientGPT
from gtts import gTTS
from k_amino import Client as kClient
from k_amino import SubClient as kSubClient
import json
from urllib import parse, request
import Edits





email = "rainbowinfinityacounts+10@hotmail.com"
password = "123456789O"
#clientFix = aminofix.Client()
#clientFix.login(email, password)
#YohanVid = aminofix.Client()
#YohanVid.login(email="Sofiajuliadelmilagros@gmail.com", password="05Tomato05")


kc = kClient()
kc.login(email=email, password=password)

images = open("gatos.txt", "r") .read().split()
print(images)

#UTILES
def VerificacionIMG(image):
    apiurl = f'https://hyzensfw.squareweb.app/checknsfw'
    img_btes = requests.get(image).content
    file = {'image': img_btes}
    res = requests.post(apiurl, files=file).json()
    return max(res['prediction'], key=res['prediction'].get)

client_id = "8835eb66ab8d4a09a6e3a4334e029ad1"
client_secret = "7202daa01b854c5b9aa6309396071914"
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def Download(link, filename):
  yt = YouTube(link)
  yt = yt.streams.get_audio_only()
  try:
    yt.download(filename=filename)
  except:
    print("Hubo un error al descargar el video del URL proporcionado...")
  print("¡Descarga completada con éxito!")


#Ahorcado 
words = ["pene", "fototeta", "rainbow", "amino", "ganastecoins"]
def choose_word():
    return rd.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_ "
    return display




bot = Bot(command_prefix="/",community_id = 67,)

@bot.on_ready()
def ready():
	 hora_actual = dt.datetime.now().strftime('%-I:%M %p')
	 print(f"{bot.profile.username} esta en linea ({hora_actual})")



#        TRADUCTOR SE RESPONDER
#@bot.command("traducir")
#def traducir(ctx: Context):
#    info = bot.community.fetch_messages(chatId=ctx.chatId, size=1).data
#    extensions=info[0]['extensions']
#    if 'replyMessage' in extensions:
#        reply_message = info[0]['extensions']['replyMessage']['content']
#        traductor = Translator()
#        detect_result = traductor.translate(reply_message, dest='es').text
#        reply = "[IC]"+str(detect_result)
#        ctx.reply(f"{reply}")

          #ARCHIVOS
@bot.command("gato")
def gato(ctx: Context):
	comId = ctx.comId
	image = rd.choice(images)
	bot.community.send_image(comId=comId, chatId=ctx.chatId, image=image)
@bot.command("cat")
def cat(ctx: Context):
	comId = ctx.comId
	image = rd.choice(images)
	bot.community.send_image(comId=comId, chatId=ctx.chatId, image=image)
@bot.command("Gato")
def Gato(ctx: Context):
	comId = ctx.comId
	image = rd.choice(images)
	bot.community.send_image(comId=comId, chatId=ctx.chatId, image=image)
@bot.command("Cat")
def Cat(ctx: Context):
	comId = ctx.comId
	image = rd.choice(images)
	bot.community.send_image(comId=comId, chatId=ctx.chatId, image=image)

@bot.command(name="traducir", aliases=["Traducir", "td" "TD", "tD", "Td"])
def Tradi(ctx: Context, message: str):
	trad = Translator(from_lang="english", to_lang="spanish") 
	txt = ctx.message.replied.message.content
	rId = ctx.message.replied.message.messageId
	print(txt)
	res = trad.translate(txt)
	ctx.reply(res, rId)


@bot.command("audio")
def audioo(ctx: Context, message: str):
	chatId = ctx.chatId
	comId = ctx.comId
	bot.community.send_audio(audio=f"AUDIOS AMINO/audio{message}.mp3", chatId=chatId, comId=comId)
@bot.command("audior")
def audior(ctx: Context, message: str):
	chatId = ctx.chatId
	comId = ctx.comId
	aud = rd.randrange(1, 32)
	bot.community.send_audio(audio=f"AUDIOS AMINO/audio{aud}.mp3", chatId=chatId, comId=comId)

@bot.command("invocar")
def invocar(ctx: Context):
	comId = ctx.comId
	mentioned_users = ctx.message.mentioned_dictionary
	mentioned = ctx.prepare_mentions(mentioned_users)
	for i in range(5):
		ctx.send("jutsu de invocacion:  " + ", ".join(mentioned), mentioned=list(mentioned_users))

@bot.on_mod_deleted_message()
def abuso(ctx: Context, message: str):
	name = ctx.author.username
	ctx.send(f"hey no abuse de su poder, {name} no hizo nada malo \nToma tu mensajito de vuelta^^")
	ctx.reply(message)

@bot.on_vc_permission_open_to_everyone()
def join(ctx: Context):
	chatId = ctx.chatId
	comId = ctx.comId
	msj = """[C]Hola como estan
[C]^^"""
	bot.community.start_vc(chatId=chatId, comId=comId)
	bot.community.send_message(chatId=chatId, content=msj, comId=comId)

@bot.on_vc_permission_invited_and_requested()
def join2(ctx: Context):
	chatId = ctx.chatId
	comId = ctx.comId
	msj = """[C]Hola como estan
[C]^^"""
	bot.community.start_vc(chatId=chatId, comId=comId)
	bot.community.send_message(chatId=chatId, content=msj, comId=comId)

@bot.on_vc_permission_invite_only()
def join3(ctx: Context):
	chatId = ctx.chatId
	comId = ctx.comId
	msj = """[C]Hola como estan
[C]^^"""
	bot.community.start_vc(chatId=chatId, comId=comId)
	#bot.community.(chatId=chatId, content=msj, comId=comId)

@bot.on_vc_start()
def dentro(ctx: Context):
	chatId = ctx.chatId
	comId = ctx.comId
	bot.community.start_vc(chatId=chatId, comId=comId)



@bot.command("hora")
def hora(ctx: Context, message: str):
	hora_actual = dt.datetime.now().strftime('%-I:%M %p')
	ctx.send(f"Hora de mecxico>>> {hora_actual}") 




@bot.command("molestar")
def molestar(ctx: Context, message: str):
	te = 10
	inicio = tm.time()
	def fspam():
		while True:
		      	tt = tm.time() - inicio
		      	if tt >= te:
		      		break
	      		try:
	      			bot.community.follow(userId, comId)
	      			bot.community.unfollow(userId, comId)
	      		except:
	      			pass
	comId = ctx.comId
	try:
		infos = ctx.message.mentioned_dictionary
		for user_id, user_name in infos.items():
			userId = user_id
		print("93944848")
		si = 0
	except:
		si = 1
	if si==1:
		userId = bot.community.fetch_object_id(message)
		print("88383")
	for i in range(50):
		Thread(target=fspam).start()
	
@bot.command("no me sigas")
def peru(ctx: Context):
	comId = ctx.comId
	userId = ctx.message.userId
	bot.community.unfollow(userId, comId)
#@bot.command("comentar")
#def comentar(ctx: Context, message: str):
#	uid = bot.community.fetch_object_id(message)
#	for i in range(10):
#		bot.community.comment_on_profile(userId=uid, content="hola")



@bot.on_chat_tip()
def donacion(ctx: Context):
	comId = ctx.comId
	userId = ctx.author.userId
	chatId = ctx.chatId
	coins = ctx.message.extensions["tippingCoins"]
	msj = f"gracias por donar {coins} monedas {ctx.author.username}! ayudas a la anfi a pagar la (comida de los coas^^", f"Gracias por las {coins} monedas {ctx.author.username}, si a la poroxima no donas mas eres fan de kunno^^"
	msj = rd.choice(msj)
	image = rd.choice(images)
	msj2 = "a", "b", "c"
	s = rd.choice(msj2)
	if s=="a":
		bot.community.send_embed(comId=comId, chatId=ctx.chatId, title="GRACIAAS!!!", content=f"{ctx.author.username} por las {coins} coins <3", image=ctx.author.icon, link=f"ndc://user-profile/{userId}")
	elif s=="b":
		ctx.send(msj)
	elif s=="c":
		bot.community.send_embed(comId=comId, chatId=chatId, title="GRACIAAS!!!", content="Ten te regalo un gatito", image=image, link=image)


@bot.command("QR")
def QR(ctx: Context, message: str):
	comId = ctx.comId
	qr = qrcode.QRCode()
	qr.add_data(message)
	img = qr.make_image()
	name = rd.randrange(1, 100000000000000000)
	img.save(f'QRS/Amino{name}.png')
	print(f"\nTu QR Amino{name} esta creado...")
	chatId = ctx.chatId
	bot.community.send_image(image=f'QRS/Amino{name}.png', chatId=chatId, comId=comId)
	
#@bot.on_member_join()
#def member_join(ctx: Context):
#	image = rd.choice(images)
#	ctx.send_embed(title="Aqui tienes tu lindo gatito", content=f"graci:as por donar {ctx.author.username}! ayudas a la anfi a pagar la comida de su chiguagua^^", image=image)


#@bot.on_member_join()
#def bienvenida(ctx: Context):
#	comId = ctx.comId
#	userId = ctx.author.userId
#	link = bot.community.fetch_user(comId=comId, userId=ctx.userId)
#	bot.community.send_embed(comId=comId, chatId=ctx.chatId, title="BIENVENIDO!!!", content=ctx.author.nickname, image=ctx.author.icon, link=f"ndc://user-profile/{userId}")
#	openai.api_key = "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"
#	respuesta = openai.Completion.create(engine="text-davinci-003", prompt=f"da la bienvenida a {ctx.author.nickname}", max_tokens=150)
#	ctx.reply(respuesta.choices[0].text)

@bot.on_member_join()
def bienvenida2(ctx: Context):
	userId = ctx.author.userId
	iconLink = ctx.author.icon
	iconImage = requests.get(iconLink).content
	chatId = ctx.chatId
	comId = ctx.comId
	name = ctx.author.nickname
	hora_actual = dt.datetime.now().time()
	fecha = f"{hora_actual.hour}-{hora_actual.minute}-{hora_actual.second}"
	ruta = f"Edits/Bienvenidas/Creadas/UID-{userId}--CID-{chatId}--FECHA-{fecha}.jpg"
	iconName = "Edits/Icons/Descargados/UID-{userId}--CID-{chatId}--FECHA-{fecha}.jpg"
	iconFile = open(iconName, "wb")
	iconFile.write(iconImage)
	iconFile.close()
	Edits.dar_bienvenida(name=name, icon=iconName, ruta=ruta)
	bot.community.send_image(chatId=chatId, comId=comId, image=ruta)
	#bot.community.send_embed(chatId=chatId, comId=comId, link=f"ndc://user-profile/{userId}", image=ruta, content=None, title=None)
	#bot.community.send_link_snippet(chatId=chatId, comId=comId, link=f"ndc://user-profile/{userId}", image=ruta, mentioned=None, message=f"Bienvenido {name}")

#@bot.on_member_leave()
#def leave(ctx: Context):
#	ctx.send("Miren se fue por ser fan de kunno")

@bot.command("invitar")
def invitar(ctx: Context, message: str):
	comId = ctx.comId
	chatId = ctx.chatId
	uids = bot.community.									fetch_online_users(comId=comId, start=0, size=1000).userId
	bot.community.send_message(comId=comId, chatId=chatId, content="Me ban a banear por esto :(...")
	bot.community.send_message(comId=comId, chatId=chatId, content="iniciando invitacion masiva en...")
	tm.sleep(1)
	bot.community.send_message(comId=comId, chatId=chatId, content="3")
	tm.sleep(1)
	bot.community.send_message(comId=comId, chatId=chatId, content="2")
	tm.sleep(1)
	bot.community.send_message(comId=comId, chatId=chatId, content="1")
	tm.sleep(1)
	bot.community.send_message(comId=comId, chatId=chatId, content="invitacion masiva iniciada, fue un gusto conocerlos ")
	for _ in range(1000):
		bot.community.invite_chat(comId=comId, chatId=chatId, userIds=uids)
		print("invitandoooooooooo")


@bot.command("bId")
def bid(ctx: Context, message: str):
	Id = bot.community.fetch_object_id(message)
	ctx.send(f"La id es: {Id}")

@bot.command("join")
def joined(ctx: Context, message: str):
	ctx.join_chat()



@bot.command("8ball")
def ball(ctx: Context, message: str):
	respuestas = ("Si", "No", "Talvez", "No lo se")
	respuesta = rd.choice(respuestas)
	print(f"{ctx.author.username}: {message} ({respuesta})")
	ctx.reply(respuesta)

@bot.command("love")
def love(ctx: Context, message: str):
    respuesta = rd.randrange(0, 101)
    print(f"{ctx.author.username}: {message} ({respuesta}%)")
    ctx.reply(f"{respuesta}% ♡")





@bot.on_image_message()
def dimage(ctx: Context, image:str):
	 imsage = ctx.message.mediaValue
#	 resp = VerificacionIMG(imsage)
#	 print(resp)
	 msjId = ctx.message.messageId
	 comId = ctx.comId
	 hora_actual = dt.datetime.now().time()
	 img = requests.get(image).content
	 file = open(f"AminoImages/{ctx.author.userId}{hora_actual.hour}-{hora_actual.minute}-{hora_actual.second}.jpg", "wb")
	 file.write(img)
	 file.close()
#	 	print(resp)
#		 if resp == "hentai" or resp == 'porn':
#	 		 ctx.reply("No se permiten ese tipo de imagenes aqui...")
#		 	 bot.community.delete_message(chatId=ctx.chatId, messageId=msjId, comId=ctx.comId)


#@bot.command("id")
def id(ctx: Context):
    n = ctx.author.username
    i = ctx.message.userId
    ch = ctx.chatId
    co = ctx.comId
    ctx.send(f"""
[C]Nombre : {n}

[C]UserId : {i}

[C]ChatId : {ch}

[C]ComId : {co}

""")

@bot.command("chatId")
def CHATID(ctx: Context):
    chatId = ctx.chatId
    ctx.send(chatId)
@bot.command("userId")
def USERID(ctx: Context):
    userId = ctx.userId
    ctx.send(userId)
@bot.command("comId")
def COMID(ctx: Context):
    comId = ctx.comId
    ctx.send(str(comId))
@bot.command("comIds")
def COMIDS(ctx: Context):
    comsId = bot.community.joined_communities().json()
    comsId = [item["ndcId"] for item in comsId]
    ctx.send(str(comsId))


@bot.command("live")
def live(ctx: Context, message: str):
    comId = ctx.comId
    bot.community.start_vc(comId=comId, chatId=ctx.chatId)
    ctx.reply("Te inicio pero me cuidas el chat^^")

@bot.command("end")
def end(ctx: Context, message: str):
    comId = ctx.comId
    bot.community.stop_vc(comId=comId, chatId=ctx.chatId)
    ctx.reply("Se acabo la fiesta")

@bot.command(name="videolive", aliases=["videollamada", "cam", "quiero ver tu cara mami"])
def videolive(ctx: Context):
	admins = bot.community.fetch_chat_moderators(chatId=ctx.chatId, comId=ctx.comId)
	userId = ctx.author.userId
	if userId in admins:
		comId = ctx.comId
		clientFix.start_vc(comId=comId, chatId=ctx.chatId)
		ctx.reply("Okey te inicio")
		ctx.reply("Pero recuerda que las videollamadas son mas delicadas")
		ctx.reply("Y algo mas, esto esta un poco bug, para que se vea la camara de alguuen esa persona tiene que reiniciae la app de amino listo. DISFRUTEN!!!")
	else:
		ctx.reply("No tienes permiso para iniciar vifeollamadas ^^")


@bot.command("sigueme")
def sigueme(ctx: Context):
	comId = ctx.comId
	userId = ctx.author.userId
	print("          siguiendo a      ", userId)
	bot.community.follow(userId, comId)
	ctx.send("Pero me sigues tu tambien ? porfi")
@bot.command("sígueme")
def sígueme(ctx: Context):
	comId = ctx.comId
	userId = ctx.message.userId
	print("                  ", userId)
	bot.community.follow(userId, comId)
	ctx.send("Pero me sigues tu tambien ? porfi")

@bot.command("dueño")
def dueño(ctx: Context):
	uswr = bot.community.fetch_object_id("http://aminoapps.com/p/56myz7s")
	name = bot.community.fetch_user(userId=uswr).nickname
	icon = bot.community.fetch_user(userId=uswr).icon
	comId = ctx.comId
	bot.community.send_embed(comId=comId, chatId=ctx.chatId, title=name, content="Dueño", image=icon, link=f"ndc://user-profile/{uswr}")


#@bot.command("info")
#def info(ctx: Context, message: str):
#	comId = ctx.comId
#	uid = bot.community.fetch_object_id(message)
#	a = bot.community.fetch_user(comId, uid)
#	a = a.json()
#	a = str(a)
#	ctx.reply(a)

@bot.command("escribir")
def escribir(ctx: Context, message: str):
	ctx.send(message) 
@bot.command("spam")
def spam(ctx: Context, message: str):
	chatId = ctx.chatId
	comId = ctx.comId
	admins = bot.community.fetch_chat_moderators(chatId=chatId, comId=comId)
	numero_entero = ""
	for caracter in message:
	    	if caracter.isdigit():
	    		numero_entero += caracter
	numero_entero = int(numero_entero)
	if numero_entero <= 10:
		print("ok")
		ne = numero_entero
	elif numero_entero > 10:
		ne = 10
		if ctx.author.userId in admins:
			ne = numero_entero
	letra = str(numero_entero)
	message = message.replace(letra, "")
	def SuperSpam():
		ctx.send(message)
	for _ in range(ne):
		Thread(target=SuperSpam).start()
		print(_+1)

@bot.command("silencio")
def silencio(ctx: Context, message: str):
	comId = ctx.comId
	bot.community.set_view_only(comId=comId, chatId=ctx.chatId, viewOnly=True)
	ctx.send("No pus a callar todos los mortales")
@bot.command("nosilencio")
def nosilencio(ctx: Context, message: str):
	comId = ctx.comId
	bot.community.set_view_only(comId=comId, chatId=ctx.chatId, viewOnly=False)
	ctx.send("Esta bien me apido de los mortales")

@bot.command("corto")
def corto(ctx: Context, message: str):
	_ = 0
	comId = ctx.comId
	chatId = ctx.chatId
	for _ in range(1000):
		_ = _+1
		bot.community.start_vc(chatId, comId)
		bot.community.stop_vc(chatId, comId)
	ctx.send(f"no mames {ctx.author.username} aun no soy antiagua")

#@bot.command("ban")
#def ban(ctx: Context, message: str):
#	perm = ctx.userId
#	userId = ctx.message.mentioned_userids
#	reason = "por ser fan de kunno"
#	if perm==("9bdbbe71-581c-472e-b819-1f3e22cd737e"):
#		bot.community.kick(userId, reason)
#		ctx.send("por ser fan de kunno")
#		print(f"usuario baneado {ctx.author.username}")
#	if perm==("userId"):
#		bot.community.kick(userId, reason)
#		ctx.send("por ser fan de kunno")
#		print(f"usuario baneado {ctx.author.username}")
#	if perm==("userId"):
#		bot.community.kick(userId, reason)
#		ctx.send("por ser fan de kunno")
#		print(f"usuario baneado {ctx.author.username}")

@bot.command("sugerencia")
def sugerencia(ctx: Context, message: str):
	hora_actual = dt.datetime.now()
	with open(f"Sugerencias_de_comandos/sugerencia_de_{ctx.author.userId}---{hora_actual.day}_{hora_actual.hour}_{hora_actual.minute}_{hora_actual.second}.txt", "a") as file:
		file.write(message)
		file.close()
		ctx.reply(f"Gracias por tu ayuda {ctx.author.username} Le mandare esto al flojo de mi creador")

#@bot.command("palta")
#def nosilencio(ctx: Context, message: str):
#	perm = ctx.userId
#	print(perm)
#	userId = ctx.message.mentioned_userids
#	if perm==("9bdbbe71-581c-472e-b819-1f3e22cd737e"):
#		ctx.send("no pendejo, es aguacate, pinche fan de kunno, si sigues asi te baneo")
#		print(f"advertencia mandada a {ctx.author.username}")

@bot.command("comandos")
def comandos(ctx: Context):
	comandos = "                    [C] Lista de comandos \n\n\n /gato \n manda una foto de un gato \n\n \decir \n repite lo que dice en el mensaje \n\n /spam \n spamea 10 veces lo del mensaje \n\n /invocar \n usa el @ para invocar a algiien con 5 mensajes \n\n /live \n sirve para iniciar llamada \n\n /end \n sirve para terminar llamada \n\n /corto \n le da un corto circuito al bot \n\n Proximamente mas..."
	ctx.send(comandos)

#@bot.command("dentro")
#def dentro(ctx: Context):
#	boy = Bot(command_prefix="/",community_id = 67,)
#	boy = bot.run("yohanllanes@hotmail.com", "123456789O")
#	boy.community.start_vc(ctx.chatId)
#	print("yohan dentro")
#@bot.command("fuera")
#def fuera(ctx: Context):
#	boy = Bot(command_prefix="/",community_id = 67,)
#	boy = bot.run("yohanllanes@hotmail.com", "123456789O")
#	boy.community.stop_vc(ctx.chatId)
#	print("yohan fuerq")

@bot.command("salir")
def salir(ctx: Context):
	comId = ctx.comId
	bot.community.stop_vc(comId=comId, chatId=ctx.chatId)
@bot.command("entrar")
def entrar(ctx: Context):
	comId = ctx.comId
	bot.community.start_vc(comId=comId, chatId=ctx.chatId)

@bot.command("Tp")
def Tp(ctx: Context, message: str):
	comId = ctx.comId
	chatId = bot.community.fetch_object_id(message)
	bot.community.join_chat(comId=comId, chatId=chatId)
	print(f"\n\n {ctx.author.username}:", message, "\n\n")
	ctx.reply("Ok ya entro")
@bot.command("tp")
def tp(ctx: Context, message: str):
	comId = ctx.comId
	chatId = bot.community.fetch_object_id(message)
	bot.community.join_chat(comId=comId, chatId=chatId)
	print(f"\n\n {ctx.author.username}:", message, "\n\n")
	ctx.reply("Ok ya entro")
@bot.command("tpc")
def tpc(ctx: Context, message: str):
	comId = bot.fetch_community_id(message)
	bot.community.join_community(comId=comId)
	print(f"\n\n {ctx.author.username}:", message, "\n\n")
	ctx.reply("Ok ya entro")
	
	

@bot.command("Tarara")
def Tarara(ctx: Context, message: str):
	comId = ctx.comId
	ctx.reply("Me voy por que nadie me quiere :( ")
	bot.community.leave_chat(comId=comId, chatId=ctx.chatId)
@bot.command("tarara")
def tarara(ctx: Context, message: str):
	comId = ctx.comId
	ctx.reply("Me voy por que nadie me quiere :( ")
	bot.community.leave_chat(comId=comId, chatId=ctx.chatId)


@bot.command("bio")
def bio(ctx: Context, message: str):
	comId = ctx.comId
	bot.community.edit_profile(comId=comId, content=message)
	ctx.reply("puesto")
@bot.command("name")
def name(ctx: Context, message: str):
	comId = ctx.comId
	bot.community.edit_profile(comId=comId, nickname=message)
	ctx.reply("puesto")
@bot.command(name="icon")
def icon(ctx: Context, message: str):
	comId = ctx.comId
	aicon = ctx.message.replied.message.mediaValue
	bot.community.edit_profile(comId=comId, icon=aicon)
	ctx.reply("puesto")
@bot.command(name="aver", aliases=["Aver", "A ver", "ver", "Ver"])
def aver(ctx: Context, message: str):
	comId = ctx.comId
	users = ctx.message.mentioned_dictionary
	for user_id, user_name in users.items():
		userId = user_id
	icon = bot.community.fetch_user(userId).icon
	bot.community.send_image(comId=comId, chatId=ctx.chatId, image=icon)
	ctx.send("ahi ta")



@bot.command("clon")
def clon(ctx: Context, message: str):
	users = ctx.message.mentioned_dictionary
	for user_id, user_name in users.items():
		userId = user_id
	comId = ctx.comId
	name = bot.community.fetch_user(comId=comId, userId=userId).nickname
	bio = bot.community.fetch_user(comId=comId, userId=userId).content
	icon = bot.community.fetch_user(comId=comId, userId=userId).icon
	background = bot.community.fetch_user(comId=comId, userId=userId).json()["mediaList"]
	typ = bot.community.fetch_user(comId=comId, userId=userId).json()["extensions"]
	text = str(typ)
	posi = text.find("#")
	sub = text[90 : posi+7]
	text2 = str(background)
	posi2 = text2.find("http")
	posi3 = text2.find("jpg")
	sub2 = text2[posi2 : posi3+3]
	print(sub2)
	bot.community.edit_profile(comId=comId, nickname=name, content=bio, icon=icon, cover_image=sub2)
	ctx.reply("puesto")

@bot.command(name="copyname", aliases=["clonname", "Copyname", "copyn", "cn"])
def copyname(ctx: Context, message: str):
	users = ctx.message.mentioned_dictionary
	for user_id, user_name in users.items():
		userId = user_id
	comId = ctx.comId
	name = bot.community.fetch_user(comId=comId, userId=userId).nickname
	bot.community.edit_profile(comId=comId, nickname=name)
	ctx.reply("puesto")
@bot.command(name="copybio", aliases=["clonbio", "Copybio", "copyb", "cb"])
def copybio(ctx: Context, message: str):
	users = ctx.message.mentioned_dictionary
	for user_id, user_name in users.items():
		userId = user_id
	comId = ctx.comId
	bio = bot.community.fetch_user(comId=comId, userId=userId).content
	bot.community.edit_profile(comId=comId, content=bio)
	ctx.reply("puesto")
@bot.command(name="copyicon", aliases=["clonicon", "Copyicon", "copyi", "ci"])
def copyicon(ctx: Context, message: str):
	users = ctx.message.mentioned_dictionary
	for user_id, user_name in users.items():
		userId = user_id
	comId = ctx.comId
	icon = bot.community.fetch_user(comId=comId, userId=userId).icon
	bot.community.edit_profile(comId=comId, icon=icon)
	ctx.reply("puesto")









@bot.command("coment")
def coment(ctx: Context, message: str):
	users = ctx.message.mentioned_dictionary
	for user_id, user_name in users.items():
		userId = user_id
		name = user_name
	comId = ctx.comId
#	num = message.find(" ")
#	print(num)
#	msj = message[2 : num]
#	message.replace(msj, "", num)
	message = message.replace("@"+name, "")
	bot.community.comment_on_profile(comId=comId, userId=userId, content=f"{message} (Comentado por {ctx.author.nickname})")
	ctx.reply("Listo ^^")



#@bot.on_text_message()
#def message(ctx: Context):
#	userId =  ctx.message.author.userId
#	if userId==("ec6f6ea7-76ec-4c5a-9400-164fad7eb76c"):
#		bot.community.delete_message(chatId=ctx.chatId, messageId=ctx.message.messageId)

@bot.command("chiste")
def chiste(ctx: Context, message: str):
	comId = ctx.comId
	chistes = pyjokes.get_joke(language='es', category="neutral")  
	print(chistes)
	ctx.reply(chistes)

@bot.command("ia")
def ia(ctx: Context, message: str):
	ctx.send(content="Pensando...")
	openai.api_key = "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"
	respuesta = openai.Completion.create(engine="text-davinci-003", prompt=message, max_tokens=150)
	ctx.reply(respuesta.choices[0].text)

@bot.command("IA")
def IA(ctx: Context, message: str):
	ctx.send(content="Pensando..")
	openai.api_key = "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"
	respuesta = openai.Completion.create(engine="text-davinci-003", prompt=message, max_tokens=150)
	ctx.reply(respuesta.choices[0].text)

#@bot.task()
#def a():
#	while True:
#		@bot.command(name="chat", 					aliases=["Chat", "CHAT"])
#		def chat(ctx: Context, message: str):
#			openai.api_key = "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"
#			conversation = ""
#			question = message
#			conversation += "\nHumano: " + question + "\nAI:"
#			respuesta = openai.Completion.create(engine="text-davinci-003",
#			prompt=conversation,
#			temperature=0.9,
#			max_tokens=150,
#			top_p=1,
#			frequency_penalty=0,
#			presence_penalty=0.9,
#			stop=["\n", "Humano:", "AI:"]
#			)
#			answer = respuesta.choices[0].text.strip()
#			conversation += answer
#			ctx.reply(answer)

@bot.command(name="imagen", aliases=["IAM", "IMG", "img", "Img"])
def imagen(ctx: Context, message: str):
	verify = 0
	if verify==0:
		pass
	elif verify==1:
		openai.api_key = "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"
		try:
			ctx.send(content="Creando Imagen...")
			response = openai.Image.create(
			prompt=message,
			n=1,
			size="1024x1024"
			)
			ImageLink = response["data"][0]["url"]
			ctx.send_image(ImageLink)
		except:
			ctx.send("Texto no permitido, escrube otta cosa...")








@bot.command("admins")
def admins(ctx: Context, message: str):
	chatId = ctx.chatId
	comId = ctx.comId
	mods = bot.community.fetch_chat_moderators(comId=comId, chatId=chatId)
	rango = len(mods)
	_ = -1
	nombres = ("")
	for i in range(rango):
		_ = _+1
		mod = mods[_]
		name = bot.community.fetch_user(comId=comId, userId=mod).username
		nombres = nombres+"\n[C]"+name
	ctx.send(f"[C]Admins\n {nombres}")

@bot.command(name="permiso", aliases=["op", "OP", "Op", "oP", "Permiso", "PERMISO"])
def permiso(ctx: Context, message: str):
	userId = ctx.author.userId
	if message=="set":
		op = int(message)
		with open(f"permisos/{userId}.txt","w") as OpFile:
			OpFile.write(op)
		ctx.send("✅️")
	elif message=="view" or message=="ver":
		try:
			with open(f"permisos/{userId}.txt","r") as OpFile:
				userOp = OpFile.read()
				ctx.send(userOp)
		except:
			ctx.send("[C]Aun no tienes un op, escribe /op start para poder usar comandos de op")
	elif message=="start":
		with open(f"permisos/{userId}.txt","w") as OpFile:
			OpFile.write(1)
		ctx.send("✅️")


@bot.command("dox")
def dox(ctx: Context, message: str):
	users = ctx.message.mentioned_dictionary
	for user_id, user_name in users.items():
		ctx.send(user_id)

@bot.command("kick")
def kick(ctx: Context, message: str):
	userId = ctx.author.userId
	comId = ctx.comId
	chatId = ctx.chatId
	mods = bot.community.fetch_chat_moderators(comId=comId, chatId=chatId)
	botId = "c0bc08ab-473d-4b81-9f97-df3e9a673688"
	if botId in mods:
		pass
	else:
		ctx.send("Nesesito ser coa para esto...")
	if userId in mods:
		users = ctx.message.mentioned_dictionary
		for user_id, user_name in users.items():
			bot.community.kick(userId=user_id, comId=comId, chatId=chatId, allowRejoin=True)
		ctx.send("Fuera negro")
	else:
		ctx.send("Los mortales no pueden usar ese comando...")
		
@bot.command("ban")
def ban(ctx: Context, message: str):
	userId = ctx.author.userId
	comId = ctx.comId
	chatId = ctx.chatId
	mods = bot.community.fetch_chat_moderators(comId=comId, chatId=chatId)
	botId = "c0bc08ab-473d-4b81-9f97-df3e9a673688"
	if botId in mods:
		pass
	else:
		ctx.send("Nesesito ser coa para esto...")
	if userId in mods:
		users = ctx.message.mentioned_dictionary
		for user_id, user_name in users.items():
			bot.community.kick(userId=user_id, comId=comId, chatId=chatId, allowRejoin=False)
		ctx.send("Baneado NAJAJA")
	else:
		ctx.send("Los mortales no pueden usar ese comando...")


#Acciones
@bot.command("golpear")
def golpear(ctx: Context, message: str):
	comId = ctx.comId
	chatId = ctx.chatId
	users = ctx.message.mentioned_dictionary
	for user_id, user_name in users.items():
		vicname = user_name
	autorId = ctx.author.nickname
	reaction = "punch"
	url = get(f"https://api.otakugifs.xyz/gif?reaction={reaction}&format=gif").json()["url"]
	#bot.community.send_embed(chatId=chatId, comId=comId, title=f"{autorId} mato a {vicname}", content=None, image=url)
	ctx.send(f"{autorId} golpeo a {vicname}")
	ctx.send_gif(url)
@bot.command("pat")
def pat(ctx: Context, message: str):
	comId = ctx.comId
	chatId = ctx.chatId
	users = ctx.message.mentioned_dictionary
	for user_id, user_name in users.items():
		vicname = user_name
	autorId = ctx.author.nickname
	reaction = "pat"
	url = get(f"https://api.otakugifs.xyz/gif?reaction={reaction}").json()["url"]
	#bot.community.send_embed(chatId=chatId, comId=comId, title=f"{autorId} mato a {vicname}", content=None, image=url)
	ctx.send(f"{autorId} da mimos a {vicname}")
	ctx.send_gif(url)
	#bot.community.send_image(comId=comId, chatId=chatId, image=url)
	#bot.community.send_link_snippet(image=url, link=url, chatId=chatId)
	#a = bot.community.upload_media(media=open("/sdcard/Download/7a29a8b4-98e8-42b6-aa91-60df27b11a4a.jpeg"))
#	print(a)
#	print("a")

@bot.command("besar")
def besar(ctx: Context, message: str):
	comId = ctx.comId
	chatId = ctx.chatId
	users = ctx.message.mentioned_dictionary
	for user_id, user_name in users.items():
		vicname = user_name
	autorId = ctx.author.nickname
	reaction = "kiss"
	url = get(f"https://api.otakugifs.xyz/gif?reaction={reaction}&format=gif").json()["url"]
	ctx.send(f"{autorId} le dio un beso a {vicname}")
	ctx.send_gif(url)
@bot.command(name="tirarbeso")
def tirarbesl(ctx: Context, message: str):
	comId = ctx.comId
	chatId = ctx.chatId
	users = ctx.message.mentioned_dictionary
	for user_id, user_name in users.items():
		vicname = user_name
	autorId = ctx.author.nickname
	reaction = "airkiss"
	url = get(f"https://api.otakugifs.xyz/gif?reaction={reaction}&format=gif").json()["url"]
	ctx.send(f"{autorId} le tiro un beso a {vicname}")
	ctx.send_gif(url)
@bot.command(name="abrazo", aliases=["hug", "abrazo", "abrazar", "abraso", "abrasar", "Abrazar", "Abrazo"])
def abrazo(ctx: Context, message: str):
	comId = ctx.comId
	chatId = ctx.chatId
	users = ctx.message.mentioned_dictionary
	for user_id, user_name in users.items():
		vicname = user_name
	autorId = ctx.author.nickname
	reaction = "hug"
	url = get(f"https://api.otakugifs.xyz/gif?reaction={reaction}&format=gif").json()["url"]
	actions = f"{autorId} abrazo a {vicname}", f"{autorId} le dio un abrazo a {vicname}", f"{autorId} esta abrazando a {vicname}"
	action = rd.choice(actions)
	ctx.send(action)
	ctx.send_gif(url)
@bot.command(name="morder", aliases=["bite", "Bite", "Morder", "Vite", "vite", "mordida", "Morder"])
def morder(ctx: Context, message: str):
	comId = ctx.comId
	chatId = ctx.chatId
	users = ctx.message.mentioned_dictionary
	for user_id, user_name in users.items():
		vicname = user_name
	autorId = ctx.author.nickname
	reaction = "bite"
	url = get(f"https://api.otakugifs.xyz/gif?reaction={reaction}&format=gif").json()["url"]
	actions = f"{autorId} mordio a {vicname}", f"{autorId} le dio una mordida a {vicname}", f"{autorId} esta mordiendo a {vicname}"
	action = rd.choice(actions)
	ctx.send(action)
	ctx.send_gif(url)



#Reacciones
@bot.command(name="sonrojarse", aliases=["blush", "sonrrojarse", "Sonrrojarse", "Blush"])
def sonrrojarse(ctx: Context, message: str):
	comId = ctx.comId
	autorId = ctx.author.nickname
	chatId = ctx.chatId
	reaction = "blush"
	url = get(f"https://api.otakugifs.xyz/gif?reaction={reaction}&format=gif").json()["url"]
	actions = f"{autorId} se esta sonrrojando" , f"{autorId} esta sonrrojado", f"{autorId} se ha sonrrojado", f"{autorId}, empezo a sonrrojarse"
	action = rd.choice(actions)
	ctx.send(action)
	ctx.send_gif(url)
	
@bot.command(name="llorar", aliases=["cry", "Llorar", "Cry"])
def llorar(ctx: Context, message: str):
	comId = ctx.comId
	autorId = ctx.author.nickname
	chatId = ctx.chatId
	reaction = "cry"
	url = get(f"https://api.otakugifs.xyz/gif?reaction={reaction}&format=gif").json()["url"]
	actions = f"{autorId} esta llorando", f"{autorId} se puso a llorar", f"{autorId} empezo a llorar"
	action = rd.choice(actions)
	ctx.send(action)
	ctx.send_gif(url)

@bot.command(name="avergonzarse", aliases=["shy", "Avergonzarse", "Shy"])
def avergonzarse(ctx: Context, message: str):
	comId = ctx.comId
	autorId = ctx.author.nickname
	chatId = ctx.chatId
	reaction = "shy"
	url = get(f"https://api.otakugifs.xyz/gif?reaction={reaction}&format=gif").json()["url"]
	actions = f"{autorId} esta avergonzado", f"{autorId} se esta avergonzando", f"a {autorId} le gano la vergurnza"
	action = rd.choice(actions)
	ctx.send(action)
	ctx.send_gif(url)

@bot.command(name="sonreir", aliases=["smile", "Sonreir", "Smile"])
def sonreir(ctx: Context, message: str):
	comId = ctx.comId
	autorId = ctx.author.nickname
	chatId = ctx.chatId
	reaction = "smile"
	url = get(f"https://api.otakugifs.xyz/gif?reaction={reaction}&format=gif").json()["url"]
	actions = f"{autorId} esta sonrriendo", f"{autorId} empezo a sonrreir"
	action = rd.choice(actions)
	ctx.send(action)
	ctx.send_gif(url)

@bot.command(name="sorprendido", aliases=["surprised", "Sorprendido", "Surprised", "sorprenderse", "Sorprenderse"])
def sorprendido(ctx: Context, message: str):
	comId = ctx.comId
	autorId = ctx.author.nickname
	chatId = ctx.chatId
	reaction = "surprised"
	url = get(f"https://api.otakugifs.xyz/gif?reaction={reaction}&format=gif").json()["url"]
	actions = f"{autorId} esta sorprendido", f"{autorId} sw a sorprendio"
	action = rd.choice(actions)
	ctx.send(action)
	ctx.send_gif(url)

#Busquedas
@bot.command(name="neko")
def neko(ctx: Context, message: str):
	comId = ctx.comId
	chatId = ctx.chatId
	url = requests.get("https://api.waifu.pics/sfw/neko").json()["url"]
	#innnn = requests.get(url=url).content()
	print(url)
	#ctx.send("aqui tienes a tu neko cuidala mucho")
	#bot.community.send_link_snippet(message="aqui tienes a tu neko cuidala mucho", link=url, image=inagem, comId=comId, chatId=chatId)
	ctx.send("aqui tienes a tu neko cuidala mucho")
	ctx.send_image(url)
	#ctx.send_link_snippet(image=innnn, message="Aqui tienes a tu neko cuidala mycho ^^", link=url)

@bot.command(name="waifu")
def waifu(ctx: Context, message: str):
	comId = ctx.comId
	chatId = ctx.chatId
	url = requests.get("https://api.waifu.pics/sfw/waifu").json()["url"]
	print(url)
	#bot.community.send_link_snippet(message="aqui tienes a tu waifu cuidala mucho", link=url, image=url, comId=comId, chatId=chatId)
	ctx.send("Aqui tienes a tu waifu cuidala mucho")
	ctx.send_image(url)
#nsfw
@bot.command(name="nekonsfw")
def nekonsfw(ctx: Context, message: str):
	comId = ctx.comId
	chatId = ctx.chatId
	url = requests.get("https://api.waifu.pics/nsfw/neko").json()["url"]
	print(url)
#	bot.community.send_link_snippet(message="aqui tienes a tu neko maldito enfermo", link=url, image=url, comId=comId, chatId=chatId)
	ctx.send("aqui tienes a tu neko cuidala mucho")
	ctx.send_image(url)

@bot.command(name="waifunsfw")
def waifunsfw(ctx: Context, message: str):
	comId = ctx.comId
	chatId = ctx.chatId
	url = requests.get("https://api.waifu.pics/nsfw/waifu").json()["url"]
	print(url)
	#bot.community.send_link_snippet(message="aqui tienes a tu waifu maldito enfermo", link=url, image=url, comId=comId, chatId=chatId)
	ctx.send("Aqui tienes a tu waifu cuidala mucho")
	ctx.send_image(url)

@bot.command(name="trap")
def trap(ctx: Context, message: str):
	comId = ctx.comId
	chatId = ctx.chatId
	url = requests.get("https://api.waifu.pics/nsfw/trap").json()["url"]
	print(url)
	#bot.community.send_link_snippet(message="aqui tienes a tu waifu maldito enfermo", link=url, image=url, comId=comId, chatId=chatId)
	ctx.send("Aqui tienes a tu trap cuidale mucho")
	ctx.send_image(url)

@bot.command(name="blowjob")
def blowjob(ctx: Context, message: str):
	comId = ctx.comId
	chatId = ctx.chatId
	url = requests.get("https://api.waifu.pics/nsfw/blowjob").json()["url"]
	print(url)
	#bot.community.send_link_snippet(message="aqui tienes a tu waifu maldito enfermo", link=url, image=url, comId=comId, chatId=chatId)
	ctx.send("Aqui tienes a tu blowjob cuidale mucho")
	ctx.send_image(url)



@bot.command("spotify")
def spotify(ctx: Context, message: str):
	comId = ctx.comId
	chatId = ctx.chatId
	cancion = message
	results = sp.search(q=cancion, limit=1, type='track')
	if results['tracks']['items']:
	    info = results['tracks']['items'][0]
	    name = info['name']
	    link = info['external_urls']['spotify']
	    ctx.send(f"[C]nombre de la cancion {name} \n[C]Pedida por {ctx.author.nickname} \n[C]ink de la cancion {link}")
	else:
	    print('Canción no encontrada.')

@bot.command(name="YT", aliases=["Yt", "yT", "yt", "youtube", "YouTube", "cancion", "Cancion", "canción", "Canción"])
def YT(ctx: Context, message: str):
	ctx.send("Buscando...")
	name = ctx.author.nickname
	userId = ctx.author.userId
	chatId = ctx.chatId
	comId = ctx.comId
	hora_actual = dt.datetime.now()
	filename = f"AminoCanciones/{message}-{userId}-{hora_actual.day}-{hora_actual.hour}-{hora_actual.minute}-{hora_actual.second}.mp3"
	videosSearch = VideosSearch(message, limit = 1)
	link = (videosSearch.result()['result'][0]['link'])
	cname = (videosSearch.result()['result'][0]['title'])
	Download(link=link, filename=filename)
	try:
		ctx.send_audio(filename)
		ctx.send(f"""[C]Cancion pedida por: {name}

[C]Nombre de la cancion: {cname}

[C]Link de la cancion: {link}""")
	except:
		ctx.send("La cancion es demaciado larga")




#Divercion
@bot.command(name="suma", aliases=["Suma", "Sumar", "zuma", "+"])
def Matess(ctx: Context):
	chatId = ctx.chatId
	comId = ctx.comId
	n1 = rd.randrange(1, 1000)
	n2 = rd.randrange(1, 1000)
	n3 = n1+n2
	n3 = str(n3)
	ctx.send(f"Cuanto es {n1} + {n2} ?")
	rep = ctx.wait_for_message(message=n3, timeout=15)
	if rep is None:
		ctx.send(f"Error! El resultado es {n3}")
	else:
		ctx.send("Felicidades!!! No estas tan pendejo como crei ^^")

@bot.command(name="multiplicación", aliases=["Multiplicación", "multiplicar", "Multiplicar", "×"])
def Matesm(ctx: Context):
	chatId = ctx.chatId
	comId = ctx.comId
	n1 = rd.randrange(1, 1000)
	n2 = rd.randrange(1, 1000)
	n3 = n1*n2
	n3 = str(n3)
	ctx.send(f"Cuanto es {n1} × {n2} ?")
	rep = ctx.wait_for_message(message=n3, timeout=25)
	if rep is None:
		ctx.send(f"Error! El resultado es {n3}")
	else:
		ctx.send("Felicidades!!! No estas tan pendejo como crei ^^")

@bot.command(name="resta", aliases=["restar", "Resta", "-"])
def Matesr(ctx: Context):
	chatId = ctx.chatId
	comId = ctx.comId
	n1 = rd.randrange(1, 1000)
	n2 = rd.randrange(1, 1000)
	n3 = n1-n2
	n3 = str(n3)
	ctx.send(f"Cuanto es {n1} - {n2} ?")
	rep = ctx.wait_for_message(message=n3, timeout=15)
	if rep is None:
		ctx.send(f"Error! El resultado es {n3}")
	else:
		ctx.send("Felicidades!!! No estas tan pendejo como crei ^^")

@bot.command(name="divicion", aliases=["dividir", "dibicion", "Divicion", "division", "÷"])
def Matesd(ctx: Context):
	chatId = ctx.chatId
	comId = ctx.comId
	n1 = rd.randrange(1, 1000)
	n2 = rd.randrange(1, 1000)
	n3 = n1/n2
	n3 = round(n3, 2)
	n3 = str(n3)
	ctx.send(f"Cuanto es {n1} ÷ {n2} ?")
	rep = ctx.wait_for_message(message=n3, timeout=25)
	if rep is None:
		ctx.send(f"Error! El resultado es {n3}")
	else:
		ctx.send("Felicidades!!! No estas tan pendejo como crei ^^")

@bot.command(name="open")
def oppen(ctx: Context, message: str):
	comId = 67
	chatId = ctx.chatId
	joinType = int(message)
	YohanVid.start_vc(chatId=chatId, comId=67, joinType=joinType)

@bot.command("ruleta")
def ruleta(ctx: Context):
	chatId = ctx.chatId
	comId = ctx.comId
	msj = "Has perdido :(", "Felicidades ganaste!!!"
	num = rd.choice(msj)
	ctx.send(num)


@bot.command(name="VoR", aliases=["Vor", "vor", "VOR", "vOr", "VerdadOReto", "verdadoreto"])
def verdad_o_reto(ctx: Context , message: str):
	Verdades = open("Verdades.txt").read().splitlines()
	Retos = open("Retos.txt").read().splitlines()
	eleccion = message
	if eleccion == "verdad":
	   ctx.reply(rd.choice(Verdades))
	elif eleccion == "reto":
		ctx.reply(rd.choice(Retos))
	elif eleccion == "Verdad":
	   ctx.reply(rd.choice(Verdades))
	elif eleccion == "Reto":
		ctx.reply(rd.choice(Retos))
	elif eleccion == "v":
	   ctx.reply(rd.choice(Verdades))
	elif eleccion == "r":
		ctx.reply(rd.choice(Retos))
	elif eleccion == "V":
	   ctx.reply(rd.choice(Verdades))
	elif eleccion == "R":
		ctx.reply(rd.choice(Retos))


@bot.command("decir")
def decir(ctx: Context, message: str):
	hora_actual = dt.datetime.now().time()
	audio = gTTS(text=message, lang="it")
	audio.save(f"AminoHabladas/Audio-de-{ctx.author.userId}{hora_actual.hour}-{hora_actual.minute}-{hora_actual.second}.mp3")
	ctx.send_audio(f"AminoHabladas/Audio-de-{ctx.author.userId}{hora_actual.hour}-{hora_actual.minute}-{hora_actual.second}.mp3")










@bot.command("ping")
def ping(ctx: Context):
	ctx.send(f"""Pong!
[C]Bot funcionando a {bot.ping()}ms""")



@bot.command(name="autodestruccion", aliases=["lider", "Lider", "LIDER", "curador", "Curador", "CURADOR"])
def autodestruccion():
	clientFix.delete_account(password)


@bot.command("purga")
def purga(ctx: Context, message: str):
	chatId = ctx.chatId
	num = int(message)
	msjIds = bot.community.fetch_messages(chatId=chatId, start=1, size=num).messageId
	for a in msjIds:
		bot.community.delete_message(chatId=chatId, messageId=a)
	ctx.send("Purga completa^^")


@bot.command(name="exorcismo", aliases=["Exorcismo", "exorsismo", "Exorsismo", "kill", "Kill", "kil", "Kil"])
def exorcismo(ctx: Context, message: str):
	ctx.send("Empezando exorcismo")
	chatId = bot.community.fetch_object_id("http://aminoapps.com/p/ru6mafc")
	comId = ctx.comId
	users = ctx.message.mentioned_dictionary
	for user_id, user_name in users.items():
		userId = user_id
	kam_client = kSubClient(comId=comId, client=kc)
	te = 30
	inicio = tm.time()
	def spam_asistent():
	       while True:
	       	tt = tm.time() - inicio
	       	if tt >= te:
	       		break
	       	try:
	       	   kam_client.set_cohost(chatId=chatId, userId=userId)
	       	   kam_client.del_cohost(chatId=chatId, userId=userId)
	       	except Exception as ExpectingValue:
	       	   print(ExpectingValue)
	for _ in range(50):
	    Thread(target=spam_asistent).start()
	tm.sleep(te)
	ctx.send("¡¡¡Ya acabe el exorcisml ^^!!!")

@bot.on_text_message()
def juego(ctx: Context):
	api_key = "7aWM973fF3essNMvdCHQFb3yYaovsDeC"
	check = 0
	pregunta = ctx.message.content
	palabra = "Tengo hambre"
	palabra2 = "tengo hambre"
	print(pregunta)
	if palabra in pregunta:
		ctx.send("Pideme algo")
		check = 1
	elif palabra2 in pregunta:
		ctx.send("Pideme algo")
		check = 1
	userId = ctx.author.userId
	while check==1:
		if check==2:
			break
		try:
			@bot.on_text_message()
			def juegoId(ctx: Context):
				userId2 = ctx.message.userId
				respuesta = ctx.message.content
				if userId==userId2:
					if "Pizza" in respuesta:
						busqueda = "Comoda Pizza"
						url_api = f'https://api.giphy.com/v1/gifs/random?api_key={api_key}&tag={busqueda}'
						response = requests.get(url_api)
						data = response.json()
						gif_url = data['data']['images']['original']['url']
						ctx.send("Aqui tienes una Pizza")
						ctx.send_gif(gif_url)
						check2 = 1
					elif "Donas" in respuesta:
						busqueda = "Pan Donas"
						url_api = f'https://api.giphy.com/v1/gifs/random?api_key={api_key}&tag={busqueda}'
						response = requests.get(url_api)
						data = response.json()
						gif_url = data['data']['images']['original']['url']
						ctx.send("Aqui tienes unas Donas")
						ctx.send_gif(gif_url)
						check2 = 1
					elif "Helado" in respuesta:
						busqueda = "Helado"
						url_api = f'https://api.giphy.com/v1/gifs/random?api_key={api_key}&tag={busqueda}'
						response = requests.get(url_api)
						data = response.json()
						gif_url = data['data']['images']['original']['url']
						ctx.send("Okey deja te busco helado")
						ctx.send_gif(gif_url)
						check2 = 1
				global check
				check = 2
		except:
			m = "hhhhh"

#Juegos
@bot.command("jugar")
def ahorcado(ctx: Context):
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    ctx.send("¡Bienvenido al juego del ahorcado!")

    while attempts > 0:
        display = display_word(word_to_guess, guessed_letters)
        ctx.send(f"Palabra a adivinada {display}")
        if "_ " not in display:
            ctx.send("""[C]Waos pense que perderias pero...
[C]GANASTEEE!!!""")
            break
        ctx.wait_for_message(message="/letra", timeout=100000)
        mensa = bot.community.fetch_messages(chatId=ctx.chatId, comId=ctx.comId, size=0).content[0]
        guess = mensa.lower()

        if len(guess) != 1 or not guess.isalpha():
            ctx.send("Aprende a jugar solo pon 1 letra.")
            continue

        if guess in guessed_letters:
            ctx.send("No seas pendejo ya intentaste esta letra")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            ctx.send("Bien adivinaste una letra ^^")
        else:
            attempts -= 1
            ctx.send(f"Letra incorrecta. {attempts} Intentos restantes...")


    if "_ " in display:
        ctx.send(f"Perdiste. La palabra era: {word_to_guess}")



@bot.command(name="loteria")
def damedame(ctx: Context):
	chatId = ctx.chatId
	comId = ctx.comId
	userId = ctx.author.userId
	coin = rd.randrange(1, 101)
	ksub = kSubClient(comId=comId, client=kc.client)
	publicacion = ksub.get_user_blogs(userId=userId, size=0).blogId[0]
	try:
		ksub.tip_coins(coins=coin, blogId=publicacion)
		ctx.reply(f"Felicidades ganaste {coin} coins")
	except:
		ctx.reply("No pude donarte sorry :(")
	

#DATOS
#def DATOS(userId: str = None, chatId: str = None, UserName: str = None, UserAlias: str = None):
#	DatoUserAlias = ""
#	DatoUserName = ""
#	DatoUserId = ""
#	DatoChatId = ""
#	try:
#		if chatId==str:
#			 with open(f"DATOS/Alias/{userId}alias.txt:", "r") as AlissFile:
#			 	DatoUserAlias = AlissFile.read()
#			 with open(f"DATOS/Names/{userId}name", "r") as NameFile:
#			 	DatoUserName = NameFile.read()
#			 with open(f"DATOS/UserIds/{userId}uId", "r") as UserIdFile:
#			 	DatoUserId = UserIdFile.read()
#		else:
#			pass
#	except:
#		DatoUserAlias = open(f"DATOS/Alias/{userId}alias.txt:", "w")
#		DatoUserAlias.write(UserAlias)
#		DatoUserAlias.close()
#		DatoUserName = open(f"DATOS/Names/{userId}name", "w")
#		DatoUserName.write(UserName)
#		DatoUserName.close()
#		DatoUserId = open(f"DATOS/UserIds/{userId}uId", "w")
#		DatoUserId.write(userId)
#		DatoUserId.close()
#	try:
#		if chatId==str:
#			DatoChatId = open(f"DATOS/ChatIds/{chatId}cId", "r").read()
#		else:
#			pass
#	except:
#		DatoChatId = open(f"DATOS/ChatIds/{chatId}cId", "w")
#		DatoChatId.write(chatId)
#		DatoChatId.close()
#	return DatoUserAlias, DatoUserName, DatoUserId, DatoChatId


#@bot.command(name="info", aliases=["INFO", "Info"])
#def DatoInfo(ctx: Context):
#	userId = ctx.author.userId
#	name = ctx.author.nickname
#	chatId =  ctx.chatId
#	DatoUserAlias, DatoUserName, DatoUserId, DatoChatId = DATOS(userId=userId, chatId=chatId, UserName=name)
#	ctx.send(f"""
#[C]Nombre >>> {DatoUserName}
#[C]Alias >>> {DatoUserAlias}
#[C]UserId >>> {DatoUserId}
#[C]chatId >>> {DatoChatId}
#""")

#def DATOS(UserId: str = None, ChatId: str = None, UserName: str = None, UserAlias: str = None):
#    DatoUserAlias = ""
#    DatoUserName = ""
#    DatoUserId = ""
#    DatoChatId = ""
#    
#    if UserId is not None:
#        try:
#            with open(f"DATOS/Alias/{UserId}alias.txt", "r") as AliasFile:
#                DatoUserAlias = AliasFile.read()
#        except:
#            with open(f"DATOS/Alias/{UserId}alias", "w") as AliasFile:
#                DatoUserAlias.write(UserAlias)
#    if UserName is not None:
#        try:
#            with open(f"DATOS/Names/{UserId}name", "r") as NameFile:
#                DatoUserName = NameFile.read()
#        except:
#            with open(f"DATOS/Names/{UserId}name", "w") as ChatIdFile:
#                DatoUserName.write(UserName)
#    if userId is not None:
#        try:
#            with open(f"DATOS/UserIds/{UserId}uId", "r") as UserIdFile:
#                DatoUserId = UserIdFile.read()
#        except:
#            pass
#    else:
#        with open(f"DATOS/Alias/{UserId}alias.txt", "r") as AliasFile:
#            DatoUserAlias = AliasFile.read()
#        with open(f"DATOS/Names/{UserId}name", "r") as NameFile:
#            DatoUserName = NameFile.read()
#        with open(f"DATOS/UserIds/{UserId}uId", "r") as UserIdFile:
#            DatoUserId = UserIdFile.read()
#        if DatoUserAlias is None:
#            with open(f"DATOS/Alias/{UserId}alias.txt", "w") as AliasFile:
#                AliasFile.write(UserAlias)
#        if DatoUserName is None:
#            with open(f"DATOS/Names/{UserId}name", "w") as NameFile:
#                NameFile.write(UserName)
#        if DatoUserId is None:
#            with open(f"DATOS/UserIds/{UserId}uId", "w") as UserIdFile:
#                UserIdFile.write(userId)
#    try:
#        if ChatId is not None:
#            with open(f"DATOS/ChatIds/{ChatId}cId", "r") as ChatIdFile:
#                DatoChatId = ChatIdFile.read()
#    except:
#        with open(f"DATOS/ChatIds/{ChatId}cId", "w") as ChatIdFile:
#            ChatIdFile.write(ChatId)
#    
#    return DatoUserAlias, DatoUserName, DatoUserId, DatoChatId
#    

#@bot.command(name="info", aliases=["INFO", "Info"])
#def DatoInfo(ctx: Context):
#	userId = ctx.author.userId
#	name = ctx.author.nickname
#	chatId = ctx.chatId
#	DatoUserAlias, DatoUserName, DatoUserId, DatoChatId = DATOS(UserId=userId, ChatId=chatId, UserName=name)
#	ctx.send(f"""
#[C]Nombre >>> {DatoUserName}
#[C]Alias >>> {DatoUserAlias}
#[C]UserId >>> {DatoUserId}
#[C]chatId >>> {DatoChatId}
#""")

import os

def DATOS(UserId: str = None, ChatId: str = None, UserName: str = None, UserAlias: str = None):
    DatoUserAlias = ""
    DatoUserName = ""
    DatoUserId = ""
    DatoChatId = ""
    
    if UserId is not None:
        alias_file_path = f"DATOS/Alias/{UserId}alias.txt"
        if os.path.exists(alias_file_path):
            with open(alias_file_path, "r") as AliasFile:
                DatoUserAlias = AliasFile.read()
        else:
            with open(alias_file_path, "w") as AliasFile:
                AliasFile.write(UserAlias)
    
    if UserName is not None:
        name_file_path = f"DATOS/Names/{UserId}name.txt"
        if os.path.exists(name_file_path):
            with open(name_file_path, "r") as NameFile:
                DatoUserName = NameFile.read()
        else:
            with open(name_file_path, "w") as NameFile:
                NameFile.write(UserName)
    
    if UserId is not None:
        user_id_file_path = f"DATOS/UserIds/{UserId}uId.txt"
        if os.path.exists(user_id_file_path):
            with open(user_id_file_path, "r") as UserIdFile:
                DatoUserId = UserIdFile.read()
        else:
            with open(user_id_file_path, "w") as UserIdFile:
                UserIdFile.write(UserId)
    
    if ChatId is not None:
        chat_id_file_path = f"DATOS/ChatIds/{ChatId}cId.txt"
        if os.path.exists(chat_id_file_path):
            with open(chat_id_file_path, "r") as ChatIdFile:
                DatoChatId = ChatIdFile.read()
        else:
            with open(chat_id_file_path, "w") as ChatIdFile:
                ChatIdFile.write(ChatId)
    
    return DatoUserAlias, DatoUserName, DatoUserId, DatoChatId

@bot.command(name="info", aliases=["INFO", "Info"])
def DatoInfo(ctx: Context):
    userId = ctx.author.userId
    name = ctx.author.nickname
    chatId = ctx.chatId
    DatoUserAlias, DatoUserName, DatoUserId, DatoChatId = DATOS(UserId=userId, ChatId=chatId, UserName=name)
    ctx.send(f"""
[C]Nombre >>> {DatoUserName}
[C]Alias >>> {DatoUserAlias}
[C]UserId >>> {DatoUserId}
[C]chatId >>> {DatoChatId}
""")

	
	










@bot.on_text_message()
def verchat(ctx: Context, message: str):
		comId = ctx.comId
		hora_actual = dt.datetime.now().strftime('%-I:%M %p')
		print(f"{ctx.author.nickname}: {ctx.message.content} ({hora_actual})")
		posi = message.find("http")
		msj = message[posi : posi+4]
		#if msj==("http"):
			#bot.community.delete_message(comId=comId, chatId=ctx.chatId, messageId=ctx.message.messageId)
			#ctx.send("sin enlaces porfi")
#		if ctx.message.content.startswith("rata"):
#			ctx.send("rata tu m***e")
#		if ctx.message.content.startswith("Rata"):
#			ctx.send("Rata tu m***e")
#		if ctx.message.content.startswith("anfi"):
#			ctx.send("la anfi es muy floja")
#		if ctx.message.content.startswith("Anfi"):
#			ctx.send("La anfi es muy floja")
#		if ctx.message.content.startswith("secreto"):
#			ctx.send("el es fan de kunno")
#		if ctx.message.content.startswith("Secreto"):
#			ctx.send("El es fan de kunno")
		if ctx.message.content=="que":
			tm.sleep(0.2)
			ctx.send("so")
		if ctx.message.content=="Que":
			tm.sleep(0.2)
			ctx.send("So")
		if ctx.message.content=="EA":
			ctx.send("""[C]Insultalo por mi ^^
[C]ndc://user-profile/00000000-0000-0000-0000-000000000000""")
#		if ctx.message.content.startswith("rra"):
#			ctx.send("eres")
#		if ctx.message.content.startswith("Rra"):
#			ctx.send("Eres")
#		if ctx.message.content.startswith("tu"):
#			ctx.send("madre")
#		if ctx.message.content.startswith("Tu"):
#			ctx.send("Madre")
#		if ctx.message.content.startswith("primero"):
#			ctx.send("antes que que la mia")
#		if ctx.message.content.startswith("Primero"):
#			ctx.send("Antes que que la mia")
#		if ctx.message.content.startswith("el q lo dice lo es"):
#			ctx.send("con su cara de pez")
#		if ctx.message.content.startswith("El q lo dice lo es"):
#			ctx.send("Con su cara de pez")
#		if ctx.message.content.startswith("el que lo dice lo es"):
#			ctx.send("con su cara de pez")
#		if ctx.message.content.startswith("El que lo dice lo es"):
#			ctx.send("Con su cara de pez")
		if ctx.message.content.startswith("adios"):
			ctx.send("miren se va triste por un camino de piedras a buscar un chat dónde lo reciban mejor 🍁")
		if ctx.message.content.startswith("Adios"):
			ctx.send("Miren se va triste por un camino de piedras a buscar un chat dónde lo reciban mejor 🍁")
		if ctx.message.content.startswith("adiós"):
			ctx.send("miren se va triste por un camino de piedras a buscar un chat dónde lo reciban mejor 🍁")
		if ctx.message.content.startswith("Adiós"):
			ctx.send("Miren se va triste por un camino de piedras a buscar un chat dónde lo reciban mejor 🍁")
#		if ctx.message.content.startswith("main"):
#			ctx.send("Main")
#		if ctx.message.content.startswith("Main"):
#			ctx.send("Main")
		#if ctx.message.content.startswith("mesi"):
			#ctx.reply("es un inutil")
		#if ctx.message.content.startswith("Mesi"):
			#ctx.reply("Es un inutil")
		#if ctx.message.content.startswith("messi"):
			#ctx.reply("es un inutil")
		#if ctx.message.content.startswith("Messi"):
		if ctx.message.content.startswith("Hola"):
			lista = ["Adios", "HOLAAAAAAAA, Si eres fan de kunno porfa alejate de mi"]
			rsp = rd.choice(lista)
			ctx.send(rsp)
		if ctx.message.content.startswith("hola"):
			lista = ["Adios", "HOLAAAAAAAA, Si eres fan de kunno porfa alejate de mi"]
			rsp = rd.choice(lista)
			ctx.send(rsp)
		if ctx.message.content==("@yo"):
			ctx.send(ctx.author.nickname)

@bot.on_error()
def error(error: Exception):
 	print(f"An error has occurred: {error}")

bot.run(email, password)
