rest_apis = [
    {
        "name": "TestAPI1",
        "version": "1.0.0",
        "context": "test1",
        "policies": ["Unlimited"],
        "endpointConfig": {
            "endpoint_type": "http",
            "sandbox_endpoints": {"url": "http://localhost:3000/"},
            "production_endpoints": {"url": "http://localhost:3000/"}
        }
    },
    {
        "name": "TestAPI2",
        "version": "1.0.0",
        "context": "test2",
        "policies": ["Unlimited"],
        "endpointConfig": {
            "endpoint_type": "http",
            "sandbox_endpoints": {"url": "http://localhost:3000/"},
            "production_endpoints": {"url": "http://localhost:3000/"}
        }
    }
]

graphql_schema_file_path = "./resources/schema_graphql.graphql"
