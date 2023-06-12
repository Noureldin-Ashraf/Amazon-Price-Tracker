# Amazon Price Tracker
<h2><u>Brief</u></h2>
<p>A Python program which tracks a certain product on amazon and send an email notification message once the product price is below a certain threshold or if the product became out of stock.
</p>
<br>

<h2><u>How Does it Work ?</u></h2>
<p>The program starts by scrapping the product data (title, price, availability) from the product URL.
It checks if the product is available or not (out of stock) and sends a notification email in case if it's out ot stock.
If the availabilty criteria is met the scrapped price is then compared to a pre-set price for the product and a notification email is sent if the scrapped price is lower than the pre-set one.
</p>
<br>

<h2><u>Run</u></h3>
 <p>Before running the program You first need to:<br>
 <ul><li>Change both of the "PRODUCT_URL" and the "PRODUCT_TARGET_PRICE" in the "Main" file to point at the product and the price threshold you want to track.</li>
 <li>Change both of "MY_EMAIL" and "MY_PASSWORD" in the "email_notification" file with the credentials of the email you want to send notifications from</li>
 <li>Optimally you will need the program to run automatically in a desired time interval (Daily, Weekly, Monthly...etc) to do the check.<br>
 So you can either upload the program to a python hosting service like <a href="https://www.pythonanywhere.com/" target="_blank">PythonAnywhere</a> and set a scheduler to run to your liking,<br>Or you can generate an exe file using <a href="https://pyinstaller.org/en/stable/" target="_blank">Pyinstaller</a> and setup a windows task scheduler to run it at the selected intervals.</li>
 </ul></p>
 
 
<br>

<h2><u>Libraries Used</u></h3>
<ul>
<li>The web scrapping is done using Python's <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">BeautifulSoup</a> Library</li>
<li>The email notification is sent using Python's <a href="https://docs.python.org/3/library/smtplib.html" target="_blank">smtplib</a> Module</li>
</ul>

