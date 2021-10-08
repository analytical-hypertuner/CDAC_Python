import mypkg.mymod
import importlib
import myclient

print("Start of Changer after imports of mypkg.mymod, and myClient")
# mypkg.mymod.countChars(mypkg.mymod.actual)
mypkg.mymod.test(mypkg.mymod.actual)

print("RELOADING MyMoD... .. . .")

importlib.reload(mypkg.mymod)

print("Just RELOADED MyMoD... .. .")
print("End of Changer, last print statement.")
