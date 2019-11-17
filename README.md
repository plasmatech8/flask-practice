# Flask Practice

## Quick commands

Flask help menu: `flask`

Run a flask python file: `python helloworld.py`

Send GET/POST requests via curl. Alternatively, you can use the Postman Chrome extension.

## Tutorial 1

*Building a REST API using Python and Flask | Flask-RESTful*

See https://www.youtube.com/watch?v=s_ht4AKnWZg

1. helloword_website.py
    * Create a dynamic website with pure flask
    * Use `python 01_helloword_website.py`
    * Notice that if you include the `-v verbose` parameter, you can see that it is a HTML server. Not json/REST.
    * You can use `jsonify` to change the content type to something else.

2. helloword_api.py:
    * / (index) get request:
        * `curl http://127.0.0.1:5000/`
    * / (index) post request:
        * `curl -H "Content-Type: application/json" -X POST -d '{"key":"value"}' http://127.0.0.1:5000/`
        * Don't use powershell or cmd. Use bash on Windows or otherwise (`bash`).
    * /multi/(int) get request:
        * `curl http://127.0.0.1:5000/multi/5`

3. helloworld_rest.py (using the flask-restful extension)
    * Use same commands as above


