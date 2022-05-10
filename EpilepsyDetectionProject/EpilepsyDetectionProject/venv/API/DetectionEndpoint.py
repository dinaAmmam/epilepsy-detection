class Detection(Resource):
    # methods go here
   # @app.route('/api/detection', methods=['POST'])
    def post(self):
        content = request.get_json(silent=True)
        print(content) # Do your processing
        return
    pass

api.add_resource(Detection, '/detection')  # '/detection' is our entry point