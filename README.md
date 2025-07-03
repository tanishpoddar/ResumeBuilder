# Resume Builder

A modern, full-stack web application for creating professional resumes with real-time editing, multiple templates, and PDF export capabilities.

## 🚀 Features

- **6 Professional Templates**: Choose from Classic, Modern, Elegant, Creative, Technical, and Compact designs
- **Real-time Editing**: Live preview as you edit your resume sections
- **Dynamic Sections**: Add, edit, and remove education, work experience, projects, skills, and more
- **PDF Export**: Download your resume as a high-quality PDF with one click
- **User Authentication**: Secure login/registration system
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **PWA Ready**: Progressive Web App support with manifest and icons

## 🛠️ Tech Stack

### Backend
- **Django 5.2.3**: Web framework
- **Django REST Framework**: API development
- **PostgreSQL**: Database
- **PDFShift API**: PDF generation (cloud-native, no binary dependencies)

### Frontend
- **Bootstrap 5.3.0**: UI framework
- **Vanilla JavaScript**: Dynamic interactions
- **HTML5/CSS3**: Modern web standards

### DevOps & Tools
- **python-dotenv**: Environment variable management
- **CORS headers**: Cross-origin resource sharing
- **Django Crispy Forms**: Form styling

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL
- Git

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd new
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   PDFSHIFT_API_KEY=your_pdfshift_api_key_here
   ```
   
   Get your free API key from [PDFShift](https://pdfshift.io/signup)

5. **Configure database**
   ```bash
   # Create PostgreSQL database
   createdb resume_db
   
   # Run migrations
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   Open your browser and go to `http://127.0.0.1:8000`

## 📖 Usage

### For Users

1. **Register/Login**: Create an account or sign in
2. **Select Template**: Choose from 6 professional templates
3. **Fill Resume Details**: Add your personal information, education, work experience, etc.
4. **Preview**: See your resume in real-time
5. **Download PDF**: Export your resume as a professional PDF

### For Developers

#### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/templates/` | GET | List all available templates |
| `/api/templates/<id>/` | GET | Get specific template details |
| `/api/resumes/` | GET, POST | List user's resumes or create new |
| `/api/resumes/<id>/` | GET, PUT, DELETE | Get, update, or delete resume |
| `/api/resumes/<id>/render/` | GET | Get rendered HTML for preview |
| `/api/resumes/<id>/export_pdf/` | GET | Download resume as PDF |

#### Running Tests
```bash
python manage.py test resumes
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `PDFSHIFT_API_KEY` | API key for PDF generation | Yes |

### Database Configuration

The project uses PostgreSQL by default. Update `DATABASES` in `backend/resume_builder/settings.py` if needed.

## 🚀 Deployment

### Local Development
```bash
python manage.py runserver
```

### Production
1. Set `DEBUG = False` in settings
2. Configure `ALLOWED_HOSTS`
3. Set up HTTPS
4. Use a production database
5. Set environment variables

### Cloud Deployment
This application is designed to work on any cloud platform:
- **Vercel**: Serverless deployment
- **Heroku**: Container-based deployment
- **AWS/GCP/Azure**: VM or container deployment

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

Run specific app tests:
```bash
python manage.py test resumes
```

## 📁 Project Structure

```
new/
├── backend/
│   ├── resume_builder/     # Django project settings
│   ├── resumes/           # Resume app (models, views, serializers)
│   ├── web/              # Web app (templates, static files)
│   └── manage.py
├── web/
│   └── templates/
│       └── resume_templates/  # Resume HTML templates
├── requirements.txt
└── README.md
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**Tanish Poddar** (he/him)
- CSE student at SRM IST
- Excelled in WebDev, Kotlin, Python & MySQL
- **Website**: [tanish-poddar.is-a.dev](https://tanish-poddar.is-a.dev/)
- **Email**: tanishpoddar.18@gmail.com
- **GitHub**: [@tanishpoddar](https://github.com/tanishpoddar)

## 🙏 Acknowledgments

- [PDFShift](https://pdfshift.io/) for cloud-native PDF generation
- [Bootstrap](https://getbootstrap.com/) for the UI framework
- [Django](https://www.djangoproject.com/) for the web framework

---

Made with ❤️ by [Tanish Poddar](https://tanish-poddar.is-a.dev/) 