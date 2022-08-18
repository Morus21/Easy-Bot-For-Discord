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
        msg = await ctx.send("**Aby sie zweryfikować kliknij emotikon '✅' pod wiadomością**")
        ctx.send(msg)
        await msg.add_reaction('✅')



@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 1009907963240128654:
        if payload.emoji.name == '✅':
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            rola = guild.get_role(1009910687012749362)
            await member.add_roles(rola)



#✅

#commands

#-------------------------------------------------------------------------------------------------------------

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Użyłeś Komende Ban")
    embed.add_field(name="***help**",value="*Pokazuje liste komend.*", inline=True)
    embed.add_field(name="***clear [ilość]**",value="*Usuwa daną ilość wiadomości.*", inline=True)
    embed.set_footer(text="Morus Bot")
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
    embed.set_footer(text="Morus Bot")
    await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------------------------------

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member,reason="**Brak Powodu**"):
    await member.ban(reason=reason)
    print(f"{member} is banned, reason: {reason}")
    embed1=discord.Embed(title="Użyłeś Komende Ban")
    embed1.add_field(name=f"Zbanowałeś Użytkownika {member} ",value=f"Powód: {reason}", inline=False)
    embed1.set_footer(text="Morus Bot")
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


bot.run(":D")

#Morus 2022 
