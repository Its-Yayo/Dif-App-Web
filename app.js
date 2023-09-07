"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var express = require("express");
var app = express();
var port = 3000;
app.use(express.json());
app.get('/', function (req, res) {
    res.send('TODO implementation');
});
app.listen(port, function () {
    console.log('Server is listening on port 3000');
});
