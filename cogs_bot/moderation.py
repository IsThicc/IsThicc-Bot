#
#                          IsThicc-bot Tickets.py | 2020-2021 (c) IsThicc
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
import discord, asyncio
from discord.ext import commands
from discord import Embed as em
from datetime import datetime
import random, string
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot     = bot
        self.db      = bot.db

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.has_guild_permissions(ban_members=True)
    @commands.cooldown(1, 1, commands.BucketType.user)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason = "Banned from IsThicc Software"):
        self.avatar = self.bot.user.avatar_url

        lets_make_sure = em(
            title=f"Are you sure you want to ban {member.display_name}?",
            colour=discord.Colour.dark_red(),
            timestamp=datetime.utcnow()
        )
        lets_make_sure.set_footer(
            icon_url=self.avatar,
            text="IsThicc Moderation"
        )
        msg = await ctx.send(embed=lets_make_sure)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')

        try:
            print('e1')
            def yes_no(reaction, user):
                return user.id == ctx.author.id and reaction.channel.id == ctx.channel.id
            print('e2')
            reaction, user = await self.bot.wait_for('reaction_add', check=yes_no) # , timeout=60)
            print('e')

        except asyncio.TimeoutError:

            timeout = em(
                title="Timed out!",
                description="You timed out! make sure to react within 60 seconds next time!",
                colour=discord.Colour.red(),
                timestamp=datetime.utcnow()
            )
            timeout.set_footer(
                icon_url=self.avatar,
                text="IsThicc Moderation"
            )
            await msg.clear_reactions()
            return await msg.edit(embed=timeout)

        await msg.clear_reactions()
        emoji = str(reaction.emoji)

        print(emoji)
        if emoji == '👍':

            bye_hoe = em(
                title="You have been banned from IsThicc Software!",
                colour=discord.Colour.red(),
                timestamp=datetime.utcnow()
            )
            bye_hoe.add_field(
                name="Reason:",
                value=reason
            )
            bye_hoe.add_field(
                name="Banned by:",
                value=ctx.author
            )
            bye_hoe.set_footer(
                icon_url=self.avatar,
                text="IsThicc Moderation"
            )
            try:

                await member.send(embed=bye_hoe)
                await member.ban(reason=reason)

            except Exception:
                ohno = em(
                    title="Uh oh!",
                    description=f"Sorry! I couldn't ban {member.mention}! Please make sure I have proper permissions!",
                    colour=discord.Colour.red(),
                    timestamp=datetime.utcnow()
                )
                ohno.set_footer(
                    icon_url=self.avatar,
                    text="IsThicc Moderation"
                )
                return await msg.edit(embed=ohno)

            return await msg.edit(embed=em(
                title="Banned!",
                description=f"I banned {member} for {reason}!",
                colour=discord.Colour.green(),
                timestamp=datetime.utcnow()
            ).set_footer(
                icon_url=self.avatar,
                text="IsThicc Moderation"
            ))

        else:
            return await msg.edit(embed=em(
                title=f"I won't ban {member}!",
                colour=discord.Colour.green(),
                timestamp=datetime.utcnow()
            ).set_footer(
                icon_url=self.avatar,
                text="IsThicc Moderation"
            ))

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.has_guild_permissions(kick_members=True)
    @commands.cooldown(1, 1, commands.BucketType.user)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason = "Kicked from IsThicc Software"):

        lets_make_sure = em(
            title=f"Are you sure you want to kick {member.display_name}?",
            colour=discord.Colour.dark_red(),
            timestamp=datetime.utcnow()
        )
        lets_make_sure.set_footer(
            icon_url=self.bot.user.avatar_url,
            text="IsThicc Moderation"
        )
        msg = await ctx.send(embed=lets_make_sure)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')

        try:

            def yes_no(reaction, user):
                return user.id == ctx.author.id and reaction.channel.id == ctx.channel.id

            reaction, user = await self.bot.wait_for('reaction_add', check=yes_no, timeout=60)

        except asyncio.TimeoutError:

            await msg.clear_reactions()
            return await msg.edit(embed=em(
                title="Timed out!",
                description="You timed out! make sure to react within 60 seconds next time!",
                colour=discord.Colour.red(),
                timestamp=datetime.utcnow()
            ).set_footer(
                icon_url=self.bot.user.avatar_url,
                text="IsThicc Moderation"
            ))

        await msg.clear_reactions()
        emoji = str(reaction.emoji)

        if emoji == '👍':

            try:

                await member.send(embed=em(
                    title="You have been kicked from IsThicc Software!",
                    colour=discord.Colour.red(),
                    timestamp=datetime.utcnow()
                ).add_field(
                    name="Reason:",
                    value=reason
                ).add_field(
                    name="Kicked by:",
                    value=ctx.author
                ).set_footer(
                    icon_url=self.avatar,
                    text="IsThicc Moderation"
                ))
                await member.ban(reason=reason)

            except Exception:
                return await msg.edit(embed=em(
                    title="Uh oh!",
                    description=f"Sorry! I couldn't kick {member.mention}! Please make sure I have proper permissions!",
                    colour=discord.Colour.red(),
                    timestamp=datetime.utcnow()
                ).set_footer(
                    icon_url=self.bot.user.avatar_url,
                    text="IsThicc Moderation"
                ))

            return await msg.edit(embed=em(
                title="Kicked!",
                description=f"I kicked {member} for {reason}!",
                colour=discord.Colour.green(),
                timestamp=datetime.utcnow()
            ).set_footer(
                icon_url=self.bot.user.avatar_url,
                text="IsThicc Moderation"
            ))

        else:
            return await msg.edit(embed=em(
                title=f"I won't kick {member}!",
                colour=discord.Colour.green(),
                timestamp=datetime.utcnow()
            ).set_footer(
                icon_url=self.bot.user.avatar_url,
                text="IsThicc Moderation"
            ))

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.has_role(744012353808498808)
    @commands.cooldown(1, 1, commands.BucketType.user)
    @commands.command()
    async def warn(self, ctx, member: discord.Member, *, reason = "No reason specified."):

        await ctx.send(embed=em(
            title="Warned!",
            description=f"I warned {member.mention} for {reason}!",
            colour=discord.Colour.green(),
            timestamp=datetime.utcnow()
        ).set_footer(
            icon_url=self.bot.user.avatar_url,
            text="IsThicc Moderation"
        ))
        await member.send(embed=em(
            title="You have been warned in IsThicc Software!",
            colour=discord.Colour.red(),
            timestamp=datetime.utcnow()
        ).set_footer(
            icon_url=self.bot.user.avatar_url,
            text="IsThicc Moderation"
        ))

        warn_id = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(15))
        await self.db.warn(ctx.author.id, reason, datetime.utcnow(), True, warn_id)

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @commands.has_role(739510850079162530)
    @commands.cooldown(1, 1, commands.BucketType.user)
    @commands.command()
    async def unwarn(self, ctx, member: discord.Member, warnid: str):

        try:
            await self.db.unwarn(warnid)
            return await ctx.send(embed=em(
                title="Unwarned!",
                description=f"I removed the warning `{warnid}` for {member.mention}!",
                colour=discord.Colour.green(),
                timestamp=datetime.utcnow()
            ).set_footer(
                icon_url=self.bot.user.avatar_url,
                text="IsThicc Moderation"
            ))
        except Exception as e:
            print(e)
            return await ctx.send(embed=em(
                title="Error!",
                description=f"An internal error has occurred! Sorry about this!",
                colour=discord.Colour.red(),
                timestamp=datetime.utcnow()
            ).set_footer(
                icon_url=self.bot.user.avatar_url,
                text="IsThicc Moderation"
            ))

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
    @ban.error
    @kick.error
    @warn.error
    @unwarn.error
    async def mod_error(self, ctx, error):

        if isinstance(error, commands.MissingRole):
            return await ctx.send(embed=em(
                title="Missing Permissions!",
                description="Sorry! This command is only for staff members!",
                colour=discord.Colour.red(),
                timestamp=datetime.utcnow()
            ).set_footer(
                icon_url=self.bot.user.avatar_url,
                text="IsThicc"
            ))

        if isinstance(error, commands.MissingPermissions):
            return await ctx.send(embed=em(
                title="Sorry! You don't have permission!",
                timestamp=datetime.utcnow(),
                colour=discord.Colour.red()
            ).set_footer(
                icon_url=self.bot.user.avatar_url,
                text="IsThicc Moderation"
            ))

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
def setup(bot):
    bot.add_cog(mod(bot))
