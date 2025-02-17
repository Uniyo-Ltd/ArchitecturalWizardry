from flask import Flask, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from models import Session, HubSpotField, UpsoEmailCadence
from mock_services import mock_hubspot_api_call, mock_upso_api_call

app = Flask(__name__)

@app.route('/api/hubspot/fields', methods=['POST'])
def add_hubspot_field():
    with Session() as session:
        data = request.json
        new_field = HubSpotField(field_name=data['field_name'], field_type=data['field_type'])
        session.add(new_field)
        session.commit()
        mock_hubspot_api_call(data['field_name'], data['field_type'])
        return jsonify({"message": "Field added successfully"}), 201

@app.route('/api/hubspot/fields/<string:field_name>', methods=['PUT'])
def update_hubspot_field(field_name):
    with Session() as session:
        field = session.query(HubSpotField).filter_by(field_name=field_name).first()
        if field:
            field.field_name = request.json.get('new_field_name', field.field_name)
            session.commit()
            mock_hubspot_api_call(field.field_name, field.field_type)
            return jsonify({"message": "Field updated successfully"}), 200
        return jsonify({"error": "Field not found"}), 404

@app.route('/api/upso/cadences', methods=['PUT'])
def update_upso_cadence():
    with Session() as session:
        cadence = session.query(UpsoEmailCadence).filter_by(cadence_name=request.json['cadence_name']).first()
        if cadence:
            cadence.timing = request.json.get('timing', cadence.timing)
            cadence.email_template = request.json.get('email_template', cadence.email_template)
            session.commit()
            mock_upso_api_call(cadence.cadence_name, cadence.timing, cadence.email_template)
            return jsonify({"message": "Cadence updated successfully"}), 200
        return jsonify({"error": "Cadence not found"}), 404
