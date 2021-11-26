# Currency Exchange Rate Monitor(GBP Vs LKR)
A script to web scrape multiple SriLankan Financial organization websites to compare exchange rate of GBP Vs LKR and visualized with H2O Wave framework

#### H2O wave
<img src="https://www.h2o.ai/wp-content/uploads/2020/12/wave-type-yellow-1024x410.png" width="300">
Visual comparision of exchage data is done with H20 Wave framework

### Quickstart
#### Pre-requisites
- Python3
- git
 
#### Install H20 wave
1. Download and extract the H2O Wave SDK from https://github.com/h2oai/wave/releases
2. Navigate to the extarcted directory and initialize the wave server using the following command
  ```
./waved
```
##### Application setup
1. Navigate to the directory where you want to place the application.
2. Clone the repository with the following command
  ```
git clone https://github.com/Archulan/exchangeMonitor.git
```
2. Set up a virtual environment
  ```
python3 -m venv venv
source venv/bin/activate
```
3. Install the required Python packages via the following command
  ```
pip install -r requirements.txt
```
4. Start the Exchange monitor
  ```
wave run exchangeMonitor.py
```
5. Go to http://localhost:10101/demo to access the application.

