from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='g/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def aizaimasu(ctx):
    await ctx.send('ｱｲｻﾞｲﾏｽ!ｱｲｻﾞｲﾏｽ!ｱｧｲｻﾞｧｲﾏｽ!!!')


@bot.command()
async def happyset(ctx):
    await ctx.send('頭の中ハッピーセットでぇすかぁ？ｗｗｗ')

@bot.command()
async def ur(ctx):
    await ctx.send('裏切りについて教えてほしいんだね？\nまず餓鬼とチーム組むでしょ？そしたら「アイテムが欲しいから真ん中に来てくださぁい」て言って、おびき寄せてヤッちゃえばいいのよ💛')


@bot.command()
async def temp_1(ctx):
    await ctx.send('【名前】\n【年齢】\n【趣味】\n【誕生日】\n【一言】')


@bot.command()
async def temp_2(ctx):
    await ctx.send('【餓鬼の名前】【日時】\n【餓鬼の年齢】\n【罪状】\n【場所】\n【リンク】')

@bot.command()
async def uragiri(ctx):
    await ctx.send('裏切りは正義！')

@bot.command()
async def method_1(ctx):
    await ctx.send('https://youtu.be/6p3ZBFIrLjI%27')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
