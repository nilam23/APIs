var express = require("express");
var app = express();
var request = require("request");

app.set("view engine", "ejs");

app.get("/", (req, res) => {
    res.render("index");
})

app.get("/results", (req, res) => {
    var movieName = req.query.movieName;
    var url = "http://www.omdbapi.com/?s=" + movieName + "&apikey=<your_key>";
    request(url, (error, response, body) => {
        if (!error && response.statusCode === 200) {
            var parseData = JSON.parse(body);
            res.render("results", { data: parseData });
        }
    });
});

app.listen(3000, () => {
    console.log("Server listening on port 3000...");
});