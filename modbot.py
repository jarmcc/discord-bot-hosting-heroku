import discord
from discord.ext import commands
import time
import asyncio

serverid = 571254725341741057
bot = commands.Bot(command_prefix = "!")
botname = "Moderation#1368"
cmdperm = ["EternalFlamePMC#0737"]
modwords = ["anal","anus","arse","ass","ballsack","balls","bastard","bitch","biatch","bloody","blowjob","blow job","bollock","bollok","boner","boob","bugger","bum","buttplug","clitoris","cock","coon","crap","cunt","dick","dildo","dyke","fag","feck","fellate","fellatio","felching","fuck","f u c k","fudgepacker","fudge packer","flange","Goddamn","homo","jerk","jizz","knobend","knob end","labia","muff","nigger","nigga","penis","piss","poop","prick","pube","pussy","queer","scrotum","sex","shit","s hit","sh1t","slut","smegma","spunk","tit","twat","vagina","wank","whore"]

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game(name = "Don't talk to me like that."))
    print("ModBot is online.")

@bot.event
async def on_message(message):
    for word in modwords:
        if word in str(message.content):
            try:
                channel = message.channel
                await message.delete()
                await channel.send(f"{message.author.mention}, the message you sent was inappropriate.")
            except discord.errors.NotFound:
                return
    await bot.process_commands(message)

@bot.command()
async def mbping(ctx):
    await ctx.send(f"Bot ping: {round(bot.latency * 1000)}ms")

@bot.command()
async def purge(ctx, amt = 10000000000000):
    if str(ctx.author) in cmdperm:
        await ctx.channel.purge(limit = amt)
    elif str(ctx.author) not in cmdperm:
        await ctx.channel.send(f"{ctx.author.mention}, you do not have access to that command.")

@bot.command()
async def mbcmds(ctx):
    embed = discord.Embed(title = "Moderation Bot Commands", description = "The following are the commands for Moderation.", color = 0x0080ff)
    embed.add_field(name = "!mbping", value = "This command is public. It returns the latency of the Moderation bot.")
    embed.add_field(name = "!purge", value = "This command is accessible to specific users. It deletes all of the messages in a channel.")
    embed.add_field(name = "!kick @Person#1234", value = "This command is accessible to specific users. It kicks a member for 5 minutes.")
    embed.add_field(name = "!mute @Person#1234", value = "This command is accessible to specific users. It mutes a member for 5 minutes.")
    embed.add_field(name = "!unmute @Person#1234", value = "This command is accessible to specific users. It unmutes a member.")
    embed.add_field(name = "!ban @Person#1234", value = "This command is accessible to specific users. It bans a member.")
    embed.add_field(name = "!unban Person#1234", value = "This command is accessible to specific users. It unbans a member. Do take note that you don't need to mention that user, which means no @.")
    embed.set_author(name = "Moderation", icon_url = "https://cdn.discordapp.com/avatars/574535936956956673/97d42f404990ed27c8d99287d7537522.png?size=256&")
    await ctx.author.send(embed = embed)

@bot.command()
async def kick(ctx,member : discord.Member, *, reason = None):
    if str(ctx.author) in cmdperm:
        await member.send(f"{member.mention}, you have been kicked from RbxScripting, this is the reason why: {reason}")
        await member.kick(reason = reason)
        await ctx.author.send(f"{ctx.author.mention}, you have kicked {member.mention} for: {reason}")
    elif str(ctx.author) not in cmdperm:
        await ctx.channel.send(f"{ctx.author.mention}, you do not have access to that command.")

@bot.command()
async def mute(ctx,member : discord.Member, *, reason = None):
    if str(ctx.author) in cmdperm:
        role = discord.utils.get(ctx.guild.roles, name = "Muted")
        await member.add_roles(role)
        await member.send(f"{member.mention}, you have been muted from RbxScripting, this is the reason why: {reason}")
        await member.send(f"{member.mention}, you will be able to chat in 5 minutes. We are currently counting.")
        await ctx.author.send(f"{ctx.author.mention}, you have muted {member.mention} for: {reason}")
        await asyncio.sleep(300)
        await member.remove_roles(role)
    elif str(ctx.author) not in cmdperm:
        await ctx.channel.send(f"{ctx.author.mention}, you do not have access to that command.")

@bot.command()
async def unmute(ctx,member : discord.Member, *, reason = None):
    if str(ctx.author) in cmdperm:
        role = discord.utils.get(ctx.guild.roles, name = "Muted")
        await member.send(f"{member.mention}, you have been unmuted from RbxScripting, this is the reason why: {reason}")
        await ctx.author.send(f"{ctx.author.mention}, you have unmuted {member.mention} for: {reason}")
        await member.remove_roles(role)
    elif str(ctx.author) not in cmdperm:
        await ctx.channel.send(f"{ctx.author.mention}, you do not have access to that command.")

@bot.command()
async def ban(ctx,member : discord.Member, *, reason = None):
    if str(ctx.author) in cmdperm:
        await member.send(f"{member.mention}, you have been banned from RbxScripting, this is the reason why: {reason}")
        await member.ban(reason = reason)
        await ctx.author.send(f"{ctx.author.mention}, you have banned {member.mention} for: {reason}")
    elif str(ctx.author) not in cmdperm:
        await ctx.channel.send(f"{ctx.author.mention}, you do not have access to that command.")

@bot.command()
async def unban(ctx, *, member, reason = None):
    if str(ctx.author) in cmdperm:
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user, reason = reason)
                await user.send(f"{member.mention}, you have been unbanned from RbxScripting this is the reason why: {reason}")
                await ctx.author.send(f"{ctx.author.mention}, you have unbanned {member.mention} for: {reason}")
    elif str(Ctx.author) not in cmdperm:
        await ctx.channel.send(f"{ctx.author.mention}, you do not have access to that command.")

bot.run("NTc0NTM1OTM2OTU2OTU2Njcz.XNaiyg.-ES2d6LFfwmyqLku6QXKWRGhAmw")
