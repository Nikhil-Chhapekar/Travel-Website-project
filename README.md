# 🌍 Discovering Paradise - Travel Website

A comprehensive Django-based travel platform that helps users explore and discover amazing travel destinations worldwide. Browse destinations, read reviews, book accommodations, and plan your next adventure!

![Django](https://img.shields.io/badge/Django-5.2-green.svg)
![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📸 Website Preview

### Homepage
![Homepage Hero Section](static/images/hero-bg.jpg)
*Explore featured destinations and start your journey*

### Destinations Gallery
![Destinations](static/images/backgrounds/destinations-bg.jpg)
*Browse through stunning travel destinations across continents*

### Featured Locations

<table>
  <tr>
    <td><img src="static/images/destinations/paris.jpg" alt="Paris" width="200"/><br/><b>Paris, France</b></td>
    <td><img src="static/images/destinations/bali.jpg" alt="Bali" width="200"/><br/><b>Bali, Indonesia</b></td>
    <td><img src="static/images/destinations/santorini.jpg" alt="Santorini" width="200"/><br/><b>Santorini, Greece</b></td>
  </tr>
  <tr>
    <td><img src="static/images/destinations/maldives.jpg" alt="Maldives" width="200"/><br/><b>Maldives</b></td>
    <td><img src="static/images/destinations/kyoto.jpg" alt="Kyoto" width="200"/><br/><b>Kyoto, Japan</b></td>
    <td><img src="static/images/destinations/machu-picchu.jpg" alt="Machu Picchu" width="200"/><br/><b>Machu Picchu, Peru</b></td>
  </tr>
</table>

### Accommodations
![Luxury Resort](static/images/accommodations/luxury-resort.jpg)
*Premium accommodations for your perfect stay*

### Activities & Experiences
<table>
  <tr>
    <td><img src="static/images/activities/scuba-diving.jpg" alt="Scuba Diving" width="250"/></td>
    <td><img src="static/images/activities/city-tour.jpg" alt="City Tour" width="250"/></td>
    <td><img src="static/images/activities/hiking.jpg" alt="Hiking" width="250"/></td>
  </tr>
</table>

## ✨ Features

### 🗺️ Destination Management
- Browse destinations by continent, country, or category
- Detailed destination pages with highlights and best visiting times
- Featured destinations showcase
- Beautiful image galleries

### 🏨 Accommodation Booking
- Multiple accommodation types (Hotels, Resorts, Villas, Hostels)
- Detailed amenities and pricing information
- Easy booking system with date selection
- Room type preferences

### 🎯 Activities & Experiences
- Curated activities for each destination
- Duration and pricing details
- Activity booking system
- Photo galleries

### ⭐ User Reviews
- Leave reviews for visited destinations
- Rating system
- Recent reviews showcase
- User authentication integration

### 👤 User Accounts
- User registration and login
- Profile management
- Booking history
- Personalized experience

### 📧 Contact & Newsletter
- Contact form for inquiries
- Newsletter subscription
- FAQ section
- Privacy policy and terms of service

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd travel_website
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install django pillow
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the website**
   - Open your browser and navigate to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📁 Project Structure

```
travel_website/
├── accounts/           # User authentication and profiles
├── bookings/          # Booking management system
├── core/              # Core functionality (home, contact, etc.)
├── destinations/      # Destination and accommodation management
├── reviews/           # Review system
├── discovering_paradise/  # Main project settings
├── static/            # Static files (CSS, JS, images)
├── templates/         # HTML templates
├── media/             # User-uploaded media files
└── manage.py          # Django management script
```

## 🛠️ Technology Stack

### Backend
- **Django 5.2** - High-level Python web framework
- **SQLite** - Database (can be switched to PostgreSQL/MySQL)
- **Pillow** - Image processing library

### Frontend
- **Bootstrap 5.3** - Responsive CSS framework
- **Font Awesome** - Icon library
- **Custom CSS** - Modern animations and styling
- **JavaScript** - Interactive features

### Key Django Apps
- **Core** - Homepage, contact, newsletter, FAQ
- **Destinations** - Destination browsing and details
- **Bookings** - Accommodation and activity bookings
- **Accounts** - User authentication and profiles
- **Reviews** - User reviews and ratings

## 🎨 Design Features

- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- **Modern UI/UX** - Clean and intuitive interface
- **Smooth Animations** - CSS transitions and hover effects
- **Image Optimization** - Optimized media delivery
- **Accessibility** - WCAG compliant design patterns

## 📊 Database Models

### Destination
- Name, country, continent
- Description and highlights
- Best time to visit
- Featured status
- Image gallery

### Accommodation
- Multiple types (Hotel, Resort, Villa, etc.)
- Amenities and pricing
- Linked to destinations
- Booking system

### Review
- User ratings (1-5 stars)
- Review text
- Linked to users and destinations
- Timestamp tracking

### Booking
- User information
- Check-in/check-out dates
- Room preferences
- Special requests
- Unique booking ID

## 🔐 Admin Panel

Access the Django admin panel to manage:
- Destinations and accommodations
- User accounts and permissions
- Reviews and ratings
- Bookings and reservations
- Newsletter subscribers
- Contact messages
- FAQ entries

**Admin URL:** `http://127.0.0.1:8000/admin/`

## 🌟 Key Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Featured destinations and recent reviews |
| Destinations | `/destinations/` | Browse all destinations |
| Destination Detail | `/destinations/<slug>/` | Detailed destination information |
| About | `/about/` | About the platform |
| Contact | `/contact/` | Contact form |
| FAQ | `/faq/` | Frequently asked questions |
| Login | `/accounts/login/` | User login |
| Register | `/accounts/register/` | User registration |
| Profile | `/accounts/profile/` | User profile and bookings |

## 📝 Usage Examples

### Adding a New Destination (Admin)
1. Login to admin panel
2. Navigate to Destinations
3. Click "Add Destination"
4. Fill in details (name, country, description, etc.)
5. Upload destination image
6. Mark as featured (optional)
7. Save

### Booking an Accommodation (User)
1. Browse destinations
2. Select a destination
3. View available accommodations
4. Click "Book Now"
5. Fill in booking details
6. Submit booking request

### Leaving a Review (User)
1. Login to your account
2. Visit a destination page
3. Click "Write a Review"
4. Rate and write your experience
5. Submit review

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Team

![Team Member 1](static/images/team/team-1.jpg) ![Team Member 2](static/images/team/team-2.jpg) ![Team Member 3](static/images/team/team-3.jpg)

## 📞 Contact

For any inquiries or support, please use the contact form on the website or reach out through the admin panel.

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team
- Font Awesome
- Unsplash for placeholder images
- All contributors and users

---

**Made with ❤️ by the Discovering Paradise Team**

*Start your journey today and discover paradise!* 🌴✈️🌊

