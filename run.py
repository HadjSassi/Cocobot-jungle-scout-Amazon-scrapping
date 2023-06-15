from booking.searching import Searching
import pandas as pd

with Searching(True) as bot:
    # # bot.land_first_page(query="machine à laver")
    # # bot.land_first_page(query="toner cartouche cartbridge")
    # bot.land_first_page(query="iphone 14 pro max")
    # # bot.land_fist_page(query="iphone+14+pro+max&page=2")
    # bot.close_PoP_Up()
    # # bot.search("iphone 14 pro max")
    # # bot.search("machine à laver")
    # # bot.close_PoP_Up()
    # # bot.implicitly_wait(100)
    # collectione = pd.DataFrame(bot.getFirstDataFrame())
    # collectione.to_csv('test.csv',index=False)
    # df = bot.getSecondDataFrame(collectione)
    collectione = pd.read_csv('test.csv')
    bot.getSecondDataFrame(collectione)

