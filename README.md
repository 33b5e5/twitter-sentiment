# twitter-sentiment.py

Sentiment analysis of Twitter accounts using TextBlob

## Prerequisites

### Python 3 Modules

```bash
pip3 install argparse
pip3 install termcolor
pip3 install textblob
pip3 install TwitterSearch
```

### Twitter API Keys

You'll need a Twitter developer account and API keys. Create an "app" here:

<https://developer.twitter.com/en/apps>

Navigate to "Keys and Tokens" under the new app's settings.

Export these four environment variables (using your actual key values):

```bash
export CONSUMER_KEY="aPi-KeY"
export CONSUMER_SECRET="ApI-SeCrET-kEy"
export ACCESS_TOKEN="AcCEsS-tOkEn"
export ACCESS_TOKEN_SECRET="ACceSs-ToKEn-sEcReT"
```

## Screenshot

![screen.png](https://github.com/33b5e5/twitter-sentiment/raw/main/screen.png?raw=true)

## Credits

### TextBlob

Copyright 2013-2020 Steven Loria

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

### TwitterSearch

License (MIT)

Copyright (C) 2013 Christian Koepp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

### Misc Python Libraries

Other builtin Python libraries are licensed under the Python Software
Foundation's License Agreement:

<https://docs.python.org/3/license.html>
