import undetected_chromedriver.v2 as uc
import time
import random
email = ''
password = ''

driver = uc.Chrome()
count = 0
followers = 0
followersFailed = 0


with open('accounts.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

with driver:
    driver.get('https://namemc.com/login')
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    for x in content:
        driver.get(f"https://namemc.com/{x}")
        time.sleep(random.randint(7,15))
        try:
            if count >= 40:
                count = 0
                time.sleep(1800)
            driver.find_element_by_id('followMenuButton').click()
            driver.find_element_by_xpath("//button[@class='btn btn-link dropdown-item rounded-0']").click()
            time.sleep(3)
            try:
                driver.find_element_by_xpath("//div[@class='card bg-warning text-center text-black']")
                followersFailed = followersFailed + 1
                print('===================')
                print('Rate limted! Wait 1200s')
                print('===================')
                print(f'Followers: {followers}')
                print(f'Failed: {followersFailed}')
                print(f'Total: {count}')
                print('===================')
                time.sleep(1800)
            except:
                count = count + 1
                followers = followers + 1
                print('===================')
                print(f'Followed {x}!')
                print('===================')
                print(f'Followers: {followers}')
                print(f'Failed: {followersFailed}')
                print(f'Total: {count}')
                print('===================')
                time.sleep(random.randint(7,15))
        except:
            count = count + 1
            followersFailed = followersFailed + 1
            print('===================')
            print(f"Can't follow {x}")
            print('===================')
            print(f'Followers: {followers}')
            print(f'Failed: {followersFailed}')
            print(f'Total: {count}')
            print('===================')
            if count >= 40:
                count = 0
                time.sleep(1800)
                print("[!] Stopping for 10ish minutes to prevent rate limiting.")
            continue
    print("Done!")