import discord
from discord.ext import commands
token="ODE3MzgzNTkzNTc5NjQyOTUw.YEItyg.rI2CKvB7_tWSfO6P2QAILYo2uxI"
bot=commands.Bot(command_prefix='!')
@bot.command(pass_context=True)
async def Poftor(ctx,arg):
    await ctx.send(arg)

@bot.command()
async def pribav (ctx,a:int,b:int):
    await ctx.send(a+b)
    
@bot.command()
async def ymn (ctx,a:int,b:int):
    await ctx.send(a*b)

@bot.command()
async def delen (ctx,a:int,b:int):
    await ctx.send(a/b)

@bot.command()
async def minys (ctx,a:int,b:int):
    await ctx.send(a-b)

@bot.command()
async def cat (ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")\

@bot.command()
async def baldesh (ctx):
    await ctx.send("https://tenor.com/view/funny-face-animals-cat-gif-20680235")

bot.remove_command('help')
@bot.command()
async def help (ctx):
    embed=discord.Embed(title="Razvlechenie bot" ,description="Спасибо что добавили! Бот может:",color=0xeee657)
    embed.add_field(name="!Poftor",value="Это команда повторяет сообщение (Которое после команды)",inline=False)
    embed.add_field(name="!pribav",value="Эта команда прибавляет числа, пример:!pribav 2 2",inline=False)
    embed.add_field(name="!ymn",value="Это команда умножает числа,пример:!ymn 2 2 ",inline=False)
    embed.add_field(name="!delen",value="Это команда делит числа,пример:!delen 2 2 ",inline=False)
    embed.add_field(name="!minys",value="Это команда отнимает числа,пример:!minys 2 2 ",inline=False)
    embed.add_field(name="!cat",value="Это команда присылает в чат гифку с котом",inline=False)
    embed.add_field(name="!baldesh",value="Это команда присылает в чат гифку с котом который балдеет",inline=False)
    embed.add_field(name="!info",value="Это команда присылает информацию о боте",inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def info (ctx):
    embed=discord.Embed(title="Razvlechenie bot" ,description="Спасибо что добавили!Информация о боте в низу",color=0xeee657)
    embed.add_field(name="Автор:",value="✰Asͥђlͣeͫץ✰#8537")
    embed.add_field(name="Бот был создан для: ",value="Для развлечения, для упрощение жизни и крч топ бот")
    embed.add_field(name="Связь с мной:",value="Дискорд: ✰Asͥђlͣeͫץ✰#8537")
    await ctx.send(embed=embed)

    






bot.run(token)

