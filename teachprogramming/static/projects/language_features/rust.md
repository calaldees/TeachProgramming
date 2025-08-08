```rust
impl<T, U: From<T>> Into<U> for T {
    fn into(value: T) -> U {
        U::from(value)
    }
}
```

implement TryFrom but use try_into:

```rust
#[derive(Debug)]
struct MalformedAuthError;

struct BasicAuth {
    username: String,
    password: String,
}

impl TryFrom<String> for BasicAuth {
    type Error = MalformedAuthError;

    fn try_from(value: String) -> Result<Self, Self::Error> {
        let parts: Vec<&str> = value.split(':').collect();
        if parts.len() == 2 {
            Ok(Self {
                username: parts[0].to_string(),
                password: parts[1].to_string(),
            })
        } else {
            Err(MalformedAuthError)
        }
    }
}

fn main() {
    let auth_string = "user:password".to_string();
    let auth: BasicAuth = auth_string.try_into().expect("Failed to parse BasicAuth");
}
```

From and Into rather than the try versions to not add error noise

That’s basically implement Into for all types that implement From

What till you see the implementation of the serialization library that’s a library not a language feature but is better than most built in language features

---

You can add methods to someone elses static types from their library.

---


Did this the other day:
```rust
#[derive(Deserialize, Debug)]
struct  GenerateParams {
    gigya_id: String,
    #[serde(flatten)]
    license_type: LicenseType,
}

#[derive(Deserialize, Debug)]
#[serde(tag = "license_type", rename_all = "kebab-case")]
enum LicenseType {
    AllIn,
    Podcast,
    Catchup,
    Live,
    Custom { stream: String },
}
```

Converts this with type safety:
```
{"gigya_id": "aaa", "license_type": "all-in"}
```
But also this:
```
{"gigya_id": "aaa", "license_type": "custom", "stream": "http://..."}
```
Stream is only valid when license type is custom