# Readme

A simple bot that detects the mood of the user.

Example from [Rasa getting started tutorial](https://rasa.com/docs/get_started_step1/)

# Installation Notes

* Clone [Rasa starter pack](https://github.com/RasaHQ/starter-pack-rasa-stack)

```
git clone https://github.com/RasaHQ/starter-pack-rasa-stack.git
cd starter-pack-rasa-stack
```
* Install **PIP**
(Source: [Stackoverflow](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x))

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
* Install **requirements** 
(Source:[ Rasa Homepage](https://rasa.com/docs/get_started_step3/) and [Solve tensorflow with Python 3.7 bug](https://github.com/tensorflow/tensorflow/issues/20444))

```
brew switch python 3.6.5
brew install hdf5

python -m pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl

pip3 install -U -r requirements.txt

```

* Install **Rasa packages**

```
pip3 install -U --user rasa_core
pip3 install -U --user rasa_nlu[tensorflow]
pip3 install -U --user ipython

```
* Set ``$PATH`` variable according to your system

# Usage

## Train NLU

```
python3 -m rasa_nlu.train -c nlu_config.yml --data data/nlu_data.md -o model --fixed_model_name nlu --project current --verbose
```

## Test intent recognitation

```
python3 tests/test_args.py hello

This is the name of the script:  tests/test_args.py
Number of arguments:  2
The arguments are:  ['tests/test_args.py', 'hello']

{
  "intent": {
    "name": "greet",
    "confidence": 0.9781364798545837
  },
  "entities": [],
  "intent_ranking": [
    {
      "name": "greet",
      "confidence": 0.9781364798545837
    },
    {
      "name": "mood_affirm",
      "confidence": 0.03868754208087921
    },
    {
      "name": "mood_unhappy",
      "confidence": 0.014160260558128357
    },
    {
      "name": "goodbye",
      "confidence": 0.0
    },
    {
      "name": "mood_deny",
      "confidence": 0.0
    },
    {
      "name": "mood_great",
      "confidence": 0.0
    }
  ],
  "text": "hello"
}

```

## Train dialogue
```
python3 -m rasa_core.train -d domain.yml -s data/stories.md -o model/dialogue
```

## Start terminal chat

```
python3 run.py

<div class="chat-window" <p>Hi! you can chat in this window. Type 'stop' to end the conversation.</p></div>
<div class="chat-window" <p>Hi! you can chat in this window. Type 'stop' to end the conversation.</p><p></p></div>

Hello

<div class="chat-window" <p>Hi! you can chat in this window. Type 'stop' to end the conversation.</p><p></p><p>Hello</p><p>Hey! How are you?</p></div>

I feel great!

<div class="chat-window" <p>Hi! you can chat in this window. Type 'stop' to end the conversation.</p><p></p><p>Hello</p><p>Hey! How are you?</p><p>I feel great!</p><p>Great carry on!</p></div>

```
