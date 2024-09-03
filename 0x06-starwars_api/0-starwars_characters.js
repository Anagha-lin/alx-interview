#!/usr/bin/node

const request = require('request');

// Get the Movie ID from command line arguments
const movieId = process.argv[2];

// Define the API URL
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make the request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Iterate over each character URL and fetch the character's name
  characters.forEach((characterUrl) => {
    request(characterUrl, (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }

      // Parse and print the character's name
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});

