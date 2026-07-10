.PHONY: all setup notebooks figures report clean

all: notebooks figures report

setup:
	pip install -r requirements.txt

notebooks:
	cd notebooks && jupyter nbconvert --to notebook --execute 00_data_exploration.ipynb --output 00_data_exploration.ipynb --ExecutePreprocessor.timeout=120
	cd notebooks && jupyter nbconvert --to notebook --execute 01_pitch_arsenal_analysis.ipynb --output 01_pitch_arsenal_analysis.ipynb --ExecutePreprocessor.timeout=120
	cd notebooks && jupyter nbconvert --to notebook --execute 02_performance_metrics.ipynb --output 02_performance_metrics.ipynb --ExecutePreprocessor.timeout=120
	cd notebooks && jupyter nbconvert --to notebook --execute 03_platoon_and_situational.ipynb --output 03_platoon_and_situational.ipynb --ExecutePreprocessor.timeout=120
	cd notebooks && jupyter nbconvert --to notebook --execute 04_summary_dashboard.ipynb --output 04_summary_dashboard.ipynb --ExecutePreprocessor.timeout=120

figures: notebooks

report:
	python script/generate_report.py
	python script/generate_presentation.py

clean:
	rm -rf figures/*.png figures/*.csv report/*.docx report/*.pptx
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete
