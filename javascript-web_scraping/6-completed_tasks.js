#!/usr/bin/node
/* Script that computes the number of tasks completed by user id */

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const todoList = JSON.parse(body);
  const completedTasksPerUser = {};

  for (const todoItem of todoList) {
    if (todoItem.completed === true) {
      if (todoItem.userId in completedTasksPerUser) {
        completedTasksPerUser[todoItem.userId]++;
      } else {
        completedTasksPerUser[todoItem.userId] = 1;
      }
    }
  }
  console.log(completedTasksPerUser);
});
