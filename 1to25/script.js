function generate() {
    var quotes = {
        "- Mary Astell" : "“If all men are born free, how is it that all women are born slaves?”",
        "- C.S. Lewis" : "“I was not born to be free---I was born to adore and obey.”",
        "- John Galsworthy" : "“Life calls the tune, we dance.”"
    }

    var authors = Object.keys(quotes);

    var author = authors[Math.floor(Math.random()) * authors.length]

    var quote = quotes[author]

    document.getElementById("quote").innerHTML = quote;
    document.getElementById("author").innerHTML = author;
}