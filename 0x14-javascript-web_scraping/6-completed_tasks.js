#!/usr/bin/node
/**
 * a script that computes the number of
 * tasks completed by user id.
 */
const request = require('request');

const url = process.argv[2];
let userId;
let todos;

const computedObj = {};

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    todos = JSON.parse(body);

    for (let i = 0; i < todos.length; i++) {
      userId = todos[i].userId;
      if (todos[i].completed) {
        computedObj[userId] ? computedObj[userId]++ : computedObj[userId] = 1;
      }
    }
    console.log(computedObj);
  }
});
