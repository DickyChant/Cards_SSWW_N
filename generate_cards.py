import os
for mass in [1500,1750,2000,2500,5000,7500,10000,15000,20000]:
    carddir = f"cards_4_scan/HeavyN_SSWW_MuMu_onlyVmuN1_M{mass}"
    os.mkdir(carddir)
    for name in os.listdir("cards"):
        if "param_card" in name:
            continue
        items = name.split("_")
        items = items[:4] + [f"M{mass}"] + items[4:]
        str_ = "_"
        newname = str_.join(items)
        if "custom" in name:
            with open(f"cards/{name}","r") as f:
                rc = f.read().replace('set param_card  mass 9900012 3.000000e+02',f'set param_card  mass 9900012 {mass:e}')
                with open(f"{carddir}/{newname}","w") as wf:
                    wf.write(rc)
                    wf.close()
                f.close()
        else:
            os.system(f"cp cards/{name} {carddir}/{newname}")

            