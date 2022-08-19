
from email import message
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord import member
import asyncio
import random

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix= "*", intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("I am a online")
    await bot.change_presence(activity=discord.Game(name = "*help"))
    print("My status is on")

#-------------------------------------------------------------------------------------------------------------

@bot.command()
async def verify(ctx):
    await ctx.channel.purge(limit = ilosc1)
    embed = discord.Embed(title="**WERYFIKACJA")
    embed.add_field(name="**Aby sie zweryfikować kliknij emoij/reakcje '✅'**",value="*Dzięki weryfikacji otrzymasz dostęp do reszty kanałów na tym serwerze.*", inline=False)
    embed.set_footer(text="Bot: MKM#8907")
    msg = await ctx.send(embed = embed)
    await msg.add_reaction('✅')



@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 1010146096883961967:
        if payload.emoji.name == '✅':
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            rola = guild.get_role(1009910687012749362)
            await member.add_roles(rola)





#-------------------------------------------------------------------------------------------------------------

@bot.command()
async def selfrole1(ctx):
    await ctx.channel.purge(limit = ilosc1)
    embed = discord.Embed(title="Sefl Role Płeć")
    embed.add_field(name="**Chłopak = 👦🏽**",value="*Wybirz tą role jeśli jesteś płci męskiej.*", inline=False)
    embed.add_field(name="**Dziewczyna = 👧🏽**",value="*Wybirz tą role jeśli jesteś płci żeńskiej.*", inline=False)
    embed.add_field(name="**Helikopter = 🚁**",value="*Wybirz tą role jeśli jesteś helikopterem bojowym.*", inline=False)
    embed.set_footer(text="Bot: MKM#8907")
    msg = await ctx.send(embed =embed)
    await msg.add_reaction('👦🏽')
    await msg.add_reaction('👧🏽')
    await msg.add_reaction('🚁')





    



@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 1010269737030275164:
        if payload.emoji.name == '👦🏽':
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            rola = guild.get_role(1010269896409612298)
            await member.add_roles(rola)
        if payload.emoji.name == '👧🏽':
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            rola1 = guild.get_role(1010269949069103155)
            await member.add_roles(rola1)
        if payload.emoji.name == '🚁':
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            rola2 = guild.get_role(1010269952399392858)
            await member.add_roles(rola2)


@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 1010269737030275164:
        if payload.emoji.name == '👦🏽':
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            rola = guild.get_role(1010269896409612298)
            await member.remove_roles(rola)
        if payload.emoji.name == '👧🏽':
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            rola1 = guild.get_role(1010269949069103155)
            await member.remove_roles(rola1)
        if payload.emoji.name == '🚁':
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            rola2 = guild.get_role(1010269952399392858)
            await member.remove_roles(rola2)
            






#✅

#commands

#-------------------------------------------------------------------------------------------------------------

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Użyłeś Komende help")
    embed.add_field(name="***help**",value="*Pokazuje liste komend.*", inline=True)
    embed.add_field(name="***clear [ilość]**",value="*Usuwa daną ilość wiadomości.*", inline=True)
    embed.set_footer(text="Bot: MKM#8907")
    await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------------------------------

@bot.command()
async def clear(ctx, ilosc : int):
    await ctx.channel.purge(limit = ilosc)
    await ctx.channel.send(f"**Usunięto {ilosc} wiadomości**")
    await asyncio.sleep(5)
    await ctx.channel.purge(limit =ilosc1)

#-------------------------------------------------------------------------------------------------------------

@bot.command()
@has_permissions(ban_members=True)
async def kick(ctx, member : discord.Member,reason="**Brak Powodu**"):
    await member.kick(reason=reason)
    print(f"{member} is kicked, reason: {reason}")
    embed=discord.Embed(title="Użyłeś Komende Ban")
    embed.add_field(name=f"Wyrzuciłeś Użytkownika {member} ",value=f"Powód: {reason}", inline=False)
    embed.set_footer(text="Bot: MKM#8907")
    await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------------------------------

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member,reason="**Brak Powodu**"):
    await member.ban(reason=reason)
    print(f"{member} is banned, reason: {reason}")
    embed1=discord.Embed(title="Użyłeś Komende Ban")
    embed1.add_field(name=f"Zbanowałeś Użytkownika {member} ",value=f"Powód: {reason}", inline=False)
    embed1.set_footer(text="Bot: MKM#8907")
    await ctx.send(embed=embed1)


#EVENTY

#-------------------------------------------------------------------------------------------------------------
ilosc1 = 1  
ilosc2 = 2



@bot.event
async def on_message(message):
    words = ["JD", "jd", "JEBAĆ", "KURWA"]
    for i in words:             
        if i == message.content:
            await message.channel.purge(limit=ilosc1)
            await message.channel.send("**NIE PISZ TAK!**") 
            print(f"{message.author} broke the rules")
            await asyncio.sleep(5)   
            await message.channel.purge(limit = ilosc1)
    await bot.process_commands(message)

#-------------------------------------------------------------------------------------------------------------

@bot.event
async def on_member_join(member):
    przywitanie = ["witamy na pokładzie!" , "dołączył do drużyny!" , "przybył do naszej galaktyki!" , "wszedł na serwer!"]
    guild = bot.get_guild(1008088227393052813) 
    welcome_channel = guild.get_channel(1009898069552283729)  
    rola = guild.get_role(1009899340610932817)
    przywitanie_g = random.choice(przywitanie)
    print(f"{member} joined to server")
    await member.add_roles(rola)
    await welcome_channel.send(f"**{member}** *{przywitanie_g}*")

#-------------------------------------------------------------------------------------------------------------

@bot.event
async def on_member_remove(member):
    porzegnanie = ["wyleciał za burte!" , "odszedł z drużyny!" , "odleciał z  naszej galaktyki!" , "wyszedł z serwera!"]
    guild = bot.get_guild(1008088227393052813) 
    welcome_channel = guild.get_channel(1009898101307363338)  
    porzegnanie_g = random.choice(porzegnanie)
    print(f"{member} gone to server")
    await welcome_channel.send(f"**{member}** *{porzegnanie_g}*")

#-------------------------------------------------------------------------------------------------------------


#Please leave this command
@bot.command()
async def code(ctx):
    embed=discord.Embed(title="Code Bota", url="https://github.com/Morus21/Easy-Bot-For-Discord/blob/main/EBFD.PY")
    embed.add_field(name="Author = Morus#3085", value="Code opublikowany na github.", inline=False)
    embed.set_footer(text="Bot: MKM#8907")
    await ctx.send(embed=embed)


bot.run(":D")

#Morus 2022 
