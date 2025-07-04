## Wonderwise Travel Planner

A Flask web application that uses the OpenAI API to generate personalized travel itineraries based on user inputs. It also suggests local activities from a built-in `activities` dataset.

---

### Features

* **Dynamic Itinerary Generation:** Uses OpenAI's GPT-4 model to create a detailed day-by-day travel plan.
* **Local Activities Filter:** Filters and displays local activities from `activities/activity_data.py` that match the user's destination and style preferences.
* **Secure API Key Management:** Loads the OpenAI API key from an environment variable (`.env` file) using `python-dotenv`.

---

### Prerequisites

* Python 3.8 or higher
* Git
* An OpenAI API key

---

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/kamy-99/wonderwise.git
   cd wonderwise
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project root:

   ```ini
   OPENAI_API_KEY=sk-your-actual-openai-key-here
   ```

5. **Ensure `.env` is ignored**

   ```bash
   echo ".env" >> .gitignore
   ```

---

### Running the App

```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:5000` to access the app.

---

### Project Structure

```
wonderwise/
├── app.py                # Main Flask application
├── activities.py         # Local activities data
├── templates/
│   ├── index.html        # Form page template
│   └── result.html       # Itinerary display template
├── .env                  # Environment variables (ignored by Git)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

### Usage

1. Fill out the form on the homepage with:

   * **Destination** (city or country)
   * **Number of days**
   * **Budget** (in USD)
   * **Travel style** (e.g., luxury, budget, adventure)
   * **Group type** (solo, couple, family, friends)
2. Submit the form.
3. View the generated itinerary and local activity suggestions.

---

### Troubleshooting

* **No itinerary returned:** Ensure your OpenAI API key is valid and has quota.
* **`dotenv` errors:** Make sure the `python-dotenv` package is installed and `.env` is in the root.
* **Filtering issues:** Confirm that `activities.activity_data` entries use lowercase city names and matching style tags.

---

### Contributing

Contributions are welcome! Please open an issue or submit a pull request.


