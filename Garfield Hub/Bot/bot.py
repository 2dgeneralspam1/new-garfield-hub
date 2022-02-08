import discord
from discord.ext import commands
import os

prefix = "!"
client = commands.Bot(command_prefix=prefix)

client.remove_command("help")
confirmEmoji = '\U00002705'    

@client.event
async def on_ready():
    print("Garfield Bot is ready!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Garfield Hub'))

@client.command(aliases= ['purge','delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command(name="kick", aliases=["Kick", "KICK"])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if member == ctx.author:
        await ctx.send("You can't kick yourself!")
    else:
        embed = discord.Embed(colour=0xBE33FF)

        embed.set_author(name=f'User Kicked | {member}', icon_url=member.avatar_url)
        embed.add_field(name='User', value=f'{member.mention}', inline=True)
        embed.add_field(name='Moderator',value=f'{ctx.author.mention}', inline=True)
        embed.add_field(name='Reason', value=f'{reason}', inline=True)
        
        embed2 = discord.Embed(description=f'**You were kicked from {ctx.guild.name}**', colour=0xBE33FF)
        embed2.add_field(name='Reason', value=f'{reason}', inline=True)
        embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)
    
        await ctx.send(embed=embed)                  
        await member.send(embed=embed2)                   
        await member.kick(reason=reason)
    
@client.command(name="ban", aliases=["Ban", "BAN"])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if member == ctx.author:
        await ctx.send("You can't ban yourself!")
    else:
        embed = discord.Embed(colour=0xBE33FF)

        embed.set_author(name=f'User Banned | {member}', icon_url=member.avatar_url)
        embed.add_field(name='User', value=f'{member.mention}', inline=True)
        embed.add_field(name='Moderator', value=f'{ctx.author.mention}', inline=True)
        embed.add_field(name='Reason', value=f'{reason}', inline=True)

        embed2 = discord.Embed(description=f'You were banned from {ctx.guild.name}', colour=0xBE33FF)
        embed2.add_field(name='Reason', value=f'{reason}', inline=True)
        embed2.add_field(name='Moderator', value=f'{ctx.author.name}', inline=True)

        await ctx.send(embed=embed)              
        await member.send(embed=embed2)                       
        await member.ban(reason=reason)

@client.command(name="unban", aliases=["Unban", "UNBAN"])
@commands.has_permissions(ban_members=True)
async def unban(ctx, member: discord.Member, *, reason=None):
    if member == ctx.author:
        await ctx.send("You're not banned.")
    else:
        embed = discord.Embed(colour=0xBE33FF)

        embed.set_author(name=f'User Unbanned | {member}', icon_url=member.avatar_url)
        embed.add_field(name='User', value=f'{member.mention}', inline=True)
        embed.add_field(name='Moderator', value=f'{ctx.author.mention}', inline=True)

        await ctx.send(embed=embed)              

@client.command(name="help", aliases=["Help", "HELP"])
async def help(ctx):
    embed = discord.Embed(description="List of all commands:", colour=0xBE33FF)
    
    embed.add_field(name="help", value="Shows a list of all commands.", inline=True)
    
    embed.add_field(name="kick", value="Kicks the specified user.", inline=True)

    embed.add_field(name="ban", value="Bans the specified user.", inline=True)

    embed.add_field(name="clear", value="Clears a specified amount of messages", inline=True)

    embed.add_field(name="nigger", value="Clears a specified amount of messages", inline=True)
    
    await ctx.send(embed=embed)

client.run('OTM4OTE1MDc0MTg4Mzc4MTUy.YfxOzQ.wMU1bfeRy2LR0HSY19X6jpgUs94')