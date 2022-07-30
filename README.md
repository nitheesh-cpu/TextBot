# About this Project

Python TextBot is a textbot that uses a collection of scripts I wrote to simplify certain aspects of my life such as remembering birthdays and homework assignments. I am able to send daily reminders on upcoming birthdays and homework assignments and I can also utilize slash commands to access a variety of other information such as the news, weather, or simply a random meme. 

I am utilizing the [PyTextNow package](https://pypi.org/project/PyTextNow/) in order to communicate through a phone number using text messages which are then proccessed by the Raspberry Pi to output the desired information. 

## How to Use

There is a wide range of commands, here are a few of them:

### /help
Returns a list of commands that can be used.
<img src="{{site.baseurl | prepend: site.url}}IMG_9190.GIF" alt="/help" />

### /quote
Returns a random Kanye quote from the [Kanye Rest API](https://api.kanye.rest).
<img src="{{site.baseurl | prepend: site.url}}IMG_9185.GIF" alt="/quote" />

### /meme
Returns a random meme from a [Meme API](https://meme-api.herokuapp.com/gimme).
<img src="{{site.baseurl | prepend: site.url}}IMG_9187.GIF" alt="/birthdays" />

### /joke
Returns a random joke from a [Joke API](https://icanhazdadjoke.com/).
<img src="{{site.baseurl | prepend: site.url}}IMG_9186.GIF" alt="/joke" />

### /apod
Returns the astronomy picture of the day from the [APOD API](https://api.nasa.gov/planetary/apod).
<img src="{{site.baseurl | prepend: site.url}}IMG_9189.GIF" alt="/apod" />

### /news
Returns the top news headlines from the [News API](https://newsapi.org/).
<img src="{{site.baseurl | prepend: site.url}}IMG_9188.GIF" alt="/apod" />

### /birthdays
Returns the next birthday
<img src="{{site.baseurl | prepend: site.url}}IMG_9192.GIF" alt="/birthdays" />