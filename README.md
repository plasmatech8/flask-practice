# Flask Practice

## Quick commands

Flask help menu: `flask`

Run a flask python file: `python <filename>.py` (i.e. `python helloword_website.py`)

Send GET/POST requests via curl as shown below. Alternatively, you can use the Postman Chrome extension.

(Note: 127.0.0.1 can be substituted with localhost)

## Tutorial 1

*Building a REST API using Python and Flask | Flask-RESTful*

See https://www.youtube.com/watch?v=s_ht4AKnWZg

1. helloword_website.py
    * Create a dynamic website with pure flask
    * Notice that if you include the `-v verbose` parameter, you can see that it is a HTML server. Not json/REST.
    * You can use `jsonify` to change the content type to something else.

2. helloword_api.py
    * (Ensure you are using an appropriate terminal if using Windows i.e. bash)
    * / (index) get request:
        * `curl http://127.0.0.1:5000/`
    * / (index) post request:
        * `curl -H "Content-Type: application/json" -X POST -d '{"key":"value"}' http://127.0.0.1:5000/`
        * Don't use powershell or cmd. Use bash on Windows or otherwise (`bash`).
    * /multi/(int) get request:
        * `curl http://127.0.0.1:5000/multi/5`

3. helloworld_rest.py (using the flask-restful extension)
    * Use same commands as above

## Practice 1

1. production_website.py
    * Flask uses a debug server which updates in real-time, but does not scale well and only serves one request at a time by default.
    * Use gevent.pywsgi.WSGIServer can be used for a production website.
    * Use same commands as above

2. apiserver_conecpt.py
    * Creating my own concept for an API server using Flask (like flask-restful)
        * Properties:
            * Features
            * Input schema validation (can validate dictionaries and types)
            * Pass your function into the `APIServer.add_resource` function and have an quick and easy API function.

        * Shortcommings:
            * Input schema validation is odd when considering GET request data using query strings because query strings can have duplicated key-value pairs and you cannot write dictionary or list types into a query string.
            * Floats.Json float values are automatically converted Python float types. This is bad because the developer may have sensitive monetary values and wish to use a more precise number type (like decimal types).
            * It is an annoyance that passing a number without a decimal place (e.g. 1) into a json value that is meant to be a float gives a validation error (while 1.0 does not give any error).

        * Potential features/improvements:
            * Was planning to have an `input_validation` parameter which would have the same schema as `input_schema`, except this parameter would allow lambda functions to convert/transform/validate the values.
            * json validation should perhaps be moved to a seperate function that developers can use in their API function if they chose to. I know that other json validation packages exist (e.g. `jsonschema`), but I think that a custom solution may be simpler and easier for developers.
            * Need to learn `swagger` and know how to integrate it with this concept.
            * Better password management.
            * Better access denied/error messaging.
            * Implement a production webserver when debug=False

    * Usage:
        * Create the API server as seen at the bottom of `apiserver_concept.py` under `if __name__ == '__main__':`
        * Use `python apiserver_concept.py` to activate the server.

    * Testing:
        * (Ensure you are using an appropriate terminal if using Windows i.e. activate bash for windows using the `bash` command)
        * Use `curl -H "Content-Type: application/json" -X POST -d '{"num":1, "foo":"1", "hoo": {"raa": 1.0, "naa":[1,2,2,3,3]}, "password":"jackamoly"}' http://127.0.0.1:5000/multi` to query the multiply10 POST request resource. Note that GET requests will not work because query strings cannot handle to complex dictionary/array structures.
        * Use `curl 127.0.0.1:5000/ ` to query the index GET request resource. It will simply return the