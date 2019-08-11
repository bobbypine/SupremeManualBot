# SupremeManualBot

Let's face it, going manual on Supreme has been having very high rates of success lately. This script will help you be a little faster than the average manual user while avoiding any kind of bot detection. 

This program, written in Python 3, finds products on Supreme's website, regardless of category. Once a product is found it will automatically open the product page on your default browser. Then the user can add to cart and checkout manually.  

Even if the site is lagging you will be going straight to the product page which is a slight advantage over the normal manual user who navigates from the category page or even the shop home page.  

When you start the program you'll be prompted to enter keywords. You can use a single phrase like 'colorblocked hooded' or a word. If you're searching for multiple products your keywords have to be seperated by a comma only, not a comma and a space. For example: penco,band,colorblocked hoodie. Once you hit return the program will search for the keyword(s).

If the product you're searching for is not found (possibly due to a late drop or site lag) the program will search for the term every quarter of a second 240 more times before finally ending.  If your keyword is found in multiple products or if you search for multiple keywords (for example, polartec in week 19 FW'18) all the products will be pulled and an individual tab will be opened for each product with that keyword. If you open your default web browser and open gmail in a tab the new tab will populate in that same browser window and gmail will still be open too, this may give you an additional advantage with captcha's at checkout. 

When using keywords you really have to pay attendtion to how items are named. For example, during a Stone Island® or The North Face® release the '®' is part of the name, so if necessary you'll need it in your keyword too. During the SS'19 Stone Island collaboration the key phrase 'stone island® hooded' would pull the hoodie while 'stone island hooded' would yield no results. I use the Sup Comm app to keep track of droplists ahead of time to see what keywords I want to use. Also be mindful if your keyword conflicts witn an existing item on the website, try not to be super generic (e.g. tee). 

If you're new to python and don't have an interpreter you can run the code in your computers terminal/command prompt/powershell. Download the script and the necessary modules and then open your command window and type in python3 Keyword.py and it should initiate the script. I recommend running it around 10:59:50 AM, the error handling will kick in for the first few loops and by 11AM it should find the product. Personally Spring/Summer '19 has been the most successful Superme season for me due to this script. Some highlights include: the North Face Arc Logo Mountain Parka, the directors chair, the cupid tee, the HotWheels M3, the Swarovski box logo tee, the Buju Banton tee, etc. 

Good luck!
