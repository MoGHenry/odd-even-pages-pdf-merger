import discord
import os
from discord.ext import commands
from discord import app_commands


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=785936637615013888))
    print(f'Logged on as {client.user}!')


@tree.command(name="hello",
              description="My first application Command",
              guild=discord.Object(id=785936637615013888))
async def first_command(interaction):
    await interaction.response.send_message("Hello!")


@tree.command(name="novel", description="find downloadable novel online", guild=discord.Object(id=785936637615013888))
async def find_novel(interaction, args1: str, args2: str):
    await interaction.response.send_message(f"I am trying!\nYour parameter 1 is {args1}\nYour parameter 2 is {args2}")

client.run('MTEzMzY0MjgyMTU2MDE4MDgzNw.GuX0jH.E8MNRM0RlFhr1VkFYnBMf3v7jkkKCQuVhm4oTQ')
