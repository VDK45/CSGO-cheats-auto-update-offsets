import pymem, keyboard, time, datetime, offsets, random
from random import choice




dwGlowObjectManager = offsets.dwGlowObjectManager  # (0x531A118)
m_iGlowIndex = offsets.m_iGlowIndex  # (0x10488)
dwLocalPlayer = offsets.dwLocalPlayer  # (0xDB65EC)
dwEntityList = offsets.dwEntityList  # (0x4DD1E1C)
m_iTeamNum = offsets.m_iTeamNum  # (0xF4)
m_flFlashMaxAlpha = offsets.m_flFlashMaxAlpha #  Flash
dwForceAttack = offsets.dwForceAttack
m_iCrosshairId = offsets.m_iCrosshairId
m_fFlags = offsets.m_fFlags
dwForceJump = offsets.dwForceJump


try:
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
except:
    print("Can't find CSGO.exe")
    print("1 - Start CSGO!")
    print("2 - Find server")
    print("3 - Chose team")
    print("4 - Start triple.exe")
    print("5 - Enter 10 and more symboles")
    print("6 - Click start")
    print("7 - Ready.. = OK")
    print("-------------------")
    print("Неудалось найти CSGO.exe")
    print("1 - Запустите CSGO!")
    print("2 - Найдите сервер!")
    print("3 - Вфберите команду!")
    print("4 - Запустите triple.exe")
    print("5 - В поле ввода введите более 10 любых символов!")
    print("6 - Нажмите start")
    print("7 - Ready.. = OK")
    
    time.sleep(1)
    print("Exit")
    time.sleep(7)
    exit(0)
# initialize gui gui.window.mainloop()
#thread1 = threading.Thread(target=gui.window.mainloop(), args=())
#thread1.start()

def shot_1():
    pm.write_int(client + dwForceAttack, 6)
    
def shot_2():
    pm.write_int(client + dwForceAttack, 6)
    time.sleep((random.randint(1, 3))*0.1)
    pm.write_int(client + dwForceAttack, 6)
    
def shot_3():
    pm.write_int(client + dwForceAttack, 6)
    time.sleep((random.randint(1, 3))*0.1)
    pm.write_int(client + dwForceAttack, 6)
    time.sleep((random.randint(1, 4))*0.1)
    pm.write_int(client + dwForceAttack, 6)
    
functions = shot_1, shot_2, shot_3
shots = choice(functions)

def jump():
    if keyboard.is_pressed("space"):
        force_jump = client + dwForceJump
        player = pm.read_int(client + dwLocalPlayer)
        if player:
            on_ground = pm.read_int(player + m_fFlags)
            if on_ground and on_ground == 257:
                pm.write_int(force_jump, 5)
                time.sleep(0.08)
                pm.write_int(force_jump, 4)


def gold_eye():
    global pm
    global client
    # Flash
    player = pm.read_int(client + dwLocalPlayer)
    if player:
        flash_value = player + m_flFlashMaxAlpha
    if flash_value:
        pm.write_float(flash_value, float(0))
        
        
def glow():
    global pm
    global client
    glow_manager = pm.read_int(client + dwGlowObjectManager)
    for i in range(1, 32): # players
        entity = pm.read_int(client + dwEntityList + i * 0x10)
        if entity:
            entity_team_id = pm.read_int(entity + m_iTeamNum)
            entity_glow = pm.read_int(entity + m_iGlowIndex)
        else:
            continue
        if entity_team_id == 2:
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))
            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0))
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))
            pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)
        elif entity_team_id == 3:
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))
            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
            pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))
            pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)						
        else:
            pass


def trigger():
    global pm
    global client
    localPlayer = pm.read_int(client + dwLocalPlayer)
    crosshairID = pm.read_int(localPlayer + m_iCrosshairId)
    getTeam = pm.read_int(client + dwEntityList + (crosshairID - 1) * 0x10)
    localTeam = pm.read_int(localPlayer + m_iTeamNum)
    crosshairTeam = pm.read_int(getTeam + m_iTeamNum)
                    
    if crosshairID > 0 and crosshairID < 32 and localTeam != crosshairTeam:
        shots()


def main():
    global antivac
    global pm
    global client
    READY = ["Ready.", "Ready..", "Ready...", "Ready....", "Enjoy!", "OK", "GO", "GO GO GO!", "Start"]
    config = open('config.md', 'r')
    antivac = config.readline()  # Edit every week so Hash of the file changes
    #print(f"HASH = {antivac}")
    GLOW = config.readline().split()
    GLOW = int(GLOW[0])
    FLASH = config.readline().split()
    FLASH = int(FLASH[0])
    TRIGGER = config.readline().split()
    TRIGGER = int(TRIGGER[0])
    config.close()
    hash_changed = antivac
    current_datetime = datetime.datetime.now()
    year = current_datetime.year
    month = current_datetime.month
    if year >= 2022 and month > 6:
        print('Problem has found! Please go to https://www.patreon.com/vdk45 for update!')
        time.sleep(15)
        exit(0)
    try:
        current_datetime = datetime.datetime.now()
        year = current_datetime.year
        month = current_datetime.month
        if year >= 2022 and month > 6:
            print('Problem has found! Please go to https://www.patreon.com/vdk45 for update!')
            time.sleep(15)
            exit(0)
        print(READY[random.randint(0, (len(READY)-1))])
        
        while True:
                if keyboard.is_pressed("End"):
                    exit(0)
                if keyboard.is_pressed("F6"):
                    FLASH = 1
                if keyboard.is_pressed("F7"):
                    FLASH = 0
                if keyboard.is_pressed("F8"):
                    GLOW = 1
                if keyboard.is_pressed("F9"):
                    GLOW = 0
                if keyboard.is_pressed("F10"):
                    TRIGGER = 1
                if keyboard.is_pressed("F11"):
                    TRIGGER = 0
                try:
                    if FLASH == 1:
                        gold_eye()
                    else:
                        pass
                except:
                    pass
                try:
                    if GLOW == 1:
                        glow()
                    else:
                        pass
                except:
                    pass
                try:
                    if TRIGGER == 1:
                        trigger()
                    else:
                        pass
                except:
                    pass
                try:
                    jump()
                except:
                    pass
                time.sleep(0.002)
                    
                
    except Exception as error:
        time.sleep(5)
        exit(0)
    
        
# if __name__ == '__main__':
# 	main()
