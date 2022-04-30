import requests, re, math
from math import sqrt, pi, atan

r = requests.get("https://github.com/frk1/hazedumper/blob/master/csgo.hpp")
r = r.text

offsets = ["dwEntityList", "dwLocalPlayer","m_flFlashMaxAlpha", "m_iTeamNum",\
        "dwGlowObjectManager", "m_iGlowIndex", "dwForceJump", "m_fFlags",\
        "dwForceAttack", "m_iCrosshairId", "m_bSpotted", "m_iShotsFired",\
        "m_aimPunchAngle", "dwClientState", "dwClientState_ViewAngles",\
        "m_iObserverMode","m_bIsDefusing","m_bGunGameImmunity","m_iHealth",\
        "m_dwBoneMatrix","m_vecOrigin","m_vecViewOffset","m_bDormant",\
        "dwbSendPackets","dwInput","clientstate_last_outgoing_command",\
        "clientstate_net_channel"]

d = {}
offs = []
for i in range(len(offsets)):
    if offsets[i] in r:
        search = re.findall(str(offsets[i]) + '\s'"= (.*);", r)
        search = search[0]
        search = list(search)
        search = search[20:]
        search = search[:-7]
        search = ''.join(map(str, search))
        #print(search)
        #print(f'{offsets[i]} = {search}')
        offs.append(search)
        
i = 0
while i <= len(offsets)-1:
    (key, val) = offsets[i], offs[i]
    d[key] = val
    i += 1

dwEntityList = int(d["dwEntityList"], base = 16)
dwLocalPlayer = int(d["dwLocalPlayer"], base = 16)
m_flFlashMaxAlpha = int(d["m_flFlashMaxAlpha"], base = 16)
m_iTeamNum = int(d["m_iTeamNum"], base = 16)
dwGlowObjectManager = int(d["dwGlowObjectManager"], base = 16)
m_iGlowIndex = int(d["m_iGlowIndex"], base = 16)
dwForceJump = int(d["dwForceJump"], base = 16)
m_fFlags = int(d["m_fFlags"], base = 16)
dwForceAttack = int(d["dwForceAttack"], base = 16)
m_iCrosshairId = int(d["m_iCrosshairId"], base = 16)
m_bSpotted = int(d["m_bSpotted"], base = 16)
m_iShotsFired = int(d["m_iShotsFired"], base = 16)
m_aimPunchAngle = int(d["m_aimPunchAngle"], base = 16)
dwClientState = int(d["dwClientState"], base = 16)
dwClientState_ViewAngles = int(d["dwClientState_ViewAngles"], base = 16)
m_iObserverMode = int(d["m_iObserverMode"], base = 16)
m_bIsDefusing = int(d["m_bIsDefusing"], base = 16)
m_iHealth = int(d["m_iHealth"], base = 16)
m_bGunGameImmunity = int(d["m_bGunGameImmunity"], base = 16)
m_iDefaultFOV = (0x332C) # Welp not on Hazedumper (Special Offset)
m_totalHitsOnServer = (0xA3A8) # Welp not on Hazedumper (Special Offset)
m_dwBoneMatrix = int(d["m_dwBoneMatrix"], base = 16)
m_vecOrigin = int(d["m_vecOrigin"], base = 16)
m_vecViewOffset = int(d["m_vecViewOffset"], base = 16)
m_bDormant = int(d["m_bDormant"], base = 16)
dwbSendPackets = int(d["dwbSendPackets"], base = 16)
dwInput = int(d["dwInput"], base = 16)
clientstate_last_outgoing_command = int(d["clientstate_last_outgoing_command"], base = 16)
clientstate_net_channel = int(d["clientstate_net_channel"], base = 16)

    