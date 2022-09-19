const express = require('express');
const res = require('express/lib/response');
const path = require('path');
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }))


app.get('/', (req, res) => {
    res.send("Hello");
});
app.listen(5000,()=>console.log("Server is started on port 5000")); 