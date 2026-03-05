from flask import Blueprint, request, jsonify
import pandas as pd

# Create a blueprint
pivot_bp = Blueprint('pivot', __name__)

@pivot_bp.route('/generate-pivot', methods=['POST'])
def generate_pivot():
    # Check if an Excel file is uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    
    # Read the uploaded Excel file
    try:
        df = pd.read_excel(file)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    # Get parameters from the request
    index = request.form.getlist('index')
    columns = request.form.getlist('columns')
    values = request.form.getlist('values')
    aggfunc = request.form.get('aggfunc', 'sum')
    
    # Generate pivot table
    try:
        pivot_table = df.pivot_table(index=index, columns=columns, values=values, aggfunc=aggfunc)
        return jsonify({'pivot_table': pivot_table.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

