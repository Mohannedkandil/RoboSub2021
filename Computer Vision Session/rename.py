import os


def main():
    path = "D:\\VORTEX\\UnderWater_Hackathon\\Datasets\\data\\"
    for count, filename in enumerate(os.listdir(path)):
        src = path+filename
        dst = "stingray"+str(count)+".jpg"
        #dst = path + dst

        os.rename(src, dst)


if __name__ == '__main__':
    # Calling main() function
    main()