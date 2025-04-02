# Microloan Tracker

A full-stack web application to manage microloans, built with Django, Supabase, Bootstrap, and deployed on Vercel. Track loans, toggle statuses, visualize analytics, and switch between dark/light themes—all in a responsive, user-friendly interface.

## Live Demo

[https://microloan-tracker.vercel.app](https://microloan-tracker.vercel.app)

## Features

- **Loan Management**: Create, edit, delete, and toggle loan statuses (Active/Paid).
- **Overdue Alerts**: Highlights loans past due dates.
- **Analytics**: Pie chart visualization of Active vs. Paid loans using Chart.js.
- **Theme Toggle**: Dark/light mode with cookie-based persistence.
- **Responsive UI**: Styled with Bootstrap for seamless use on desktop and mobile.
- **Data Validation**: Client-side checks for dates (YYYY-MM-DD), amounts, and categories.

## Tech Stack

- **Frontend**: Bootstrap, JavaScript, Chart.js
- **Backend**: Django, Python
- **Database**: Supabase (PostgreSQL)
- **Deployment**: Vercel
- **Tools**: Git, GitHub

## Installation (Local Setup)

1. **Clone the Repo**

   git clone https://github.com/ConradPB/microloan-tracker.git
   cd microloan-tracker

2. **Set Up Virtual Environment**

   python -m venv venv
   source venv/bin/activate # Mac/Linux
   venv\Scripts\activate # Windows

3. **Install Dependencies**

   pip install -r requirements.txt

4. **Configure Supabase**

- Sign up at [Supabase](https://supabase.com), create a project.
- Set up a `loans` table with columns: `id`, `borrower`, `amount`, `status`, `due_date`, `category`.
- Update `settings.py` with your Supabase URL and key:
  ```
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'postgres',
          'USER': 'postgres',
          'PASSWORD': '[YOUR_SUPABASE_KEY]',
          'HOST': '[YOUR_SUPABASE_HOST]',
          'PORT': '5432',
      }
  }
  ```

5. **Run Migrations**

   python manage.py makemigrations
   python manage.py migrate

6. **Start the Server**

   python manage.py runserver

- Visit `http://127.0.0.1:8000`.

## Deployment

- **Vercel**:
  - Push to GitHub, link to Vercel, set `DEBUG = False` in `settings.py`.
  - Add `vercel.json` for routing (see repo).

## Contributing

Fork, branch, and PR! Issues welcome on GitHub.

## License

MIT License - feel free to use and adapt.

## Contact

Name: Conrad Philip B. M

Email: cpbmbaz57@gmail.com

GitHub: ConradPB (https://github.com/ConradPB)
