# zippy - An Open Source CLI for Bionifying eBooks for the Kindle

`zippy` a simple python CLI for 'bionifying' eBooks. Bionification is a technique that bolds the initial letters of words to improve reading speed and comprehension. This tool specifically targets eBooks in the ePub format and is ideal for use with Kindle devices.

## Setup Instructions

### Step 1: Clone the Repository

```fish
git clone https://github.com/yourusername/zippy.git
cd zippy
```

### Step 2: Set Up a Python Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```fish
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required Python packages using `pip`:

```fish
pip3 install -r requirements.txt
```

## Usage Instructions

To bionify an ePub eBook, use the following command:

```fish
python3 zippy.py <input_file> <output_file> [--algorithm <algorithm>]
```

### Example

```fish
python3 zippy.py "Lying (Sam Harris).epub" "Lying (Sam Harris) Bionic.epub"
```

### Optional Algorithm Parameter

You can customize the bionification algorithm using the `--algorithm` parameter. The default algorithm is `"- 0 1 1 2 0.4"`. This parameter controls how many letters are bolded based on word length and other factors.

```fish
python zippy.py "Lying (Sam Harris).epub" "Lying (Sam Harris) Bionic.epub" --algorithm "- 0 1 1 2 0.4"
```

## Credits

This project is inspired by and uses parts of the code from [Bionify](https://github.com/Cveinnt/bionify) Chrome extension.
