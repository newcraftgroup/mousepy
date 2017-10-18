# nci-python-mouseflow

## API

### Connection

Before running any command, Mouseflow must first be initiated with a username a token generated within the Mouseflow site.

#### Code

```py
connection = Mouseflow(
    user,
    token
)
```

#### Parameters
* ```user```: The username provided by mouseflow to connect to their API
* ```token``` The token key provided by mouseflow to connect to their API
* ```location``` Which server to connect to (Mouseflow.LOCATION_EUROPE, LOCATION_UNITED_STATES)
* ```debug```: (optional) If set to True and when running in the terminal, all calls will be printed out


### Website
A representation of a specific website

#### Code
```py
connection.websites(name)
```

#### Parameters
* ```name```: The name of the site to select

#### Methods

* ```id()```: This the unique ID associated with the website
* ```name()```: An alias or name you have given for your website (defaults to the website domain)
* ```created()```: The time the website was registered in Mouseflow
* ```status()```: A string indicating whether the website is currently recording (values: NotInstalled, Recording, Stopped, Paused). Stopped means that you have manually stopped recording your users. Paused means that the website will start recording once you get credits in your account.
* ```thumb()```: A partial URL for a thumbnail image generated from your website
* ```read_only()```: A Boolean value (true / false) that indicates whether you have readOnly or full access to the website
* ```alignment()```: The alignment of your website (Center, Left, Right, Flexible). This setting is used to make the mouse movement heatmaps more precise.
* ```width()```: The width in pixels of you website. This setting is used to make the mouse movement heatmaps more precise.
* ```page_identifiers()```: An alias or name you have given for your website (defaults to the website domain)
* ```encoding()```: An alias or name you have given for your website (defaults to the website domain)
* ```anonymize_ips()```: A setting that controls whether to anonymize users’ IP addresses by removing the last digits.
* ```excluded_ips()```: A list of IP addresses or patterns to exclude from recording. Use asterisk (*) at the end of the string as wildcard. Example: 100.100.*
* ```merge_urls()```: Used for merging several URLs into one in the heatmap lists. Use asterisk (*) as wildcard, or use regular expressions.
* ```recordings(...)```
    *  ```id: str```: (Optional) The id of the recording to load (Returns Recording instead of Recordings)
    *  ```search: str```: (Optional) Use any free-text search here. The system searches in all filterable fields, and includes the user agent string, the IP address, the city and region of the visitor. However, when used in heatmap page lists, it only searches in the page URLs
    *  ```from_date: str```: (Optional) The start date of the query. The actual start time is midnight on the selected date, according to the user’s selected time zone. ***example: 2015-10-04***
    *  ```to_date: str```: (Optional) The end date of the query. This date is not included in the query.
    *  ```country: str```: (Optional) Only visitors from a specific country. Countries are represented by their two-character country codes, defined by the ISO 3166-1 alpha-2 standard.
    *  ```tags: list```: (Optional) A list of tags to filter by
    *  ```vars: dict```: (Optional) A list of variables to filter by
    *  ```star: bool```: (Optional) Filter only by stared recordings


### Websites

Returns a list of websites available

```py
connection.websites()
```

### Methods

* ```list()```: Returns a list of dictionaries with information about each available site

#### Methods


### Recordings

```
connection.websites(site_name).recordings()
```


## Examples

### Listing all available websites

```python
connection = Mouseflow(
    user,
    token
)

list_of_websites = connection.websites().list()
```

### Selecting a specific site

```python
connection = Mouseflow(
    user,
    token
)

website = connection.websites("website name or id")
```