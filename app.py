from flask import Flask, request, render_template
import openai
from activities import activity_data

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "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"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form inputs
        destination = request.form.get('destination')
        days = request.form.get('days')
        budget = request.form.get('budget')
        style = request.form.get('style')
        group = request.form.get('group')

        # Call OpenAI to generate itinerary
        prompt = f"""
You are an expert travel planner.

Plan a {days}-day vacation to {destination} for a {group} traveler.
The budget is ${budget}, and the preferred travel style is {style}.
Give a daily breakdown with activities, meals, and tips.
"""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful travel planning assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            itinerary = response['choices'][0]['message']['content']
        except Exception as e:
            itinerary = f"Error generating itinerary: {str(e)}"

        # Filter local activities by city and style (case insensitive)
        filtered_activities = [
            act for act in activity_data
            if act['city'].lower() == destination.lower() and style.lower() in act['type'].lower()
        ]

        return render_template('result.html', itinerary=itinerary, activities=filtered_activities, destination=destination)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
