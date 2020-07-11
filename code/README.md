# Master thesis

Master Thesis on integrating the handbook into Alexa

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
