# OCR Testing Setup

## Prerequisites

- Display card that allows GPU accelleration (ex. Ubuntu on Xorg, x11)
    - If unsure, check current display server with the following command: 
    ```echo $XDG_SESSION_TYPE```

- The *_tesseract-for-squish-4.1.1_* download (See [here](https://doc.qt.io/squish/ocr-and-installing-tesseract-for-squish.html) for  downlaod)

<br/>

## Instructions

1. Follow tesseract installation process. Make sure to enable **Register the Tesseract installation with Squish**.
   
<p align="center">
    <img src=info_assets/image-1.png width="700" align="center">
</p>

3. Configure Tesseract OCR engine by clicking **Edit > Preferences** to open the Preferences window. Then, in the side bar, click **Squish > OCR > Tesseract** to ensure installation path with Squish.


   
5. Verify with test run. 

<br/>

## Verifying with test run

<p align="center">
    <img src=info_assets/Screen-Recording-2024-11-15-at-2.gif width="700" align="center">
</p>

1. Create a Test Recording using the Squish GUI
2. Using the Controller window, click **OCR Text** under the **Verify** tab 
3. Select automatically detected text or configure your own **Search Text** Verification

<br/>

## FAQ

### 1. When trying to implement OCR Verification, I don't see my GUI in the **Select Text for Verification** window, and get the following error: 

#### *Squish desktop screenshot failed error*

This issue is due to incompatible display card/server. Depending on the Ubuntu version, the default display card may be **wayland**, which is incompatible with Squish OCR functions. Attempt to follow these isntructions:

- Make sure you choose a proper display card: 

<p align="center">
    <img src=info_assets/image-2.png width="500" align="center">
</p>

- NOTE: If you see Guest drivers are required for GPU acceleration when selecting **virtio-gpu-gl-pci**, run:

```
sudo apt install mesa-utils mesa-vulkan-drivers # mesa package for virtio-gpu
sudo apt install qemu-guest-agent # to optimize performance between host and guat
sudo apt install xserver-xorg-video-qxl
sudo apt update
sudo apt upgrade
```

- Run the following commands:**
   
```
# Reconfigure for Xorg
sudo dpkg-reconfigure xserver-xorg
sudo apt install --reinstall xorg

# Make sure you have the appropriate drivers
sudo apt install xserver-xorg-video-qxl # for virtio
sudo apt install xserver-xorg-video-vmware # for vmware
sudo apt install qemu-guest-agent # to optimize performance between host and guat

# Update drivers
sudo apt update
sudo apt upgrade
sudo ubuntu-drivers autoinstall

# Check if you're using GPU acceleration
glxinfo | grep "OpenGL renderer"
```

- Finally, in the Login screen, click to use Xorg on the bottom left corner.

<p align="center">
    <img src=info_assets/image-5.png width="700" align="center">
</p>

<br/>

### 2. I am able to open the OCR Text verification window using the Controller window, but, upon opening, I get the error: 

#### *Failed retrieving the engine properties: Cannot find the Leptonica library*

If encountering Leptonica library issues, verify library path. For example, if applicable, change the default **lib64** folder to **lib** as listed in the tesseract download.

<br/>

### 3. When troubleshooting and attempting to verify tesseract installation using **tesseract --version**, I get the following error: 

#### *symbol lookup error: tesseract: undefined symbol: _ZN9tesseract16TessPAGERendererC1EPKc*

This issue, as well as similarly structured symbol lookup errors, are caused by incompatible Leptonica and Tesseract downloads, or multiple Tesseract versions installed in the system. Clear Tesseract and all related libraries and reinstall.

- Find all instances of tesseract and remove. For example, you can find all instrances of "tesseract" and proceed to remove those files with the following commands: 
```
find / -type d -name "tesseract" 2>/dev/null # Use this to see where all tesseract related files are located in your machine

$ Some example removal commands
sudo find /usr -name "tesseract*" -exec rm -rf {} \;
sudo find /opt -name "tesseract*" -exec rm -rf {} \;
```

- Run the *_tesseract-for-squish-4.1.1_* executable from Squish again

If using the binary file still shows errors, you can try to use tesseract straight from the source. For example, you can rebuild with the following commands: 

- Force Rebuild and Reinstall Tesseract
```
# Navigate to the Tesseract source directory: 
cd /path/to/tesseract/source

# Clean any previous builds
make clean

# Reconfigure and rebuild
./autogen.sh
./configure
make
sudo make install
sudo ldconfig  # Update linker cache
```

- Reinstall tesseract and libtesseract:
```
sudo apt remove --purge tesseract-ocr libtesseract-dev
sudo apt autoremove

# Reinstall the official packages
sudo apt install tesseract-ocr libtesseract-dev
```
