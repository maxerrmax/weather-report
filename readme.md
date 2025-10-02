# Weather Report Generator

A simple Python project that generates random weather reports for any city.  
The script simulates weather conditions and temperatures, and can be extended to use real weather APIs.  

---

## Features
- Generates a random weather condition (sunny, cloudy, raining, snowing, etc.).
- Adjusts temperature ranges based on the weather type.
- Easy to run from the command line.
- Ready for extension with real API calls.

---

## Requirements
Python **3.10+** is recommended.  

Dependencies are listed in `requirements.txt`. Install them with:

```bash
pip install -r requirements.txt

```
---

## Usage

Run the script from the terminal:
```bash
python weather.py
```

You will be prompted to enter a city name. Example:

```bash
Enter a city name: Barcelona
Todays is sunny in Barcelona with a temperature of 32 degrees celsius, thanks for being here see you tomorrow!
```
## Testing

This project uses pytest for unit testing. To run the tests:
```bash
pytest
```
## Future Improvements

- Integrate real-time weather data using the requests library and an API (e.g., OpenWeatherMap).

- Add command-line arguments instead of user prompts.

- Build a Flask web interface for weather reports.

## License

This project is licensed under the MIT License.