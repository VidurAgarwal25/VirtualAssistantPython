import datetime
import winsound

def alarm(tt):
    altime=str(datetime.datetime.now().strptime(tt,"%I:%M %p"))
    altime=altime[11:-3]
    horeal=altime[:2]
    horeal=int(horeal)
    Mireal=altime[3:5]
    Mireal=int(Mireal)

    print(f"Done, alarm is set for {tt}")

    while True:
        if horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("alarm is running")
                winsound.PlaySound('abc',winsound.SND_LOOP)
            elif Mireal<datetime.datetime.now().minute:
                break