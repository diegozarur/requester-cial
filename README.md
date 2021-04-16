# Requester Cial Dnb

the application given a list of website URLs as input, visits them and finds, extracts and outputs the websites’ logo
image URLs and all phone numbers (e.g. mobile phones, land lines, fax numbers) present on the websites.

## **Installation**

1. clone project `git clone https://diegozfd@bitbucket.org/diegozfd/requester-cial.git` 
2. `cd request-cial`
3. Edit websites file `nano websites.txt` and add your own websites (or create your own txt file)
4. build docker `docker build -t requester-cial .`
5. execute docker `docker run -i requester-cial`

## **Usage**

The project will search for txt file in the root directory

#### Command to build project

```terminal
➜  resquester-cial docker build -t requester-cial . 
```

#### Command to run
```terminal
➜  resquester-cial docker run -i requester-cial
```

Results are written to the console without formatting

#### Print Results

Example of result with formatting

```python
[
    {
        "logo": "https://www.illion.com.au/wp-content/uploads/2019/03/ION-RGB-Gradient-64.png",
        "phones": [],
        "website": "https://www.illion.com.au/"
    },
    {
        "logo": "https://www.illion.com.au/wp-content/uploads/2019/03/ION-RGB-Gradient-64.png",
        "phones": [
            "+61 3 9828 3200",
            "+61 8 7122 9452"
        ],
        "website": "https://www.illion.com.au/contact-us/"
    }
]
```