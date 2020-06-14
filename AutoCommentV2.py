import pyautogui
import os
import time

def main():
    import pyautogui
    import os
    import time


    clear = lambda: os.system("cls")
    clear()
    print("Welcome to Omar Hegazy's (AutoCommenting) Program. All Rights Reserved, 2020.")
    time.sleep(1.5)
    print("")
    print("For the program to work, you have to enter: the number of comments (will be multiplied by 5), 5 comments of your own to be posted,")
    print("and the delay between each comment and the other, then hurry up and click on the (Comments) box for the program to function properly.")
    print("Enjoy the show!")
    print("")
    print("Happy Commenting. :)")
    time.sleep(5)
    print("")
    no_comments=(int(input("Enter Number of Comments (will be multiplied by 5): ")))
    comment1=input("Enter Comment 1: ")
    comment2=input("Enter Comment 2: ")
    comment3=input("Enter Comment 3: ")
    comment4=input("Enter Comment 4: ")
    comment5=input("Enter Comment 5: ")

    allcomments=[comment1, comment2, comment3, comment4, comment5]

    timewait=int(input("Enter how many seconds delay between each comment and the other (whole number): "))

    print("HURRY AND REDIRECT TO THE COMMENTING BOX")
    print("COMMENTS WILL BE POSTED IN")
    time.sleep(1)
    print("5")
    time.sleep(1)
    clear = lambda: os.system("cls")
    clear()
    print("HURRY AND REDIRECT TO THE COMMENTING BOX")
    print("COMMENTS WILL BE POSTED IN")
    print("4")
    time.sleep(1)
    clear = lambda: os.system("cls")
    clear()
    print("HURRY AND REDIRECT TO THE COMMENTING BOX")
    print("COMMENTS WILL BE POSTED IN")
    print("3")
    time.sleep(1)
    clear = lambda: os.system("cls")
    clear()
    print("HURRY AND REDIRECT TO THE COMMENTING BOX")
    print("COMMENTS WILL BE POSTED IN")
    print("2")
    time.sleep(1)
    clear = lambda: os.system("cls")
    clear()
    print("HURRY AND REDIRECT TO THE COMMENTING BOX")
    print("COMMENTS WILL BE POSTED IN")
    print("1")
    time.sleep(1)
    clear = lambda: os.system("cls")
    clear()





    for i in range(no_comments):

        pyautogui.typewrite(comment1)
        pyautogui.typewrite("\n")
        pyautogui.typewrite(comment2)
        pyautogui.typewrite("\n")
        pyautogui.typewrite(comment3)
        pyautogui.typewrite("\n")
        pyautogui.typewrite(comment4)
        pyautogui.typewrite("\n")
        pyautogui.typewrite(comment5)
        pyautogui.typewrite("\n")

        time.sleep(timewait)
while True:
    main()
    print("All done! Hope this program helped. :). ")
    print("Project (AutoCommenting Bot) Done By: Omar Adel Hegazy")
    print("Add me on Facebook: facebook.com/Omar57844")
    print("Follow me on Instagram: @Omar57844")
    print("Follow me on Twitter: @Omar57844")
    time.sleep(2)
    print("")
    if input("Is there any other victim you want to try the program on? (Y/N) ").strip().upper() != 'Y': 
        break
