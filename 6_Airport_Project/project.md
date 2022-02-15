# Most popular destination airports

## What is our dataset?

We use the [openflights](https://openflights.org/data.html) dataset and the `routes.dat` in particular.
You can find the dataset and its description in the `./Airport_project/data` folder.
Each row in the data describes one route along which flights are provided and include a source and a destination airport.
An airport can be described by a three letter code and a number (ID), which are provided in two separate columns for both source and destination.

## What do we want to achieve?

We want to find the most popular destination airport.
To do this we want to count the number of routes that lead to any destination airport.
This aggregate of counts we want to write to a [JSON](https://en.wikipedia.org/wiki/JSON) file as a dictionary.
The dictionary keys should be the destination airport identifier (string label or integer ID).
The dictionary values should be the count of the number of routes to the destination airport.
As a bonus you could filter the counts on the top 10 most popular destinations.

## What steps do we need to do?

We will use the following techniques we have learned during the course:

1. file handling to read the `routes.dat` file
2. loop over the lines in the file with a `for` loop
3. split the lines into columns and select the columns of interest
4. use a dictionary to accumulate our counts
5. write the dictionary to a JSON file with the [json](https://docs.python.org/3.8/library/json.html) library
6. BONUS 1: filter the top 10 destination airports before writing to JSON
7. BONUS 2: write code that can perform the same analysis on both source and destination airport

### hints
Hints are provided for the above steps (excluding bonus) in the `./Airport_project/hints` folder.
These are python files with skeletal code.

## What do I need to deliver?

Create one python script which executes the steps described above.
Write the aggregated count to a JSON file.
