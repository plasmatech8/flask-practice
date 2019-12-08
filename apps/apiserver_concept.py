from flask import Flask, jsonify, request
import logging


password = "jackamoly"


def index(data):
    return data


def multiply10(data):
    if data['password'] != password:
        return "Access denied"

    return {"thing": data['num'] * 10}


class ApiServer():
    def __init__(self):
        """Initialises a new API server
        """
        self.flask_app = Flask(__name__)

    def _validate_input_schema(self, schema):
        """Validates the input schema object such that it can be used to check
        input data objects.
        """
        if isinstance(schema, type):
            pass
        elif isinstance(schema, dict):
            for key in schema:
                self._validate_input_schema(schema[key])
        elif schema is None:
            pass
        else:
            raise ValueError("Invalid validation schema. Please ensure that "
                             "dictionary values are either dicts objects "
                             "or types.")

    def _validate_input_data(self, data, schema, at_key=None):
        """Validates the input data from a GET or POST request such that it
        matches the structure of a data schema.
        """
        if isinstance(schema, type):
            # Check type (type)
            if not isinstance(data, schema):
                raise ValueError(
                    f"Input data does not match schema. Type of a value "
                    f"differs from schema. Value of '{at_key}' is "
                    f"{type(data)} but schema expects {schema}.")
        elif isinstance(schema, dict):
            # Check type (dict)
            if not isinstance(data, dict):
                raise ValueError(
                    f"Input data does not match schema. Type of a value "
                    f"differs from schema. Value of '{at_key}' is "
                    f"{type(data)} but schema expects {dict}.")
            # Check keys (dict)
            if data.keys() != schema.keys():
                keys_unexpected = set(data.keys()) - set(schema.keys())
                keys_missing = set(schema.keys()) - set(data.keys())
                raise ValueError(f"Input data does not match schema. "
                                 f"Dictionary keys mismatch with schema. "
                                 f"Unexpected keys: {keys_unexpected}. "
                                 f"Missing keys: {keys_missing}. ")
            # Check values recursively(dict)
            for key in schema:
                self._validate_input_data(data[key], schema[key], at_key=key)
        elif schema is None:
            pass
        else:
            raise ValueError("Invalid schema. Please ensure that dictionary "
                             "values are either types, None or dict objects.")

    def _retrieve_input_data(self):
        """Retrieves the input data from GET or POST request.
        """
        print(request.data)
        if (request.method == 'POST'):
            data = request.get_json()
        elif (request.method == 'GET'):
            data = request.args.to_dict()
        else:
            raise ValueError("Method is not POST or GET")
        return data

    def _new_resource(self, func, input_schema):
        """Returns a function wrapped around  handler code for the API.
        """
        def function_wrapper(*args, **kargs):
            data = self._retrieve_input_data()
            print("Request with data:", data)
            self._validate_input_data(data, input_schema)
            output = func(data, *args, **kargs)
            return jsonify(output)
        return function_wrapper

    def add_resource(self, func, rule, methods=['POST'], input_schema=None):
        """Adds an function to a resource as an API operation.
        """
        self._validate_input_schema(input_schema)
        new_func = self._new_resource(func, input_schema)
        self.flask_app.add_url_rule(rule,
                                    endpoint=func.__name__,
                                    view_func=new_func,
                                    methods=methods)

    def run(self, debug=False):
        """Start the API server
        """
        self.flask_app.run(host="0.0.0.0", port=5000, debug=debug)


if __name__ == '__main__':
    app = ApiServer()
    app.add_resource(index, '/', ['GET'])
    app.add_resource(multiply10, '/multi', ['POST', 'GET'],
                     input_schema={"num": int, "foo": str,
                                   "hoo": {"raa": float, "naa": list},
                                   "password": str})
    app.run(debug=True)
