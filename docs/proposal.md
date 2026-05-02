# Smart Home Cloud Pi
#### Student Name: *Tiago de Gregori*   Student ID: *20119203*

**Project Description**

This project implements a Raspberry Pi-based Personal Cloud Storage System using Nextcloud, enhanced with camera integration, Sense HAT functionality, and a lightweight AI assistant.

The system allows users connected to the same local WiFi network to access, store, and manage files within a private home cloud environment. In addition, secure remote access over the internet is supported, allowing authorised users to access the system using login credentials, similar to a cloud storage service.

A QR code-based authentication mechanism is implemented using the Raspberry Pi camera to control administrative access. This ensures that only authorised users can perform management actions on the system.

A lightweight AI assistant is integrated as an extension to the system to provide basic interaction and system support. When the assistant is active, the Sense HAT LED matrix displays a simple visual indicator (":)") to represent its presence.

The Sense HAT is also used to monitor environmental data such as temperature and humidity, and to provide system status feedback. 

The Raspberry Pi operates as a continuously running server, ensuring that the cloud system remains available independently of other devices such as personal computers.

## Tools, Technologies and Equipment

**Hardware**

- Raspberry Pi 4 (used as the main server)
- Raspberry Pi Camera Module (used for QR code authentication)
- Sense HAT (used for environmental sensing and LED status display)
- External Hard Drive – 500GB (used for file storage in the cloud system)

**Software / Programming**

- Python (Hopefully)
- Raspberry Pi OS
- Nextcloud (for cloud storage and file management)
    
**Networking**

- Local WiFi Network (for local access to the cloud system)
- Internet Connection (for secure remote access)
- HTTP/HTTPS Protocol (for web-based access)

**Tools**

- Visual Studio Code
- GitHub
- OpenCV (for camera processing)
- Pyzbar (for QR code scanning)
- Sense HAT Python Library

## Project Repository

https://github.com/tagrgr/Smart-Home-Cloud-Pi

