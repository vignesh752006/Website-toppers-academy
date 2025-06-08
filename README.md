# Toppers Academy Website

A comprehensive website for Toppers Academy, featuring multiple modules for managing admissions, results, fees, gallery, events, and team information.

## Features

- Modern, responsive design using Bootstrap 5
- Multiple modules for different functionalities
- User-friendly interface
- Mobile-first approach
- Easy to maintain and extend

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd toppersacademy
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The website will be available at `http://127.0.0.1:8000/`

## Project Structure

- `core/` - Main app with home, about, and contact pages
- `admissions/` - Handles student admissions
- `results/` - Manages student results
- `fees/` - Handles fee management
- `gallery/` - Photo gallery
- `events/` - School events and announcements
- `team/` - Faculty and staff information

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any queries, please contact:
- Email: info@toppersacademy.com
- Phone: +1234567890 