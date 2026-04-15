
# How to Build and Run Freeplane

This guide walks you through the process of cloning the repository, compiling the code with Gradle, launching the application, and generating a distribution package.

##  Prerequisites

Before you begin, ensure your system meets the following requirements:
* **Java:** Version 11 or later.
* **Gradle:** Version 6.0 or higher.

---

## Step-by-Step Instructions

### 1. Download and Setup Gradle
1. Download a compatible version of Gradle from the [official releases page](https://gradle.org/releases/).
2. Unzip the downloaded archive into your home directory (or another preferred location). 

### 2. Clone the Repository
Open your terminal, clone the official Freeplane source code, and navigate into the directory:

```bash
git clone [https://github.com/freeplane/freeplane.git](https://github.com/freeplane/freeplane.git)
cd freeplane

```

### 3. Build the Project

_Note: Gradle wrapper files (`gradlew`) are intentionally ignored in the repository's version control. You must use your locally installed Gradle executable._

Execute the `build` command, replacing the path below with the actual location where you unzipped Gradle:

Bash

```
~/Downloads/gradle-6.0.1/bin/gradle build

```

### 4. Run the Application

Once the build process completes successfully, navigate to the binary output folder and run the executable specific to your operating system:

-   **For Linux / macOS:**
    
    Bash
    
    ```
    cd BIN
    ./freeplane.sh
    
    ```
    
-   **For Windows:**
    
    DOS
    
    ```
    cd BIN
    freeplane.bat
    
    ```
    



## Create Package

If you want to create a clean, standalone distribution package of Freeplane, you can chain the `clean`, `build`, and `dist` tasks together:

Bash

```
~/Downloads/gradle-6.0.1/bin/gradle clean build dist

```

After the command finishes, your generated packages will be located in the `DIST` directory. You can view them by running:

Bash

```
ls DIST

```

## Setting Up VS Code for Freeplane Development

While the [official documentation](https://docs.freeplane.org/coding/IDE_setup.html) covers Eclipse, IntelliJ, and Netbeans, you can follow these steps to configure VS Code for a smooth development experience.

## 1. Prerequisites

Before starting, ensure you have the following installed:

-   **JDK** (Check the `build.gradle` file for the required version—usually Java 11 or 17).
    
-   **Visual Studio Code**.
    
-   **Extension Pack for Java** (included in the Extension Pack).
    
    

## 2. Import the Project

1.  Open VS Code and select **File > Open Folder...**.
    
2.  Navigate to your local Freeplane repository (the root folder containing `settings.gradle`) and open it.
    
3.  Wait for the **Java Language Server** to activate. You will see a progress bar in the bottom status bar. VS Code will automatically detect the Gradle project structure.
    

## 3. Initial Build (Crucial Step)

Freeplane uses generated code (like lexers). If you don't run a build first, VS Code will show many "symbol not found" errors.

1.  Open the integrated terminal (`Ctrl` + `` ` ``).
    
2.  Run the following command:
    
    Bash
    
    ```
    ./gradlew clean build -x test
    
    ```
    
    _Note: If you have old `MANIFEST.MF` files from previous builds, delete them as suggested in the official docs._
    

## 4. Configuring the Launch (Debug)

To run and debug Freeplane directly from VS Code, you need a `launch.json` file.

1.  Go to the **Run and Debug** view (`Ctrl+Shift+D`).
    
2.  Click on **create a launch.json file** and select **Java**.
    
3.  Paste the following configuration (adjusting the `projectName` if necessary):
    

JSON

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "java",
            "name": "Debug Freeplane",
            "request": "launch",
            "mainClass": "org.freeplane.launcher.Launcher",
            "projectName": "freeplane_debughelper",
            "vmArgs": "-Dorg.freeplane.basedir=${workspaceFolder}",
            "args": ""
        }
    ]
}

```

## 5. Working with Gradle Tasks

You can use the **Gradle side-bar** (the elephant icon) to access all Freeplane tasks:

-   **Build**: Use the `build` task to compile everything.
    
-   **Run**: Use the `run` task under the `freeplane_debughelper` module to launch the app without the debugger.
    

----------

> 
> 
> **Using other IDEs?**
> 
> If you prefer to use Eclipse, IntelliJ, or Netbeans, please refer to the official [Freeplane IDE Setup Guide](https://docs.freeplane.org/coding/IDE_setup.html) for detailed, platform-specific instructions.


