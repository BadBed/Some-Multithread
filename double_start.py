import threading
import main
import s_main


t1 = threading.Thread(target=main.main)
t2 = threading.Thread(target=s_main.main)

t1.start()
t2.start()

t1.join()
t2.join()
