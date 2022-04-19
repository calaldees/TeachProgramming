Workshop 2: JSON data (30min)
---------------------

JavaScript Object Notation (JSON)

* Using the code snippets below. Perform these tasks
    * Pick a language: python or javascript
    * Setup the data variable (in the snippets below)
    * What is (you can trial this in the console)
        * data['a']
        * data[0]['b']
        * data[2]['e'][1]
        * data[2]['f']['h']
    * Change the following in memory
        * data[1]['c'] = 100
        * data[2]['f']['z'] = "addition"
    * Serialize the data to a string
    * Load up in language2, copy and paste the string, decode the data in language2
    * Modify the data in language2
    * Serialize the data to a string in language2
    * decode the data the string in language1

python
```python
import json

data = [
    {'a': 1, 'b': 2},
    {'c': 3, 'd': 4},
    {'e': [5,6,7], 'f': {'g': 10, 'h': "something"}},
]
string_data = json.dumps(data)
print(string_data)
data2 = json.loads(string_data)
```

javascript
```javascript
const data = [
    {'a': 1, 'b': 2},
    {'c': 3, 'd': 4},
    {'e': [5,6,7], 'f': {'g': 10, 'h': "something"}},
];
const string_data = JSON.stringify(data);
console.log(string_data);
const data2 = JSON.parse(string_data);
```

### JSON in static languages
* Using JSON in static languages is MUCH harder
* They generally need to bound to Class's. (in some cases there are general object wrappers)
* Representing strings is hard as escaping double-quotes `\"` is a pain
* The `{'e': [...` line, because it is a different structure to the other elements, creates massive problems for static languages.
* In most cases JSON handling is not built into the base language and needs and external library.

```csharp
    var stringifiedJson = @"{""Topic"":""Json Serialization Part 1"",""Part"":1,""Author"":""Marc"",""Co-Author"":""Helen"",""Keywords"":[""json"",""netcore"",""parsing""]}";
    var blogPost = JsonDocument.Parse(stringifiedJson);
    var topic = blogPost.RootElement.GetProperty("Topic").GetString();
    Console.WriteLine(topic);
    Console.WriteLine(JsonSerializer.Serialize(blogPost));
    // manipulating values is hard - https://kevsoft.net/2021/12/29/manipulate-json-with-system-text-json-nodes.html
```

Extension Task: Attempt to decode the jsonstring (from the last exercise) and `Console.WriteLine` the value for `data[2]['e'][1]`
You may need the documentation for [JsonElement](https://docs.microsoft.com/en-us/dotnet/api/system.text.json.jsonelement?view=net-6.0)

```csharp
    class Pet {
        public string name  { get; set; }
        public string type  { get; set; }
    }
    class Person {
        public String name  { get; set; }
        public int age  { get; set; }
        public List<Pet> pets  { get; set; }
    }

    var p = new Person {
        name = "Test",
        age = 100,
        pets = new List<Pet> {
            new Pet {name = "Kitty", type = "cat"},
            new Pet {name = "Doggy", type = "dog"},
        },
    };
    string data = JsonSerializer.Serialize<Person>(p);
    Console.WriteLine(data);
    var p2 = JsonSerializer.Deserialize<Person>(data);
    Console.WriteLine(p2.pets[1].name);
```

### Further thoughts

#### Other data formats
* XML (legacy 2005)
* Protobuff
* GraphQL
* YAML (superset)
* TOML

#### JSON Schema

JSON is by default totally unstructured. We can use additional tools to ensure that output meets a know structure or specification
* [json-schema](https://json-schema.org/)
