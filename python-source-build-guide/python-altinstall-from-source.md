# 📘 Build Python from Source (Generic Altinstall Method)

## ⚠️ Important Rules

* **DO NOT** modify system Python
* **ALWAYS** use `make altinstall`
* Install required development libraries first
* **NEVER** create `/usr/bin/python` symlink manually

---

# 1️⃣ Install Required Build Dependencies

## 🟥 For RHEL / Rocky / Alma (EL Family)

Applies to:

* Red Hat Enterprise Linux
* Rocky Linux
* AlmaLinux

```bash
sudo dnf groupinstall "Development Tools" -y

sudo dnf install -y \
openssl-devel \
bzip2-devel \
libffi-devel \
zlib-devel \
readline-devel \
sqlite-devel \
xz-devel \
tk-devel \
gdbm-devel \
ncurses-devel \
wget
```

---

## 🟦 For Debian / Ubuntu (Debian Family)

Applies to:

* Debian
* Ubuntu

```bash
sudo apt update

sudo apt install -y \
build-essential \
wget \
libssl-dev \
zlib1g-dev \
libbz2-dev \
libreadline-dev \
libsqlite3-dev \
libffi-dev \
libncursesw5-dev \
xz-utils \
tk-dev \
libgdbm-dev \
liblzma-dev
```

---

# 2️⃣ Set Python Version (Change Only This)

```bash
PY_VERSION=3.13.0
```

You may replace with:

```
3.12.3
3.11.9
3.10.14
etc.
```

---

# 3️⃣ Download & Extract

```bash
cd /usr/src
sudo wget https://www.python.org/ftp/python/${PY_VERSION}/Python-${PY_VERSION}.tgz
sudo tar -xzf Python-${PY_VERSION}.tgz
cd Python-${PY_VERSION}
```

---

# 4️⃣ Clean Previous Builds (If Rebuilding)

```bash
sudo make distclean
```

Ignore error if this is the first build.

---

# 5️⃣ Configure (With OpenSSL Support)

```bash
sudo ./configure \
--enable-optimizations \
--with-openssl=/usr \
--with-ensurepip=install
```

### ✅ Verify

Ensure output contains:

```
checking for OpenSSL... yes
```

---

# 6️⃣ Compile

```bash
sudo make -j$(nproc)
```

---

# 7️⃣ Install Safely (ALTINSTALL ONLY)

```bash
sudo make altinstall
```

This installs:

```
/usr/local/bin/pythonX.Y
```

Examples:

```
/usr/local/bin/python3.13
/usr/local/bin/python3.12
```

System Python remains untouched.

---

# 8️⃣ Verify Installation

Check version:

```bash
/usr/local/bin/pythonX.Y --version
```

Check SSL support:

```bash
/usr/local/bin/pythonX.Y -c "import ssl; print(ssl.OPENSSL_VERSION)"
```

---

# 9️⃣ Create Virtual Environment

```bash
/usr/local/bin/pythonX.Y -m venv myenv
source myenv/bin/activate
```

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

---

# 📂 Installation Locations

Binary:

```
/usr/local/bin/pythonX.Y
```

Libraries:

```
/usr/local/lib/pythonX.Y/
```

---

# 🛑 Never Do This

❌ `sudo make install`
❌ Remove system Python
❌ Modify `/usr/bin/python`
❌ Replace `/usr/bin/python3`

---

# 🧹 Remove Custom Python (If Needed)

```bash
sudo rm -f /usr/local/bin/pythonX.Y
sudo rm -rf /usr/local/lib/pythonX.Y
```

---

# ✅ Final Result

You now have:

* System Python (untouched)
* Custom Python installed under `/usr/local`
* SSL working
* pip working
* venv ready
* Multiple Python versions coexisting safely
* Works on EL family and Debian family systems

---
