# SupremeManualBot
Finds a product on Supreme's website, then automatically opens the product page. After opening the user will then add the product to cart and checkout manually.

This program, written in Python 3, finds products on Supreme's website, regardless of category. Once a product is found it will automatically open the product page on your browser. Then the user can add to cart and checkout manually.  

Given the recent success of manual users on Supreme's website this program will allow you to navigate to the product page as quickly as possible. Even if the site is lagging you will be going straight to the product page which is a slight advantage over the normal manual user who navigates from the category page or even the shop home page.  

When you start the program you'll be prompted to enter keywords. You can use a single phrase like 'colorblocked hooded' or a series of words, but they have to be seperated by a comma only, not a comma and a space. For example: penco,band,colorblocked hoodie. Once you hit return the program will search for the keyword(s) (in an actual drop enter the keyword whenever and then hit return right at 11).

If the product you're searching for is not found (possibly due to a late drop or site lag) the program will search for the term every half a second ten more times before finally ending.  If your keyword is found in multiple products or if you search for multiple keywords (for example, polartec in week 19) all the products will be pulled and an individual tab will be opened for each product with that keyword. If you open your default web browser and open gmail in a tab the new tab will populate in that same browser window and gmail will still be open too, this may give you an additional advantage with captcha's at checkout. 

If you're new to python and don't have an interpreter you can run the code in your computers terminal/command prompt/powershell. Download the script and the necessary modules and then open your command window and type in python3 Keyword.py and it should initiate the script. 

Good luck!
