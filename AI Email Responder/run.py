from main import main
import time

while True:
    main()
    print("⏳ Waiting for next cycle...")
    time.sleep(3600)  # every 1 hour
