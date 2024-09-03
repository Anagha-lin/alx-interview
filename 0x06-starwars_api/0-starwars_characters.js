#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;
let characterUrls = [];
const characterNames = [];

// Function to fetch the list of character URLs from the film endpoint
const fetchCharacterUrls = async () => {
  await new Promise((resolve) => {
    request(filmUrl, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        console.error('Failed to fetch data:', error, '| Status Code:', response.statusCode);
      } else {
        const data = JSON.parse(body);
        characterUrls = data.characters;
        resolve();
      }
    });
  });
};

// Function to fetch and store the names of characters from their respective URLs
const fetchCharacterNames = async () => {
  if (characterUrls.length > 0) {
    for (const url of characterUrls) {
      await new Promise((resolve) => {
        request(url, (error, response, body) => {
          if (error || response.statusCode !== 200) {
            console.error('Failed to fetch character:', error, '| Status Code:', response.statusCode);
          } else {
            const characterData = JSON.parse(body);
            characterNames.push(characterData.name);
            resolve();
          }
        });
      });
    }
  } else {
    console.error('No characters found.');
  }
};

// Function to initiate the fetching process and display the names
const displayCharacterNames = async () => {
  await fetchCharacterUrls();
  await fetchCharacterNames();

  characterNames.forEach((name, index) => {
    process.stdout.write(name + (index < characterNames.length - 1 ? '\n' : ''));
  });
};

displayCharacterNames();

