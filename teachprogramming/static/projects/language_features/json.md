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

Can be used in https://dotnetfiddle.net/ with `.NET 7` or higher
```csharp
using System;
using System.Text.Json;
using System.Net.Http;
using System.Threading.Tasks;

public class Program {
	static readonly HttpClient client = new HttpClient();
	public static async Task Main() {
		//var responseBody = $$"""
		//  {"userId": 1, "id": 1, "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"}
		//""";

		HttpResponseMessage response = await client.GetAsync("https://jsonplaceholder.typicode.com/posts/1");
		response.EnsureSuccessStatusCode();
		string responseBody = await response.Content.ReadAsStringAsync();
		Console.WriteLine(responseBody);

		var json = JsonDocument.Parse(responseBody);
		Console.WriteLine(json.RootElement.GetProperty("title").GetString());
		// manipulating values is hard - https://kevsoft.net/2021/12/29/manipulate-json-with-system-text-json-nodes.html
		Console.WriteLine(JsonSerializer.Serialize(json));
	}
}
```

### Extension Task
* Attempt to decode the jsonstring (from the last python/javascript exercise) in csharp
* and `Console.WriteLine` the value for `data[2]['e'][1]`
You may need the documentation for [JsonElement](https://docs.microsoft.com/en-us/dotnet/api/system.text.json.jsonelement?view=net-7.0)


### Further thoughts
* Most static languages serialise and deserialize json from schema's or object structures

#### Other data formats
* XML (legacy 2005)
* Protobuff
* GraphQL
* YAML (superset)
* TOML

#### JSON Schema

JSON is by default totally unstructured. We can use additional tools to ensure that output meets a know structure or specification
* [json-schema](https://json-schema.org/)
