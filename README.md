# AIlly-challenge
Tech challenge for AIlly

## Instructions
![image](https://user-images.githubusercontent.com/38657416/193954516-5aaf6ed9-71a3-41d4-a5e4-4bdf20420f3b.png)

## Code
The code is located in the file main.py and can be run anywhere using python3 (probably even python2 should work).

## Observations 
The graph is directed and unweighted. In order to represent such graph, we can easily implement an adjacency list and construct it from both list of vertices and list of edges. Also an adjacency list should cover all the use cases asked for the challenge. For efficiency, typically we need to store this list in a hashmap. As a benefit, we can mention the constant time access O(1) on the vertex elements.

The graph should be constructed from two inputs (here chosen randomly):
 - A list of vertices, example: `[“a”, “b”, “c”, “d”]`
 - A list of edges, example: `[(“a”, “b”), (“a”, “c”), (“c”, “d”)]`

Visual représentation of the sample graph:
![image](https://user-images.githubusercontent.com/38657416/193952510-583c37f8-2cc1-465c-8c4a-e1331b47aaec.png)

The adjacency list is a key-value pair where the key is a vertex and the value is a list of vertex directly reachable from it. Note that if a vertex has an out degree equals to 0, we still need to track it and its value should remain an empty list -> `[]`.
```
graph = {
  a: [‘b’, ‘c’], 
  b: [],
  c: [‘d’],
  d: []
}
```
## Construct from the inputs:
We can construct the adjacency list from those inputs basically in 2 steps. At first, we loop through the vertices list and add in the dictionary all the elements as keys. We need to do that because the list of edges might not contain all the existing vertices. Then we lop through the edges list and, considering that an edge is a tuple (v, u) which means “vertex v had a direction to u”, we append `u` to the current values of `dict[v]`.

## Compute the number of edges:
The total number of edges is equal to the count of all the elements in any of the dictionary values (here 3). This is linear time O(n) where n is the number of vertices.

## Compute the number of vertices:
The total number of vertices is equal to the count of the dictionary keys (here 4).
This is constant time O(1).

## Compute the in degrees per vertex:
The in degree of a vertex is equal to the count of its occurrence in any of the dictionary values
For example, in degree of `d` is equal to 1 as `d` appears only once in the values
Here we can use a second dictionary to track the occurrences while looping through all the values. 

## Compute the out degrees per vertex:
The out degree of a vertex is equal to the count of the items in its value
For example, out degree of vertex `a` is simply equal to `len(graph[“a”])=2` which is basically constant time.

## Serializatoin/Deserialization
For the serialization/deserialization part, I’ve chosen to use json format which is human readable and can easily be shared with other applications/platforms. It makes sens to me as we want to simply store a dictionary. This will be converted into a json object behind the scene. The main thing to pay attention is to release the file once we are done with it.

Some basic checks are needed in order to avoid random crashes such as checking if the file exist before writing to it, or if a vertex is already set in the adjacency list before trying to append an element to its values.

For my own tests, I have added an extra method to add an edge to the current graph and one for outputting the dictionary. This allowed me to compare the adjacency list before and after adding new edges.

## Sample execution
![image](https://user-images.githubusercontent.com/38657416/193957259-e6763ba9-f0a9-4130-99a6-f1245e3d381e.png)


