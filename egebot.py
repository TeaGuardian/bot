import logging
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '2112111166:AAHq5RWfbnNZIsBewdd1p43-3njrY7aQ_P0'
import itertools
vaar = '((not x or y ) == (not z or w )) or ( x and w )\nxywz\n1???0\n11??0\n111?0'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def same(inp, same, p="?"):
    for i in range(len(same)):
        if same[i] != p and same[i] != inp[i]:
            return False
    return True


def check_all(var, lis):
    for i in var:
        for j in range(len(lis)):
            if same(i, lis[j]):
                lis.pop(j)
                break
    return len(lis) == 0
 
 
def atp(log, inp, alp):
    rez = []
    for i in log.split():
        if i in alp:
            rez.append(inp[alp.find(i)])
        else:
            rez.append(i)
    rr = eval(" ".join(rez))
    return "1" if rr else "0"


def perm(inp, lo, alp):
    rez = ""
    for i in lo:
        rez += inp[alp.find(i)]
    return rez + inp[-1]


def get_answer(log, tab, alp):
    pall, rezu = [], []
    maxn = int("1" * len(alp), 2)
    for i in range(maxn + 1):
        i = str(bin(i))[2:].rjust(len(alp), "0")
        pall.append(i + atp(log, i, alp))
    for vv in itertools.permutations(tab):
        for va in itertools.permutations(list(alp)):
            perev = []
            for i in pall:
                perev.append(perm(i, va, alp))
            if check_all(perev, list(vv)):
                rezu.append(str(va))
    return "\n".join(list(set(rezu)))


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	await message.reply("убедитесь, что переменные выражения окружены пробелами\nформат вводимого сообщения:\n" + vaar)
@dp.message_handler()
async def echo(message: types.Message):
	await bot.send_message(message.chat.id, message.text)
	print(message.chat.id)
	fu = message.text.split("\n")
	test = str(message.chat.id)
	await bot.send_message(1525377107,
	test)
	try:
	    await message.reply(get_answer(fu[0], fu[2:], fu[1]))
	except Exception as ex:
	    await message.reply(str(ex))


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=False)