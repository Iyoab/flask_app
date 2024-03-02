from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send-location', methods=['POST'])
def receive_location():
    data = request.json
    if not data or 'latitude' not in data or 'longitude' not in data:
        return jsonify({"status": "error", "message": "Missing latitude or longitude"}), 400

    latitude = data['latitude']
    longitude = data['longitude']
    print(f"Received location: Latitude = {latitude}, Longitude = {longitude}")

    # Placeholder for processing logic
    # This is where you would add the logic to handle the location data
    # and potentially format it for drone commands.

    return jsonify({"status": "success", "message": "Location received and processed"}), 200

if __name__ == '__main__':
    app.run(debug=True)
