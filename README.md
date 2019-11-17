# Flask Practice

## Quick commands

Flask help menu: `flask`
Run a flask python file: `python helloworld.py`

## Tutorial 1
See https://www.youtube.com/watch?v=s_ht4AKnWZg

1. helloword_website.py
    * Create a dynamic website with pure flask
    * Use `python 01_helloword_website.py`
    * Notice that if you include the `-v verbose` parameter, you can see that it is a HTML server. Not json/REST.
    * You can use `jsonify` to change the content type to something else.

2. helloword_api.py:
    * Curl with key-value pairs: `curl -d "data=example1&data2=example2" <url>`
    * Curl with `curl -H "Content-Type: application/json" -X POST -d '{"key":"value"}' <url>`

`
3. helloworld_rest.py
    * Create a flask API using the flask-restful extension


