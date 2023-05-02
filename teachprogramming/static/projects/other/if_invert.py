# https://www.youtube.com/shorts/Zmx0Ou5TNJs

def anyFunction():
    if (wifi):
        if (login):
            if (admin):
                seeAdminPanel()
            else:
                print("must be admin")
        else:
            print("must be logged in")
    else:
        print("must be connected")

def anyFunctiona():
    if (not wifi):
        print("must be connected")
        return
    if not login:
        print("")
        return
    if not admin:
        print()
        return
    seeAdminPanel()
