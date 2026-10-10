# Bass Diffusion Model: Claude Sonnet 4

Homework on the Bass Model, Marketing Analytics, AUA.

This project forecasts the adoption of Claude Sonnet 4 (TIME Best Inventions 2025)
in the United States, using the Internet as a look-alike innovation.

## Project structure

- `report/`
  - `report.ipynb`: the full analysis (steps 1–7, conclusion, references)
  - `report.html`: HTML export of the notebook
  - `report.pdf`: PDF version of the report
- `data/`
  - `share-of-individuals-using-the-internet.csv`: share of the population using the Internet, by country and year (ITU, via Our World in Data)
- `img/`
  - `internet_adoption_world.png`: share of the world population using the Internet, 2005–2025
  - `bass_fit_internet_us.png`: Bass model fit on the US Internet data (cumulative and yearly)
  - `claude_diffusion_forecast.png`: forecast of Claude's diffusion in the US
- `helper_functions.py`: Bass model equations, parameter estimation, R² and peak time
- `requirements.txt`: Python packages used

## How to run

pip install -r requirements.txt

Then open `report/report.ipynb` and run all cells.

## Data source

Our World in Data, Share of the population using the Internet:
https://ourworldindata.org/grapher/share-of-individuals-using-the-internet