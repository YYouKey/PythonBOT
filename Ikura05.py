import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "雑談部屋": # We check to make sure we are sending the message in the general channel
            await channel.send(f"""撃 エンジョイ組へようこそ {member.mention}様！(≧▽≦)ﾉｼ\n\
まず第五人格チャンネルの”ルール”という所に目を通してください！( *´艸｀)\n\
目を通したらそれぞれグッとボタンを押しましょう！⋆⸜(* ॑꒳ ॑* )⸝\n\
そして”自己紹介”という所で自己紹介もお忘れなく！(✿´꒳`)ﾉ°+.*\n\
自己紹介の文章は長めに書いてくれると個人的に嬉しいです～«٩(´ ꒳ ｀)۶»\n\
ほかの方々がやられているようにプロフ画像もちゃんと貼りましょう！₍₍ ( ๑॔˃̶◡ ˂̶๑॓)◞♡\n\
レッツエンジョイ！٩(ˊᗜˋ*)و""")

            

            
@client.event
async def on_message(message):
#    print('Message from {0.author}: {0.content} in {0.channel}'.format(message))
    if message.author == client.user:
        return

    if message.content.startswith('Hi'):
       await message.channel.send('こんにちは！お邪魔しております！')
    if message.content.startswith('やゆよよよasdf'):
       await message.channel.send('始めまして！٩(*´︶`*)۶\n家政婦のいくらと申します\
！(ﾉ*>∀<)ﾉ\nサーバー運営スタッフであるMentaukoさん手作りのBot\
となりますので、暴走することもありますが\
ご了承ください！๐·°(৹˃ᗝ˂৹)°·๐\n基本的にMentaukoさんがログインしている間に\
インしています！(*´∀`*)\nmentionの付いていない簡単な単語に\
反応します！(⑅•ᴗ•⑅)\n「Ikura」と呼んでいただける\
と軽い自己紹介をします！\n何卒宜しくお願い致します！！！レッツエンジョイ！٩(ˊᗜˋ*)و')
    if message.content.startswith('Ikura'):
       await message.channel.send('始めまして！いくらと申します！٩(*´︶`*)۶\n\
Mentaukoさんの部下に当たります！よろしくお願いします！(*ﾟ▽ﾟ)ﾉ\n\
私はサイコロを振ることができます！「D3」「D4」「D5」「D6」「D8」「D10」「D20」「D100」\
と打ってみてください！\nコイントスもできます！「coin」と打ってください！\n\
簡単な単語に反応しますが、他に言葉を教えてくれる方はぜひMentaukoさんに\
相談してみてください！Mentaukoさん経由で言葉を勉強します！(*´∇`*)\
何卒よろしくお願いします！！！')
       
    if message.content.startswith('疲れた'):
       await message.channel.send('お疲れ様です！ゆっくり休んでください！')
    if message.content.startswith('めたうんこ'):
       await message.channel.send('やめましょう！Mentaukoさんが傷つきますよっ！\
我慢の限界が近いそうです！！！！')
    if message.content.startswith('攻撃'):
       await message.channel.send('ﾊﾟｰﾝﾁ!(oﾟДﾟ)=======O三★)ﾟ◇ﾟ)三★))ﾟ□ﾟ)三★))ﾟ○ﾟ)')
    if message.content.startswith('オラオラ'):
       await message.channel.send('ｵﾗｵﾗｵﾗｵﾗ (三・o・)三☆三(｀ε´三)無駄無駄無駄無駄')
    if message.content.startswith('めんさ'):
       await message.channel.send('Mentaukoさんはサボり中です！\
邪魔しないであげてください！')
    if message.content.startswith('めんた'):
       await message.channel.send('Mentaukoさんはサボり中です！\
邪魔しないであげてください！')
    if message.content.startswith('Ment'):
       await message.channel.send('Mentaukoさんは今とても忙しいです！')
    if message.content.startswith('ゆーま'):
       await message.channel.send('ゆーまさんは電波が悪くて繋がりません!')
    if message.content.startswith('ゆうま'):
       await message.channel.send('ゆーまさんは電波が悪くて繋がりません!')
    if message.content.startswith('遊楽'):
       await message.channel.send('？？？「やめてください！セクハラですよ！」')
    if message.content.startswith('あの'):
       await message.channel.send('あのさん！呼ばれていますよっ！！！')
    if message.content.startswith('ようこそです！'):
       await message.channel.send('よろしくお願いします！\n\
撃 エンジョイ組へようこそ！')
    if message.content.startswith('君の名は'):
       await message.channel.send('イクラと申します！以後お見知りおきを！')
    if message.content.startswith('防御'):
       await message.channel.send('(((（（≪≪☆＼(≧▽≦)／☆≫≫））)))ﾊﾞﾘｱ!!')
    if message.content.startswith('ガクブル'):
       await message.channel.send('((((；ﾟДﾟ))))ｶﾞｸｶﾞｸﾌﾞﾙﾌﾞﾙ')
    if message.content.startswith('ゆき'):
       await message.channel.send('ゆきさんから伝言です！【「Cafe＆Bar vinculum」へよう\
こそ。ゆったりとした時間をお過ごし下さいませ。】')
    if message.content.startswith('にや'):
       await message.channel.send('(￣ー￣)ﾆﾔﾘ')
    if message.content.startswith('ニヤ'):
       await message.channel.send('(￣ー￣)ﾆﾔﾘ')
    if message.content.startswith('おなかす'):
       await message.channel.send('(๑･﹃ ･｀๑)ｼﾞｭﾙﾘ')
    if message.content.startswith('腹減'):
       await message.channel.send('(๑･﹃ ･｀๑)ｼﾞｭﾙﾘ')
    if message.content.startswith('波動拳'):
       await message.channel.send('(ﾉ ﾟДﾟ){======◎波動拳!!')
    if message.content.startswith('敬礼'):
       await message.channel.send('(￣^￣)ゞピッ')
    if message.content.startswith('ﾁﾗ'):
       await message.channel.send('|ω･`)ﾁﾗｯ')
    if message.content.startswith('♪'):
       await message.channel.send('(/_ _ )/♪へ(-。-へ)♪(/_ _ )/')
    if message.content.startswith('メモ'):
       await message.channel.send('((((…φ(｀･ω･´)φ…))))ﾋｯｻﾂ両手ｶｷｺ!!')

    '''
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    if message.content.startswith(''):
       await message.channel.send('')
    '''
    if message.content.startswith('こんにち'):
       msg = message.author.mention + "さん こんにちは！"
       await message.channel.send(msg)
    if message.content.startswith('おはよ'):
       msg = message.author.mention + "さん おはようございます！"
       await message.channel.send(msg)
    if message.content.startswith('こんばん'):
       msg = message.author.mention + "さん こんばんは！"
       await message.channel.send(msg)
    if message.content.startswith('おやす'):
       msg = message.author.mention + "さん おやすみなさい！"
       await message.channel.send(msg)

    
    if message.content == 'D3':
            dice = random.randint(1,3)
            await message.channel.send(str(dice))
    if message.content == 'D100':
            dice = random.randint(1,100)
            await message.channel.send(str(dice))
    if message.content == 'D10':
            dice = random.randint(1,10)
            await message.channel.send(str(dice))
    if message.content == 'D6':
            dice = random.randint(1,6)
            await message.channel.send(str(dice))
    if message.content == 'D4':
            dice = random.randint(1,4)
            await message.channel.send(str(dice))
    if message.content == 'D5':
            dice = random.randint(1,100)
            await message.channel.send(str(dice))
    if message.content == 'D20':
            dice = random.randint(1,100)
            await message.channel.send(str(dice))
    if message.content == 'D8':
            dice = random.randint(1,100)
            await message.channel.send(str(dice))
    if message.content == 'coin':
        dice = random.randint(1,2)
        if dice == 1:
            await message.channel.send('表')
        else:
            await message.channel.send('裏')


       
#    if message.content.startswith('めんた'):
#       await message.channel.send('Hello!')
#    if message.content.startswith('めんた'):
#       await message.channel.send('Hello!')
#    if message.content.startswith('めんた'):
#       await message.channel.send('Hello!')

client.run('NjE2MzAwOTMxMDA4NjkyMjM0.XWamDA.f_ydLnQ8h9E6FBzZFt8ltX8v10I')

