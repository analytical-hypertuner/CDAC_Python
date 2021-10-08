from mypkg.mymod import countChars
import mypkg.mymod

actual = "D:\\PG-DAI\\LAB\\Lab 6\\mypkg\\new.txt"
print("Start of MyClient, myClient import successful!")

print(dir(mypkg.mymod.countChars(actual)), "\nMyClient Function I")
print(countChars.__dict__, "MyClient Function II")
print(dir(countChars(actual)), "\nMyClient Function III")
print("End of MyClient, last print statement of myClient")
