import threading
import time

def walk_dog(first):
    time.sleep(8)
    print(f"You finished walking the dog named {first}")

def take_out_trash():
    time.sleep(2)
    print(f"You took out the trash.")

def get_mail():
    time.sleep(4)
    print(f"You got the mail from the mailbox.")

chore1 = threading.Thread(target=walk_dog, args=("Scooby",))
chore1.start()

chore2= threading.Thread(target=take_out_trash)
chore2.start()

chore3= threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")