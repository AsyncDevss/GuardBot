import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class GuardBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        self.owner_id = int(os.getenv("OWNER_ID", 0))

    async def on_ready(self):
        print(f"[{self.user.name}] Sunucu güvenliği için yayında.")
        await self.change_presence(activity=discord.Game(name="Güvenlik Enes tarafından sağlanmaktadır."))

    def embed_şablon(self, title, desc, color=discord.Color.red()):
        embed = discord.Embed(title=title, description=desc, color=color)
        embed.set_footer(text="Enes tarafından yapılmıştır")
        return embed

bot = GuardBot()


@bot.event
async def on_guild_channel_delete(channel):
    guild = channel.guild
    async for entry in guild.audit_logs(action=discord.AuditLogAction.channel_delete, limit=1):
        if entry.user.id in [bot.user.id, bot.owner_id]:
            return

        executor = guild.get_member(entry.user.id)
        if executor and executor.top_role < guild.me.top_role:
            await executor.ban(reason="İzinsiz kanal silme tespiti.")

        yeni_kanal = await channel.clone(reason="Guard Otomatik Geri Yükleme")
        await yeni_kanal.send(embed=bot.embed_şablon(
            title="🛡️ Kanal Koruma Sistemi",
            description=f"**{channel.name}** kanalı silindi. Silen kişi engellendi ve kanal tekrar oluşturuldu."
        ))

@bot.event
async def on_guild_role_delete(role):
    guild = role.guild
    async for entry in guild.audit_logs(action=discord.AuditLogAction.role_delete, limit=1):
        if entry.user.id in [bot.user.id, bot.owner_id]:
            return

        executor = guild.get_member(entry.user.id)
        if executor and executor.top_role < guild.me.top_role:
            await executor.edit(roles=[], reason="İzinsiz rol silme tespiti.")

@bot.event
async def on_member_ban(guild, user):
    async for entry in guild.audit_logs(action=discord.AuditLogAction.ban, limit=1):
        if entry.user.id in [bot.user.id, bot.owner_id]:
            return

        executor = guild.get_member(entry.user.id)
        if executor and executor.top_role < guild.me.top_role:
            await executor.ban(reason="Sağ tık ban limiti aşımı.")
        
        await guild.unban(user, reason="Haksız atılan ban Guard tarafından kaldırıldı.")



@bot.command(name="guard")
async def guard_status(ctx):
    await ctx.send(embed=bot.embed_şablon(
        title="🛡️ Guard Sistemi Aktif",
        description="Kanal, rol ve üye güvenliği anlık olarak bu altyapı ile korunuyor.",
        color=discord.Color.green()
    ))

if __name__ == "__main__":
    token = os.getenv("TOKEN")
    if token:
        bot.run(token)
    else:
        print("[HATA] .env dosyasında TOKEN bulunamadı.")
