# 🔐 File Encryption Manager

A professional file encryption tool built with Python and cryptography.

## 🚀 Features
- File & Folder Encryption/Decryption
- Secure Key Management  
- Recursive Directory Processing
- User-friendly Interface

## ⚙️ System Requirements

### 🐍 Python Version
- **Python 3.8 or higher** required
- Download from: [python.org](https://python.org)

### 📦 Dependencies
- **cryptography** library
- **No admin rights needed** for installation

## 🛠️ Installation

### 1. Install Required Package
```bash
pip install cryptography
```

### 2. Alternative Installation Methods

#### 🪟 Windows Users:
```cmd
pip install cryptography
```

#### 🐧 Linux/macOS Users:
```bash
pip3 install cryptography
```

#### 🔧 If pip fails, try:
```bash
python -m pip install cryptography
```

## 🎯 Quick Start

1. **Install cryptography** (see above)
2. **Run the program**:
```bash
python main.py
```

3. **Follow the on-screen instructions**

## 📁 Project Structure
```
FileEncryptionManager/
├── main.py              # Main application
├── folder/              # Target directory for files
├── secret/              # Encryption keys storage
└── README.md           # This file
```

## 🔧 Usage Guide

### 🔐 Encryption
1. Select option `1` for Encryption
2. Navigate through folders using numbers
3. Choose files or folders to encrypt
4. System automatically skips already encrypted files

### 🔓 Decryption  
1. Select option `2` for Decryption
2. Navigate to encrypted files/folders
3. System detects and decrypts encrypted files only
4. Skips files that are not encrypted

### 🎮 Navigation
- Use numbers to select folders/files
- `Back` options to navigate up
- `Encrypt/Decrypt Folder` for bulk operations

## 👨‍💻 Developer
**Kahitsino** - Grade 12 student
- GitHub: [Kahitsino](https://github.com/kahitsino)

## 🛠️ Technologies
- Python 3.12
- Cryptography (Fernet)
- OS Module

## ❓ Troubleshooting

### 🔴 "ModuleNotFoundError: No module named 'cryptography'"
**Solution:** Run `pip install cryptography`

### 🔴 "pip not found"
**Solution:** 
- Windows: `python -m pip install cryptography`
- Linux/macOS: `pip3 install cryptography`

### 🔴 Permission Errors
**Solution:** Use virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install cryptography
```

### 🔴 Key File Corruption
**Solution:** Program automatically detects and generates new key

## ⚠️ Important Notes
- **Keep your key file safe** - losing it means losing access to encrypted files
- **Backup important files** before encryption
- **Test with sample files** first before real data
- **One-time encryption** - files can only be encrypted once for security

## 🔒 Security Features
- Fernet symmetric encryption
- Automatic duplicate encryption prevention
- Secure key storage and validation
- Corrupted key detection and recovery

---
*Built with passion for cybersecurity education* 🔥

## ⚠️ LEGAL DISCLAIMER

### 🚨 **IMPORTANT LEGAL NOTICE**

**THIS SOFTWARE IS FOR EDUCATIONAL AND LEGITIMATE SECURITY PURPOSES ONLY**

### 🔒 **INTENDED USAGE**
- ✅ **Educational purposes** - Learning cryptography concepts
- ✅ **Personal file protection** - Securing your own files
- ✅ **Authorized testing** - On systems you own or have permission to test
- ✅ **Cybersecurity training** - Understanding encryption principles

### 🚫 **PROHIBITED USAGE**  
- ❌ **Illegal activities** - Including but not limited to ransomware attacks
- ❌ **Unauthorized access** - Encrypting files without owner consent
- ❌ **Malicious purposes** - Data hostage situations or extortion
- ❌ **Network intrusion** - Unauthorized system access

### ⚖️ **LEGAL COMPLIANCE**
- Users are **solely responsible** for how they use this software
- Developer assumes **no liability** for misuse or damages
- **Comply with local laws** - Encryption regulations vary by country
- **Obtain proper authorization** before testing on any systems

### 🔐 **ETHICAL GUIDELINES**
- Only encrypt files you **own or have permission** to modify
- Maintain **secure backups** of encryption keys
- Use for **defensive security** purposes only
- Report vulnerabilities responsibly

### 📜 **LICENSE AGREEMENT**
By using this software, you agree to:
1. Use it **legally and ethically**
2. Accept **full responsibility** for your actions
3. Not hold the developer liable for misuse
4. Comply with all **applicable laws**

### 🛡️ **RESPONSIBLE DISCLOSURE**
- Do not exploit without permission

---

**⚠️ WARNING: UNAUTHORIZED USE MAY RESULT IN LEGAL CONSEQUENCES**

*This tool demonstrates cybersecurity concepts - use your knowledge responsibly* 🔐

## 🎓 **EDUCATIONAL PURPOSE STATEMENT**

This project was developed as part of a **Computer Science learning journey** to understand:
- File encryption/decryption principles
- Python programming and cryptography
- Secure software development practices
- Ethical cybersecurity implementation

**Remember: With great power comes great responsibility!** 🕷️

---
*Use this knowledge to protect, not to harm* ✨