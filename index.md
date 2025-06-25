---
layout: home
title: "TextBot Project"
heading: "Python TextBot"
subheading: "An intelligent SMS automation system that simplifies daily life through text messaging"
---

<div class="space-y-12">
    <!-- Main Featured Image - Smaller and Centered -->
    <div class="flex justify-center">
        <img class="object-cover object-top w-full max-w-md h-auto rounded-lg shadow-lg" 
             src="{{ site.baseurl }}/assets/img/IMG_9190.GIF" 
             alt="Python TextBot Demo - Help Command">
    </div>

    <div class="space-y-6">
        <div class="space-y-4">
            <h3 class="text-3xl font-bold leading-tight text-gray-900 sm:text-4xl dark:text-white">
                Python TextBot
            </h3>

            <p class="text-base font-normal text-gray-500 sm:text-lg dark:text-gray-400">
                Python TextBot is a textbot that uses a collection of scripts I wrote to simplify certain aspects of my life such as remembering birthdays and homework assignments. I am able to send daily reminders on upcoming birthdays and homework assignments and I can also utilize slash commands to access a variety of other information such as the news, weather, or simply a random meme.
            </p>
            <p class="text-base font-normal text-gray-500 sm:text-lg dark:text-gray-400">
                I am utilizing the <a href="https://pypi.org/project/PyTextNow/" target="_blank" class="text-primary-600 hover:text-primary-700 dark:text-primary-500">PyTextNow package</a> in order to communicate through a phone number using text messages which are then processed by the Raspberry Pi to output the desired information.
            </p>
        </div>

        <!-- Technology Tags -->
        <div class="flex items-center gap-2.5 flex-wrap">
            <div class="p-1 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800">
                <span class="inline-flex items-center px-3 py-1 text-xs font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300">
                    Python
                </span>
            </div>
            <div class="p-1 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800">
                <span class="inline-flex items-center px-3 py-1 text-xs font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300">
                    PyTextNow
                </span>
            </div>
            <div class="p-1 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800">
                <span class="inline-flex items-center px-3 py-1 text-xs font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300">
                    Raspberry Pi
                </span>
            </div>
            <div class="p-1 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800">
                <span class="inline-flex items-center px-3 py-1 text-xs font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300">
                    REST APIs
                </span>
            </div>
            <div class="p-1 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800">
                <span class="inline-flex items-center px-3 py-1 text-xs font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300">
                    Automation
                </span>
            </div>
        </div>

        <!-- How to Use Section -->
        <div class="mt-8">
            <h4 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">How to Use</h4>
            <p class="text-base text-gray-500 dark:text-gray-400 mb-8">
                There is a wide range of commands, here are a few of them:
            </p>

            <!-- Command Examples Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Help Command -->
                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">/help</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Returns a list of commands that can be used.</p>
                    <img class="w-full h-auto rounded border border-gray-200 dark:border-gray-700"
                         src="{{ site.baseurl }}/assets/img/IMG_9190.GIF" alt="/help command demo">
                </div>

                <!-- Quote Command -->
                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">/quote</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Returns a random Kanye quote from the <a href="https://api.kanye.rest" target="_blank" class="text-primary-600 hover:text-primary-700 dark:text-primary-500">Kanye Rest API</a>.</p>
                    <img class="w-full h-auto rounded border border-gray-200 dark:border-gray-700"
                         src="{{ site.baseurl }}/assets/img/IMG_9185.GIF" alt="/quote command demo">
                </div>

                <!-- Meme Command -->
                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">/meme</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Returns a random meme from a <a href="https://meme-api.herokuapp.com/gimme" target="_blank" class="text-primary-600 hover:text-primary-700 dark:text-primary-500">Meme API</a>.</p>
                    <img class="w-full h-auto rounded border border-gray-200 dark:border-gray-700"
                         src="{{ site.baseurl }}/assets/img/IMG_9187.GIF" alt="/meme command demo">
                </div>

                <!-- Joke Command -->
                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">/joke</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Returns a random joke from a <a href="https://icanhazdadjoke.com/" target="_blank" class="text-primary-600 hover:text-primary-700 dark:text-primary-500">Joke API</a>.</p>
                    <img class="w-full h-auto rounded border border-gray-200 dark:border-gray-700"
                         src="{{ site.baseurl }}/assets/img/IMG_9186.GIF" alt="/joke command demo">
                </div>

                <!-- APOD Command -->
                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">/apod</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Returns the astronomy picture of the day from the <a href="https://api.nasa.gov/planetary/apod" target="_blank" class="text-primary-600 hover:text-primary-700 dark:text-primary-500">APOD API</a>.</p>
                    <img class="w-full h-auto rounded border border-gray-200 dark:border-gray-700"
                         src="{{ site.baseurl }}/assets/img/IMG_9189.GIF" alt="/apod command demo">
                </div>

                <!-- News Command -->
                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6">
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">/news</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Returns the top news headlines from the <a href="https://newsapi.org/" target="_blank" class="text-primary-600 hover:text-primary-700 dark:text-primary-500">News API</a>.</p>
                    <img class="w-full h-auto rounded border border-gray-200 dark:border-gray-700"
                         src="{{ site.baseurl }}/assets/img/IMG_9188.GIF" alt="/news command demo">
                </div>

                <!-- Birthdays Command -->
                <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-6 md:col-span-2">
                    <h5 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">/birthdays</h5>
                    <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Returns the next birthday.</p>
                    <div class="flex justify-center">
                        <img class="w-full max-w-sm h-auto rounded border border-gray-200 dark:border-gray-700"
                             src="{{ site.baseurl }}/assets/img/IMG_9192.GIF" alt="/birthdays command demo">
                    </div>
                </div>
            </div>
        </div>

        <!-- GitHub Button -->
        <div class="mt-8">
            <a href="https://github.com/nitheesh-cpu/TextBot" target="_blank" title="View on GitHub"
                class="text-white inline-flex items-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                role="button">
                View Source Code
                <svg aria-hidden="true" class="w-5 h-5 ml-2" fill="none" stroke="currentColor"
                    stroke-width="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3">
                    </path>
                </svg>
            </a>
        </div>
    </div>

</div>
