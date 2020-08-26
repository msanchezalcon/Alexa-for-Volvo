# Master thesis: A conversational driver's handbook built on Alexa.

Summary of the thesis:

The inspiration behind this study comes from an opportunity to work with Volvo Trucks (VT) and their need to effortlessly make their driver’s handbook more accessible. In our thesis, we present a report on what truck drivers need from a voice-based handbook from initial interviews as well as a small corpus of instructional dialogues in the vehicle domain. We also make an analysis of the corpus and implement the observed dialogue phenomena into an Alexa skill with Python and Amazon Web Services (AWS) Lambda, using a finite-state approach. Finally, we evaluate the skill by how well it can perform in relation to the phenomena observed during the analysis. We conclude that a finite-state approach to the implementation is an adequate solution for the dialogue moves identified in the analysis. 

This repo contains a demo of the voice-first application developed for the thesis.

## See demos:
1. https://drive.google.com/file/d/1SLMRRvd68UomCXXoFC4sB7MjdOP6ZRme/view?usp=sharing
2. https://drive.google.com/file/d/1JWA65Mu5yxZrHWe0IDs2Al9Vm6H53hvx/view?usp=sharing

## Code structure

```bash
masterthesis/
├── interactionModels
│   └── custom
│       └── en-US.json
├── lambda
│   ├── lambda_function.py
│   ├── requirements.txt
│   └── utils.py
├── README.md
└── skill.json
```

The frontend code is in **en-US.json**.
The backend code is mainly in **lambda_functions.py**. Any helper functions should be put in utils.py.
