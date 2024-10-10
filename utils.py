async def control(name):
    users = {
        "Asilbek": 'Darsda bor',
        "Azizbek": 'Darsda bor',
        "Jaloliddin": 'Yoq',
    }
    try:
        return str(users[name])
    except:
        return "Bunday o'quvchi mavjud emas"
    

async def calculate(text):
    try:
        a, b = text.split("+")
        ans = int(a) + int(b)
        return str(ans)
    except Exception as e:
        return f"{e}"
