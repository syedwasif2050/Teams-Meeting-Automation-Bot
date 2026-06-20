from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- SETUP ---
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\temp\\wasif_ultimate_bot") 
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--use-fake-ui-for-media-stream")

driver = webdriver.Chrome(options=chrome_options)

def start_bot(meeting_link):
    try:
        driver.get(meeting_link)
        print("Bot: Loading... 15 seconds wait karein.")
        time.sleep(15)

        # 1. MIC & CAMERA OFF
        print("Bot: Mic/Cam check kar raha hoon...")
        media_selectors = ["//button[contains(@aria-label, 'mute')]", 
                           "//button[contains(@aria-label, 'turn camera off')]"]
        for s in media_selectors:
            try:
                el = driver.find_element(By.XPATH, s)
                el.click()
            except: pass

        # 2. AUTO JOIN
        print("Bot: Join button dhoond raha hoon...")
        join_btn = WebDriverWait(driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Join now')] | //button[contains(@data-tid, 'prejoin-join-button')]"))
        )
        join_btn.click()
        print("Bot: Join ho gaya! Ab chat monitoring shuru...")

        # 3. LIVE CHAT MONITORING & REPLY
        replied = False 
        last_seen_messages = set() # Taake ek hi message baar baar print na ho

        while True:
            # Teams ke chat messages ki list uthana
            try:
                # Ye selector chat ke har message ko pakarta hai
                messages = driver.find_elements(By.CSS_SELECTOR, ".message-body-container, [data-tid='chat-pane-message']")
                
                for msg in messages:
                    text = msg.text.strip()
                    if text and text not in last_seen_messages:
                        # --- YAHAN CHAT VS CODE MEIN PRINT HOGI ---
                        print(f"NEW MESSAGE: {text}") 
                        last_seen_messages.add(text)

                        # Check for Roll No / Name
                        if any(id in text for id in ["60", "Wasif", "wasif"]) and not replied:
                            print(">>> BINGO! Aapka naam mil gaya. Reply bhej raha hoon...")
                            chat_box = driver.find_element(By.XPATH, "//div[@aria-label='Type a new message'] | //div[contains(@data-tid, 'chat-input')]")
                            chat_box.send_keys("Present Sir")
                            chat_box.send_keys(Keys.ENTER)
                            print(">>> Bot: Present lag gayi! ✅")
                            replied = True
            except:
                pass # Agar chat panel band hai toh error na aaye
                
            time.sleep(4) # Har 4 second baad chat check karega

    except Exception as e:
        print(f"Bot Error: {e}")

link = input("Wasif bhai, Meeting Link paste karein: ")
start_bot(link)