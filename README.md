# Nepali Transliteral Dataset
> An Open Source Nepali Transliteral Dataset that can be used for automatic transliteration of Nepali language.

[![GitHub license](https://img.shields.io/github/license/SushilShrestha/pyBSDate)](https://github.com/SushilShrestha/pyBSDate/blob/master/License)


This repository aims to maintain mapping of unicode nepali words with its transliteral version. An example of transliteration would be `"नेपाल" => "nepal"`. A good transliteral dataset can be super handy creating an automated machine learning model to acheive such transliteration. So as we are taking an initiative to maintain a good data source for transliteration project. 

## Contributing
**Every contribution made to the repo will be counted towards hacktober fest points.** Feel free to contribute and let's maintain a solid dataset for Nepali transliteration.

You can start editing the file under `transliterals` folder and send a pull request after you update the transliterals for each file in that folder. Each file can be counted as a single pull request. 

For example, Given following template on the file, fill up the empty transliteral word for each unicode word.
```json
{
  "ओ": "",
  "पक्डिदेउ": "",
  "मल्ल": "",
  "हिँडेछु": "",
  "स्वतन्त्र": "",
  "पुग्न": "",
  "हर्षले": "",
  "डिउटी": ""
}
```

Expected endresult is shown in `transliteral_words_000.json` file.

#### Creating a pull request
1. Fork it (<https://github.com/SushilShrestha/NepaliTransliteralDataset/fork>)
2. Clone the repo to local machine(`git clone repourl`)
2. Create a new branch(`git checkout -b branchname`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin branchname`)
5. Create a new Pull Request

🎉🎉🎉🎉


